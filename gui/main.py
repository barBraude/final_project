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
        self.title_label.setGeometry(20,10,520,100)
        self.title_label.setTextFormat(Qt.RichText)
        font = QFont("Helvetica", 14)

        # Set the font of the QLabel widget
        self.title_label.setFont(font)
        # Set the text of the QLabel widget
        self.title_label.setText("Welcome to CVD risk prediction application")
        # Create a label to display the image
        # self.image_label = QLabel(self)
        # self.image_label.setGeometry(100,100,300,168)
        # # Create a QPixmap object and load the image from a file
        # pixmap = QPixmap()
        # pixmap.load("back-pain-r.png")
        # self.image_label.setPixmap(pixmap)
       

     
        # Create a QPalette object
        palette = QPalette()

        # Load the image and create a QBrush object with it
        image = QImage(QPixmap("back-pain-r.png"))
        #brush = QBrush()
        pixmap = QPixmap('image.png')
       # pixmap.setTextureRepeat(False)
        brush = QBrush(pixmap)
        # Set the brush as the background for the palette
        brush.setTextureImage(image)

        # Disable repeating
        #pixmap.setTextureRepeat(False)

        # Set the brush as the background for the palette
        palette.setBrush(QPalette.Background, brush)
        brush.setTransform(QTransform().scale(1,1))
        # Apply the palette to the application
        app.setPalette(palette)
        
        
       
        self.opening_button = QPushButton('Go to prediction', self.opening_page)
        # Set the button location and size
        self.opening_button.setGeometry(160, 400, 150, 40)
        self.opening_button.setStyleSheet("font: 9pt Helvetica;")
        self.opening_button.clicked.connect(self.go_to_main_page)
        # Create the main page
        self.main_page = QWidget()
        
        # Create a button to open the file dialog
        self.button = QPushButton('Open CSV', self)
        self.button.clicked.connect(self.open_csv)

        # Create a table view and a model
        self.table_view = QTableView()
        self.model = QStandardItemModel(self)

        # Set the model for the table view
        self.table_view.setModel(self.model)

        # Create a layout and add the table view and button
        layout = QVBoxLayout(self.main_page)
        layout.addWidget(self.table_view)
        layout.addWidget(self.button)

        # Add the pages to the stacked widget
        self.stacked_widget.addWidget(self.opening_page)
        self.stacked_widget.addWidget(self.main_page)

        # Set the opening page as the current page
        self.stacked_widget.setCurrentIndex(0)

         # Create a layout and add the stacked widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Set the application icon
        app.setWindowIcon(QIcon("sitting-icon.png"))

        

    def open_csv(self):
        # Open the file dialog and get the selected file
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
            svm_loaded_model = joblib.load('svm_Model_24.12.pkl')
            model = svm_loaded_model.best_estimator_

            if data.ndim != 2:
                data = [data]
            pred = model.predict(data)


            # Clear the model
            self.model.clear()

            # Set the column names
            self.model.setHorizontalHeaderLabels(['The Result'] )

            # Add the data to the model
            for row in pred:
                items = [QStandardItem(str(row))]
                self.model.appendRow(items)

            # Resize the columns
            self.table_view.resizeColumnsToContents()
            # print(pred)

    def go_to_main_page(self):
        self.stacked_widget.setCurrentIndex(1)
        self.title_label.hide()
        #self.image_label.hide()


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
