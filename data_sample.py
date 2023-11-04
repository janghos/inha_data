import pandas as pd
import matplotlib.pyplot as plt
from konlpy.tag import Okt
plt.rcParams['font.family'] = 'Malgun Gothic'


# CSV 파일 읽기
df = pd.read_csv("output.csv")

# 'hit' 열의 데이터를 숫자로 변환
def convert_hit_to_number(hit_str):
    if 'k' in hit_str:
        return int(float(hit_str.replace(' k', '')) * 1000)
    else:
        return int(hit_str)

df['hit'] = df['hit'].apply(convert_hit_to_number)

# 조회수 상위 10% 데이터 추출
top_10_percent = df.nlargest(int(len(df) * 0.1), 'hit')

# 형태소 분석을 위한 KoNLPy 초기화
okt = Okt()

# 형태소 분석하여 단어 추출
words = []
for title in top_10_percent['title']:
    words += okt.nouns(title)

# 단어 빈도수 계산
word_counts = pd.Series(words).value_counts()

# 상위 20개의 단어 추출
top_words = word_counts.head(20)

# 그래프 그리기
plt.figure(figsize=(12, 6))
top_words.plot(kind='bar')
plt.title("상위 20개 형태소 단어 및 빈도수")
plt.xlabel("단어")
plt.ylabel("빈도수")
plt.xticks(rotation=45)
plt.show()