from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn import svm
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.svm import OneClassSVM
from sklearn.cluster import DBSCAN

from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
# from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
import datetime

def byte_decoder(val):
    # decodes byte literals to strings
    
    return val.decode('utf-8')

def plot_confusion_matrix(cm, title, classes=['abnormal', 'normal'],
                          cmap=plt.cm.Reds):
    
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90)
    plt.yticks(tick_marks, classes)

    fmt = '.1%'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

sa_columns = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment",
                           "urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted",
                           "num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login",
                           "is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate",
                           "same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
                           "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
                           "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
                           "dst_host_rerror_rate","dst_host_srv_rerror_rate"]
sf_columns = ["duration", "service", "src_bytes", "dst_bytes"]

toDecodeSA = ["protocol_type", "service", "flag", "target"]

toDecodeSF = ["service", "target"]    

# Model wrapper
def Estimators(num_extimators = 100, max_samples = 0.25, contamination = 0.2, eps = 0.2):  
    ifsf = IsolationForest(max_samples=max_samples, random_state=0, contamination=contamination, n_estimators=num_extimators, n_jobs=-1)
    lofsf = LocalOutlierFactor(n_neighbors=15, metric='euclidean', algorithm = 'auto', contamination=contamination, n_jobs=-1)
    ocsvm = OneClassSVM(nu=contamination, kernel="rbf",gamma=0.1)
    dbscan = DBSCAN(eps=eps, min_samples=10, metric='euclidean', algorithm = 'auto', n_jobs=-1)
    return {
        "if": ifsf,
        "lof": lofsf,
        "dbs": dbscan,
        "svm": ocsvm
    }


# def model(estimators = Estimators(), x_train, y_train, x_test, y_test , algorithm = "if"):
#     s = datetime.datetime.now()
#     y_pred = estimators[algorithm].fit(x_train).predict(x_test)
#     t = datetime.datetime.now() - s
#     print(f"trainning finished in {t}")
#     print(classification_report(y_test, y_pred, target_names=['anomaly', 'normal']))
#     print ("AUC: ", "{:.1%}".format(roc_auc_score(y_test, y_pred)))
#     plot_confusion_matrix(confusion_matrix(y_test, y_pred), f"Confusion Matrix for {algorithm} on SF test dataset")
#     return (t, precision_recall_fscore_support(y_test, y_pred, labels=[-1]))

class Model:
    def __init__(self, subset="SF", percent10=False):
        dataset = datasets.fetch_kddcup99(subset=subset, percent10=percent10)
        if subset == "SA":
            columns = sa_columns
            toDecode = toDecodeSA
        else:
            toDecode = toDecodeSF
            columns = sf_columns
        self.df=pd.DataFrame(dataset.data, columns=columns)
        assert len(self.df)>0, f"{subset} dataset not loaded."
        self.df["target"]=dataset.target
        anomaly_rate = 1.0 - len(self.df.loc[self.df["target"]==b'normal.'])/len(self.df)
        print(f"SA anomaly rate is {anomaly_rate:.1%}")

        self.df["binary_target"] = [1 if x==b'normal.' else -1 for x in self.df["target"]]    
        le = preprocessing.LabelEncoder()
        for f in toDecode:
            self.df[f] = list(map(byte_decoder, self.df[f]))
            self.df[f] = le.fit_transform(self.df[f])
        
        a, b, c, d = train_test_split(self.df.drop(["target", "binary_target"], axis=1), self.df["binary_target"], test_size=0.33, random_state=0)
        self.x_train = a
        self.x_test = b
        self.y_train = c
        self.y_test = d
        
        self.estimators = Estimators()
    
    def fit_predict(self, algorithm):
        s = datetime.datetime.now()
        if algorithm == "lof":
            y_pred = self.estimators[algorithm].fit_predict(self.x_test)
        elif algorithm == "dbscan":
            db = self.estimators[algorithm].fit(self.x_test)
            y_pred = [1 if i != -1 else i for i in db.labels_]
        else:
            y_pred = self.estimators[algorithm].fit(self.x_train).predict(self.x_test)
        t = datetime.datetime.now() - s
        print(f"trainning finished in {t}")
        print(classification_report(self.y_test, y_pred, target_names=['anomaly', 'normal']))
        print ("AUC: ", "{:.1%}".format(roc_auc_score(self.y_test, y_pred)))
        plot_confusion_matrix(confusion_matrix(self.y_test, y_pred), f"Confusion Matrix for {algorithm} on SF test dataset")
        return (t, precision_recall_fscore_support(self.y_test, y_pred, labels=[-1]))



