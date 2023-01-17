import joblib
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import metrics
import pandas as pd
import seaborn as sn

# load the model
svm_loaded_model = joblib.load('model/svm_model.pkl')
model = svm_loaded_model.best_estimator_
# test values for the model
x_test_scaled = joblib.load('model/X_test_scaled.csv')
# labels for the test values
y_test = joblib.load('model/y_test.csv')
label_test = pd.Series(y_test).array
label_prediction = model.predict(x_test_scaled)
# print(label_prediction)
 
confusion_matrix = metrics.confusion_matrix(label_prediction,label_test, labels=["Low", "Medium", "High"])
reported = metrics.classification_report(label_prediction,label_test,labels=["Low", "Medium", "High"])
print(reported)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ["Low", "Medium", "High"])

cm_display.plot()
plt.show()


print("length:",len(label_test))
print("length:",len(label_prediction))

print(f'Low Risk')

TP = 0 #The model correctly identifies a case as Low-Risk
FP = 0 #The model incorrectly identifies a case as Low-Risk
FN = 0 #The model incorrectly identifies a case as Medium-Risk or High-Risk
TN = 0 #The model correctly identifies a case as Medium-Risk or High-Risk

# Low Risk
for true,pred in zip(label_test,label_prediction):
      


    if true == 'Low' and pred == 'Low' :
        TP += 1
    elif (pred == 'Medium' or pred == 'High') and (true == 'Medium' or true == 'High'):
        TN += 1
    elif pred == 'Low' and (true == 'Medium' or true == 'High'):
        FP += 1
    elif (pred == 'Medium' or pred == 'High') and true == 'Low':
        FN += 1


TPR = TP / (TP + FN)
FPR = 1 - (TN / (TN + FP))
Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)

print(f'True Positive  {TP}')
print(f'True Negative {TN}')
print(f'False Positive {FP}')
print(f'False Negative {FN}')

# print(f'True Positive Rate (TPR) {TPR}')
# print(f'False Positive Rate (FPR) {FPR}')
print(f'Accuracy  {Accuracy}')
print(f'Precision  {Precision}')  

print(f'Medium Risk')

TP = 0 #The model correctly identifies a case as Low-Risk
FP = 0 #The model incorrectly identifies a case as Low-Risk
FN = 0 #The model incorrectly identifies a case as Medium-Risk or High-Risk
TN = 0 #The model correctly identifies a case as Medium-Risk or High-Risk


# Medium Risk
for true,pred in zip(label_test,label_prediction):
      

    # 2 - positive, 3 - negative
    if true == 'Medium' and pred == 'Medium' :
        TP += 1
    elif (pred == 'Low' or pred == 'High') and (true == 'Low' or true == 'High'):
        TN += 1
    elif pred == 'Medium' and (true == 'Low' or true == 'High'):
        FP += 1
    elif (pred == 'Low' or pred == 'High') and true == 'Medium':
        FN += 1


TPR = TP / (TP + FN)
FPR = 1 - (TN / (TN + FP))
Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)

print(f'True Positive  {TP}')
print(f'True Negative {TN}')
print(f'False Positive {FP}')
print(f'False Negative {FN}')

# print(f'True Positive Rate (TPR) {TPR}')
# print(f'False Positive Rate (FPR) {FPR}')
print(f'Accuracy  {Accuracy}')
print(f'Precision  {Precision}')  


print(f'High Risk')

TP = 0 #The model correctly identifies a case as Low-Risk
FP = 0 #The model incorrectly identifies a case as Low-Risk
FN = 0 #The model incorrectly identifies a case as Medium-Risk or High-Risk
TN = 0 #The model correctly identifies a case as Medium-Risk or High-Risk


# High Risk
for true,pred in zip(label_test,label_prediction):
      

    # 2 - positive, 3 - negative
    if true == 'High' and pred == 'High' :
        TP += 1
    elif (pred == 'Low' or pred == 'Medium') and (true == 'Low' or true == 'Medium'):
        TN += 1
    elif pred == 'High' and (true == 'Low' or true == 'Medium'):
        FP += 1
    elif (pred == 'Low' or pred == 'Medium') and true == 'High':
        FN += 1


TPR = TP / (TP + FN)
FPR = 1 - (TN / (TN + FP))
Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)

print(f'True Positive  {TP}')
print(f'True Negative {TN}')
print(f'False Positive {FP}')
print(f'False Negative {FN}')

# print(f'True Positive Rate (TPR) {TPR}')
# print(f'False Positive Rate (FPR) {FPR}')
print(f'Accuracy  {Accuracy}')
print(f'Precision  {Precision}')  
