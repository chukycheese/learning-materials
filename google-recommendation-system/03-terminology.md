---
marp: true
---

# 용어

---

## Items (또는 documents)

* 시스템이 추천하는 항목
* 구글 플레이스토어에서는 설치하라고 추천하는 앱
* 유튜브에서는 영상이 item

---

## Query (또는 context)

* 시스템이 추천에 사용하는 정보
* 사용자 정보 (user information)
  * 사용자 ID
  * 이전에 이용한 item
* 추가 맥락 (context)
  * 사용자의 기기
  * 사용 시간

---

## 임베딩 (Embedding)

* 유한 집합 (이 경우에서는 query 집합 또는 추천하고자 하는 item) 에서 임베딩 공간 (embedding space) 라고 부르는 벡터 공간으로의 매핑
* 많은 추천 시스템이 query 와 item 의 적절한 임베딩 표현을 학습하는 것에 의존
