"""
A PySide6 application that allows users to select a source file, a destination path,
and a file containing rename data, then copies and renames the source file to the destination
前缀、后缀用装饰器加
"""
import PySide6,sys
from PySide6.QtWidgets import QTextEdit,QGridLayout,QMainWindow,QApplication,QWidget,QPushButton,QFileDialog,QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PathSelector import PathSelector
from copy__rename_file import copy_and_rename_file
from get_data import read_excel_column
from FileSelector import FileSelector
import os

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.src_file_selector()
        self.dst_path_selector()
        self.get_rename()
        self.file_formations()
        self.excel_choose()
        self.display_rename_widget()
        self.layout()

    def src_file_selector(self) -> None:       #the method of choosing workplace
        self.src_file_selector = FileSelector()
        self.src_file_selector.setWindowModality(Qt.ApplicationModal)
        self.src_file_selector.file_edit.setPlaceholderText("请选择源文件")

    def dst_path_selector(self) -> None:       #the method of choosing workplace
        self.dst_path_selector = PathSelector()
        self.dst_path_selector.setWindowModality(Qt.ApplicationModal)
        self.dst_path_selector.path_edit.setPlaceholderText("请选择目标文件夹")

    def get_rename(self) -> None:
        self.renamedata_selector = FileSelector()
        self.renamedata_selector.setWindowModality(Qt.ApplicationModal)
        self.renamedata_selector.file_edit.setPlaceholderText("请选择重命名数据文件")
    
    def file_formations(self) -> None:
        self.input_file_format = QTextEdit()
        self.input_file_format.setPlaceholderText("请输入文件格式，如：.jpg")

    def excel_choose(self) -> None:
        self.excel_indexorname = QComboBox()
        self.excel_indexorname.addItems(["列索引（如：0）", "列标题（如：姓名）", "列名（如：A）"])
        self.excel_index = QTextEdit()
        self.excel_index.setPlaceholderText("请输入列")

    def display_rename_widget(self) -> None:
        self.display_rename_widget = QTextEdit()
        self.display_rename_widget.setPlaceholderText("重命名预览")
        self.display_rename_widget.setReadOnly(True)
        self.display_rename_widget_button = QPushButton("预览")
        self.display_rename_widget_button.clicked.connect(self.update_display_rename)

    def update_display_rename(self) -> None:
        self.display_rename_widget.setPlainText("xxx"+self.input_file_format.toPlainText())

    def file_operations(self) -> None:
        src_file = self.src_file_selector.file_edit.text()
        dst_path_raw = self.dst_path_selector.path_edit.text()
        column_str = self.excel_index.toPlainText()
        column_type = self.excel_indexorname.currentIndex()             #考虑True选择name,False选择index怎么实现
        #list_dst_path_processed = read_excel_column(self.renamedata_selector.file_edit.text(), "Sheet1", (lambda column_type:column_name=column_str if column_type else column_index=int(column_str)))    
        if column_type:  # 列索引
            list_dst_path_processed = read_excel_column(self.renamedata_selector.file_edit.text(), "Sheet1", column_name=column_str)    
        else:  # 列标题
            list_dst_path_processed = read_excel_column(self.renamedata_selector.file_edit.text(), "Sheet1", column_index=int(column_str))     
        
        for name in list_dst_path_processed:
            name = name + self.input_file_format.toPlainText()
            dst_path_processed = os.path.join(dst_path_raw, name)
            if src_file and dst_path_processed:
                copy_and_rename_file(src_file, dst_path_processed)
        else:
            print("请先选择源文件和目标文件路径")   #please choose source file and destination file first
    
    def layout(self) -> None:
        main_layout = QGridLayout()
        self.central_widget.setLayout(main_layout)
        main_layout.addWidget(self.src_file_selector, 0, 0)
        main_layout.addWidget(self.dst_path_selector, 1, 0)
        main_layout.addWidget(self.renamedata_selector, 2, 0)
        main_layout.addWidget(self.input_file_format, 2, 1)
        main_layout.addWidget(self.excel_indexorname, 0, 1)
        main_layout.addWidget(self.excel_index, 1, 1)
        main_layout.addWidget(self.display_rename_widget, 3, 1)
        main_layout.addWidget(self.display_rename_widget_button, 4, 1)
        self.run_button = QPushButton("执行文件操作")
        self.run_button.clicked.connect(self.file_operations)
        main_layout.addWidget(self.run_button, 3, 0)


if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()