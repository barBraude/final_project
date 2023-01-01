import joblib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a button to open the file dialog
        self.button = QPushButton('Open CSV', self)
        self.button.clicked.connect(self.open_csv)

        # Create a table view and a model
        self.table_view = QTableView()
        self.model = QStandardItemModel(self)

        # Set the model for the table view
        self.table_view.setModel(self.model)

        # Create a layout and add the table view and button
        layout = QVBoxLayout(self)
        layout.addWidget(self.table_view)
        layout.addWidget(self.button)

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

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
