import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_make.clicked.connect(self.make)
        self.sh_paint = False

    def paintEvent(self, event):
        if self.sh_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_circle(qp)
            # Завершаем рисование
            qp.end()

    def draw_circle(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        x1, y1 = randint(101, 260), randint(51, 200)
        x2, y2 = x1 + randint(0, 50), y1 + randint(0, 50)
        qp.drawEllipse(x1, y1, x2, y2)

    def make(self):
        self.sh_paint = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())