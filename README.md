# Progress history
## W1-2 : 19.04 - 03.05 : Initialize the document, trainning algorithms on default parameters
## W3-4 : 03.05 - 17.05 : Parameter tuning on different configurations
## W5-6 : 17.05 - 31.05 : Increasing the number of anomaly
## W7 : Finalizing

# W3-4 : Parameter tuning and cross-validation search
## Methodology : 
1. Train test split the data, rate = 0.25
2. 3-fold cross-validation on the trainning data so that the test size of each split will be equal to the final test size
3. Apply best parameters to test data
4. Compared with default parameters

## Trainning configuration for specific algorithm :
### OneClass SVM
1. 
	* Dataset: SF 10%
	* Anomaly rate : 4.5%	
	* random_state = 1
	* nu : tuned using gridsearch_cv [0.045, 0.18]
	* kernel : default
	* gamma : default

2. 
	* Dataset: SF 10%
	* Anomaly rate : 4.5%
	* random_state : 2
	* nu: tuned using gridsearch_cv [0.045, 0.18]
	* kernel : poly
	* gamma : default
	* degree : default

3. 
	* Dataset: SF 10%
	* Anomaly rate : 4.5%	
	* random_state = 3
	* nu : tuned using gridsearch_cv [0.045, 0.18]
	* kernel : default
	* gamma : default

### Isolation Forest
1. 
	* Dataset: SF 100%
	* Anomaly rate : 0.5%	
	* random_state = 1
	* contamination : tuned using gridsearch_cv [0.005, 0.2]
	* n_estimator : default
	* max_samples : default

1. 
	* Dataset: SF 100%
	* Anomaly rate : 0.5%	
	* random_state = 2
	* contamination : tuned using gridsearch_cv [0.005, 0.02]
	* n_estimator : default
	* max_samples : default

3. 
	* Dataset: SF 100%
	* Anomaly rate : 0.5%
	* random_state : 3
	* contamination : tuned using gridsearch_cv [0.005, 0.02]
	* n_estimator : default
	* max_samples : default

## Dataset size influence on algorithm's performance :

### Isolation Forest 
1. 
	* Dataset: SF 10%
	* Anomaly rate : 4.5%	
	* random_state = 1
	* contamination : tuned manually [0.045, 0.02]
	* n_estimator : default
	* max_samples : default

2. 
	* Dataset: SF 20%
	* Anomaly rate : 0.5%	
	* random_state = 2
	* contamination : tuned manually [0.005, 0.02]
	* n_estimator : default
	* max_samples : default

3. 
	* Dataset: SF 50%
	* Anomaly rate : 0.5%	
	* random_state = 2
	* contamination : tuned manually [0.005, 0.02]
	* n_estimator : default
	* max_samples : default

5. 
	* Dataset: SF 70%
	* Anomaly rate : 0.5%
	* random_state : 3
	* contamination : tuned manually [0.005, 0.02]
	* n_estimator : default
	* max_samples : default

6. 
	* Dataset: SF 100%
	* Anomaly rate : 0.5%
	* random_state : 4
	* contamination : tuned manually [0.005, 0.02]
	* n_estimator : default
	* max_samples : default

## Anomaly_rate influence on algorithm's performance : 

### Isolation Forest 
1. 
	* Dataset: SF 100%
	* Anomaly rate : 0.5%	
	* random_state = 1
	* contamination : tuned using gridsearch_cv [0.005, 0.02]
	* n_estimator : default
	* max_samples : default

1. 
	* Dataset: SF 20%
	* Anomaly rate : 4.5%	
	* random_state = 2
	* contamination : tuned using gridsearch_cv [0.045, 0.18]
	* n_estimator : default
	* max_samples : default

3. 
	* Dataset: SF 50%
	* Anomaly rate : 10%
	* random_state : 3
	* contamination : tuned using gridsearch_cv [0.01, 0.04]
	* n_estimator : default
	* max_samples : default

4. 
	* Dataset: SF 100%
	* Anomaly rate : 20%
	* random_state : 4
	* contamination : tuned using gridsearch_cv [0.2, 0.8]
	* n_estimator : default
	* max_samples : default

# Author
Phan Trung Thành
