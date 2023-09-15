import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# 욕설 데이터셋을 읽어옵니다.
df = pd.read_csv("./data.csv", encoding='cp949')

# 욕설 데이터셋을 학습 데이터셋과 테스트 데이터셋으로 나눕니다.
X_train, X_test, y_train, y_test = train_test_split(
    df["A"], df["B"], test_size=0.2, random_state=42
)

# TF-IDF 벡터화 객체를 생성합니다.
tfidf_vectorizer = TfidfVectorizer()

# 학습 데이터와 테스트 데이터에 TF-IDF 변환을 적용합니다.
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# 욕설 분류 모델을 생성합니다.
model = LogisticRegression()

# 모델을 학습합니다.
model.fit(X_train_tfidf, y_train)

# 테스트 데이터셋에서 모델의 성능을 평가합니다.
print(model.score(X_test_tfidf, y_test))