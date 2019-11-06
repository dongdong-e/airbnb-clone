#### Djnago Conceps

* **App:** function들의 집합
  * Room App: Room Search, Room Delete, Room Update...
* **urls.py:** url 관리
* **admin.py**:  'http://127.0.0.1:8000/admin/ '에 반영 (admin 패널에 반영)
  * **@admin.register(models.User)**: "'admin' 패널에서 'models.py' 안에 있는 User를 보고 싶어!"라는  의미
  * 'User'를 컨트롤할 클래스가 'CustomUserAdmin'이라는 의미
  * **list_display:** 'admin' 패널에 노출시킬 사용자 속성값 설정

<br>

![image](https://user-images.githubusercontent.com/42408554/68260935-d99dcc80-0081-11ea-8f03-7ef1496ac9b4.png)

<br>

![image-20191106104118381](C:\Users\KYD\AppData\Roaming\Typora\typora-user-images\image-20191106104118381.png)

<br>

![image](https://user-images.githubusercontent.com/42408554/68261692-3e5a2680-0084-11ea-9fb5-19717492022b.png)

<br>

![image](https://user-images.githubusercontent.com/42408554/68261728-65185d00-0084-11ea-9b18-09caf51656e5.png)

<br>

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