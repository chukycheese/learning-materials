# Week 3 Content-Based Filtering Part 1

## Indroduction to Content-Based Recommenders

### Basic Idea: Stable Preferences (measured by content attributes)

* News: tech, ...
* Clotings: cotton, blue, low-priced, ...
* Movies: Tom Hanks, ...
* Hotels: WiFi

### The key ideas

* 아이템을 관련 속성에 맞춰서 모델링
* 사용자의 선호를 속성에 따라 모델링 또는 찾아내기
* 짜잔! 추천 시스템 완성

### Learning Objectives

* 컨텐츠 기반 추천 방식의 범위와 가치에 대해서 이해한다
  * 순수한 정보 필터링 시스템
  * case-based reasoning system
  * 지식 기반 네비게이션 시스템
* 컨텐츠 기반 필터링이 잘 작동하는 또는 잘 작동하지 않는 상황을 구분할 수 있다
* 키워드, 태그 또는 다른 속성들의 관점에서 사용자 선호도와 아이템 표현을 나타내는 벡터 모델을 만들 수 있다
* TF-IDF 와 코사인 유사도 알고리즘을 이용해서 추천과 예측을 계산할 수 있다
* 컨텐츠 기반 필터링에서 데이터 normalization 을 이해하고, 설명하고, 적용할 수 있다
* TF-IDF 알고리즘에 대해 이해하고 설명할 수 있으며, 특히 IDF 가중치 요소가 나오게 된 문제도 이해하고 설명할 수 있다

### Content-Based Filtering

* 주된 컨셉: 속성 또는 키워드 선호의 벡터를 만드는 것
* 사례: [Karakatoa Chronicle](https://www.w3.org/Conferences/WWW4/Papers/93)
  * 기사에 대한 선호 점수가 기사마다 달려있음
  * 기사에 할당된 공간도 달라짐
  * 사용자 정보를 업데이트하면, 사용자의 키워드, 커뮤니티 가중치, 편집자 판단에 얼마나 맞는지를 보고 재배치
  * ![Communication between the server and the client](https://www.w3.org/Conferences/WWW4/Papers/93/communication.gif)

### Wide range of Possibilities

* 사용자가 직접 프로파일을 입력해야함 (어색...)
  * 하지만 사용자가 프로파일을 수정하도록 하는 것은 가치있을 수 있음
  * 직접 생각하는 것은 좀 어렵긴 하지만 일부 선택지를 먼저 던져주면 이를 수정하는 것은 잘 함
* 사용자의 행동으로부터 프로파일 추론
  * 읽음, 구매, 클릭, ...
* 명시적인 사용자 평점으로 프로파일 추론
  * 아이템 선호도를 속성 선호도에 매핑하는 방법
* 행동/명시적 평점을 합쳐서 평점(명시적/암묵적) 으로부터 추론

### How to build preferences

* 사용자가 좋아하거나, 싫어하거나, 아직 잘 모를 수 있는 "키워드" 들에 대한 생각으로부터 시작
  * 필요 없는 단어(stop words) 는 제외
* 쉽게는 각 키워드별로 사용자가 선택(또는 선택에 실패한) 횟수를 셀 수 있음
* 또는 더 복잡해질 수도 있다!

### How to use preferences

* 키워드 선호도에 대한 벡터가 주어지면
  * 좋아요와 싫어요만 단순히 더하면 될까?
  * 연관성이 높거나 낮은 키워드들이 어떤 것인지 알아낼 수 있나?
* Forward preference: TF-IDF
  * Term Frequency: 각 문서에서 특정 단어의 빈도
  * Inverse Document Frequency: 전체 문서에서 해당 단어가 나오는 문서의 비율

### Case-Based Recommendation

* 관련된 특성 집합(가격, 기능, 성능 등)을 가지고 케이스 데이터베이스를 구축
* 사례나 특성 쿼리에 기반해서 질의를 하고, 관련된 케이스를 수집
* 개인화가 되어 있으면서도 시간적 특수성이나 상황적 특수성을 반영한 방법
* 알려진 문제점: 상호작용을 구조화하는 방법이 많음

### etown's Ask Ida

* 서비스가 중단된 사이트
* 특성에 대한 선호를 파악하기 위해 인터뷰 과정을 이용
* 제품 추천에 선호도를 이용
* 추천을 향후 선호도를 이끌어내기 위한 지점으로 이용
* Note: 영구적인 취향을 파악하기 위한 것은 아니며, 서비스를 이용하는 당시에만 해당

### Knowledge-Based Recommender

* Case-Based Example with Naviation Interface
* FindMe Systems (e.g., Entree)
  * 좋아하는 식당을 넣으면 유사한 특징을 가지고 있는 식당을 추천해줌
  * 그 외에 다른 특징들을 추가할 수 있고, 그럼 그 특징에 맞는 다른 식당을 또 추천해줌

### More Generally

* Case-Based 접근법 (Knowledge, Database, etc.) 는 보통 일시적인 개인적 경험에 가장 유용함
  * 쇼핑: 유사하고 관련있는 제품을 제안
    * Collaborative: 같이 구매 되었거나, 같이 본 제품을 제안
  * 컨텐츠: 유사한 이야기를 제안
* Case-Based 추천시스템은 사용자에게 설명하기가 보통 더 쉬움
  * Content-Based: 보다 장기간의 취향을 모델링할 때 적절함

### Challenges and Drawbacks

* Content-Based 기법은 일반적으로...
  * 취향/선호도에 맞춰서 잘 구조화된 특성들에 의존
  * 여러 아이템에 걸쳐 특성이 골고루 분포해 있어야함(반대도 마찬가지)
  * 기대하지 못했던 것들을 발견할 가능성은 낮음
  * 보완재를 찾는 것이 대체재를 찾는 것보다 어려움
    * 어떤 특징들과 유사한 것을 찾기는 쉬움
    * 보완재를 찾으려면 더 복잡한 방법을 사용해야함

### Some take-away lessons

* 컨텐츠에 기반한 추천을 만드는 다양한 방법 (제품 특성)
  * 장기: 컨텐츠 취향에 대한 프로파일 작성
  * 단기: 케이스에 대한 데이터베이스를 만들고 둘러보기
* 컨텐츠 기반 기법은 사용자가 많이 없더라도 잘 작동함(아이템 데이터는 필요)
* 대체재를 찾는 경우, 구매를 위해 둘러볼 때, 설명이 필요할 때 용이

### Moving Forward

* TF-IDF 와 컨텐츠 기반 필터링 심화
* 확장
* Case-based, Knowledge-based 기법 전문가와의 인터뷰
* 컨텐츠 기반에서 벡터 공간 접근법까지의 진화 과정

## TF-IDF and Content Filtering

### Learning Objectives

* 검색이나 필터링에 가중치가 필요한 문제에 대해 이해한다
* TF-IDF 가중치에 대해 세부적으로 이해하고, 검색과 필터링에 어떻게 사용되는지 이해한다
* TF-IDF 의 다양한 변형과 대안에 대해 이해한다
* 컨텐츠 필터링과 검색의 유사점과 차이점을 구별한다

### The Search Problem

* 초기의 검색엔진들이 실패한 이유
* 초기 검색엔진들의 기능
  * 특정 단어가 들어간 모든 문서 보여주기: 엄청나게 많은 문서가 나옴
  * 검색어가 더 많이 나온 문서를 높은 순위로 매기기
* 최소한 고려해야할 두 가지
  * Term Frequecy 는 유의미할 수도 있다
  * 모든 단어(term) 가 동일하게 관련이 있는 것은 아니다: 불용어의 경우 큰 의미가 없음

### TF-IDF weighting

* Term Frequency * Inverse Document Frequency
* Term Frequency: 해당 문서에서 검색어의 출현 빈도 수 (단순한 빈도도 가능)
* Inverse Document Frequency: 얼마나 적은 문서가 검색어를 가지고 있었나
  * $log(\frac{문서\ 수}{검색어를\ 포함한\ 문서\ 수})$

### What does TF-IDF do

* 불용어와 자주 쓰는 단어를 자동적으로 낮게 평가
* 우연히 나온 단어보다 주요 단어를 높게 평가
* 실패하는 경우는 언제인가
  * 주요 단어/개념이 문서에서 많이 사용되지 않은 경우: 계약 문서에서 이름 대신 갑/을 등으로 사용
  * 검색 성능이 안 좋은 경우: 단어를 일부만 넣었다거나, 철자가 틀렸다거나

### How does TF-IDF apply to CBF

* 컨텐츠 필터링의 목적: 사용자의 컨텐츠 취향에 대한 프로파일을 만드는 것
* TF-IDF 개념은 문서/대상의 프로파일을 작성할 때 사용할 수 있음
  * 영화를 관련 태그의 가중치 벡터로 나타낼 수 있음
* 이러한 TF-IDF 프로파일은 사용자 프로파일을 만들기 위해 평점과 합칠 수도 있고, 향후 문서와 맞춰볼 수도 있음

### Variants and Alternatives

* TF 에 대한 다양한 변형
  * 0 또는 1의 값 (특정 횟수를 기준으로): 해당 threshold 가 0인 경우도 있음, term 들이 고정된 경우에 사용하기 좋음
  * 로그값 ($log(TF + 1$): 값이 굉장히 큰 경우에는 로그를 취해서 작게 만들어줌
  * normalize 값 (문서의 길이로 나눔)
* [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) (a.k.a. Okapi BM25) 는 검색 엔진에서 사용하는 순위 함수
  * 질의, 문서 내에서의 빈도, 문서 수, 길이 등을 포함
  * 다양한 가중치를 이용한 변형이 존재: BM11, BM15, ...

### Actually much harder, as we said

* 구절과 n-grams
  * "computer science" != "computer" and "science"
  * 인접어(Adjacency)
* 문서 내에서의 유의성
  * 제목, 부제목 등이 본문에 있는 단어보다는 가중치를 크게 주기도 함
  * Tag 의 경우 신뢰도 있는 사용자의 tag 에 높은 가중치를 주기도 함
* General Document Authority
  * Pagerank 와 유사한 접근법
* 암시된 컨텐츠
  * 링크, 사용, ...

### Take-away and Moving Forward

* Take-away
  * TF-IDF 와 필요한 이유에 대해 이해했다
  * TF-IDF 의 한계에 대해서도 이해 했다
* Moving forward
  * 컨텐츠 프로파일을 만들고 적용하기

## Contet-Based Filtering: Deeper Dive

### Learning Objectives

* TF-IDF 개념에 기반하여 컨텐츠 기반 추천 시스템을 만들 수 있다
  * 아이템을 설명하기 위한 벡터 연산
  * 사용자 선호도 프로파일 생성
  * 아이템에 대한 사용자 관심도 예측
* CBF 추천시스템을 구현에 있어서 주요 변형들과 이들의 장단점을 이해한다

### Key concept: Keyword Vector

* 가능한 키워드의 전체 집단이 컨텐츠 공간을 정의한다
  * 각 키워드는 차원(dimension) 이다
    * 키워드는 단어일 수도 있고, 영화라면 장르, 감독, 배우 등이 될 수도 있음
  * 각 아이템은 그 공간에서 위치(position) 가 있고, 이 위치가 벡터를 정의한다
    * 이 위치는 해당 차원(dimension) 에 대한 수치
  * 각 사용자는 취향 프로파일(하나 또는 다수)이 있고, 이 또한 그 공간에서의 벡터이다
  * 사용자 선호도와 아이템의 짝은 두 벡터가 얼마나 가깝게 위치해있느냐로 측정한다
  * 키워드 공간을 제한하거나 축소해야할 수 있다
    * stem: 원형으로 만드는 것
    * stop: 불용어 제거

### Useful reference

* Vector Space Model (originally conceived for queries, indexing)
  * [벡터 공간 모델](https://ko.wikipedia.org/wiki/%EB%B2%A1%ED%84%B0_%EA%B3%B5%EA%B0%84_%EB%AA%A8%EB%8D%B8)
  * [Vector space model](https://en.wikipedia.org/wiki/Vector_space_model)
  * [A vector space model for automatic indexing; Salton, Wong, and Yang(1995)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.446.5101&rep=rep1&type=pdf)

### Where choices come into play

* 키워드 벡터로 아이템 표현하기
  * 간단하게 0과 1 (키워드가 있거나, 없거나)
  * 빈도 수
  * $TF-IDF = log(\frac{# docs}{# docs\ with\ term})$
  * 문서 길이와 같은 값을 가지고 있는 다른 변형들
  * 이 벡터들은 나중에 normalize 되기도 함

### A Little Formalization
