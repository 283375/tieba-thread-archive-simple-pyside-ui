from ui.threadInfoDialog_ui import Ui_Dialog
from PySide6.QtWidgets import QDialog
from tieba_thread_archive.models.archive import ThreadInfo


class ThreadInfoDialog(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setThreadInfo(self, thread_info: ThreadInfo):
        self.idLabel.setText(str(thread_info.id))
        self.titleLabel.setText(thread_info.title)
        self.lzLabel.setText(thread_info.author.name_show)
        self.barLabel.setText(f"{thread_info.forum.name}吧")
