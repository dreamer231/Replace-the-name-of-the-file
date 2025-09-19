import PySide6,sys
from PySide6.QtWidgets import QTextEdit,QGridLayout,QMainWindow,QApplication,QWidget,QPushButton,QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PathSelector import PathSelector

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 600)
        self.workplace_selector()


    def workplace_selector(self) -> None:       #the method of choosing workplace
        self.path_selector = PathSelector(self)
        self.path_selector.setWindowModality(Qt.ApplicationModal)
        self.path_selector.setlayout

    def layout(self) -> None:
        main_layout = QGridLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.path_selector, 0, 0)


if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()