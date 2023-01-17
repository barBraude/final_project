from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a stacked widget
        self.stacked_widget = QStackedWidget(self)

        # Create the opening page
        self.opening_page = QWidget()
        self.opening_page.setStyleSheet('background-color: blue')
        self.opening_label = QLabel('This is the opening page', self.opening_page)
        self.opening_label.setStyleSheet('color: white')
        self.opening_button = QPushButton('Go to main page', self.opening_page)
        self.opening_button.clicked.connect(self.go_to_main_page)
        layout = QVBoxLayout(self.opening_page)
        layout.addWidget(self.opening_label)
        layout.addWidget(self.opening_button)

        # Create the main page
        self.main_page = QWidget()
        self.main_page.setStyleSheet('background-color: green')
        self.main_label = QLabel('This is the main page', self.main_page)
        self.main_label.setStyleSheet('color: white')
        self.main_button = QPushButton('Go to opening page', self.main_page)
        self.main_button.clicked.connect(self.go_to_opening_page)
        layout = QVBoxLayout(self.main_page)
        layout.addWidget(self.main_label)
        layout.addWidget(self.main_button)

        # Add the pages to the stacked widget
        self.stacked_widget.addWidget(self.opening_page)
        self.stacked_widget.addWidget(self.main_page)

        # Set the opening page as the current page
        self.stacked_widget.setCurrentIndex(0)

        # Create a layout and add the stacked widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

    def go_to_main_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_opening_page(self):
        self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()