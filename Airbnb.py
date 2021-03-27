#라이브러리 설치
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

#데이터 셋 불러오기
train=pd.read_csv('C:/Users/황한희/Desktop/TIL/TIL/train_users_2.csv.zip')
test=pd.read_csv('C:/Users/황한희/Desktop/TIL/TIL/test_users.csv.zip')
ses=pd.read_csv('C:/Users/황한희/Desktop/TIL/TIL/sessions.csv.zip')

#파생변수 생성
var_sec=ses.groupby('user_id')['secs_elapsed'].agg(['median','count']) #id별 행동 지속시간
id_action=ses.groupby('user_id')['action','action_detail','action_type'].nunique().add_prefix('nunique_') #id별 action 관련 칼럼 값 보유수
action_direct=ses.groupby(['user_id','action'])['secs_elapsed'].agg(len).unstack() #직접적인 통계치 (002qnbzfs5의 action 중 10의 행동을 한 데이터가 9개 있다는 뜻)

#데이터 프로세싱
alldata=pd.concat([train,test])
alldata=alldata.rename(columns={'id':'user_id'}) #파생변수와 합병의 기준이 되는 'id'칼럼명 동일하게 수정
alldata=alldata.join(var_sec,on='user_id')
alldata=alldata.join(id_action,on='user_id')
alldata=alldata.join(action_direct,on='user_id')


#시각화
plt.figure(figsize=(13,10))
sns.boxplot(alldata['country_destination'],alldata['count'], showfliers=False) #id별 행동시간에 관한 값의 수가 NDF와 PL이 큰 차이가 안보임
sns.boxplot(alldata['country_destination'],alldata['nunique_action'], showfliers=False) #행동관련 값은 NDF와 PL의 차이가 잘 나타남

#데이터 프로세싱2
alldata2=alldata.drop(['user_id','date_account_created','timestamp_first_active','date_first_booking','country_destination'],axis=1)
le=LabelEncoder()
cat_col=alldata2.columns[alldata2.dtypes==object]
for i in cat_col:
    alldata2[i]=le.fit_transform(alldata2[i])
alldata2=alldata2.fillna(-1)
train2=alldata2[:len(train)]
test2=alldata2[len(train):]
alldata2

#종속변수 LabelEncoder
labels=train['country_destination']
y=le.fit_transform(labels)

#모델링
rf=RandomForestClassifier(n_jobs=-1)
rf.fit(train2, y)
result=rf.predict_proba(test2)

#종속변수 값을 국가이름(문자열)로 재변환 시켜줘야함 & 평가방식 : 각 아이디 당 여행 예측 국가 높은 확률별로 상위 5개까지 데이터 기입할 것
ids=[]
cts=[]
id_test=test['id']
for i in range(len(id_test)):
    idx=id_test[i]
    ids+=[idx]*5
    cts+=le.inverse_transform(np.argsort(result)[::-1])[:5].tolist()
    
#sub파일 생성
sub=pd.DataFrame(np.column_stack((ids,cts)), columns=['id','country'])
sub.to_csv('Airbnb.csv' , index=False)
