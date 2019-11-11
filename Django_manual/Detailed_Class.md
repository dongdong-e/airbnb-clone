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

  