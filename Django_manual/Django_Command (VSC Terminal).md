#### Django 명령어 (VSC Terminal)

* **python manage.py runserver**
  * 명령어 실행 후, 아래 사진처럼 결과화면 등장 -> 링크 클릭
  * ***'python manage.py migrate'***: migrate가 필요하다는 명령어
    * *You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.*
      <u>*Run 'python manage.py migrate' to apply them.*</u>
    * **makemigrations:**  Checks for changes on the data shape and creates a file describing the changes.
    * **migrate:** Applies the migrations to the database! The tables and everything are created automatically by Django with 'migrate' 

<br>

![image](https://user-images.githubusercontent.com/42408554/68184844-7c533e00-ffe3-11e9-9411-7f9fd7a51942.png)

<br>

![image](https://user-images.githubusercontent.com/42408554/68184123-8b38f100-ffe1-11e9-98d1-99af2efd9b11.png)

<br>

* 'http://127.0.0.1:8000/admin/' 링크로 이동할 경우 아래와 같은 에러 페이지가 발생
  * Why? Django와 DB의 세션이 서로 일치하지 않음 ->  **'Migrage'**가 안되어있음!!

![image](https://user-images.githubusercontent.com/42408554/68185138-29c65180-ffe4-11e9-9426-825870a35348.png)

<br>

* **python manage.py migrate**
  * 명령어 실행 후, 아래 사진처럼 결과화면 등장

<br>

![image](https://user-images.githubusercontent.com/42408554/68184430-55e0d300-ffe2-11e9-9395-54f796d85d8f.png)

<br>

* **python manage.py createsuperuser**

  * 명령어 실행 후, 아래 사진처럼 결과화면 등장

  <br>

![image](https://user-images.githubusercontent.com/42408554/68184596-d7386580-ffe2-11e9-9686-17befdf65454.png)

<br>

