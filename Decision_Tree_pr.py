#라이브러리 설치
import pandas as pd
import numpy as np

#실습 파일 불러오기
tennis_df=pd.read_csv('playtennis.csv')
tennis_df

#데이터 수치화 - 기초(replace)
tennis_df['Outlook'] = tennis_df['Outlook'].replace('Sunny',0)
tennis_df['Outlook'].replace('Overcast', 1 , inplace=True) #inplace=True 데이터 셋에 변경내용 바로 저장
tennis_df['Outlook'].replace('Rain', 2, inplace=True)

tennis_df['Temperature'].replace('Hot', 0, inplace=True)
tennis_df['Temperature'].replace('Mild', 1, inplace=True)
tennis_df['Temperature'].replace('Cool', 2, inplace=True)

tennis_df['Humidity'].replace('High', 1, inplace=True)
tennis_df['Humidity'].replace('Normal', 2, inplace=True)

tennis_df['Wind'].replace('Weak', 1, inplace=True)
tennis_df['Wind'].replace('Strong', 2, inplace=True)

tennis_df['PlayTennis'].replace('No', 1, inplace=True)
tennis_df['PlayTennis'].replace('Yes', 2, inplace=True)
tennis_df

#데이터 수치화 - 심화(LabelEncoder)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le_cols = ['Outlook', 'Temperature',	'Humidity', 'Wind',	'PlayTennis' ]
for i in le_cols:
tennis_df[i] = le.fit_transform(tennis_df[i])
tennis_df

#feature 나누기 (x-독립변수, y-종속변수)
x=pd.DataFrame(data=tennis_df, columns=['Outlook', 'Temperature', 'Humidity', 'Wind'])
y=pd.DataFrame(data=tennis_df, columns=['PlayTennis'])

#train, test 스플릿
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(x,y)
#코드 설명
1. 로드(load)된 train_test_split 모듈을 이용해 변수 X에 입력한 4개 컬럼에 대한 데이터와 변수 y에 입력한
Playtennis 컬럼의 데이터를 train(훈련)과 test(테스트)로 구분해, 임의의 개수로 각각 변수 X_train, X_test,
y_train, y_test에 저장
*일반적으로 train / test의 비율 = train(7.5) : test(2.5)

#Decision Tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
dt = DecisionTreeClassifier()
dt.fit(train_x, train_y)
result = dt.predict(test_x)

#정확도(Accuracy) - 모델이 정확하게 분류 또는 예측하는 데이터의 비율
#정확도의 한계 - 분류해야 변수의 비율이 어느정도 비슷하지 않을 겨우 정확도는 부적합한 평가방법

#정확도 파악하기
from sklearn.metrics import accuracy_score
acc = accuracy_score(test_y, result)
acc

#export_graphviz
import pydotplus
from IPython.core.display import Image
feature_names = tennis_df.columns.tolist()[0:4]
target_name = np.array(['Play NO', 'Play Yes'])
dt_dot_data = export_graphviz(dt, feature_names=feature_names,
                                class_names=target_name,
                                rounded=True, filled=True,
                                special_characters=True)
dt_graph = pydotplus.graph_from_dot_data(dt_dot_data)
Image(dt_graph.create_png())