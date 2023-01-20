import joblib
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtGui import QFont
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a stacked widget
        self.stacked_widget = QStackedWidget(self)
        # Create the opening page
        self.opening_page = QWidget()
        #create title label
        self.title_label = QLabel(self)
        self.title_label.setGeometry(50,10,420,350)
        self.text_edit=QTextEdit()
        self.title_label.setText("<h1>Welcome To CVD Risk Prediction App<h1>")
        self.title_label.setWordWrap(True)
        self.set_font(self.title_label)

        # Create a QPalette object
        palette = QPalette()
        # Load the image and create a QBrush object with it
        image = QImage(QPixmap("gui/heart-attack.png"))
        #brush = QBrush()
        pixmap = QPixmap(image)
        brush = QBrush(pixmap)
        # Set the brush as the background for the palette
        brush.setTextureImage(image)
        # Set the brush as the background for the palette
        palette.setBrush(QPalette.Background, brush)
        # Apply the palette to the application
        self.opening_page.setPalette(palette)
        
        self.opening_page.setAutoFillBackground(True)
        self.opening_button = QPushButton('Go To Prediction', self.opening_page)
        self.set_button_style(self.opening_button)
        self.opening_button.clicked.connect(self.go_to_main_page)

        self.main_page = QWidget()
        self.open_csv_button = QPushButton('Load CSV File', self)
        self.set_button_style(self.open_csv_button)
        self.open_csv_button.clicked.connect(self.open_csv)
        
        self.back_to_open_screen= QPushButton('Back To Main', self)
        self.set_button_style(self.back_to_open_screen)
        self.back_to_open_screen.clicked.connect(self.go_back_to_open_screen)

        self.desc_label = QLabel(self)
        self.desc_label.setText("""Select data sheet of format type 'CSV' to load your data. \nAfter loading the data, a risk category will be presented based on your data""")
        self.set_font(self.desc_label)
        self.desc_label.setWordWrap(True)

        self.main_page.setStyleSheet("background-color: black")
        
        #result_label
        self.res_label = QLabel(self)
        self.model = QStandardItemModel(self)
    
        # Create a layout and add the table view and button
        layout = QVBoxLayout(self.main_page)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.open_csv_button)
        layout.addWidget(self.back_to_open_screen)
        layout.addWidget(self.res_label)
        # Add the pages to the stacked widget
        self.stacked_widget.addWidget(self.opening_page)
        self.stacked_widget.addWidget(self.main_page)

        # Set the opening page as the current page
        self.stacked_widget.setCurrentIndex(0)

        # Create a layout and add the stacked widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Set the application icon
        app.setWindowIcon(QIcon("gui/heart.png")) 

    
    def open_csv(self):
        # Open the file dialog and get the selected file
        self.desc_label.hide()
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Open CSV', '', 'CSV Files (*.csv)', options=options)
        if file_name:
            # Load the CSV file into a Pandas DataFrame
            data = joblib.load(file_name)

            # Insert the data into the model and train it
            svm_loaded_model = joblib.load('model/svm_model.pkl')
            model = svm_loaded_model.best_estimator_

            if data.ndim != 2:
                data = [data]
            pred = model.predict(data)

            pred_result = ', '.join(pred)
            self.res_label.setText(" Your predicted\nrisk category: \n " + pred_result)
            self.res_label.setGeometry(100,200,420,5000)
            self.setResultBackgroundColor(self.res_label,pred_result)
            self.set_font(self.res_label)

            
            self.model.clear()

    def set_button_style(self,widget):
        widget.setFixedHeight(50)
        widget.setFixedWidth(460)

        font = QtGui.QFont("Caliberi", 15)
        font.setBold(True)
        widget.setFont(font)
        widget.setStyleSheet("background-color: #B2C1FF; border: solid #000000 100px; border-radius: 10px; text-align: center; text-align: center;color: white;")
        widget.move(7, 400)

    def set_font(self,widget):
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setFamily('Caliberi')
        widget.setFont(font)
        widget.setStyleSheet("color: #FFFFFF;")
        widget.setAlignment(QtCore.Qt.AlignCenter)



    def go_to_main_page(self):
        self.stacked_widget.setCurrentIndex(1)
        self.title_label.hide()
        
    
    def go_back_to_open_screen(self):
         self.stacked_widget.setCurrentIndex(0)
         self.title_label.show()

    def setResultBackgroundColor(self,window,color):
        color_dict = {
            "Low": "#9ED6A5",
            "Medium": "#FFE4B0",
            "High": "#FF7575",
            "black": "#000000"
        }
        try:
            window.setStyleSheet("background-color: {}".format(color_dict[color]))
            self.main_page.setStyleSheet("background-color: {}".format(color_dict[color]))
        except KeyError:
            print("Invalid color")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    # Set the window title 
    title = "CVD Risk Prediction"
    window.setWindowTitle(title)
    window.show()
    # Set the window dimensions
    window.setFixedSize(500, 500)
    app.exec_()
