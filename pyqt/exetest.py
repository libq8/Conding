import sys
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QApplication, QVBoxLayout


class TestWidget(QWidget):
    def __init__(self, parent=None):
        super(TestWidget, self).__init__(parent)
        self.m_btn = QPushButton("退出")
        layout = QVBoxLayout()
        layout.addWidget(self.m_btn)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TestWidget()
    main.show()
    sys.exit(app.exec_())

