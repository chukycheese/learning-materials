# User-User Collaborative Filtering

## Reference for UUCF

* [An Algorithmic Framework for Performing Collaborative Filtering by Herlock, Konstan, Borchers, and Riedl (Proc. SIGIR 1999)](http://files.grouplens.org/papers/algs.pdf)

## Key Concept

### 비개인화 추천 (Non-Personalized Recommendation)

* $s(u, i) = \frac{\sum_{v \in U} r_{vi}}{n(U)}$
  * $u$: 사용자
  * $i$: 아이템
  * $s(u, i)$: 사용자 $u$ 의 아이템 $i$ 에 대한 예측 점수
  * $U$: 전체 사용자 집합
  * $v$: 전체 사용자 집합 내의 $u$ 가 아닌 다른 사용자
  * $r_{vi}$: 사용자 $v$ 가 아이템 $i$ 에 준 점수(rating)
  * $n(U)$: 전체 사용자 수

### User-User CF

* $s(u, i) = \frac{\sum_{v \in U} r_{vi} w_{uv}}{\sum_{v \in U}w_{uv}}$
  * $u$: 사용자
  * $i$: 아이템
  * $s(u, i)$: 사용자 $u$ 의 아이템 $i$ 에 대한 예측 점수
  * $U$: 전체 사용자 집합
  * $v$: 전체 사용자 집합 내의 $u$ 가 아닌 다른 사용자
  * $r_{vi}$: 사용자 $v$ 가 아이템 $i$ 에 준 점수(rating)
  * $w_{uv}$: 사용자 $u$ 와 사용자 $v$ 사이의 가중치로 값이 높으면 사용자 $v$ 가 사용자 $u$ 를 예측하는 데에 중요하고, 0에 가깝다면 전혀 중요하지 않음을 의미. 유사도, 예측성으로 이해할 수도 있음

## Accounting the Difference between Users

* 어떤 사용자는 점수를 높게 주고, 다른 사용자는 점수를 낮게 줄 수 있어서 이에 대해서도 고려 해야함

### 비개인화 추천 (Non-Personalized Recommendation)

* $s(u, i) = \overline{r_u} + \frac{\sum_{v \in U} (r_{vi} - \overline{r_v})}{n(U)}$
  * 아이템 $i$ 에 대한 사용자 집단의 평균 편차를 사용자 $u$ 의 평균 평점에 더해줌
  * $u$: 사용자
  * $i$: 아이템
  * $s(u, i)$: 사용자 $u$ 의 아이템 $i$ 에 대한 예측 점수
  * $U$: 전체 사용자 집합
  * $v$: 전체 사용자 집합 내의 $u$ 가 아닌 다른 사용자
  * $r_{vi}$: 사용자 $v$ 가 아이템 $i$ 에 준 점수(rating)
  * $\overline{r_u}$: 사용자 $u$ 의 평균 평점
  * $\overline{r_v}$: 사용자 $v$ 의 평균 평점
  * $n(U)$: 전체 사용자 수
* 이 계산 방법에서의 문제점
  * 경우에 따라서는 범위를 넘어서는 예측 점수가 나올 수 있어서 이에 대한 제한을 해야함

### User-User CF

* $s(u, i) = \overline{r_u} + \frac{\sum_{v \in U} (r_{vi} - \overline{r_v})w_{uv}}{\sum_{v \in U}w_{uv}}$
  * $u$: 사용자
  * $i$: 아이템
  * $s(u, i)$: 사용자 $u$ 의 아이템 $i$ 에 대한 예측 점수
  * $U$: 전체 사용자 집합
  * $v$: 전체 사용자 집합 내의 $u$ 가 아닌 다른 사용자
  * $r_{vi}$: 사용자 $v$ 가 아이템 $i$ 에 준 점수(rating)
  * $\overline{r_u}$: 사용자 $u$ 의 평균 평점
  * $\overline{r_v}$: 사용자 $v$ 의 평균 평점
  * $w_{uv}$: 사용자 $u$ 와 사용자 $v$ 사이의 가중치로 값이 높으면 사용자 $v$ 가 사용자 $u$ 를 예측하는 데에 중요하고, 0에 가깝다면 전혀 중요하지 않음을 의미. 유사도, 예측성으로 이해할 수도 있음
* 가중치를 계산하는 방법
  * 피어슨 상관계수 (Pearson Correlation)
  * $w_{uv} = \frac{\sum_{i \in I}(r_{ui} - \overline{r_u})(r_{vi} - \overline{r_v})}{\sigma_u \sigma_v}$
    * 이를 사용할 수 없는 경우에 대해서는 이후에 알아보기로 함

## Notion of Neighborhood

* `이웃` 은 사용자 집합 $U$ 를 의미
  * 필요에 따라서 집합의 크기를 제한하거나
  * 일정 기준을 만족한 사람들로만 사용자 집합 $U$ 를 구성하기도 함

### Possible Issues

* 충분히 유사하지 않은 사용자를 사용자 집합에 포함시키면 Noise 가 심해짐
  * 최소 유사도 기준을 사용하면 사용자 집합의 크기가 작을 수도 있음
  * 집합의 크기를 제한하면 최소 유사도 기준을 만족하지 못하는 사용자도 포함될 수 있음
  * 즉, 사용자 집합의 크기와 최소 유사도는 trade-off 관계
* 가중치(상관관계)가 음수인 사람들은 어떻게 하나?

### Possible Solution

* $s(u, i) = \overline{r_u} + \frac{\sum_{v \in V} (r_{vi} - \overline{r_v})w_{uv}}{\sum_{v \in V}w_{uv}}$
  * $V$: 이웃하는 사용자의 집합

## Common Characteristics

* 다양한 User-User CF 방법들에서의 공통점
* 평점을 모아놓은 데이터
* 사용자간 동의의 척도
  * 상관관계, Vector Cosine
* 개인화된 추천/예측
  * 다른 사용자의 평점에 가중치를 적용한 합
* 보다 나은 추천을 위한 변형
  * 이웃 집합의 크기 제한
  * Normalization
  * 공통된 평점이 적은 경우 이를 극복하는 방법

## Let's Formalized This

* 아이템 집합 $I$, 사용자 집합 $U$, Sparse 한 평점 행렬 $R$ 이 있을 때, 예측 점수 $s(u, i)$ 는 아래와 같이 계산한다
  * 한 사용자 $u$ 에 대해 다른 사용자들 $v$ 와의 가중치 $w_{uv}$ 를 계산
    * 유사도 메트릭(예: 피어슨 상관계수)
  * 가장 높은 $w_{uv}$ 를 가진 사용자들로 구성된 이웃 사용자 집합 $V \subset U$ 를 선택
    * Top $k$ 명의 사용자로 이웃 집합을 제한할 수 있음
    * 유사도를 특정 treshold 이상인 사용자로 이웃 집합을 제한할 수 있음
    * 특정 유사도 값 sim 또는 |sim| 을 사용할 수도 있음 (음의 상관관계에 대한 위험 존재)
    * 특정 아이템 $i$ 에 대한 평점이 있는 사용자로 사용자 집합을 제한할 수 있음 (한 아이템에 대해 일회용으로 쓰는 경우)
  * 예측 점수 계산하기
    * $s(u, i) = \overline{r_u} + \frac{\sum_{v \in V} (r_{vi} - \overline{r_v})w_{uv}}{\sum_{v \in V}w_{uv}}$

## Implementation Issues

* $m$ 은 사용자 집합 $U$ 의 크기, $n$ 은 아이템 집합 $I$ 의 크기라고 할 때
  * 연산이 Bottleneck 이 될 수 있음
    * 두 사용자 간의 상관관계는 $O(n)$
    * 한 사용자에 대한 모든 상관관계는 $O(mn)$
    * 모든 pairwise 상관관계는 $O(m^2n)$
    * 추천의 최소 복잡도는 $O(mn)$
  * 보다 실용적으로 만들 수 있는 다양한 방법들이 존재
    * 상관관계를 캐시해놓거나
    * 새로 생기는 것들에 대해서만 구하는 방법

## Core Assumptions / Limitations

* 가정: 과거의 agreement 가 미래의 agreement 를 예측한다
  * 기본 가정 1: 사용자의 취향은 개인적으로 안정적이거나, 서로 싱크된 상태에서 이동한다
    * 쉽게 말해서 어제 좋아했던 것을 내일도 좋아한다
  * 기본 가정 2: 추천 시스템은 agreement 의 분야 내에서만 적용된다
    * 한 분야에서 유사하다고 해서 다른 분야에서도 유사한 취향을 가지는 것은 아님

## Common Methods

### Common similarity

* Pearson
* Spearman
* Cosine

### Normalization

* Subtract user mean rating
* Convert to z-score
* Subtract item or item-user mean
* Must reverse normalization after computation
