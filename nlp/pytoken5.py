from konlpy.tag import Komoran
import numpy as np

# Komoran 객체 생성
komo = Komoran()

# 분석할 텍스트
text = "오늘 날씨는 구름이 많아요."

# 명사 추출
nouns = komo.nouns(text)
print(nouns)

# 단어 사전 구축 및 인덱스 부여
dics = {}
for word in nouns:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)

# 원-핫 인코딩
nb_classes = len(dics)
targets = list(dics.values())
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)
