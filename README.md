# ecg-biometrics

Signal processing Course project

Biometrics is needed where security is essential. The __electrocardiogram__ (ECG) has been used as a significant diagnostic tool for decades.

_It is a recording of the electrical activity of the heart over time_,
reflecting the underlying cardio-physiology of the subject.
Visual inspection of each heart beat within an ECG trace reveals three prominent excursions from baseline.
These excursions are termed waves – and are labeled __P, QRS and T waves__, which occur in this
temporal order.

The physiological and geometrical differences of the heart among individuals
reveal certain uniqueness in their ECG signals.

This allows for suggesting ECG as a new biometric trait.

The lure of utilizing ECG as a biometric trait comes from the fact that ECG as a biological signal is a life indicator.
Thus, it can be used as a tool for aliveness detection.
Moreover, it is difficult to be spoofed or falsified.

In this project, __we need to distinguish between three individuals using their ECG signals__.



### Installation

```shell
virtualenv -p python3.6 env
soruce env/bin/activate
pip install -r requirements.txt
```