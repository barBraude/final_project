import joblib
import pandas as pd
x_test_scaled = joblib.load('svm_Model_X_test_scaled.csv')
y_test = joblib.load('svm_Model_y_test.csv')
print(type(x_test_scaled))
label_test = pd.Series(y_test).array
print("****************** Y TEST *******************")
for index, value in enumerate(label_test):
    print(f'Index: {index}, Value: {value}')
print("****************** X TEST SCALED *******************")
# for index, value in enumerate(x_test_scaled):
#     print(f'Index: {index}, Value: {value}')


#0 
x_text_low = x_test_scaled[6]
label_test_low = label_test[6]
print("x_text_low :",x_text_low, "label_test_low :",label_test_low) 
#1
x_text_medium = x_test_scaled[1]
label_test_medium = label_test[1]
print("x_text_medium :",x_text_medium, "label_test_medium :",label_test_medium)
#5
x_text_high = x_test_scaled[7]
label_test_high = label_test[7]


x_text_low_wrong = x_test_scaled[0]
label_test_low_wrong = label_test[0]

# df = pd.DataFrame(x_text_low)

# # Save the DataFrame to a CSV file
# df.to_csv('x_text_low.csv', index=False)

import pickle
# #NEED TO CHANGE THE FILE NAME EACH TIME WHEN DUMP
# Pkl_Filename = "x_text_high.csv"  

# with open(Pkl_Filename, 'wb') as file:  
#     pickle.dump(x_text_high, file)

# Pkl_Filename = "x_text_low.csv"  

# with open(Pkl_Filename, 'wb') as file:  
#     pickle.dump(x_text_low, file)

# Pkl_Filename = "x_text_medium.csv"  

# with open(Pkl_Filename, 'wb') as file:  
#     pickle.dump(x_text_medium, file)

Pkl_Filename = "x_text_low_wrong.csv"  

with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(x_text_low_wrong, file)