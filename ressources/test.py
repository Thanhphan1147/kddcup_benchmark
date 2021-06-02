from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
import datetime

def byte_decoder(val):
    # decodes byte literals to strings
    
    return val.decode('utf-8')

sa_columns = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment",
                           "urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted",
                           "num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login",
                           "is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate",
                           "same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
                           "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
                           "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
                           "dst_host_rerror_rate","dst_host_srv_rerror_rate"]
sf_columns = ["duration", "service", "src_bytes", "dst_bytes"]

sa = datasets.fetch_kddcup99(subset='SA', percent10=False)
dfsa=pd.DataFrame(sa.data, 
                  columns=sa_columns)
assert len(dfsa)>0, "SA dataset not loaded."
dfsa["target"]=sa.target
anomaly_rate_sa = 1.0 - len(dfsa.loc[dfsa["target"]==b'normal.'])/len(dfsa)
print(f"SA anomaly rate is {anomaly_rate_sa:.1%}")


toDecodeSA = ["protocol_type", "service", "flag", "target"]
dfsa["binary_target"] = [1 if x==b'normal.' else -1 for x in dfsa["target"]]    
leSF = preprocessing.LabelEncoder()
for f in toDecodeSA:
    dfsa[f] = list(map(byte_decoder, dfsa[f]))
    dfsa[f] = leSF.fit_transform(dfsa[f])
    
dfsa_normalized = preprocessing.normalize(dfsa.drop(["target", "binary_target"], axis=1))

X_train_sa, X_test_sa, Y_train_sa, Y_test_sa = train_test_split(dfsa.drop(["target", "binary_target"], axis=1), dfsa["binary_target"], test_size=0.33, random_state=0)
X_train_sa_normalized, X_test_sa_normalized, Y_train_sa_normalized, Y_test_sa_normalized = train_test_split(dfsa_normalized, dfsa["binary_target"], test_size=0.33, random_state=0)
