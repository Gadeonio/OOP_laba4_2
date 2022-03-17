import sys

import PySide6
from PySide6.QtCore import QFile, QObject, Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QMainWindow, QLineEdit, QSpinBox, QSlider, QApplication

from Model import Model
from Observer_Model import Observer, Subject_Model, Block

class MainWidget(QMainWindow):
    def __init__(self, ui_file):
        super(MainWidget, self).__init__()
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()



class MyWindow(QObject):
    def __init__(self):
        super().__init__()
        self.widget = MainWidget('form.ui')
        name_block = ['a', 'b', 'c']
        #
        model = Subject_Model(30, 20, 50)
        blocks = []
        for element in name_block:
            lb = self.widget.window.findChild(QLineEdit, 'lineEdit_' + element)
            sb = self.widget.window.findChild(QSpinBox, 'spinBox_' + element)
            hs = self.widget.window.findChild(QSlider, 'horizontalSlider_' + element)
            block = Observer(lb, sb, hs)
            model.attach(block)
            blocks.append(block)
        model.notify()



if __name__ == "__main__":
    app = QApplication()
    Mywidget = MyWindow()
    Mywidget.widget.window.show()

    sys.exit(app.exec())




