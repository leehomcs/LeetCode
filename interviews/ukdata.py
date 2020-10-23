import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
filename = "../../../Downloads/pp-complete.csv"

def normalise(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].astype(np.float32).max()
        min_value = df[feature_name].astype(np.float32).min()
        result[feature_name] = (df[feature_name].astype(np.float32) - min_value) / (max_value - min_value)
    return result

##function to train the data and output Coefficient of det on train.
def train_and_evaluate(clf, X_train, y_train, X_test, y_test):
    clf.fit(X_train, y_train)
    # clf.predict(X_test)
    # Make predictions using the testing set
    y_pred = clf.predict(X_test)

    # The coefficients
    print('Coefficients: \n', clf.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(y_test, y_pred))

    # Plot outputs
    # plt.scatter(X_test, y_test, color='black')
    # plt.plot(X_test, y_pred, color='blue', linewidth=3)
    #
    # plt.xticks(())
    # plt.yticks(())
    #
    # plt.show()


#read in data. Note "RecordStatus" may not be needed in full file ....
data=pd.read_csv(filename, names=["TUI","Price","DateOfTransfer","Postcode","PropertyType","Old/New", "Duration","PAON", "SAON","Street","Locality","Town","District","County","PPDCategoryType","RecordStatus"])

#drop unwanted/un-needed data. Axis=1 -> column.
data.drop(['TUI','Postcode','Old/New','PAON','SAON', 'Street','Locality', 'District','County','PPDCategoryType','RecordStatus'],axis=1,inplace=True)
data['DateOfTransfer'] = pd.to_datetime(data['DateOfTransfer'])
data['DateOfTransfer']=(data['DateOfTransfer'] - data['DateOfTransfer'].min())/np.timedelta64(1,'D')
data['InLondon'] = ['1' if x=="LONDON" else '0' for x in data.Town]
data.drop('Town',axis=1,inplace=True)
data['Duration']=['1' if x=='F' else '0' for x in data.Duration]
PropertyVals={'S':'1','T':'2','F':'3', 'D':'4', 'O':'5'}
data['PropertyType']=data['PropertyType'].map(PropertyVals)
#remove rows where house prices > 3 std_dev.
data = data.drop(data[data.Price>(data.Price.mean()+2*data.Price.std())].index)

# data.to_csv('data.csv', sep=',', encoding='utf-8')

data = normalise(data)
time = pd.to_datetime('2016-01-01') - pd.to_datetime('1995-01-01')
time = int(str(time).split('days')[0])

# train = data.loc[data['DateOfTransfer']<time]
# test = data.drop(train.index)

# train=normalise(train)
# test=normalise(test)

# train=data.loc[data['DateOfTransfer']<time]
train = data.sample(frac=0.7,random_state=40)
test=data.drop(train.index)


#convert train dataframe to numpy array
x_np_train=train.values[:,1:].astype(np.float32)
y_np_train=train.values[:,0].astype(np.float32)

#convert test dataframe to numpy array
x_np_test=test.values[:,1:].astype(np.float32)
y_np_test=test.values[:,0].astype(np.float32)
print(en(y_np_test))
print(len(y_np_train))

linear=linear_model.LinearRegression()
print("LinReg: ", train_and_evaluate(linear,x_np_train,y_np_train,x_np_test,y_np_test), "\n")