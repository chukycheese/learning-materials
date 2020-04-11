# Course Introduction

## Collaborative Filtering

* 사용자와 아이템의 특성은 무시
  * 아이템이 어떤 것이고, 사용자가 누구인지에 대해서 신경 쓰지 않음
* 사용자와 아이템간의 상호작용에만 집중
  * 이러한 상호작용에서의 패턴을 찾아냄
* 순수하게 행동에 기반한 추천 시스템

## Benefits of Collaborative Filtering

* 추천하는 특정 아이템의 특성에 관계없이 작동하는 알고리즘을 만들어낼 수 있음
* 흥미로운 패턴을 찾아낼 수 있음

## Key Concepts

* Nearest Neighbor Collaborative Filtering
  * 특정 사용자와 같은 사용자들을 찾아서 그 사람들이 구매한 아이템을 추천하는 방법
* User-User CF Algorithm
  * 이웃과 파라미터 튜닝
  * 이전의 동의에 대한 대안: 사회적인 관계나 신뢰를 바탕으로
* Item-Item CF Algorithm
  * Unary data 다루기: 좋아한 것에 대한 정보만 있고 싫어하는 것에 대한 정보는 없는 경우
  * 하이브리드와 확장
  * 실용적인 함축법
* Advanced Topic
  * Cold Start: 데이터가 별로 없을 때 추천 시스템을 사용하는 방법
  * 특정 집단에 추천하기
  * 추천에 대한 설명
  * Threats

## Course Structure

* User-User Collaborative Filtering
* Item-Item Collaborative Filtering
