from sklearn.linear_model import LinearRegression

X = ([['14:56:50','2012-04-12 14:56:50','2012-04-12 15:27:01','2012-04-12 15:42:06']])  # put your dates in here
y = ['1.256400','1.430750','1.369910','1.359350']  # put your kwh in here

model = LinearRegression()
model.fit(X, y)

X_predict = ([['2012-04-13 05:55:30']])  # put the dates of which you want to predict kwh here
y_predict = model.predict(X_predict)