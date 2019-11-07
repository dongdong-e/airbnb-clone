#### Django 명령어 (VSC Terminal)

* **python manage.py runserver**
  * 명령어 실행 후, 아래 사진처럼 결과화면 등장 -> 링크 클릭
  * **'python manage.py migrate'**: migrate가 필요하다는 명령어*
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

---

* **QuerySet Command (VSC Terminal)**
  * **python manage.py shell**
    * QuerySet 콘솔 호출

```python
# 예시 코드
from users.models import User

all_user = User.objects.all()
all_user.filter(superhost=True)

kyd = User.objects.get(username="kyd")

vars(kyd)
# 결과 화면
{'_state': <django.db.models.base.ModelState object at 0x0000024752712FC8>, 'id': 2, 'password': 'pbkdf2_sha256$150000$17jGvzdexTdg$vfj0hljJWhbsc/HuOIy23gbVqVXHSEGpbZ20a2S7Bn4=', 'last_login': None, 'is_superuser': False, 'username': 'csa', 'first_name': '', 'last_name': '', 'email': '', 'is_staff': False, 'is_active': True, 'date_joined': datetime.datetime(2019, 11, 7, 10, 28, 22, tzinfo=<UTC>), 'avatar': '', 'gender': '', 'bio': '', 'birthday': None, 'language': '', 'currency': '', 'superhost': False}

dir(kyd)
# 결과화면
['CURRENCY_CHOICES', 'CURRENCY_CNY', 'CURRENCY_KRW', 'CURRENCY_USD', 'CURRENCY_YEN', 'DoesNotExist', 'EMAIL_FIELD', 'GENDER_CHOICES', 'GENDER_FEMALE', 'GENDER_MALE', 'GENDER_OTHER', 'LANGUAGE_CHINESE', 'LANGUAGE_CHOICES', 'LANGUAGE_ENGLISH', 'LANGUAGE_JAPANESE', 'LANGUAGE_KORREAN', 'Meta', 'MultipleObjectsReturned', 'REQUIRED_FIELDS', 'USERNAME_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_password', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'avatar', 'bio', 'birthday', 'check', 'check_password', 'clean', 'clean_fields', 'conversation_set', 'currency', 'date_error_message', 'date_joined', 'delete', 'email', 'email_user', 'first_name', 'from_db', 'full_clean', 'gender', 'get_all_permissions', 'get_currency_display', 'get_deferred_fields', 'get_email_field_name', 'get_full_name', 'get_gender_display', 'get_group_permissions', 'get_language_display', 'get_next_by_date_joined', 'get_previous_by_date_joined', 'get_session_auth_hash', 'get_short_name', 'get_username', 'groups', 'has_module_perms', 'has_perm', 'has_perms', 'has_usable_password', 'id', 'is_active', 'is_anonymous', 'is_authenticated', 'is_staff', 'is_superuser', 'language', 'last_login', 'last_name', 'list_set', 'logentry_set', 'message_set', 'natural_key', 'normalize_username', 'objects', 'password', 'pk', 'prepare_database_save', 'refresh_from_db', 'reservation_set', 'review_set', 'room_set', 'save', 'save_base', 'serializable_value', 'set_password', 'set_unusable_password', 'superhost', 'unique_error_message', 'user_permissions', 'username', 'username_validator', 'validate_unique']

######

from rooms.models import Room
room = Room.objects.get(id=1) # (pk=1) 동일

room.reveiw_set.all()
room.amenities.count()
```

위의 dir(kyd) 명령어의 결과 화면에서 **'conversation_set', 'list_set', 'message_set', 'review_set', 'room_set'**는 'users'가 **'ForeignKey'**로 연결되어 있다는 것을 의미한다.

