# Django Setup

#### 1. pipenv 설치 이유

* **pip**는 **global**로 설치가 되기 때문에 개별 프로젝트마다 모두 적용이 되는 단점이 존재한다. 만약 Django Version 2.0을 설치했는데, ***Version 3.0으로 업데이트할 경우 2.0으로 만든 프로젝트는 망가질 수 있다.***
* 따라서 ***다양한 Version을 각 하나의 비누방울에 넣어서 관리***하는 것이 좋다. Version 2.0은 1번 비누방울, Version 3.0은 2번 비누방울 등…

---

#### 2. **pipenv 설치 방법**

* **OS별 설치방법**
  * **Mac OS**
    - brew install pipenv
  * **Windows**
    - pip install --user pipenv

* **설치 후 세팅**

  * **PowerShell (관리자 모드)**에서 pipenv 입력한 후, 아래와 같은 화면 확인

  <br>

  ![image](https://user-images.githubusercontent.com/42408554/68102931-2feefc00-ff18-11e9-8608-c7348ee89c70.png)

<br>

* 위의 사진이 아니라 오류가 뜰 경우, **'환경변수'** 등록을 의심해볼 수 있다. 환경변수 등록에서 'PATH'에 다음과 같이 입력
  * *C:\Users\KYD\AppData\Local\Programs\Python\Python37\Scripts*
  * *C:\Users\KYD\AppData\Local\Programs\Python\Python37\*
  * *C:\Users\KYD\AppData\Roaming\Python\Python37\Scripts*

* **프로젝트에 pipenv 적용**
  1. *프로젝트를 생성할 폴더로 이동*
  2. *PowerShell (관리자): **pipenv --three** 입력*
  3. *성공적으로 설정이 됐다면 **'Successfully created virtual environment!'** 결과 확인*
  4. *VSC에서 프로젝트 폴더를 불러오기*
  5. *Terminal에서 **pipenv shell*** 입력
     * **pipenv shell**: 비누방울 안으로 들여보내주는 명령어
     * 성공적으로 실행됐다면 ***'Launching subshell in virtual environment'*** 결과 확인

---

#### 3. Django 설치하기

1. VSC의 Terminal에서 ***pipenv install Django==2.2.5*** 입력하여 설치
2. 성공적으로 설정이 됐다면 Terminal에서 ***django-admin***을 입력하고 아래와 같은 화면을 확인

<br>

![image](https://user-images.githubusercontent.com/42408554/68103545-9ecd5480-ff1a-11e9-8e1a-288d6b5b6264.png)

<br>

3. 프로젝트 폴더 안에 ***'.gitignore'*** 파일을 생성한 후, 아래의 링크에 있는 코드를 붙여넣어서 저장

    https://github.com/github/gitignore/blob/master/Python.gitignore 

---

#### 4. Django 프로젝트 설정 및 패키지 설정

1. ***'django-admin startproject mysite'*** 명령을 사용하지 않는다.
2. Terminal에서 프로젝트 폴더 경로로 이동한 후 **'django-admin startproject config'**라고 입력하여 생성한 후, 아래와 같이 ***'config'*** 폴더 유무 확인

<br>

![image](https://user-images.githubusercontent.com/42408554/68103983-76465a00-ff1c-11e9-9ceb-9dfc4936b76e.png)

<br>

3. **'config'** 폴더명을 **'Aconfig'**로 변경 (아무이름이나 상관은 없음), 폴더명 변경 후 아래 사진처럼 ***'config'*** 폴더와 ***'manage.py'*** 파일을 최상위 폴더로 이동. 그리고 ***'Aconfig' 폴더는 삭제***

<br>

![image](https://user-images.githubusercontent.com/42408554/68104094-f8cf1980-ff1c-11e9-87e4-6a18505ea7fb.png)

<br>

4. ***'manage.py'***을 열었을 때 VSC 오른쪽 하단에 다양한 Extension을 설치하라는 팝업창이 발생, 따라서 ***'Extension' 메뉴***로 가서 아래처럼 ***'Python'***을 설치

<br>

![image](https://user-images.githubusercontent.com/42408554/68104342-0c2eb480-ff1e-11e9-8502-387544516f2c.png)

<br>

5. **'Ctrl + P'**로  **'command palette'**를 호출하여 '>  python: Select Linter'을 입력하고 'flake8'을 클릭하여 '.vscode' 폴더의 'settings.json' 파일에서 아래와 같은 화면 확인

<br>

![image](https://user-images.githubusercontent.com/42408554/68104888-24073800-ff20-11e9-9d84-3132f85c5e22.png)

<br>

6. ***'manage.py'*** 파일을 열면 오른쪽 하단에 ***'flake8'***을 설치하라는 팝업창 발생. **'install'** 버튼을 누른 후 아래와 같은 화면 확인

<br>

![image](https://user-images.githubusercontent.com/42408554/68105010-85c7a200-ff20-11e9-9767-4f1e143d256c.png)

<br>

7. Terminal에서 **'pipenv install black --dev --pre'**을 입력하여 'black' 설치 후 아래와 같은 화면 확인

<br>

![image](https://user-images.githubusercontent.com/42408554/68105248-477eb280-ff21-11e9-9cea-3222478b3b42.png)

<br>

8. ***'settings.py'*** 파일에 들어가면 아래와 같은 화면을 확인. Python 코딩에 적합하지 않은 코드가 4개 존재한다는 것을 의미함.

<br>

![image](https://user-images.githubusercontent.com/42408554/68105427-d25fad00-ff21-11e9-89a3-af7ff6c8acb1.png)

<br>

* 아래는 코드가 너무 길어서 발생하는 Error 표시. 그러나 요즘에는 컴퓨터 모니터가 크기 때문에 이 부분에 대해 수정할 필요가 있음.

![image](https://user-images.githubusercontent.com/42408554/68105512-1357c180-ff22-11e9-96ee-d51ed7d9901f.png)

* ***'settings.json'*** 파일에서 아래와 같은 화면처럼 ***"python.linting.flake8Args": ["--max-line-length=88"]*** 이라고 입력한 후 저장하면 위의 사진에서 빨간 줄이 몇 개 사라진 것을 확인할 수 있음.

<br>

![image](https://user-images.githubusercontent.com/42408554/68105710-ba3c5d80-ff22-11e9-80de-c8f73053b800.png)

<br>

![image](https://user-images.githubusercontent.com/42408554/68105742-d2ac7800-ff22-11e9-8272-3639f14097eb.png)

