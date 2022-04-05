import sys
#Сохранение реализовать через модель (у модели должно быть метод save)
#Доработать работу с textBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QLineEdit, QSpinBox, QSlider, QApplication

from Observer_Model import Observer_A,Observer_B, Observer_C, Subject_Model


class MainWidget(QMainWindow):
    def __init__(self, ui_file):
        super(MainWidget, self).__init__()
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()


class MyWindow(QApplication):
    def __init__(self):
        super().__init__()
        self.name_file = 'save.txt'
        self.widget = MainWidget('form.ui')
        self.widget.installEventFilter(self)

        a = 0
        b = 0
        c = 0
        self.model = Subject_Model(a, b, c)
        self.model.parse_file(self.name_file)
        self.lastWindowClosed.connect(self.save_model)


        name_block = ['a', 'b', 'c']

        blocks = []
        for element in name_block:
            lb = self.widget.window.findChild(QLineEdit, 'lineEdit_' + element)
            sb = self.widget.window.findChild(QSpinBox, 'spinBox_' + element)
            hs = self.widget.window.findChild(QSlider, 'horizontalSlider_' + element)
            if element == 'a':
                block = Observer_A(lb, sb, hs)
                lb.editingFinished.connect(self.update_for_A)
                sb.valueChanged.connect(self.update_for_A)
                hs.valueChanged.connect(self.update_for_A)
                #hs.valueChanged.emit(int(hs.value()))

            elif element == 'c':
                block = Observer_C(lb, sb, hs)
                lb.editingFinished.connect(self.update_for_C)
                sb.valueChanged.connect(self.update_for_C)
                hs.valueChanged.connect(self.update_for_C)

            else:
                block = Observer_B(lb, sb, hs)
                lb.editingFinished.connect(self.update_for_B)
                sb.valueChanged.connect(self.update_for_B)
                hs.valueChanged.connect(self.update_for_B)
            self.model.attach(block)
            blocks.append(block)
        self.model.notify()

    def update_for_A(self):
        try:
            self.model.a = int(self.sender().value())
        except BaseException:
            self.model.a = int(self.sender().text())
        self.model.notify()

    def update_for_B(self):
        try:
            self.model.b = int(self.sender().value())
        except BaseException:
            self.model.b = int(self.sender().text())
        self.model.notify()

    def update_for_C(self):
        try:
            self.model.c = int(self.sender().value())
        except BaseException:
            self.model.c = int(self.sender().text())
        self.model.notify()

    def save_model(self):
        self.model.save_file(self.name_file)








if __name__ == "__main__":
    Mywidget = MyWindow()
    Mywidget.widget.window.show()

    sys.exit(Mywidget.exec())




