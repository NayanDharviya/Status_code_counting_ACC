import pandas as pd
data = pd.read_csv('access_log.txt',sep=" ",names = ['ip_address',"empty1",'empty2','datetime','seconds','url','status_code','code','empty3','system_info'])
data.drop(['empty1','empty2','empty3','seconds'],axis=1,inplace=True)
counts = data['status_code'].value_counts().rename_axis('Status Code').reset_index(name='Counts')
print(counts)


print("\n200 --> OK The request has succeeded\n"
"404 --> Not Found\n"
"304 --> Not Modified\n"
"302 --> Found\n"
"301 --> Moved Permanently\n"
"400 --> Bad Request\n"
"403 --> Forbidden\n")