# ECG on biometrics

---

###  Outline

- Intro

- Bakcground

- Implementation

- Result


---

## Intro

#### __ECG signal__

Electrocardiography (ECG) is a graphical representation of the electrical activity of the heart over a period of time which is recorded by the electrodes connected to the body either using three leads or twelve leads attached to the surface of the skin. Visual inspection of each heart beat within an ECG trace reveals three prominent excursions from baseline. These
excursions are termed waves – and are labeled P, QRS and T waves, which occur in this
temporal order.

## Background

#### __Dataset__

We used PTB dataset (sampling rate 1000 HZ). The dataset is splitted into two main parts `train` and `test` each part has 3 files `s1, s2, s3` each file represents an ECG signal for a separate person.
![ecg-vis](./ecg.png)
> heart beats vissualization

```shell
|-Train\
|--| s1.txt
|--| s2.txt
|--| s3.txt
|-Test\
|--| s1.txt
|--| s2.txt
|--| s3.txt
```
> data folder structure

#### __Preprocessing__

The goal of preprocessing is to clean the signal from noise and outliers and prepare it for feature extraction and classification.

The steps for preprocessing are:

 - `remove_mean`

 	In genral classification algorithms tends to fit more with _standardlized_ data, so we apply mean removal which works by calculating the average mean for the data set (summation over length) and calculate that value from each data point.

 - `butter_bandpass_filter`

   The goal of butter bandpass filter is to remove noise data like Electromagnetic fields that happens to be outlied within the data.

 - `norm`

Data normalization is another step of data _standardlization_ which limits the values between specific range (for our problem we used [-1, 1])

 - `segments`

 We split each person data for segments where each segment consists of 4 hearbeats.

#### __Feature Extraction__

Feature extraction is one of the dimensionality reduction methods. It is used to remove irrelevant or redundant features.

We apply:

- `Auto correlation`

Informally, Autocorrelation is the similarity between observations as a function of the time lag between a signal and itself.

- `Discrete cosine transformation`
The discrete cosine transform (DCT) represents a signal as a sum of sinusoids of varying magnitudes and frequencies. We use DCT to decrease the number of coeffients by mapping the signal to another domain.


#### __Classification__

- Knn


- SVM

--


## Result 
(respective to portion of train data)
#### KNN :

| Distance metric        | Acc. (100%) | Acc.(80%) |
| :-------------: |:-------------:| :-----:|
| euclidean     | 100   |  95.65 |
| manhattan     | 100   |  95.65 |
| chebyshev     | 100   |  95.65 |

#### SVM : 
(with gama = 1/num_of_features)
| kernel      | Acc. (70%) | Acc. (50%) |
| :-------------: |:-------------:| :-----:|
| linear     | 100   |  92.85 |
| poly     | 100   |  100 (keeps getting 100 until 66% data reduction)|
| sigmoid     | 100   |  100 (keeps getting 100 until 96% data reduction)|
| rbf     | 100   |  100 (keeps getting 100 until 96.4% data reduction)|


## Conclusion

The distance metric with KNN doesn't matter as the result is the same, And SVM is way better to solve this problem as rbf(the best kernel to this problem) kernel can get 100% Acc. with only 3.6% of the training data. 
