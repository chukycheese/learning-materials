---
marp: true
---

# Recommendation Using Deep Neural Networks

---

## Deep Neural Network Models

### MF 모델의 한계

* 쿼리 / 아이템 ID 를 넘어서는 피쳐들을 사용하는 것이 어려움. 그 결과 훈련용 데이터에 있는 사용자 또는 아이템만 질의 가능
* 추천의 관련성. 모든 사람에게 잘 알려진 아이템을 추천하는 경항이 있음

#### DNN 모델은 MF 모델의 이러한 한계를 극복할 수 있음

---

### Softmax DNN for Recommendation

softmax 모델은 문제를 아래와 같은 조건을 가진 다중 클래스 문제로 봄

* 입력값은 사용자 질의 (user query)
* 출력값은 corpus 의 크기와 동일한 크기의 확률 벡터이며, 이는 해당 아이템을 이용할 확률
  * 예를 들어, 유튜브에서는 해당 영상을 클릭하거나 시청할 확률

---

### Input

DNN 의 입력값은 다음을 포함할 수 있음:

* dense feature: 시청 시간, 마지막 시청으로부터 경과 시간
* sparse feature: 시청 기록, 국가

![08-1-input-layer height:400 bg right](/google-recommendation-system/images/08-1-input-layer.svg)

---

### Model Architecture

* 모델 설계에 따라 모델의 복잡성과 표현성이 좌우된다.
* 은닉층과 비선형 활성함수(ReLU) 를 추가하면 훨씬 더 복잡한 관계를 찾아낼 수 있다. 하지만 파라미터를 추가하면 일반적으로 학습 속도를 늦추고 서버에 부담을 준다.
* 마지막 은닉층의 출력값을 $\psi(x) \in \mathbb{R}^d$ 라고 표시하자.

![08-2-output-hidden height:400 bg right](/google-recommendation-system/images/08-2-output-hidden.svg)

---

### Softmax Output: Predicted Probability Distribution

* 이 모델은 마지막 층의 출력값 $\psi(x)$ 를 softmax 층을 통해서 확률 분포 $\hat{p} = h(\psi(x)V^T)$ 로 매핑한다.
  * $h: \mathbb{R}^n \rarr \mathbb{R}^n$ 은 $h(y)_i = \frac{e^{y_i}}{\sum_je^{y_j}}$ 에서 나온 softmax 함수
  * $V \in \mathbb{R}^{n \times d}$ 는 softmax 층의 가중치 행렬

![08-3-predictied-probability-distribution height:400 bg right](/google-recommendation-system/images/08-3-predictied-probability-distribution.svg)

---

## Softmax Training

---

### Training Data

* softmax 의 학습 데이터는 질의 피쳐 (query feature) $x$ 와 (확률 분포 $p$ 로 표현된) 사용자가 이용한 아이템의 벡터로 이루어져 있다.
* 이 모델의 변수 (variables) 는 신경망 층에서의 가중치이다.
* 이 모형은 일반적으로 다양한 확률적 경사 하강법 (stochastic gradient descent) 을 이용해서 학습한다.

![08-4-training height:400 bg right](/google-recommendation-system/images/08-4-training.svg)

---

### Negative Sampling

* 손실함수가 두 확률 벡터 $p, \hat{p}(x) \in \mathbb{R}^n$ (각각 실제 확률과 모델에서 예측한 확률) 을 비교하기 때문에 (하나의 쿼리 $x$ 에 대한) 손실의 기울기에 대한 계산은 corpus 의 크기 $n$ 이 엄청 클 때는 굉장히 오래 걸릴 수 있다.
* 그렇기 때문에 ground truth vector 에 존재하는 아이템 (positive item) 에 대해서만 계산하도록 만들 수도 있으나, 이런 경우라면 아레에서 설명할 폴딩 (folding) 문제에 부딫힐 수 있다.

---

### Folding

* 모델은 주어진 색깔의 쿼리/아이템 임베딩을 놓는 방법에 대해 학습할 수도 있지만, 우연에 의해 다른 색깔의 임베딩이 동일한 임베딩 공간에 놓일 수도 있다.
* 이러한 현상을 **폴딩(folding)** 이라고 하며, 이는 허위 추천을 야기할 수도 있다.
* 훈련하는 동안 모델에 **negative example** 을 알려주면 서로 다른 그룹의 임베딩을 밀어내야한 다는 것을 학습시킬 수 있다.

![08-5-negatives height:400 bg right](/google-recommendation-system/images/08-5-negatives.svg)

---

### Negative Sampling explained

* 기울기를 구할 때 모든 아이템을 다 사용하거나 (연산량이 굉장히 많을 수 있음) positive item 만 사용하는 (폴딩에 빠질 수 있음) 대신 negative sampling 을 이용할 수 있다.
* 더욱 정확하게는 다음의 아이템들로 기울기를 근사할 수 있다.
  * 모든 positive item (target label 에 나타난 것들)
  * negative item 중 일부 ($j$ in $1, ..., n$)
* negative sampling 의 몇 가지 전략
  * 동일한 확률로 표본 추출하기
  * $\psi(x) \cdot V_j$ 값이 높은 아이템 $j$ 에 높은 확률 부여하기.

---

### On Matrix Factorization vs Softmax

| | Matrix Factorization | Softmax DNN |
| - | - | - |
| Query features | 포함하기 쉽지 않음 | 포함할 수 있음 |
| Cold start | query 나 item 의 범위를 넘어서면 잘 다룰 수 없음. 휴리스틱을 이용해야함. | 새로운 쿼리도 쉽게 다룰 수 있음 |
| Folding | WALS 에 미관측 가중치를 조절함으로써 쉽게 감소시킬 수 있음 | 폴딩에 취약함. negative sampling 이나 gravity 와 같은 기법을 사용해야함. |
| Training scalability | 입력 행렬이 sparse 하다면 굉장히 큰 데이터셋에도 쉽게 적용 가능 | 매우 큰 데이터에는 적용하기 어려움. hashing 이나 negative sampling 과 같은 기법을 사용해야함. |
| Serving scalability | 임베딩 $U, V$ 는 고정적이며, candidate 집합 또한 미리 계산하고 저장할 수 있음 | 아이템 임베딩 $V$ 는 고정적이며 저장가능함. 쿼리 임베딩은 질의 시 계산해야 하므로 서빙에 조금 더 어려움. |

---

### Summary

* Matrix Factorization 은 보통 데이터셋이 큰 경우에 더 나은 선택. 스케일링도 용이하고, 질의 비용도 저렴하고, 폴딩에 빠질 위험도 적음.
* DNN 모델은 개인의 선호를 잡아내는 데에는 더 적합. 그러나 학습이 어렵고 질의 비용이 비쌈.
  * 스코어링의 경우 matrix factorization 보다 DNN 모델을 선호하는데, 연관성을 잡아내는 데에 더 많은 피쳐들을 이용할 수 있기 때문.
  * DNN 모델의 경우 폴딩에 빠지는 것을 보통 수용하기도 하는데, 그 이유는 관계가 있다고 여겨지는 이미 필터링 된 후보지의 순위를 매기는 것을 주로 신경쓰기 때문.
