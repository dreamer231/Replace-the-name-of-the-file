import PySide6
from PySide6.QtWidgets import QFileDialog, QWidget, QHBoxLayout, QPushButton, QLabel,QTextEdit,QInputDialog, QLineEdit
from PySide6.QtCore import QDir

class PathSelector(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        # 创建水平布局
        layout_main = QHBoxLayout()
        # 创建输入框
        self.path_edit = QLineEdit()
        self.path_edit.setObjectName("path_edit")
        self.path_edit.setStyleSheet("""
            QLineEdit#path_edit {
                font-size: 16px;
            }
        """)
        layout_main.addWidget(self.path_edit)
        # 创建按钮
        self.btn = QPushButton('浏览...')
        self.btn.setObjectName("btn")
        self.btn.setStyleSheet("""
            QPushButton#btn {
                font-size: 16px;
            }
        """)
        self.btn.clicked.connect(self.open_dialog)
        layout_main.addWidget(self.btn)
        # 设置布局
        self.setLayout(layout_main)

    def open_dialog(self) -> None:
        # 打开目录选择对话框
        directory = QFileDialog.getExistingDirectory(
            self, 
            "选择目录", 
            QDir.homePath(),  # 初始目录设置为用户主目录
            QFileDialog.Option.ShowDirsOnly | QFileDialog.Option.DontResolveSymlinks
        )
        # 如果用户选择了目录（非空），则更新输入框
        if directory:
            self.path_edit.setText(directory)

if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication([])
    selector = PathSelector()
    selector.show()
    app.exec()