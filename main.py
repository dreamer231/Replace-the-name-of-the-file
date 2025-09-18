import PySide6,sys
from PySide6.QtWidgets import QTextEdit

class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 600)

    def workplace_selector(self) -> None:       #the method of choosing workplace
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)
        text_edit.setPlainText("Welcome to the workplace selector!")
        





if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()