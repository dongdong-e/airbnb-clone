#### Djnago Conceps

* **App:** function들의 집합
  * Room App: Room Search, Room Delete, Room Update...
* **urls.py:** url 관리
* **admin.py**:  'http://127.0.0.1:8000/admin/ '에 반영 (admin 패널에 반영)
* **apps.py:** 'configuration' 파일
* **models.py:** 'database'의 구조를 정의
  * 'admin'의 User 메뉴에 'bio'라는 속성을 추가
  * 속성값을 하나 추가할 경우, 이전 데이터들은 신규 속성값을 가지고 있지 않기 때문에 'default'값을 추가해줘야 함. 방법은 아래의 2가지.
    1. models.TextField**(default="")** 또는
    2. models.TextField**(none=True)**

<br>

![image](https://user-images.githubusercontent.com/42408554/68197768-1fb14c80-fffe-11e9-8669-2c8f74f68928.png)

<br>

![image](https://user-images.githubusercontent.com/42408554/68200683-b5030f80-0003-11ea-8497-b4326c2f8dcd.png)

<br>

* **views.py:** 사용자가 보게 될 화면