from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a stacked widget
        self.stacked_widget = QStackedWidget(self)

        # Create the opening page
        self.opening_page = QWidget()
        self.opening_page.setStyleSheet('background-color: white')

        # Create a horizontal layout and add the images to it
        self.layout = QHBoxLayout()
        self.left_image = QLabel(self)
        self.left_image.setPixmap(QPixmap('sport_man.jpg'))
        self.left_image.setFixedSize(100, 400)
        self.layout.addWidget(self.left_image)
        self.right_image = QLabel(self)
        self.right_image.setPixmap(QPixmap('sitting_man.webp'))
        self.left_image.setFixedSize(1000, 1000)
        self.layout.addWidget(self.right_image)

        # Add the layout to the opening page
        self.opening_page.setLayout(self.layout)

        # Add the opening page to the stacked widget
        self.stacked_widget.addWidget(self.opening_page)

        # Set the opening page as the current page
        self.stacked_widget.setCurrentIndex(0)

        # Create a layout and add the stacked widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()