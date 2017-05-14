from sklearn import tree
#[height, weight, shoe size]
#classify male vs female
x = [[72, 160, 11], [65,120, 7], [64, 115, 8], [68, 134, 9],
	 [73, 170, 12], [69, 145, 9], [76, 179, 13], [70, 140, 8],
	 [70, 160, 10], [68, 136, 8],[73, 165, 11]]
y = ['male', 'female', 'female', 'female', 'male', 'male',
	'male','female','male', 'female','male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x, y)

prediction = clf.predict([[69, 145, 10]])

print prediction