import sys
from PyQt5 import QtWidgets, QtCore


class Main(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        sld.setStyleSheet("""
            QSlider{
                background: #E3DEE2;
            }
            QSlider::groove:horizontal {  
                height: 10px;
                margin: 0px;
                border-radius: 5px;
                background: #B0AEB1;
            }
            QSlider::handle:horizontal {
                background: #fff;
                border: 1px solid #E3DEE2;
                width: 17px;
                margin: -5px 0; 
                border-radius: 8px;
            }
            QSlider::sub-page:qlineargradient {
                background: #3B99FC;
                border-radius: 5px;
            }
        """)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sld)
        self.setLayout(layout)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
