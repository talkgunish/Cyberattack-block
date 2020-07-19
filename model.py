import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv('/root/logs.csv')
X =  df.iloc[: , :].to_numpy()
label = LabelEncoder()

dataset = pd.concat([pd.DataFrame(label.fit_transform(X[:,0]), columns=["clientip"]) , pd.DataFrame(label.fit_transform(X[:,1]) , columns=["timestamp"]) ,  pd.DataFrame(label.fit_transform(X[:,2]), columns=["url"])] , axis=1)

src = StandardScaler()
data_scaled = src.fit_transform(dataset)

model = KMeans()
model.fit(data_scaled)
pred  =  model.fit_predict(data_scaled)
data_scaled = pd.DataFrame(data_scaled  ,columns=['clientip'  ,'timestamp' , 'url'])
data_scaled['cluster name'] = pred

IPs_result = pd.concat([df['clientip'] , dataset['clientip']] , axis=1)

def CountFrequency(ilist , ilabel):       
                                        f = {}
                                        for item in ilist:
                                                          if(item in freq):
                                                              f[item] +=1
                                                          else:
                                                              f[item] = 1

                                        mf = 0
                                        mk = 0
                                        for key , value in f.items():
                                                                      if value > mf:
                                                                          mf = value                    
                                                                          mk = key

                                        return ilabel[ilist.index(mk)]

ip_res = CountFrequency(IPs_result['clientip'].tolist(), IPs_result['clientip'].tolist())

file = open("/root/block.txt","w")
file.write(ip_res)
file.close()
