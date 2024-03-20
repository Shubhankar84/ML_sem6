from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Load data
cancer_data = datasets.load_breast_cancer()

print(cancer_data.data.shape)

print("display the targe values")
print(cancer_data.target)


# Split data in training and testing
X_train, X_test, y_train, y_test = train_test_split(cancer_data.data, cancer_data.target, test_size=0.4, random_state=109)

cls = svm.SVC(kernel='linear')

# Train the model
cls.fit(X_train, y_train)

# make predections
pred = cls.predict(X_test)


print("Accuracy:", metrics.accuracy_score(y_test, y_pred=pred))
print("Precision:", metrics.precision_score(y_test, y_pred=pred))
print("Recall:", metrics.recall_score(y_test, y_pred=pred))
print("\nClassification Report:\n", metrics.classification_report(y_test, y_pred=pred))