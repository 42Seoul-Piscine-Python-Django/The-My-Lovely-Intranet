# My Lovely 💔 Intranet

## 👬 프로젝트 참여자!

### yongjule

#### 👅 한마디

> ~!!~~!!!~~!!!!~화이팅~!!~~!!!~~!!!!~

[![yongjule's 42 stats](https://badge42.herokuapp.com/api/stats/yongjule)](https://github.com/JaeSeoKim/badge42)

### jaeskim

#### 👅 한마디

> 피신 끝내고 자러갑시다...!!

[![jaeskim's 42 stats](https://badge42.herokuapp.com/api/stats/jaeskim)](https://github.com/JaeSeoKim/badge42)

## 제공 기능!

> ### Login
>
> ### Register
>
> 공부해야 하는 내용!
>
> - Custom User AuthSystem?

> ### Profile
>
> #### Profile Edit
>
> 공부해야 하는 내용!
>
> - file upload
> - image file 관리

### Forum

#### Post List

> ##### Pagenation
>
> 공부해야 하는 내용!
>
> - pagenation 공부하기.
> - pagenation model 호출 방법 공부.

#### Post View

##### Edit Post

##### Delete Post

<!-- TODO: 구현 될지 모르는 항목....!? -->

##### Vote System

<!-- TODO: 구현 될지 모르는 항목....!? -->

> ##### Comment
>
> ###### Edit Comment
>
> ###### Delete Comment
>
> ###### Replay Comment
>
> 공부해야 하는 내용!
>
> - 대댓글을 구햔 하기 위한 방법 찾기.
> - 대댓글을 위한 Model 구조 설게 하기.
> - Template에서 어떻게 보여줄지?
> - Bonus -> Ajax로 어떻게 불러와서 추가 할지? (추후에 생각해 보기)

> ### Admin
>
> #### Manage User
>
> ##### Profile Edit
>
> ##### Manage User Permision
>
> 공부해야 하는 내용!
>
> - Django Authtification 공부하기 -> User Login, Register 와 연관된 부분.
> - Permision Group 제어 방법 공부하기.

---

## 📆 작업 일정

### ⏰ 2021.06.05 ~ 2021.06.08 23:42 UTC+9

#### 06.05

- [x] 프로젝트 분석
- [x] 프로젝트 기본틀 작성
- [x] 공부해야 하는 목록 작성
- [x] 공부.....!! -> WIKI에 공부한 내용 정리해서 올리기!
- [x] 다음날 상세 계획 하기!

#### 06.06

- [x] 간단 명세 작성 완료!
- [x] 명세대로 다시 form model 작성하기!
- [x] 담당 part 정하기!
  - 1차 담당 파트!
  - [ ] 댓글을 제외한 Post - @JaeSeoKim
  - [ ] Profile - @yongjulejule
- [ ] 개발!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#### ... 추후 작성

#### 06.08

- [ ] 제출하기!

---

### 🧾 간단 명세

`/login` → login page

`/register` → register page

---

### login required → `/login`

`/` → post list

`get`

`pagenum` → pagenation 용도로 활용한다. 없으면 첫번째 페이지!

### 포럼 기능!

`/post`

- `get` → 새글쓰기 렌더링!

- `post` → 새글 생성

  - `title` → 글 타이틀!

  - `content` → 글 내용!

  - ? `images` → 글 내부 사진!

  - ---

  - `success` → `/post/<id>`

  - `error` → 화면에 에러 이유 출력!

`post/<id>`

- `get` → 글 렌더링!

`post/<id>/edit` → 해당 소유자만 할 수 있음. or 관리자

- `get`  → 글 수정 화면 렌더링!

- `post` → 글 수정!

  - `title`

  - `content`

  - ? `images`

  - ---

  - `success` → `/post/<id>`

  - `error` → 화면에 에러 이유 출력!

`post/<id>/delete` → 해당 소유자만 할 수 있음. or 관리자

- `post` → 글 삭제!

  - `success` → `/`

  - `error` → 화면에 에러 이유 출력!

`post/<id>/comment`

- `post` → 댓글 작성!

  - `parent_id` → 부모 댓글!

  - `comment` → 댓글 내용!

  - ---

  - `success` → `/post/<id>`

  - `error` → 화면에 에러 이유 출력!

`post/<id>/comment/delete` → 해당 소유자만 할 수 있음. or 관리자

- `post` → 댓글 삭제!

  - ---

  - `success` → `/post/<id>`

  - `error` → 화면에 에러 이유 출력!

---

### 유저 프로파일!

`/profile/<id>` → ? 해당 유저만 접근 가능 or 관리자!

- `get` → 프로파일 렌더링!

`/profile/<id>/edit` → ? 해당 유저만 접근 가능 or 관리자!

- `get` → 수정 화면 렌더링!

- `post` → 프로파일 수정

  - `name` → 이름

  - `surname` → 성

  - `description` → 설명

  - `profile_image` → 프사 → 잘 찍을 것!

---

### 추가 기능

`/logout` → session flush!!!!!

`/admin` →  접근 가능한 사람은 관리자!
