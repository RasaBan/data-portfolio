import numpy as np
import pandas as pd
import pip
from numpy.distutils.system_info import conda
from pip._internal.commands import install
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split



df= pd.read_csv("bank-additional-full.csv")[["age", 'job', 'marital', 'education', 'housing', 'loan', 'contact', 'month',
                                             'day_of_week', 'duration', 'campaign','previous', 'y']]
print(df.info())

# sumazint ieducation grupiu:
df["education"]= np.where(df["education"] =='basic.9y', 'Basic', df["education"])
df["education"]= np.where(df["education"] =='basic.6y', 'Basic', df["education"])
df["education"]= np.where(df["education"] =='basic.4y', 'Basic', df["education"])
#print(df["education"].unique())

# sukuirami dummies (2 reismes pagal Y= 0arba 1), objects reiksmes paverciamos kaip stulpeliai, susidaro daug kategoriju:
cat_vars=['job','marital','education','housing','loan','contact','month','day_of_week']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(df[var], prefix=var)
    data1=df.join(cat_list)
    df=data1
cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week']
data_vars=df.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]
data_final=df[to_keep]
print(data_final.columns.values)

#SMOTE
# X = data_final.loc[:, data_final.columns != 'y']
# y = data_final.loc[:, data_final.columns == 'y']
#
#
#
# os = SMOTE(random_state=0)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# columns = X_train.columns
#
# os_data_X,os_data_y=os.fit_sample(X_train, y_train)
# os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
# os_data_y= pd.DataFrame(data=os_data_y,columns=['y'])
#
# # we can Check the numbers of our data
# print("length of oversampled data is ",len(os_data_X))
# print("Number of no subscription in oversampled data",len(os_data_y[os_data_y['y']==0]))
# print("Number of subscription",len(os_data_y[os_data_y['y']==1]))
# print("Proportion of no subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==0])/len(os_data_X))
# print("Proportion of subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==1])/len(os_data_X))

xTrain, xTest, yTrain, yTest = train_test_split(data_final.drop(["y"], axis=1), df["y"], test_size = 0.2)
logReg = LogisticRegression()
logReg.fit(xTrain, yTrain)
print(logReg.score(xTest, yTest))