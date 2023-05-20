import time
import traceback
from typing import Any, Callable, Optional

from PySide6.QtCore import QThread, Signal
from tieba_thread_archive.local.archive.v3 import AV3LocalArchive
from tieba_thread_archive.models.progress import Progress
from tieba_thread_archive.remote.thread import RemoteThread


def remote_thread_wrapped_progress_hook(original_hook: Callable[[str], Any]):
    def wrapper(p: Progress):
        title = ["", "正在获取回复", "正在获取楼中楼"]
        progress_percent = (
            f"{(p.progress / p.total_progress) * 100:.2f}"
            if p.total_progress != 0
            else "0"
        )
        original_hook(
            f"{title[p.step]} - {p.progress} / {p.total_progress} ({progress_percent}%)"
        )

    return wrapper


def local_archive_wrapped_progress_hook(original_hook: Callable[[str], Any]):
    def wrapper(p: Progress):
        progress_percent = (
            f"{(p.progress / p.total_progress) * 100:.2f}"
            if p.total_progress != 0
            else "0"
        )
        original_hook(
            f"正在下载贴内资源 - {p.progress} / {p.total_progress} ({progress_percent}%)"
        )

    return wrapper


def update_archive(
    archive: AV3LocalArchive,
    id: Optional[int] = None,
    progress_hook: Optional[Callable[[str], Any]] = None,
):
    tid = id or archive.thread_info.id
    remote_thread = RemoteThread(tid)
    remote_thread.add_progress_hook(remote_thread_wrapped_progress_hook(progress_hook))
    remote_thread.load_remote_data()
    new_archive_thread = remote_thread.to_archive_thread()

    progress_hook("正在存档……")
    archive.update_progress.add_progress_hook(
        local_archive_wrapped_progress_hook(progress_hook)
    )
    archive.update(new_archive_thread)
    archive.dump()
    archive.download_assets()


class UpdateLocalArchiveQThread(QThread):
    progressTextUpdate = Signal(str)
    complete = Signal()
    error = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.debounceLastTimestamp = time.time() * 1000

    def progress_hook(self, text: str):
        timestamp = time.time() * 1000
        if timestamp - self.debounceLastTimestamp < 50:
            return

        self.progressTextUpdate.emit(text)
        self.debounceLastTimestamp = timestamp

    def setAttributes(self, archive: AV3LocalArchive, id: Optional[int] = None):
        self.archive = archive
        self.id = id

    def run(self):
        try:
            update_archive(self.archive, self.id, self.progress_hook)
        except Exception as e:
            self.error.emit(traceback.format_exception_only(e)[0])
        else:
            self.complete.emit()
