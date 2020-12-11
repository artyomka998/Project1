import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1000, 700)
    w.move(250, 70)
    w.setWindowTitle('Лабораторная 5')
    w.show()

    sys.exit(app.exec_())