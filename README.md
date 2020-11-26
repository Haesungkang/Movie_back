# final pjt README

[TOC]

## 1. 팀원 정보 및 업무 분담 내역

저희 조는 Front-end와 Back-end를 엄격하게 구분하지 않고, 모든 팀원이 Full-stack 개발자로서 Front와 Back을 담당하였습니다. 그 중에서도 특화된 업무는 아래와 같습니다.

| 팀원       | 업무 분담 내용                                               |
| ---------- | ------------------------------------------------------------ |
| **강해성** | Vue 컴포넌트 관리 / 웹 페이지 디자인 / 발표 영상 연출 및 출연 |
| **김현지** | 데이터 수집 및 관리(API 사용) / 발표 영상 기획, 출연 및 편집 / PPT 제작 |
| **최재영** | ERD 모델 작성 / account 관리 / PPT 제작                      |



## 2. 목표 서비스 구현 및 실제 구현 정도

- 목표 서비스: 추천하는 영화에 대해 정확하고 풍부한 정보를 전달하는 사이트를 제작한다.

- 실제 구현 정도: 70%

- 아쉬운 점

  1. 기획은 했으나 시간에 쫓겨 실제로 구현하지 못한 부분들이 꽤 많이 있다.
     - 감성 테마관: '인간 관계에 지친 그대에게', '위로가 필요한 그대에게', '사랑을 시작하고 싶은 그대에게'.. etc.
     - 날씨 테마관: 비 오는 날엔 비 내리는 씬이 있는 영화 추천, 맑은 날엔 색감이 예쁜 영화 추천
     - 시즌 테마관: 크리스마스 특선 영화만 모아서 추천
     - Adult == True 영화만 따로 모아서 보여주기

  2. 서버 배포에 도전하고자 했으나 시간 관계상 불가능했다. 계절학기 기간을 이용하여 해성과 현지는 함께 도전하기로 결심했다. 



## 3. 데이터베이스 모델링(ERD)



## 4. 필수 기능에 대한 설명

### 4-1. 홈 화면

- **로그인 전**

![](README.assets/image-20201127003830013.png)

- NAV Bar를 이용하여 주요 메뉴를 간편하게 이용할 수 있다.
- 하단의 EXPLORE 버튼으로 사이트 둘러볼 수 있다. (Now Playing Movies로 바로 연결된다.)



- **로그인 후**

![](README.assets/image-20201127005709047.png)

- 로그인 한 사용자만 이용 가능한 라우터 링크들이 홈 화면에 새롭게 나타난다.



### 4-2. 회원가입 및 로그인

- **회원가입**

![](README.assets/image-20201127005934357.png)

- ID, Password, Password Confirmation은 필수 입력 필드이다.



- **로그인**

![](README.assets/image-20201127010105842.png)

- 회원가입이 완료되면 바로 로그인 페이지로 이동한다.



### 4-3. 현재 상영 중인 영화

![](README.assets/image-20201127010309988.png)

- 2020-11-26 기준 상영 중인 최신 영화들의 정보를 확인할 수 있다.
- 포스터가 좌우로 부드럽게 넘어가도록 Vue Glide를 적용했다.



![](README.assets/image-20201127010354815.png)

- 영화 포스터를 클릭하면 각 영화에 대한 상세 정보 페이지로 이동한다.
- 각 영화에 대한 평점을 등록할 수 있다. (서술형으로^___^)



### 4-4. 전체 영화 리스트

![](README.assets/image-20201127010522746.png)



![](README.assets/image-20201127010612936.png)

- 줄거리 버튼을 누르면 영화 줄거리를 확인할 수 있다.



### 4-5. 영화 추천 기능

![image-20201127011739340](README.assets/image-20201127011739340.png)

![image-20201127011811529](README.assets/image-20201127011811529.png)

- 우리 조가 보유한 영화 데이터 중에서 10개를 랜덤으로 추출한다.
- 인기도, 평점, 개봉일(최신순)에 따라 영화를 정렬하여 보여준다.



### 4-6. 커뮤니티

- **Article List**

![image-20201127011953194](README.assets/image-20201127011953194.png)

![image-20201127012025200](README.assets/image-20201127012025200.png)

- 영화 정보와 관련된 대화를 자유롭게 나눌 수 있는 자유게시판이다.
- 게시글 제목을 클릭하면 Article Detail로 이동한다.
- `Add Article` 버튼 위에 마우스를 가져다대면 색이 변한다.



- **Article Detail**

![image-20201127012718391](README.assets/image-20201127012718391.png)

- Article 제목과 글쓴이, 생성일과 내용을 확인할 수 있다.
- 댓글도 남길 수 있다.



### 4-7. About

![image-20201127014200862](README.assets/image-20201127014200862.png)

- 웹 사이트 개발자들에 대한 정보가 담긴 페이지



## 5. 진행 과정 및 느낀 점

### 1일차 - 2020. 11. 19. (목)

- 진행 과정

```markdown
# 기획 단계
1. 개발환경 - 아키텍쳐
선정 결과: Django REST API server & Vue.js
선정 이유: 2학기 프로젝트에 대비하기 + vue.js 시험 공부

2. 서비스 기획
우선, 명세서에 따라 기본을 먼저 하자!
최소 한 개의 추천 알고리즘을 구현한 뒤, 디자인까지 다 하고도 시간이 남으면 여러 개의 추천 알고리즘을 구현한다.

3. 역할 분담
Backend와 Frontend를 모두 경험할 수 있도록 협업과 분업을 적절히 이용한다.

# 실전 단계 - 협업
1. 기본 뼈대 잡기
함께 Django와 Vue 프로젝트 생성, app 생성, url 설정, model 설정 등 기본적인 뼈대를 구축했다.

2. The Movie Database(TMDB) API를 이용하여 데이터 수집

# 실전 단계 - 분업
- 강해성: 프로젝트 과정에서 실수나 중복 처리하는 부분을 최소화하기 위해 체계적인 기획을 구상

- 김현지: Movie List 구축
API 데이터를 수집하여 영화 데이터 생성 후, dumpdata & loaddata

- 최재영: Community 구축
```

- 현지 느낀 점: API key를 사용하여 data를 받아오는 데만 진을 다 뺐다. 그래도 전에는 API Data를 받아와서 사용하는 것에 대한 막연한 두려움이 있었는데, 한 번 하고 나니 방법을 알 것 같다. 다음부턴 조금 더 수월해지겠지!

- 재영 느낀 점: 지난 수업의 자료들을 보면서 따라 하는데 제대로 동작하지 않아서 힘들었다. 수업 때는 됐는데 왜 혼자 할 때는 안 되는지 모르겠다. 지난 영상들을 다시보며 복습해야 한다는 사실을 깨달았다.

  ## 이 밑에 있는 거는 삭제해도 됩니다. 길게 써야 할 것 같아서 썼어요

  - 기본적으로 명세서에 나와 있는 것을 모두 구현하기 위해, Article과 Comment 모델을 만들었다. 그리고 이를 JSON형태의 데이터로 읽고 쓰기 위해 serializer화 했다. 이어 Article를 보고 쓸수 있는 url과 view, Article의 상세 정보를 보고 업데이트하고 삭제할 수 있는 url과 view, Comment를 만들 수 있는 url과 view, Comment를 볼 수 있는 url과 view, Comment의 상세 정보를 보고 업데이트하고 삭제할 수 있는 url과 view를 만들었다.

    - Article모델을 만드는 과정에서 user를 ForeignKey로 사용하는데, 동작하고 있는 지 아닌 지 확인을 못해서 답답했다.

    - Comment모델에서는 article과 user 모두를 ForeignKey로 사용했는데, 잘 동작하는지는 모르겠다.

      

### 2일차 - 2020. 11. 20. (금)

- 진행 과정

```markdown
# 실전 단계 - 분업
- 강해성: back도 중요하지만 back이 실행되는 과정을 볼 수 있다면 프로젝트에 더 몰입할 수 있다고 판단했다. 그래서 back보다는 front에 집중해 보여줄 수 있는 틀을 만들었다.

- 김현지: 추천 알고리즘과 영화 정보를 고객에게 보여주기 위해 The Movie Database의 API를 활용했다.
	- 분류처리 하지 않은 기본 데이터는 10개 이상의 속성들을 갖고 있었다. 그래서 모델링작업을 통해 필요한 데이터만 추출하려 했다. 그런데 다른 속성들과는 다르게 genre_ids는 list형태로 구성되어 있어 오류가 발생했다. 처음에는 이부분을 발견하지 못해 계속 같은 작업만 반복했다. 그러다 list형태인 것도 데이터가 1개가 아닌 여러개도 나온다는 사실을 알게 됐다. 이후 각 속성에 맞는 형식으로 데이터를 추출해서 문제를 해결했다. 이후 추출한 데이터를 바탕으로 front와 back 어느 곳에서나 자유롭게 쓸 수 있게 됐다.

- 최재영: Community
```

- Vue 진입
- 해성 느낀 점: `front`part에서 해야할 양이 많을 거 같아서 먼저 front 기본틀을 잡았다. 하지만 Vue part를 제대로 공부하지 못했기 때문에 먼저 Vue 공부를 한후 작업이 들어가야된다고 생각했다. 처음에는 Data를 먼저 받아
- 현지 느낀 점:
- 재영 느낀 점: `DRF` 나 `run server`를 사용해서 코드가 제대로 동작하는지 확인하고 싶었지만, 두 기능의 사용법을 다 잊어버려서 사용하는데 어려웠다. 사용법을 알고 난 후로 정상 동작하는지 확인한 결과, 오류가 발생했다. 다시보기를 보면서 오류를 수정하려 했지만 100% 수정하지 못했다. 이후 현지님에게 도움을 요청해서 문제를 해결했다. 문제의 사항은 다음과 같다. 1. models.py에 변경사항이 있었지만, 모든 db를 삭제하지 않고 작업했다. 그 결과 table에 data가 없는 오류가 발생했던 것이었다. => 모든 db를 삭제한 후 migrate 작업을 다시 실행했다. 2. `POST` 요청을 보내는 상황에서 로그인을 하지 않고 보내서 `user_id`값이 null 값이 발생하는 오류가 발생했다. => `createsuperuser`를 통해 admin 계정을 만들고 로그인한 후 POST요청을 보냈다.



### 3일차 - 2020. 11. 21. (토)

- 진행 과정

```markdown
# 실전 단계 - 분업
- 김현지: 디버깅
	- Account에서 지속적으로 에러가 발생한다고 해서 이를 해결하기 위해 비슷한 문제를 해결했던 블로그를 찾았다. 이후 Account의 back부분 디버깅을 하면서 front의 Home페이지 디자인을 작업했다. bootstrap으로 작업을 해보았는데 생각보다 이쁘지 않았다. 다른 프레임워크가 있는지 확인해 봐야겠다.
	
- 최재영: Account
```

- 현지 느낀 점: Django REST API를 사용하여

- 재영 느낀 점: 현지님이 알려주신 블로그와 다시보기를 이용해서 Account를 설계하려 했지만 실패했다. 그냥 하면 될 것 같은데 안된다.



### 4일차 - 2020. 11. 22. (일)

- 재영 느낀 점: 다시보기와 비교했지만 틀린 점을 찾지 못했다.



### 5일차 - 2020. 11. 23. (월)

- 진행 과정

```markdown
# 실전 단계 - 분업 - 강해성 합류
- 강해성: 새로운 디자인을 하고 싶었다. 그래서 다양한 프레임워크들을 찾았다. 그중 `v`라는 프레임워크가 가장 맘에 들었다. `v`의 경우 직관적인 구성으로 디자인에 익숙하지 않은 사용자에게 편리하면서 고급스러운 디자인을 가능하게 만들어 준다.

- 김현지: front 기본 작업
	- 디테일한 디자인 작업을 하기 전에 전체적인 디자인 구상과 틀을 잡아야 한다고 생각했다. 그래서 전체적인 틀 작업과 함께 이번 프로젝트에서 쓰고 싶은 이미지들을 찾았다. 이후 추가작업으로 출시 순으로 영화를 추천하는 알고리즘을 만들었다. 처음에는 영화 리스트에서 데이터를 받아와 sort작업을 하면 될 줄 알았는데 에러가 발생했다. 그래서 그냥 바로 데이터를 받고 sort작업을 해 문제를 해결했다.
	- 받아올 API 정보가 없어서 직접 수작업(..)으로 현재 상영 중인 영화들에 대한 정보를 수집했다.
	
- 최재영: Account
```



- 재영 느낀 점: 블로그 내에서는 `django-rest-knox`를 이용해서 로그인 부분을 구현하려고 했다. 배운 적 없는 방법이라 무작정 따라해봤다. 하지만 `user` 혹은 data를 `serializer`를 확인하는 과정에서 계속 오류가 발생해 교수님에게 도움을 요청했다. 교수님께서는 `decorator`를 사용하지 않고 `generic`으로 데이터를 받기 때문에 어디서 애로가 발생하는지 알 수가 없다고 했다. 그래서 원래 하던 방법으로 변경해서 다시 작업하기로 했다. 이후 app.vue에서 로그인과 로그아웃 기능을 구현했다.



### 6일차 - 2020. 11. 24. (화)

- 진행 과정

```markdown
# 실전 단계 - 분업
- 강해성: 기존 틀과 새로운 틀을 합치는 작업을 했다. 기존에 배웠던 bootstarp보다 `v` 프레임워크가 더 이쁜 거 같아서 `v` 프레임워크로 변경하자고 했다. 팀원들을 설득하기 위해 지금까지 만들어 준것을 보여주며 `v`프레임워크의 편리성과 디자인을 설명했다. 팀원들을 설득하는데 성공했지만, 변경하는 작업이 힘들었다. 변경하는 중간중간 잘 작동하면 로직들이 에러를 발생해서 로직을 변경하거나 삭제했다. login, logout, articlelist, createarticle 등 모든 동작버튼이 home에 있으면 지저분해 보였다. 그래서 홈페이지의 기본적인 부분은 nav바로 옮겼다. 그리고 이후 햄버거를 사용해서 왼쪽에도 바 형식의 메뉴를 만들었다. 이는 사용자 중심의 UI적인 설계라고 할 수 있다.

- 김현지: 영화 list에서 딱딱하게 영화를 보여주고 싶지 않았다. 그래서 보다 입체적이면서 유연하게 보여줄 수 있는 vue glide를 사용하기로 했다. 영화 list에서 기존에 하던대로 props를 사용하면 될 줄 알았는데 에러가 발생했다. 그래서 공식문서를 활용해서 vue glide의 사용법을 다시 공부했다. 이후 vue glide는 components를 사용해야 했고 각 name을 []안에 넣고 처리해야 했다. 

- 최재영: Account, community
```



- 재영 느낀 점: 드디어 로그인, 로그아웃을 구현했지만, nav에서 해당 기능을 구현하는 걸로 변경하기로 했다. 그래서 nav에서 `v`를 이용해서 로그인 로직을 구현하려 햇지만, 해당 작업이 실시 된 후 스스로 페이지를 리셋하지 못하고 직접 리셋해줘야 동작했다. 이부분에 대한 것을 해결해야 할 것 같다. 이번에는 community의 front부분을 할 차례였다. article를 만들고 리스트로 보여주는 부분을 구현했다고 생각했는데 빈 껍데기만 보여주고 제대로 된 동작은 하지 않았다. 문제를 찾지 못해서 팀원들에게 도움을 구했다.



### 7일차 - 2020. 11. 25. (수)

- 해성 느낀 점:  vuetify를 활용해서 디자인을 좀 더 깔끔하게 꾸몄다. 그리고 추천 알고리즘을 구현할 때 랜덤을 이용해서 문제를 해결하려 했다. 그런데 같은 리스트에서 랜덤을 이용해 추천을 하면 에러가 발생했다. 이부분에 대한 문제를 해결 못해서 그냥 추천할 때마다 새로운 리스트에서 랜덤으로 영화를 추천하게 만들었다. 분명 어제는 잘 작동했지만, 오늘은 작동하지 않았다. 팀원들의 코드와 비교하며 다시 코드를 작성해도 문제를 해결할 수 없었다. 이렇게 잘 동작하던 부분이 갑자기 동작하지 않으면 매우 까다롭다. 그래서 이제부터는 주석이나 메모를 하면서 코드를 작성해야겠다. 



- 현지 느낀 점: 영화를 추천하는 알고리즘에서 평균 평점을 통해 추천하는 알고리즘을 맡았다. 

  ```vue
  this.movies.sort((a, b) => (a[prop] > b[prop] ? -1 : 1));
        },
  이 부분에서 왜 -1 : 1 인지 이해하기 힘들었다. ~~해결했다.
  ```

  article을 create하는 과정에서 계속 401에러가 발생해서 이부분을 해결해야 했다. ~~이렇게 해서 문제를 해결했다. 이후 평가자들이 우리의 프로젝트를 보다 쉽고 재밌게 이해할 수 있도록 ucc를 만들었다.
  
  - serializers에 대해서 더 알아보는 시간
  - community 기능 구현 완료
  
  - UCC 제작했지만 압축파일 문제로 업로드에 실패.. 내일 최종 pjt 발표 때는 그런 일이 없도록하자!



- 재영 느낀 점: 관리자 권한의 유저만 사용할 수 있는 기능을 추가했다. 명세서에 나와있는대로 account와 movie_info의 admin만 수정했는데 이것이 끝인지 의문이 들었다. 그래서 다른 부분들을 검토했지만, 굳이 할 필요가 없어 보였다. 이후 프로젝트의 데이터 흐름을 보여줄 수 있는 erd를 작성했다. 우리의 추천 알고리즘의 경우 랜덤을 활용해 추천하기 때문에 영화정보와 추천 알고리즘 사이에 `몇 대 몇`이라고 딱 정할 수가 없어 그냥 1:1이라고 잠정지었다. 이후 이부분에 대해 팀원들과 상의를 해야 할 것 같다.



### 8일차 - 2020. 11. 26. (목)

```markdown
# 실전 단계 - 분업
- 강해성

- 김현지: backend에 새로운 app, nowplaying 생성 > 현재 상영 중인 영화들에 대한 정보를 업데이트했다. url, view, model, serializers 등을 설정하고, dumpdata-loaddata 과정을 차례로 거쳤다.

- 최재영
```



