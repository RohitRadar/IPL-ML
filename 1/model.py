import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
data = pd.read_csv('1/clean2.csv', sep=",")
# split into input (X) and output (y) variables
X = data[['season', 'matchno', 'venue', 'innings','batsmen','bowlers', 'che', 'ban', 'del','hyd', 'kol', 'mum', 'pun', 'rr']]
y = data[['runs']]
# define the keras model
model = Sequential()
model.add(Dense(14, input_dim=14, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(68, activation='relu'))
model.add(Dense(42, activation='relu'))
model.add(Dense(1, activation='softmax'))
# compile the keras model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=100)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))