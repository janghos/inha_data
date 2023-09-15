# 윈도우에서 사용 가능한 형태소 분석기는 꼬꼬마 분석기밖에 없었음
# 꼬꼬마 분석기가 반복되는 단어 이모티콘[ex) ㅋㅋ, ㅎㅎ]이 많이 포함된 문자열을 분석할 수 없음 -> soynlp 모듈 사용으로 해결
# 의미 없는 단어[ex) ㅂㄷㅂㄷㅂㄷㅂㄷ]의 반복도 약 18단어 정도 반복되면 프로그램이 멈춤 -> 미해결
from konlpy.tag import Kkma
from soynlp.normalizer import *

if __name__ == "__main__":
    kkma = Kkma()
    trainDataset = []
    with open("dataset.txt", "r", encoding='UTF-8') as f:
        for line in f:
            # 문장 좌우 공백 제거, 훈련 데이터셋의 구분자인 | 를 기준으로 문자열 분할
            dataArray = line.strip().split('|')
            trainDataset.append((dataArray[0], dataArray[1]))
    testDataset = [
        '좆두 왜 풀캠이냐??',
        '이정도면 졸업 가능한가요?',
        '피파24 환불신청함',
        '준내큰 sbc 안나오나',
        '드디어 뚫었다...',
        '94픽 4좆',
        '전국적인 탕후루 열풍에 대한 네이버기사 댓글ㅋㅋㅋㅋ',
        '뭐해 새끼들아 ㅋㅋ 올려 ㅋㅋ',
        '블래스터 상향좀 시발련들아',
        '중국인 창깨들의 만행'
    ]
    for data in trainDataset:
        print("%s, %s" % (kkma.pos(emoticon_normalize(data[0], num_repeats=2)), data[1]))
