#데이터셋 불러오기
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
train = pd.read_csv('train.csv.zip')
test = pd.read_csv('test.csv.zip')
store = pd.read_csv('stores.csv')
feature = pd.read_csv('features.csv.zip')
sub = pd.read_csv('sampleSubmission.csv.zip')

#데이터 확인
train.info()
train
train=train[train['Weekly_Sales']>-1100] #-1100보다 작은 값은 삭제(이상치 제거)
train['Weekly_Sales'].sort_values()[:20] #이상치 제거 확인
test #종속변수 - Weekly_Sales
store 
feature

#파생변수 생성
fuel_cpi=feature.groupby('Store')['Fuel_Price','CPI'].agg(['median','min','max'])
temperature=feature.drop(['Store','Date','Fuel_Price','MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5','CPI','Unemployment','IsHoliday'],axis=1)
unemployment=feature.groupby('Store')['Unemployment'].mean().to_frame('Unemployment_mean')

#파생변수 합치기
alldata=pd.concat([train,test])
alldata=alldata.join(fuel_cpi,on='Store')
alldata=alldata.join(temperature,on='Store')
alldata=alldata.join(unemployment,on='Store')
alldata=pd.merge(alldata,store,on='Store',how='left') #Type변수가 분석에 도움이 될거라 판단하여 합침

#날짜칼럼 Datetime변환
alldata['Date']=pd.to_datetime(alldata['Date'])
alldata['Year']=alldata['Date'].dt.year
alldata['Month']=alldata['Date'].dt.month
alldata['Week']=alldata['Date'].dt.week #평가방식에 week에 가중치를 5배로 두는 조건이 있으므로 매우 중요
alldata['Day']=alldata['Date'].dt.day
alldata['Week_num']=np.ceil(alldata['Day']/7)

#시각화-날짜칼럼
plt.figure(figsize=(16,10))
sns.boxplot(alldata['Week'],alldata['Weekly_Sales'],showfliers=False)#showfliers=False(이상치는 제외)
#시각화-종속변수 값의 분포 확인
sns.distplot(alldata['Weekly_Sales']) #정규분포를 따르지 않으므로 log를 취해야함

#종속변수 이상치 확인
train['Weekly_Sales'].sort_values()[:50] 
#하위 50개의 값 확인결과 - 다른 값들과 큰 편차를 보이는 값 2개(-4988,-3924) 우선제거 필요
#-1098부터는 뒷자리가 98로 끝나는 감소패턴을 보이므로 분석에 필요함을 확인하여 하위 5개(-1321까지)를 삭제한다.
#맨위의 train 데이터를 불러온 시점으로 돌아가 하위 5개 이상치 값 삭제처리

#전처리
alldata.isnull().sum() #결측치는 없는것으로 확인
le=LabelEncoder()
alldata['Type']=le.fit_transform(alldata['Type']) #모델링에 사용하기 위해 인코딩 진행
pd.set_option('display.max_columns',30) #칼럼 모두 보기
alldata['Type'].unique() #Type 변수 인코딩 결과 확인
alldata2=alldata.drop(['Date','Weekly_Sales'],axis=1) #날짜컬럼 및 종속변수 드랍
train2=alldata2[:len(train)]
test2=alldata2[len(train):]

#모델링1
rf=RandomForestRegressor(n_jobs=-1) #n_jobs=-1 빠른 학습을 위해 모든 코어 사용 
rf.fit(train2, np.log(train['Weekly_Sales']+1100)) #모델 학습
result=rf.predict(test2) #예측
result

sub['Weekly_Sales']=np.exp(result)-1100 #로그값 원래대로 반환
sub.to_csv('walmart_rf.csv', index=False)

#모델링2
lgb=LGBMRegressor(n_estimators=300, learning_rate=0.1, num_leaves=2200)
lgb.fit(np.array(train2), np.log(train['Weekly_Sales']+1100)) #2차원 변수(Fuel_Price, median)의 명칭 중복으로 np.array을 이용하여 오류 해결
result2=lgb.predict(np.array(test2))
result2

sub['Weekly_Sales']=np.exp(result2)-1100
sub.to_csv('walmart_lgb.csv', index=False)

#블렌딩
rf_model=pd.read_csv('walmart_rf.csv')
lgb_model=pd.read_csv('walmart_lgb.csv')
sub['Weekly_Sales']=rf_model['Weekly_Sales']*0.6 + lgb_model['Weekly_Sales']*0.4
sub.to_csv('Final_Walmart.csv', index=False)
#최종점수 2539점 - 12위
