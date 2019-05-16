import numpy as np
from sklearn import neighbors
from sklearn import svm
from preprocess import preprocess
from feature_extraction import extract_features
from sklearn.metrics import accuracy_score



if __name__ == "__main__":
    target = []
    x = []
    reduce_ratio = 0.8
    for person_num in range(1, 4):
        print("reading data from file", person_num)
        data = np.fromfile(
            "../Data/biometrics/train/s" + str(person_num) + ".txt", sep="\n"
        )
        data = preprocess(data, int(data.shape[0] * reduce_ratio))
        for d in data:
            x.append(extract_features(d))
            target.append(person_num)

    classifier = neighbors.KNeighborsClassifier(n_neighbors=5)

    # print(x, target)

    # classifier = svm.SVC(C=3.0, tol=0.6, kernel="linear", gamma='auto')
    classifier.fit(x, target)
    acc = 0
    for i in range(1, 4):
        test = np.fromfile("../Data/biometrics/test/s{}.txt".format(i), sep="\n")
        test = preprocess(test, int(test.shape[0] * reduce_ratio))
        test_data = []
        truth = []
        for _c in test:
            test_data.append(extract_features(_c))
            truth.append(i)
    pred = classifier.predict(test_data)
    print(accuracy_score(pred, truth))
