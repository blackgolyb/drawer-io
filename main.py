import sys

from PyQt5.QtWidgets import QApplication

from src.main_window import MainWindow


def main():
    app = QApplication([])
    app.setApplicationName("drawer-io")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
