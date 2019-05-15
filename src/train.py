import numpy as np
from sklearn import neighbors
from sklearn import svm
from preprocess import preprocess
from feature_extraction import extract_features


if __name__ == "__main__":
    target = []
    x =[]
    reduce_ratio = 0.8
    for person_num in range(1,4):
        print('reading data from file', person_num)
        data =  np.fromfile('../Data/biometrics/train/s'+str(person_num)+'.txt', sep='\n')
        data = preprocess(data, int(data.shape[0]*reduce_ratio))
        for c in data:
          x.append(extract_features(c))
          target.append(person_num)

    classifier = neighbors.KNeighborsClassifier(n_neighbors=5)

    print(x, target)
    #classifier = svm.SVC(kernel="sigmoid")
    classifier.fit(x,target)

    for i in range(1, 4):
      print('testing for ', i)
      test = np.fromfile('../Data/biometrics/train/s{}.txt'.format(i), sep='\n')
      test = preprocess(test, int(test.shape[0] * reduce_ratio))

      print(classifier.predict(test))
