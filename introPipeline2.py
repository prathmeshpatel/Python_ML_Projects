#import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
Y = iris.target

#split into train and test
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = .5)
#test_size = .5 means half data used for test

#import classifier
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

#use train to train a classifier
my_classifier.fit(X_train, Y_train)

#use test to test accuracy
predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print accuracy_score(Y_test, predictions)