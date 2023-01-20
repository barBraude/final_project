# Final Project

The main goal of this project is to be able to predict the risk of having a cardiovascular disease based physical activity and sitting habits as well as other health factors.
The data used in this project will be subjected to a process of cleaning and scaling, then supervised algorithms such as SVM, Logistic Regression, Random Forest and Knn will be implemented. 
The solution will be presented in percentages and the data will be categorized into 3 groups of risk severity: High-Risk, Medium-Risk, and Low-Risk.

## Get Started
To get starts please follow the steps below:

# Clone The project
Open the terminal and copy this command 

(if the terminal is not recognize the command , please download git to your computer)

`git clone https://github.com/barBraude/final_project.git`

## Train And Test
### To train and test our 4 models
1. Open `Prediction_Of_CVD_Risk_Following__A_Sedentary_Lifestyle.ipynb`
2. Upload to your drive `mockdata.xlsx` file 
3. Copy the `file path` from your drive
4. Insert to the right cell your `file path`
5. In the top menu `Runtime` --> `Run all`

## Prediction
### Create Python environment

Create and activate the virtual environment (for Windows)

We used version 3.10

1. `py -3 -m venv .venv`
2. `.venv\scripts\activate`
3. `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
4. Select your new environment by using the **Python: Select Interpreter** command from the **Command Palette.**
5. Install Python packages with this commend  : `pip install -r requirements.txt`
6. Run main.py

For more information :  https://code.visualstudio.com/docs/python/python-tutorial#_install-and-use-packages



