from PyQt5.QtWidgets import QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.label.setText("Hi PyQt")
        self.setCentralWidget(self.label)
