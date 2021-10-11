import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
new = pd.read_csv('heart.csv')
col = new.columns
x = new[['Age','RestingBP', 'Cholesterol','FastingBS','MaxHR','Oldpeak']]
y = new ['HeartDisease']

#sns.violinplot(new['HeartDisease'],new['Oldpeak'])
#sns.distplot(new['HeartDisease'],new['Oldpeak])
#plt.show()
X_train , X_test , Y_train , Y_test = train_test_split(x, y, test_size = 0.4)
lm = LinearRegression()
lm.fit(X_train, Y_train)
predictions = lm.predict(X_test)
print('MAE error is:',metrics.mean_squared_error(Y_test, predictions))