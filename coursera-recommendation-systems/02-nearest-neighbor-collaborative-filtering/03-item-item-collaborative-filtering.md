# Item-Item Collaborative Filtering Recommendation

## Introduction to Item-Item Collaborative Filtering

### Motivation

* User-User CF 도 잘 작동하긴 하지만, ...
* Sparcity 문제
  * 큰 아이템 집합과 더 큰 사용자 집합이 있는 경우에는 평점 수가 적어지고, 추천이 불가능한 경우가 빈번히 발생
  * 이를 해결하기 위한 다양한 방법이 존재함
    * filterbot: 인위적이지만 체계적인 평점을 줘서 density 를 만드는 방법
    * item-item: 연산 축을 바꿔서 계산
    * 차원 축소 (dimensionality reduction)
* 계산 성능
  * 수백만(또는 그 이상) 명의 사용자가 있는 경우 모든 쌍의 상관관계를 계산하는 것은 연산 비용이 비쌈
  * 점진적으로 갱신해나가는 방법조차도 비쌈
  * 그리고 사용자 프로파일이 빠르가 바뀔 수 있음
    * 사용자를 만족시키기 위해서는 실시간으로 연산해야함
    * 특히 평가를 적게 한 경우라면 추가적인 평가에 따라 추천이 크게 바뀌기도 함

### Item-Item: An Alternative

* [Item-based collaboriatve filtering recommendation algorithms: Badrul Sarwar, George Karypis, Joseph Konstan, and John Riedl, 2001](http://files.grouplens.org/papers/www10_sarwar.pdf)
  
### The Item-Item Insight

* Item-Item 유사도는 비교적 안정적임
  * 아이템 유사도: 특징에 기반한 유사도가 아님. 사용자의 선호에 대한 유사성으로, 한 아이템을 좋아한 또는 구매한 사용자가 다른 아이템도 좋아하는가.
  * 특히 아이템의 개수보다 사용자의 숫자가 훨씬 많은 경우
    * 평균적인 아이템에 대한 평가 수가 평균적인 사용자 보다 많음 (한 사용자가 여러 개의 아이템에 대한 평가를 할 수 있기 때문)
    * 직관적으로 아이템은 일반적으로 갑자기 바뀌지는 않음 - 최소한 평점 공간에서는 (특별한 경우라면 시간적 제약이 있는 아이템)
* 아이템 유사도는 사용자의 아이템 선호에 대한 예측을 계산하는 방법

### A little more detail

* Two step process:
  * 아이템 쌍들 사이의 유사도를 계산
    * 평점 벡터들의 상관관계
      * 공통적으로 평가가 된 경우에만 (multi-level 평점의 경우에만 유용)
    * 아이템 평점 벡터들의 코사인 (Cosine)
      * multi-level 또는 unary 평점 모두에 사용 가능
      * 또는 수정된 평점 (코사인을 계산하기 전에 사용자의 평점을 normalize 해야함)
    * 조건부 확률
  * user-item 평점 예측: 사용자가 사전에 평가한 아이템을 안다면, 이것들을 고려할 확률이 높으며, 다음에 고려하는 것들을 예측하는 데에 사용하기 좋을 것이라는 데에 기반함
    * 평가한 "아이템 이웃"들의 가중합
    * 평점을 예상하기 위해 선형 회귀 사용

### Item-Item Top-N

* Item-Iteam 유사도 모형은 top-N 을 직접적으로 계산하는데에 사용할 수 있음
  * k 개의 가장 유사한 아이템으로 이루어진 작은 "이웃" 들로 아이템을 제한함으로써 모형을 간소화할 수 있음
  * 아이템의 프로파일 집합을 구할 때, 각각의 프로파일 아이템에 대해 k개의 가장 유사한 아이템들을 계산 / 병합 / 정렬
    * [Item-based top-N recommendation algorithm, Mukund Deshpande and George Karypis, 2004](http://glaros.dtc.umn.edu/gkhome/node/127)

### Benefits of Item-Item

* 매우 잘 작동함
  * 예측 정확도도 좋고
  * top-N 예측은 성능도 좋음
* 구현이 효율적임
  * 적어도 사용자의 숫자가 아이템의 숫자보다 월등히 많은 경우
  * 사전에 계산이 가능한 데에서 오는 이점
* 폭넓게 적용가능하고 유연함
  * 장바구니나 사용자 프로파일에 적용하기 쉬움

### Core Assumptions / Limitations

* Item-Item 관계가 안정적이어야함
  * 대부분은 안정적인 사용자 선호에 따라오는 가정
  * 적용이 어려운 경우가 있을 수 있음 (예: 달력, 수명이 짧은 책 등)
  * 이러한 문제의 많은 경우가 일반적으로 시계열적인 문제
* 주된 제약 / 컴플레인: 우연한 발견을 할 가능성이 낮음
  * 이는 사용자 / 연구자의 불평으로 깊게 연구된 것은 없지만 직관적으로 맞는 말

### Moving Forward

* 다음 강의들에서 다룰 내용들
  * 핵심 Item-Item 알고리즘 자세히 살펴보기
  * 암묵적 피드백(unary rating) 의 특수한 경우에 대해 살펴보기
  * Item-Item 알고리즘을 확장하여 다른 정보와 합쳐보기
  * Item-Item 알고리즘의 실재 - 현업에서의 사용 돌아보기

### Learning Objectives

* Item-Item Collaborative Filtering 의 컨셉과 알고리즘에 대해 설명할 수 있으며, 핵심 튜닝 파라미터와 장단점에 대해 말할 수 있다
* Item-Item Collaborative Filtering 을 작은 데이터셋에 스프레드시트로, 그리고 프로그래밍을 통해 구현할 수 있다
* User-User 그리고 Item-Item 알고리즘의 상대적인 장단점을 이해하고, 특정 상황에서 어떤 알고리즘이 더 적합한지 찾을 수 있다

## Item-Item Algorithm

### Previously

* User-User algorithm

$s(u, i) = \frac{\sum_{v \in} w_{uv}(r_{vi} - \bar{r}_v)}{\sum_{v \in V}w_{uv}} + \bar{r}_u$

유사한 방법으로 아이템에 적용할 수도 있음!

### Structure of Item-Item CF

* 모든 아이템 쌍의 유사도를 미리 계산
* 해당 사용자가 좋아한/구매한/장바구니에 넣은 것과 유사한 아이템을 검색

### Formula of Item-Item CF

$s(u, i) = \frac{\sum_{j \in N}w_{ij}r_{uj}}{\sum_{j \in N} |w_{ij}|}$

* $i$: 아이템
* $j$: N 개의 이웃 아이템 집합에 있는 아이템
* $w_{ij}$: 아이템 $i$ 와 아이템 $j$ 사이의 가중치 (상관관계, 코사인 등)
* $r_{uj}$: 아이템 $j$ 에 대한 사용자 $u$ 의 평점

### Issues to address

* 유사도를 구하는 방법
* 이웃을 찾는 방법
* Normalization 방법

### 유사도를 구하는 방법

* 상관관계
* cosine similarity of normalized vector = $cos(\hat{\vec{r_i}}, \hat{\vec{r_j}}) = \frac{\hat{\vec{r_i}} \hat{\vec{r_j}}}{||\hat{\vec{r_i}}||_2 ||\hat{\vec{r_j}}||_2} = \frac{\sum_u \hat{r}_{ui} \hat{r}_{uj}}{\sqrt{\sum_u \hat{r}_{ui}^2} \sqrt{\sum_u \hat{r}_{uj}^2}} = \frac{\sum_u (r_{ui} - \bar{r}_i)(r_{uj} - \bar{r}_j)}{\sqrt{\sum_u (r_{ui} - \bar{r}_i)^2}{\sqrt{\sum_u (r_{uj} - \bar{r}_j)^2}}}$

### 이웃을 찾는 방법

* $N(i; u)$: 사용자 $u$ 에 대한 아이템 $i$ 의 이웃
* $s(u, i) = \frac{\sum_{j \in N}w_{ij}r_{uj}}{\sum_{j \in N} |w_{ij}|}$
  * 사용자 $u$ 가 아이템 $j$ 를 평가하지 않으면 해당 알고리즘은 작동하지 않음
  * $N(i; u)$: 사용자 $u$ 가 평가한 아이템 중 아이템 $i$ 와 가장 가까운 $k$ 개의 아이템

### Normalization 방법

* $s(u, i) = \frac{\sum_{j \in N(i; u)} w_{ij}(r_{uj} - \bar{r}_j)}{\sum_{j \in N(i; u)}| w_{ij}|} + \bar{r}_i$

### Components

* 아이템 유사도 함수
  * *interpolation weight* $w_{ij}$ 라고도 함
* 모델 빌더: 아이템 유사도를 계산
  * 속도를 향상시키기 위해서 미리 연산을 해놓기도 함
* 이웃 선택 전략
* 아이템 점수 집계 함수

### Item Similarities

* 보통은 아이템 평점 벡터들 간의 코사인 유사도를 사용함
* 우선 사용자 평점을 normalize 함
  * 아이템 평균을 뺌
  * Historically: 사용자 평균을 뺌
  * 결측치는 0으로 취급
* $w_{ij} = sim(i, j) = \frac{\sum_{u \ in U_i \cap U_j} \hat{r}_{ui} \hat{r}_{uj}}{\sqrt{\hat{r}_{uj}} \sqrt{\hat{r}_{uj}}}$

### Scoring Items

* 점수는 아이템에 따라 구해짐
* 각 아이템에 대한 점수를 구하기 위해서는
  * 사용자가 평점을 매긴 유사한 아이템을 찾고
  * 사용자의 평점으로 가중 평균을 구하고
    * $s(i; u) = \frac{\sum_{j \in N(i;u)}w_{ij}(r_{uj} - \bar{r}_j)}{\sum_{j \in N(i;u)}|w_{ij}|} + \bar{r}_i$
  * normalize 한 평점을 평균 내고, 끝난 뒤에 denormalize 함
  * 선형 회귀와 같은 다른 방법을 고려할 수도 있음

### Picking Neighbors

* 점수 매기는 공식에 이웃 $N(i;u)$ 가 존재
* 이웃은 일반적으로 가장 유사한 $k$ 개의 아이템
  * 사용자가 $u$ 가 평점을 매긴 것들 중
* 적절한 값의 $k$ 를 찾는 것이 중요함
  * $k$ 가 너무 작으면, 점수가 부정확함
  * $k$ 가 너무 크면, 잡음이 많이 들어가서 부정확해짐
  * $k$ = 20, 종종 잘 작동함

### Building the Model

* 모든 아이템 쌍에 대해서 유사도를 미리 계산
  * 아이템의 안정성 덕분에 가능
* Naively: $O(|I|^2)$
  * 유사도 함수가 대칭적인 경우($w_{ij} = w_{ji}$)라면 한 방향으로만 계산하면 됨
  * 대부분의 유사도 함수들의 경우 공통된 평점이 없다면 생략 가능

### Truncate the Model

* 모든 $I^2$ 개의 모형을 가지고 갈 필요는 없음
* 평점을 매기는 시점에 다른 이웃을 찾을 수 있을 만큼의 이웃은 필요함
  * 사용자가 모든 아이템에 평점을 매기지는 않았기 때문에, 모델에서 아이템마다 $M \gg k$ 개의 이웃이 필요함
* 양수값이 아닌 이웃은 제거 가능
* 정확도, coverage 와 메모리 사용량을 잘 조율해야함

### Model Building Algorithm

![02-1-model-building-algorithm](../images/02-1-model-building-algorithm.png)

### Conclusion

* Item-Item 은 효율적이고 간단함
* 특정 데이터나 도메인에 대해서 몇 가지 파리미터를 튜닝해야함
* 다음 강의
  * unary 데이터에 적용하는 방법
  * repurposing and hybridization

## Item-Item on Unary Data

### Data Representation

* 평점: 사용자-아이템 평점 행렬
* 데이터를 표현하기 위한 행렬이 필요함
  * Logical (1 or 0) 사용자-아이템 '구매' 행렬
  * 구매 횟수 행렬
* 문제: 0이 의미하는 것은?
  * Item-Item 에서는 무시

### Data Normalization

* Standard mean-centering 은 의미 없음
  * unary 값이라 1 또는 0(Null) 이기 때문
* 하지만 사용자 벡터를 단위 벡터로 normalize 할 수는 있음
  * 평점을 많이 매긴 사용자들은 특정 쌍에 대해 더 적은 정보를 제공해줌
* 추가적으로 고려할 수 있는 방법: $log(count)$

### 유사도 계산

* 코사인 유사도: $w_{ij} = cos(\hat{\vec{r}_i}, \hat{\vec{r}_j})$
* 조건부 확률을 사용할 수도 있음: $w_{ij} = P(r_i | r_j)$
  * Deshpande and Karypis 의 논문 참고
  * 연관 규칙 (association rules) 와 유사해짐
  * 조건부 확률은 대칭함수가 아니기 때문에 사용할 때 주의가 필요함

### Aggregating Scores

* non-binary 인 경우에 가중 평균은 작동함
  * 횟수
* binary 인 경우라면 이웃의 유사도의 합을 구함
  * fixed neighborhood size means this isn't unbounded
    * $s(i;u) = \sum_{j \in N} w_{ij}$
* 이웃 선택은 바뀌지 않음 (가장 유사한)

### Conclusion

* Item-Item 은 unary 데이터에도 잘 작동 함
* 제대로 작동하게 만들기 위해서는 알고리즘의 구성 요소를 변형해야함
* 데이터/컨텍스트에 맞춰서 바꾼 것을 테스트 해야함
  * 다음 강의에서 진행할 평가 방법이 도움이 될 듯

## Item-Item Hybrids and Extensions

### Extending Item-Item

* Item-Item 은 직접 확장하기에 좋음
* 잘 정의된 인터페이스로 이루어진 간단한 부분 덕분에 굉장히 유연함
* 확장한 부분이 어떤 역할을 하는지 이해하기 쉬움

### Example: User Trust

* 목표: 아이템 연관성 연산에 사용자의 신뢰도를 접목하기
  * 개별적인 사용자에 대한 신뢰가 아닌 전체적인 신뢰
* 방법: 아이템 유사도를 계산하기 전에 사용자의 신뢰도로 가중치를 줌
* 신뢰도가 높은 사용자가 더 큰 영향을 가짐
* [Trust-Aware Collaborative Filtering for Recommendation Systems, Massa and Avesani, 2004](https://link.springer.com/chapter/10.1007/978-3-540-30468-5_31)
* $w_{ij} = \frac{\sum_u \rho_u\hat{r}_{ui} \hat{r}_{uj}}{\sqrt{\sum_u \rho_u \hat{r}_{uj}^2} \sqrt{\sum_u \rho_u \hat{r}_{uj}^2}}$

### Extension: Papers and PageRank

* 논문 추천: useful to consider items as users who purchase the paper's citations
  * 웹페이지에도 동일한 아이디어를 적용할 수 있음
* 목표: 추천 시스템에 논문의 '중요도' 접목하기
* 방법: 논문 사용자 벡터에 논문의 PageRank(or HITS hub score) 로 가중치 적용
* [Automatically Building Research Reading Lists, Ekstrand, et al., 2010](https://md.ekstrandom.net/pubs/reading-lists.pdf)

### Restructuring: Item-Item CBF

* 기본적인 Item-Item 알고리즘은 유사도의 계산 방법에 무관함
* 컨텐츠 기반 유사도를 사용하지 못하는 이유도 없음
* 결과적으로는 협업 필터링은 아니지만 잘 작동함
* 예시: Lucene 을 사용해서 이웃과 유사도 함수로 문서 비교하기

### Restructuring: Deriving Weights

* Item-Item 은 개별의 아이템 쌍을 비교함
* 대안: 데이터로부터 계수 추론하기
  * 제곱오차를 최소화하는 계수 $w_{ij}$ 찾기
  * 일반적인 머신러닝/최적화 알고리즘(gradient descent) 방법으로 계수 학습하기

### Conclusion

* Item-Item CF 는 유연하고 다양하게 사용할 수 있음
* 이 알고리즘을 변형함으로써 다른 추천 시스템을 만들 수도 있음

## Strengths and Weaknesses of Item-Item CF

### Two Intuitions

* Item-Item 은 User-User 보다 효율적이다
  * 사용자의 숫자가 아이템의 숫자보다 월등히 많은 경우
* Item-Item 은 총합적인(aggregated) 제품 연관 추천 시스템이다

### Early Experiences

* Item-Item 은 상업적인 적용에서 굉장히 성공적이었음
* 하지만 MovieLens 에서는 그렇지 않았음

### What happened

* 아마존은 Item-Item 알고리즘을 넓게 사용함
  * 추천에서 큰 성공을 거두었고, 사용자들이 흥미있는 아이템을 찾는데에 도움을 줌
* MovieLens 에서는 불만이 많아짐
  * 추천이 너무 뻔하다
  * 과감한 추천이나 예측이 없다
* Item-Item 은 User-User 와 동일하지 않음
  * Item-Item 알고리즘에서는 굉장히 다른 아이템들을 찾아서 추천하는 것이 매우 어려움
  * User-User 에서는 기본적으로 매우 가까운 이웃이 좋아하는 아이템을 큰 근거가 없더라도 높게 평가함
  * Item-Item 예측은 덜 극단적임 (더 많은 데이터에 기반을 하고 있기 때문에)

### What was Learned

* Item-Item 은 사용자가 아이템의 숫자보다 많은 경우 훨씬 더 빠르고 안정적임
  * 안정성 덕분에 아이템간 유사도를 미리 계산하고 저장할 수 있음
* Item-Item 은 추천과 예측에서 훨씬 더 "보수적"임
  * 쇼핑이나 소비적인 일에는 좋을 수 있음
  * 브라우징이나 오락에 적용하면 실망할 수 있음

### What Next

* 예측은 재스케일이 사용자에 더 적합하다면 적용할 수 있음
  * OrdRec 은 순위 리스트를 임의의 예측 분포에 매핑할 수 있는 방법
  * 비지니스 로직을 적용하기에 굉장히 쉬움
* 행렬분해 방법은 이 디자인 스페이스에서 흥미로운(그리고 다른) 관점을 보여줌
