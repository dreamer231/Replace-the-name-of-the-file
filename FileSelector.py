import PySide6
from PySide6.QtWidgets import QFileDialog, QWidget, QHBoxLayout, QPushButton, QLabel,QTextEdit,QInputDialog, QLineEdit
from PySide6.QtCore import QDir

class FileSelector(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        # 创建水平布局
        layout_main = QHBoxLayout()
        # 创建输入框
        self.file_edit = QLineEdit()
        self.file_edit.setObjectName("path_edit")
        self.file_edit.setStyleSheet("""
            QLineEdit#path_edit {
                font-size: 16px;
            }
        """)
        layout_main.addWidget(self.file_edit)
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
        # 打开文件选择对话框
        file_info = QFileDialog.getOpenFileName(
            self,
            "选择文件", 
            "",  # 文件过滤器
            options=QFileDialog.Option.DontResolveSymlinks
        )
        # 如果用户选择了文件（非空），则更新输入框
        if file_info[0]:
            self.file_edit.setText(file_info[0])

if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication([])
    selector = FileSelector()
    selector.show()
    app.exec()