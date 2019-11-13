#### 8-5 Photo Admin

* **rooms/admin.py**
  * rooms admin 패널에서 사진이 보이게 하는 작업

```python
from django.utils.html import mark_safe

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
```

---

#### 8-6 raw_ids and Inline Admin

* **rooms/admin.py**

  * **raw_id_fields**

    ```python
    @admin.register(models.Room)
    class RoomAdmin(admin.ModelAdmin):
        # 이전/이후 코드 생략함
    	raw_id_fields = ("host",)
    ```

  * **Inline Admin (admin.TabularInline)**

    ```python
    class PhotoInline(admin.TabularInline):
        model = models.Photo
        
    @admin.register(models.Room)
    class RoomAdmin(admin.ModelAdmin):
        # 이전/이후 코드 생략함
        inlines = (PhotoInline,)
    ```

---

#### 8-7. Explaining Python super()

* **super()**: 상위 클래스에 접근할 수 있게 해줌

  ```python
  # Example
  
  class Dog:
      def __init__(self):
          print("woof woof")
  
      def pee(self):
          print("I will pee")
  
  
  class Puppy(Dog):
      def pee(self):
          super().pee()
          print("Go to the park")
  
  
  p = Puppy()
  p.pee()
  
  ```

---

#### 8.8 Intercepting Model save() and admin_save()

* **rooms/models.py**

  * **save()**

    ```python
    class Room(core_models.TimeStampedModel):
        # 이전/이후 코드 생략함
        def save(self, *args, **kwargs):
            self.city = str.capitalize(self.city)
            super().save(*args, **kwargs)
            
    
    # 참고, admin.py에 적용
    # admin 멤버중 어떤 사람이 어떤 내용을 변경했는지 확인
    @admin.register(models.Room)
    class RoomAdmin(admin.ModelAdmin):
    	def save_model(self, request, obj, form, change):
            obj.user = request.user
            super().save_model(request, obj, form, change)
    ```

---

#### 9.0 Custom manage.py commands

1. 특정 App 내부에 **'management'** 폴더를 생성하고 그 안에 **'commands'** 폴더를 생성

2. 두 폴더 모두에 ```__init___.py``` 파일을 생성

3. **'commands'** 폴더 안에 아무 이름의 ```py``` 파일을 생성

4. 생성한 ```py``` 파일 내부

   ```python
   from django.core.management.base import BaseCommand
   
   
   class Command(BaseCommand):
       help = "LOVE YOU SO MUCH"
   
       def add_arguments(self, parser):
           parser.add_argument(
               "--times",
               help="How many times do you want me to tell you that I love you?",
           )
   
       def handle(self, *args, **options):
           times = options.get("times")
           for t in range(0, int(times)):
               self.stdout.write(self.style.WARNING("LOVE YOU"))
   ```

---

#### 9.1 seed_amenities command

* 9.0과 동일하지만 코드만 다름

* **rooms\management\commands\seed_amenities.py**

  ```python
  from django.core.management.base import BaseCommand
  from rooms.models import Amenity
  
  
  class Command(BaseCommand):
  
      """
      def add_arguments(self, parser):
          parser.add_argument(
              "--times",
              help="How many times do you want me to tell you that I love you?",
          )
      """
  
      def handle(self, *args, **options):
          amenities = [
              "Air conditioning",
              "Alarm Clock",
              "Balcony",
              "Bathroom",
              "Bathtub",
              "Bed Linen",
              "Boating",
              "Cable TV",
              "Carbon monoxide detectors",
              "Chairs",
              "Children Area",
              "Coffee Maker in Room",
              "Cooking hob",
              "Cookware & Kitchen Utensils",
              "Dishwasher",
              "Double bed",
              "En suite bathroom",
              "Free Parking",
              "Free Wireless Internet",
              "Freezer",
              "Fridge / Freezer",
              "Golf",
              "Hair Dryer",
              "Heating",
              "Hot tub",
              "Indoor Pool",
              "Ironing Board",
              "Microwave",
              "Outdoor Pool",
              "Outdoor Tennis",
              "Oven",
              "Queen size bed",
              "Restaurant",
              "Shopping Mall",
              "Shower",
              "Smoke detectors",
              "Sofa",
              "Stereo",
              "Swimming pool",
              "Toilet",
              "Towels",
              "TV",
          ]
          for a in amenities:
              Amenity.objects.create(name=a)
  
          self.stdout.write(self.style.SUCCESS("Amenities created!"))
  
  ```

---

#### 9.2 seed_everything and seed_users

* **users\management\commands\seed_users.py**

  ```python
  from django.core.management.base import BaseCommand
  from django_seed import Seed
  from users.models import User
  
  
  class Command(BaseCommand):
  
      help = "This command creates users"
  
      def add_arguments(self, parser):
          parser.add_argument(
              "--number", default=2, type=int, help="How many users you want to create"
          )
  
      def handle(self, *args, **options):
          number = options.get("number")
          seeder = Seed.seeder()
          seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
          seeder.execute()
          self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
  ```

---

#### 9.3 seed_rooms part One

* **rooms\management\commands\seed_rooms.py**

  ```python
  import random
  from django.core.management.base import BaseCommand
  from django_seed import Seed
  from rooms import models as room_models
  from users import models as user_models
  
  
  class Command(BaseCommand):
  
      help = "This command creates rooms."
  
      def add_arguments(self, parser):
          parser.add_argument(
              "--number", default=1, type=int, help="How many users you want to create"
          )
  
      def handle(self, *args, **options):
          number = options.get("number")
          seeder = Seed.seeder()
          all_users = user_models.User.objects.all()
          room_types = room_models.RoomType.objects.all()
          seeder.add_entity(
              room_models.Room,
              number,
              {
                  "name": lambda x: seeder.faker.address(),
                  "host": lambda x: random.choice(all_users),
                  "room_type": lambda x: random.choice(room_types),
                  "guests": lambda x: random.randint(1, 20),
                  "price": lambda x: random.randint(1, 300),
                  "beds": lambda x: random.randint(1, 5),
                  "bedrooms": lambda x: random.randint(1, 5),
                  "baths": lambda x: random.randint(1, 5),
              },
          )
          seeder.execute()
          self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
  ```

---

#### 9.4 seed_rooms part Two

* **rooms\management\commands\seed_rooms.py**

  ```python
  import random
  from django.core.management.base import BaseCommand
  from django.contrib.admin.utils import flatten
  from django_seed import Seed
  from rooms import models as room_models
  from users import models as user_models
  
  
  class Command(BaseCommand):
  
      help = "This command creates rooms."
  
      def add_arguments(self, parser):
          parser.add_argument(
              "--number", default=1, type=int, help="How many users you want to create"
          )
  
      def handle(self, *args, **options):
          number = options.get("number")
          seeder = Seed.seeder()
          all_users = user_models.User.objects.all()
          room_types = room_models.RoomType.objects.all()
          seeder.add_entity(
              room_models.Room,
              number,
              {
                  "name": lambda x: seeder.faker.address(),
                  "host": lambda x: random.choice(all_users),
                  "room_type": lambda x: random.choice(room_types),
                  "guests": lambda x: random.randint(1, 20),
                  "price": lambda x: random.randint(1, 300),
                  "beds": lambda x: random.randint(1, 5),
                  "bedrooms": lambda x: random.randint(1, 5),
                  "baths": lambda x: random.randint(1, 5),
              },
          )
          created_photos = seeder.execute()
          created_clean = flatten(list(created_photos.values()))
          for pk in created_clean:
              room = room_models.Room.objects.get(pk=pk)
              for i in range(3, random.randint(10, 17)):
                  room_models.Photo.objects.create(
                      caption=seeder.faker.sentence(),
                      room=room,
                      file=f"room_photos/{random.randint(1, 31)}.webp",
                  )
          self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
  ```

---

#### 9.5 seed_rooms part Three

* **rooms\management\commands\seed_rooms.py**

  ```python
  import random
  from django.core.management.base import BaseCommand
  from django.contrib.admin.utils import flatten
  from django_seed import Seed
  from rooms import models as room_models
  from users import models as user_models
  
  
  class Command(BaseCommand):
  
      help = "This command creates rooms."
  
      def add_arguments(self, parser):
          parser.add_argument(
              "--number", default=1, type=int, help="How many users you want to create"
          )
  
      def handle(self, *args, **options):
          number = options.get("number")
          seeder = Seed.seeder()
          all_users = user_models.User.objects.all()
          room_types = room_models.RoomType.objects.all()
          seeder.add_entity(
              room_models.Room,
              number,
              {
                  "name": lambda x: seeder.faker.address(),
                  "host": lambda x: random.choice(all_users),
                  "room_type": lambda x: random.choice(room_types),
                  "guests": lambda x: random.randint(1, 20),
                  "price": lambda x: random.randint(1, 300),
                  "beds": lambda x: random.randint(1, 5),
                  "bedrooms": lambda x: random.randint(1, 5),
                  "baths": lambda x: random.randint(1, 5),
              },
          )
          created_photos = seeder.execute()
          created_clean = flatten(list(created_photos.values()))
          amenities = room_models.Amenity.objects.all()
          facilities = room_models.Facility.objects.all()
          rules = room_models.HouseRule.objects.all()
          for pk in created_clean:
              room = room_models.Room.objects.get(pk=pk)
              for i in range(3, random.randint(10, 30)):
                  room_models.Photo.objects.create(
                      caption=seeder.faker.sentence(),
                      room=room,
                      file=f"room_photos/{random.randint(1, 31)}.webp",
                  )
              for a in amenities:
                  magic_number = random.randint(0, 15)
                  if magic_number % 2 == 0:
                      room.amenities.add(a)
  
              for f in facilities:
                  magic_number = random.randint(0, 15)
                  if magic_number % 2 == 0:
                      room.facilities.add(f)
  
              for r in rules:
                  magic_number = random.randint(0, 15)
                  if magic_number % 2 == 0:
                      room.house_rules.add(r)
  
          self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
  ```

---

#### 9.6 seed_reviews

* **reviews\management\commands\seed_reviews.py**

  ```python
  import random
  from django.core.management.base import BaseCommand
  from django_seed import Seed
  from reviews import models as review_models
  from users import models as user_models
  from rooms import models as room_models
  
  
  class Command(BaseCommand):
  
      help = "This command creates reviews"
  
      def add_arguments(self, parser):
          parser.add_argument(
              "--number", default=2, type=int, help="How many reviews you want to create"
          )
  
      def handle(self, *args, **options):
          number = options.get("number")
          seeder = Seed.seeder()
          users = user_models.User.objects.all()
          rooms = room_models.Room.objects.all()
          seeder.add_entity(
              review_models.Review,
              number,
              {
                  "accuracy": lambda x: random.randint(0, 6),
                  "communication": lambda x: random.randint(0, 6),
                  "cleanliness": lambda x: random.randint(0, 6),
                  "location": lambda x: random.randint(0, 6),
                  "check_in": lambda x: random.randint(0, 6),
                  "value": lambda x: random.randint(0, 6),
                  "room": lambda x: random.choice(rooms),
                  "user": lambda x: random.choice(users),
              },
          )
          seeder.execute()
          self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
  ```

---

#### 9.7 seed_lists

* **lists\management\commands\seed_lists.py**

  ```python
  import random
  from django.core.management.base import BaseCommand
  from django.contrib.admin.utils import flatten
  from django_seed import Seed
  from lists import models as list_models
  from users import models as user_models
  from rooms import models as room_models
  
  
  NAME = "lists"
  
  
  class Command(BaseCommand):
  
      help = f"This command creates {NAME}"
  
      def add_arguments(self, parser):
          parser.add_argument(
              "--number", default=2, type=int, help=f"How many {NAME} you want to create"
          )
  
      def handle(self, *args, **options):
          number = options.get("number")
          seeder = Seed.seeder()
          users = user_models.User.objects.all()
          rooms = room_models.Room.objects.all()
          seeder.add_entity(
              list_models.List, number, {"user": lambda x: random.choice(users)}
          )
  
          created = seeder.execute()
          cleaned = flatten(list(created.values()))
          for pk in cleaned:
              list_model = list_models.List.objects.get(pk=pk)
              to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
              list_model.rooms.add(*to_add)
  
          self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
  ```

---

#### 9.8 seed_reservations

* **reviews\management\commands\seed_reservations.py**

  ```python
  import random
  from datetime import datetime, timedelta
  from django.core.management.base import BaseCommand
  from django.contrib.admin.utils import flatten
  from django_seed import Seed
  from reservations import models as reservation_models
  from users import models as user_models
  from rooms import models as room_models
  
  
  NAME = "reservations"
  
  
  class Command(BaseCommand):
  
      help = f"This command creates {NAME}"
  
      def add_arguments(self, parser):
          parser.add_argument(
              "--number", default=2, type=int, help=f"How many {NAME} you want to create"
          )
  
      def handle(self, *args, **options):
          number = options.get("number")
          seeder = Seed.seeder()
          users = user_models.User.objects.all()
          rooms = room_models.Room.objects.all()
          seeder.add_entity(
              reservation_models.Reservation,
              number,
              {
                  "status": lambda x: random.choice(["pending", "confirmed", "cancled"]),
                  "guest": lambda x: random.choice(users),
                  "room": lambda x: random.choice(rooms),
                  "check_in": lambda x: datetime.now(),
                  "check_out": lambda x: datetime.now()
                  + timedelta(days=random.randint(3, 25)),
              },
          )
  
          seeder.execute()
  
          self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
  ```

---

#### 10.0 Introduction to Urls and Views

* **config\urls.py**

  ```python
  from django.contrib import admin
  from django.urls import path, include
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
      path("", include("core.urls", namespace="core")),
      path("admin/", admin.site.urls),
  ]
  
  if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

* **core\urls.py**

  ```python
  from django.urls import path
  from rooms import views as room_views
  
  app_name = "core"
  
  urlpatterns = [
      path("", room_views.all_rooms, name="home"),
  ]
  ```

---

#### 10.1 HttpResponse and render

* **rooms\views.py**

  ```python
  from django.shortcuts import render
  
  
  def all_rooms(request):
      return render(request, "all_rooms")
  ```

* **참고**

  ```python
  from datetime import datetime
  from django.shortcuts import render
  from django.http import HttpResponse
  
  
  def all_rooms(request):
      now = datetime.now()
      return HttpResponse(content=f"<h1>{now}</h1>")
  ```

---

#### 10.2 Introduction to Django Templates

* **airbnb-clone\templates:** 'templates' 폴더 생성

* **templates\all_rooms.html:** 'templates' 폴더에 'all_rooms.html' 파일 생성

* **rooms\views.py**

  ```python
  from datetime import datetime
  from django.shortcuts import render
  
  
  def all_rooms(request):
      now = datetime.now()
      hungry = True
      return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
  ```

* **airbnb-clone\templates.html**

  ```html
  <h1>Hello!</h1>
  <h4>The time right now is: {{ now }}</h4>
  
  <h6>
    {% if hungry %} I'm hungry {% else %} I'm Okay {% endif %}
  </h6>
  ```

---

#### 10.3 Extending Templates part One

* **views.py:** 'html' 파일 이름은 'templates' 폴더의 파일명과 동일해야 함

  * **아래 코드 예시: 코드 속 "all_rooms.html"** 과 사진 속 **"all_rooms.html"** 파일

  ```python
  from django.shortcuts import render
  from . import models
  
  
  def all_rooms(request):
      all_rooms = models.Room.objects.all()
      return render(request, "all_rooms.html", context={"rooms": all_rooms})
  ```

  <br>

  ![image](https://user-images.githubusercontent.com/42408554/68644977-04909080-055a-11ea-92e4-3547abba892c.png)

  <br>

* **views.py:** 함수명은 **'url.py'** 속 이름과 같아야 함

  * **아래 코드 예시:** **'rooms\views.py'** 파일 안의 ```def all_rooms()```

  ```python
  from django.shortcuts import render
  from . import models
  
  
  def all_rooms(request):
      all_rooms = models.Room.objects.all()
      return render(request, "home.html", context={"rooms": all_rooms})
  ```

  * **아래 코드 예시: 'core\urls.py'** 파일 안의 ```all_rooms```

  ```python
  from django.urls import path
  from rooms import views as room_views
  
  app_name = "core"
  
  urlpatterns = [
      path("", room_views.all_rooms, name="home"),
  ]
  ```

* **'templates'** 폴더에 **'base.html' 파일 생성** (사진 참고)
*  **'rooms'**라는 하위 폴더 생성 후, **'home.html'** 파일을 이동 (사진 참고)

<br>

![image](https://user-images.githubusercontent.com/42408554/68647850-3574c380-0562-11ea-9856-b0c4069eaeea.png)

<br>

* **'base.html' 코드**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    &copy; Nbnb
  </body>
</html>
```

* **'views.py' 코드**

```python
from django.shortcuts import render
from . import models


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
```

---

#### 10.4 Extending Templates part Two and Includes

* **'templates'** 폴더 안에 **'partials'** 폴더를 만든 후, **'header.html'** 파일과 **'footer.html'** 파일을 생성 (사진 참고)

<br>

![image](https://user-images.githubusercontent.com/42408554/68649008-09a70d00-0565-11ea-83ad-df3b016a346b.png)

<br>

* **'header.html'** 코드

  ```html
  <header>
    <a href="/">Ybnb</a>
    <ul>
      <li><a href="#">Login</a></li>
    </ul>
  </header>
  ```

- **'footer.html' 코드**

  ```html
  <footer>
    &copy; Ybnb
  </footer>
  ```

* **'base.html' 코드**

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta http-equiv="X-UA-Compatible" content="ie=edge" />
      <title>{% block page_name %}{% endblock page_name %} | Ybnb</title>
    </head>
    <body>
      {% include "partials/header.html" %}
  
      {% block content %} {% endblock %}
  
      {% include "partials/footer.html" %}
    </body>
  </html>
  ```

* **'home.html' 코드**

  ```html
  {% extends "base.html" %}
  
  <!-- page_name -->
  {% block page_name %} Home {% endblock page_name %}
  
  <!-- room contents -->
  {% block content %}
      {% for room in rooms %}
      <h1>{{ room.name }} / {{ room.price }}</h1>
      {% endfor %}
  {% endblock content %}
  ```

---

#### 11.0 HomeView Intro

---

#### 11.1 Pagination with Limit and Offset

* **rooms\view.py**

  ```python
  from django.shortcuts import render
  from . import models
  
  
  def all_rooms(request):
      page = int(request.GET.get("page", 1))
      page_size = 10
      limit = page_size * page
      offset = limit - page_size
      all_rooms = models.Room.objects.all()[offset:limit]
      return render(request, "rooms/home.html", context={"rooms": all_rooms})
  ```

---

#### 11.2 Pages List Navigation

* **rooms\view.py**

  ```python
  from math import ceil
  from django.shortcuts import render
  from . import models
  
  
  def all_rooms(request):
      page = request.GET.get("page", 1)
      page = int(page or 1)
      page_size = 10
      limit = page_size * page
      offset = limit - page_size
      all_rooms = models.Room.objects.all()[offset:limit]
      page_count = ceil(models.Room.objects.count() / page_size)
      return render(
          request,
          "rooms/home.html",
          context={
              "rooms": all_rooms,
              "page": page,
              "page_count": page_count,
              "page_range": range(1, page_count),
          },
      )
  
  ```

* **templates\rooms\home.html**

  ```html
  {% extends "base.html" %}
  
  <!-- page_name -->
  {% block page_name %} Home {% endblock page_name %}
  
  <!-- room contents -->
  {% block content %}
      {% for room in rooms %}
      <h1>{{ room.name }} / {{ room.price }}</h1>
      {% endfor %}
  
      <h5>Page {{page}} of {{page_count}}</h5>
  
      {% for page in page_range %}
          <a href="?page={{page}}">{{page}}</a>
      {% endfor %}
  
  {% endblock content %}
  ```

---

#### 11.3 Next Previous Page Navigation

* **templates\rooms\home.html**

  ```html
  {% extends "base.html" %}
  
  <!-- page_name -->
  {% block page_name %} Home {% endblock page_name %}
  
  <!-- room contents -->
  {% block content %}
  
      {% for room in rooms %}
      <h1>{{ room.name }} / {{ room.price }}</h1>
      {% endfor %}
  
      <h5>
      {% if page is not 1  %}
          <a href="?page={{page|add:-1}}">Previous</a>
      {% endif %}
      Page {{page}} of {{page_count}}
      
      {% if not page == page_count %}
          <a href="?page={{page|add:+1}}">Next</a>
      {% endif %}
      </h5>
  
  {% endblock content %}
  ```

---

#### 11.4 Using Django Paginator

* **rooms\view.py**

  ```python
  from math import ceil
  from django.shortcuts import render
  from django.core.paginator import Paginator
  from . import models
  
  
  def all_rooms(request):
      page = request.GET.get("page")
      room_list = models.Room.objects.all()
      paginator = Paginator(room_list, 10)
      rooms = paginator.get_page(page)
      return render(request, "rooms/home.html", context={"rooms": rooms})
  ```

* **templates\rooms\home.html**

```html
{% extends "base.html" %}

<!-- page_name -->
{% block page_name %} Home {% endblock page_name %}

<!-- room contents -->
{% block content %}

    {% for room in rooms.object_list %}
    <h1>{{ room.name }} / {{ room.price }}</h1>
    {% endfor %}

    <h5>
    {% if rooms.has_previous %}
        <a href="?page={{rooms.number|add:-1}}">Previous</a>
    {% endif %}
    
    Page {{rooms.number}} of {{rooms.paginator.num_pages}}

    {% if rooms.has_next %}
        <a href ="?page={{rooms.number|add:+1}}">Next</a>
    {% endif %}
    </h5>

{% endblock content %}
```

---

#### 11.5 get_page vs page

* **rooms\view.py**

  ```python
  from math import ceil
  from django.shortcuts import render
  from django.core.paginator import Paginator
  from . import models
  
  
  def all_rooms(request):
      page = request.GET.get("page", 1)
      room_list = models.Room.objects.all()
      paginator = Paginator(room_list, 10, orphans=5)
      rooms = paginator.page(int(page))
      return render(request, "rooms/home.html", context={"page": rooms})
  ```

* **templates\rooms\home.html**

```html
{% extends "base.html" %}

<!-- page_name -->
{% block page_name %} Home {% endblock page_name %}

<!-- room contents -->
{% block content %}

    {% for room in page.object_list %}
    <h1>{{ room.name }} / {{ room.price }}</h1>
    {% endfor %}

    <h5>
    {% if page.has_previous %}
        <a href="?page={{page.previous_page_number}}">Previous</a>
    {% endif %}
    
    Page {{page.number}} of {{page.paginator.num_pages}}

    {% if page.has_next %}
        <a href ="?page={{page.next_page_number}}">Next</a>
    {% endif %}
    </h5>

{% endblock content %}
```

---

#### 11.6 Handling Exceptions

* **rooms\view.py**

  ```python
  from math import ceil
  from django.shortcuts import render, redirect
  from django.core.paginator import Paginator, EmptyPage
  from . import models
  
  
  def all_rooms(request):
      page = request.GET.get("page", 1)
      room_list = models.Room.objects.all()
      paginator = Paginator(room_list, 10, orphans=5)
      try:
          rooms = paginator.page(int(page))
          return render(request, "rooms/home.html", context={"page": rooms})
      except EmptyPage:
          return redirect("/")
  ```

---

#### 11.7 Class Based Views

* **rooms\view.py**

  ```python
  from django.views.generic import ListView
  from . import models
  
  
  class HomeView(ListView):
  
      """ HomeView Definition """
  
      model = models.Room
      paginate_by = 10
      paginate_orphans = 5
      ordering = "created"
  ```

* **'rooms\home.html'을 'rooms\room_list.html'로 이름 변경**

  ```html
  {% extends "base.html" %}
  
  <!-- page_name -->
  {% block page_name %} Home {% endblock page_name %}
  
  <!-- room contents -->
  {% block content %}
  
      {% for room in object_list %}
      <h1>{{ room.name }} / {{ room.price }}</h1>
      {% endfor %}
  
      <h5>
      {% if page_obj.has_previous %}
          <a href="?page={{page_obj.previous_page_number}}">Previous</a>
      {% endif %}
      
      Page {{page_obj.number}} of {{page_obj.paginator.num_pages}}
  
      {% if page_obj.has_next %}
          <a href ="?page={{page_obj.next_page_number}}">Next</a>
      {% endif %}
      </h5>
  
  {% endblock content %}
  ```

---

#### 11.8 Class Based Views part Two

* **rooms\view.py**

  ```python
  from django.views.generic import ListView
  from . import models
  
  
  class HomeView(ListView):
  
      """ HomeView Definition """
  
      model = models.Room
      paginate_by = 10
      paginate_orphans = 5
      ordering = "created"
      context_object_name = "rooms"
  ```

*  **'rooms\room_list.html'**

  ```html
  {% extends "base.html" %}
  
  <!-- page_name -->
  {% block page_name %} Home {% endblock page_name %}
  
  <!-- room contents -->
  {% block content %}
  
      {% for room in rooms %}
      <h1>{{ room.name }} / {{ room.price }}</h1>
      {% endfor %}
  
      <h5>
      {% if page_obj.has_previous %}
          <a href="?page={{page_obj.previous_page_number}}">Previous</a>
      {% endif %}
      
      Page {{page_obj.number}} of {{page_obj.paginator.num_pages}}
  
      {% if page_obj.has_next %}
          <a href ="?page={{page_obj.next_page_number}}">Next</a>
      {% endif %}
      </h5>
  
  {% endblock content %}
  ```

---

