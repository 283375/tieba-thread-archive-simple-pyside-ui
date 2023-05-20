import traceback

from PySide6.QtCore import QDir, Slot
from PySide6.QtWidgets import QDialogButtonBox, QFileDialog, QMainWindow, QMessageBox
from tieba_thread_archive.local.archive.detect import detect_archive_version
from tieba_thread_archive.local.archive.v3 import AV3LocalArchive
from tieba_thread_archive.models import ArchiveOptions, ThreadInfo
from tieba_thread_archive.remote.api.base import get_posts
from tieba_thread_archive.remote.protobuf.response.PbPageResIdl_pb2 import PbPageResIdl

from threadInfoDialog import ThreadInfoDialog
from ui.mainwindow_ui import Ui_MainWindow
from update_archive import UpdateLocalArchiveQThread


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.store_fileDialog = QFileDialog(self)
        self.store_fileDialog.setObjectName("store_fileDialog")
        self.store_fileDialog.setFileMode(QFileDialog.FileMode.Directory)
        self.store_fileDialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        self.update_fileDialog = QFileDialog(self)
        self.update_fileDialog.setObjectName("update_fileDialog")
        self.update_fileDialog.setFileMode(QFileDialog.FileMode.Directory)
        self.update_fileDialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        self.setupUi(self)

        self.store_selectedDir: QDir | None = None
        self.update_selectedDir: QDir | None = None
        self.update_local_archive: AV3LocalArchive | None = None
        self.store_updateLocalArchiveQThread = UpdateLocalArchiveQThread()
        self.store_updateLocalArchiveQThread.progressTextUpdate.connect(
            self.store_confirmButton.setText
        )
        self.store_updateLocalArchiveQThread.complete.connect(
            self.store_updateQThread_complete
        )
        self.store_updateLocalArchiveQThread.error.connect(
            self.store_updateQThread_error
        )
        self.update_updateLocalArchiveQThread = UpdateLocalArchiveQThread()
        self.update_updateLocalArchiveQThread.progressTextUpdate.connect(
            self.update_confirmButton.setText
        )
        self.update_updateLocalArchiveQThread.complete.connect(
            self.update_updateQThread_complete
        )
        self.update_updateLocalArchiveQThread.error.connect(
            self.update_updateQThread_error
        )

    @Slot()
    def on_store_dirChangeButton_clicked(self):
        self.store_fileDialog.show()

    @Slot()
    def on_store_fileDialog_accepted(self):
        selected_dir = QDir(self.store_fileDialog.selectedFiles()[0])
        entry_list = selected_dir.entryList(
            QDir.Filter.AllEntries | QDir.Filter.NoDotAndDotDot
        )
        # print(entry_list)
        if len(entry_list) == 0:
            QMessageBox.information(self, "OK", "该目录有效")
            self.store_selectedDir = selected_dir
            self.store_dirLabel.setText(selected_dir.absolutePath())
        elif len(entry_list) > 0:
            QMessageBox.critical(self, "damedesu", "该目录非空，请重选")
            self.store_fileDialog.show()

    @Slot()
    def on_store_confirmButton_clicked(self):
        if not self.store_selectedDir:
            QMessageBox.critical(self, "Error", "请选择存档位置")
            return
        try:
            tid = int(self.store_idLineEdit.text())
        except Exception as e:
            QMessageBox.critical(self, "Error", "无法解析 ID，请检查输入")
            return

        thread_info = ThreadInfo.from_protobuf(
            PbPageResIdl.FromString(get_posts.call(tid, rn=3).content)
        )
        thread_info_dialog = ThreadInfoDialog(self)
        thread_info_dialog.setWindowTitle("请确认存档贴子信息")
        thread_info_dialog.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        thread_info_dialog.accepted.connect(self.store_confirmStore)
        thread_info_dialog.setThreadInfo(thread_info)
        thread_info_dialog.show()

    @Slot()
    def store_confirmStore(self):
        local_archive = AV3LocalArchive(self.store_selectedDir.absolutePath())
        local_archive.set_archive_options(
            ArchiveOptions(images=True, audios=True, videos=True, portraits=True)
        )

        self.store_updateLocalArchiveQThread.setAttributes(
            local_archive, int(self.store_idLineEdit.text())
        )
        self.store_confirmButton.setDisabled(True)
        self.store_updateLocalArchiveQThread.start()

    @Slot()
    def store_updateQThread_complete(self):
        QMessageBox.information(self, "Success", "存档完成！")
        self.store_confirmButton.setText("点此存档")
        self.store_confirmButton.setDisabled(False)

    @Slot(str)
    def store_updateQThread_error(self, text: str):
        QMessageBox.critical(self, "Error", f"发生错误：{text}")
        self.store_confirmButton.setText("点此存档")
        self.store_confirmButton.setDisabled(False)

    @Slot()
    def on_update_dirChangeButton_clicked(self):
        self.update_fileDialog.show()

    @Slot()
    def on_update_fileDialog_accepted(self):
        selected_dir = QDir(self.update_fileDialog.selectedFiles()[0])
        archive_version = detect_archive_version(selected_dir.absolutePath())
        if archive_version is None:
            QMessageBox.critical(self, "Invalid", "该目录不是有效的存档目录，请重新选择")
            self.update_fileDialog.show()
        elif archive_version == 2:
            QMessageBox.warning(self, "Invalid", "暂不支持管理 V2 存档，请选择更新版本的存档")
            self.update_fileDialog.show()
        elif archive_version == 3:
            QMessageBox.information(self, "OK", "将加载该存档，软件可能卡顿，烦请耐心等待")
            try:
                self.update_local_archive = AV3LocalArchive(selected_dir.absolutePath())
                thread_info_dialog = ThreadInfoDialog(self)
                thread_info_dialog.setWindowTitle("贴子信息")
                thread_info_dialog.setThreadInfo(self.update_local_archive.thread_info)
                thread_info_dialog.exec()
                self.update_selectedDir = selected_dir
                self.update_dirLabel.setText(selected_dir.absolutePath())
                thread_info_dialog.deleteLater()
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"发生错误：{traceback.format_exception_only(e)[0]}，请去 github 提交 issue",
                )

    @Slot()
    def on_update_confirmButton_clicked(self):
        if not isinstance(self.update_local_archive, AV3LocalArchive):
            QMessageBox.critical(self, "Error", "请选择一个本地存档")
            return

        self.update_updateLocalArchiveQThread.setAttributes(self.update_local_archive)
        self.update_confirmButton.setDisabled(True)
        self.update_updateLocalArchiveQThread.start()

    @Slot()
    def update_updateQThread_complete(self):
        QMessageBox.information(self, "Success", "更新完成！")
        self.update_confirmButton.setText("更新")
        self.update_confirmButton.setDisabled(False)

    @Slot(str)
    def update_updateQThread_error(self, text: str):
        QMessageBox.critical(self, "Error", f"发生错误：{text}")
        self.update_confirmButton.setText("更新")
        self.update_confirmButton.setDisabled(False)
