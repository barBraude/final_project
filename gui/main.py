import joblib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QFont



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a stacked widget
        self.stacked_widget = QStackedWidget(self)
        # Create the opening page
        self.opening_page = QWidget()
        #create title label
        self.title_label = QLabel(self)
        self.title_label.setGeometry(45,120,400,100)
        self.text_edit=QTextEdit()
        font = QFont("Segoe UI ", 10)
        # Set the font of the QLabel widget
        self.title_label.setFont(font)
        # Set the text of the QLabel widget
        self.title_label.setText("<h1>Welcome to CVD risk prediction App<h1>")
        self.title_label.setWordWrap(True)
        self.title_label.setStyleSheet("color: #E3DECB;")
        # Create a QPalette object
        palette = QPalette()
        # Load the image and create a QBrush object with it
        image = QImage(QPixmap("gui/heart-attack.png"))
        #brush = QBrush()
        pixmap = QPixmap(image)
       
        brush = QBrush(pixmap)
        # Set the brush as the background for the palette
        brush.setTextureImage(image)

        # Disable repeating
        #brush.setTextureRepeat(False)

        # Set the brush as the background for the palette
        palette.setBrush(QPalette.Background, brush)
        brush.setTransform(QTransform().scale(1,1))
        # Apply the palette to the application
        self.opening_page.setPalette(palette)
        self.opening_page.setAutoFillBackground(True)
        self.opening_page.setStyleSheet("position : 100px ;")
        self.opening_button = QPushButton('Go to prediction', self.opening_page)
        # Set the button location and size
        self.opening_button.setGeometry(160, 400, 150, 40)
        self.opening_button.setStyleSheet("font: 9pt Segoe UI Semibold; background-color: #EEEEEA")
        self.opening_button.clicked.connect(self.go_to_main_page)
        # Create the main page
        self.main_page = QWidget()
        
        # Create a button to open the file dialog
        self.open_csv_button = QPushButton('Load CSV file', self)

        self.open_csv_button.setStyleSheet("font: 9pt Segoe UI Semibold; background-color: #EEEEEA")
        self.open_csv_button.clicked.connect(self.open_csv)
        
        self.back_to_open_screen= QPushButton('Back to main screen', self)
        self.back_to_open_screen.setStyleSheet("font: 9pt Segoe UI Semibold; background-color: #EEEEEA")
        self.back_to_open_screen.clicked.connect(self.go_back_to_open_screen)
       
        #add label for descriptin
        self.desc_label = QLabel(self)
        self.desc_label.setText("""Select data sheet of format type 'CSV' to load your data. \nAfter loading the data, a risk category will be presented based on your data""")
        self.desc_label.setStyleSheet("font: 11pt Segoe UI Semibold;")
        self.desc_label.setWordWrap(True)
        
        #result_label
        self.res_label = QLabel(self)
        # self.res_label.setStyleSheet("font: 14pt Segoe UI bold; background-color: #E3DECB")
        
        # Create a table view and a model
        #self.table_view = QTableView()
        self.model = QStandardItemModel(self)
    
        # Create a layout and add the table view and button
        layout = QVBoxLayout(self.main_page)
        # layout.addWidget(self.table_view)
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
        app.setWindowIcon(QIcon("heart.png")) 

    
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

            # Preprocess the data
            # ...

            # Insert the data into the model and train it
            svm_loaded_model = joblib.load('model/svm_model.pkl')
            model = svm_loaded_model.best_estimator_

            if data.ndim != 2:
                data = [data]
            pred = model.predict(data)

            pred_result = ', '.join(pred)
            self.res_label.setStyleSheet("QLabel { text-align: center; }")
            self.res_label.setText(" Your predicted risk category is: \n " + pred_result)
            self.setResultBackgroundColor(self.res_label,pred_result)
            # print(pred_result)
            # Clear the model
            self.model.clear()


    def go_to_main_page(self):
        self.stacked_widget.setCurrentIndex(1)
        self.title_label.hide()
        
    
    def go_back_to_open_screen(self):
         self.stacked_widget.setCurrentIndex(0)
         self.title_label.show()

    def setResultBackgroundColor(self,window,color):
        #change typo in meduim
        color_dict = {
            "Low": "#9ED6A5",
            "Medium": "#FFF2CC",
            "High": "#FF7575"
        }
        try:
            window.setStyleSheet("background-color: {}".format(color_dict[color]))
        except KeyError:
            print("Invalid color")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    # Set the window title 
    title = "CVD risk pediction"
    window.setWindowTitle(title)
    window.show()
    # Set the window dimensions
    window.setFixedSize(500, 500)
    app.exec_()
