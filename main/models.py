# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.utils.crypto import get_random_string

# # Create your models here.
# class Place(models.Model):
#   owner = models.ForeignKey(User, on_delete=models.CASCADE)
#   name = models.CharField(max_length=255)
#   image = models.CharField(max_length=255)
#   number_of_tables = models.IntegerField(default=1)
#   font = models.CharField(max_length=100, blank=True)
#   color = models.CharField(max_length=100, blank=True)

#   def __str__(self):
#     return "{}/{}".format(self.owner.username, self.name)

# class Category(models.Model):
#   place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="categories")
#   name = models.CharField(max_length=255)

#   def __str__(self):
#     return "{}/{}".format(self.place, self.name)

# class Tag(models.Model):
#     name = models.CharField(max_length=100)


# class MenuItem(models.Model):
#   place = models.ForeignKey(Place, on_delete=models.CASCADE)
#   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
#   name = models.CharField(max_length=255)
#   description = models.TextField(blank=True)
#   price = models.IntegerField(default=0)
#   image = models.CharField(max_length=255)
#   is_available = models.BooleanField(default=True)
#   tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relationship 

#   def __str__(self):
#     return "{}/{}".format(self.category, self.name)


# class UserSession(models.Model):
#     email = models.EmailField()
#     session_id = models.CharField(max_length=255)
#     created_at = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)  # Existing field to indicate if the session is active
#     table = models.CharField(max_length=10)  # Renamed field for table number

#     def __str__(self):
#         return "{} - {}".format(self.email, self.session_id)

#     @classmethod
#     def create_session_for_email(cls, email, table):
#         # Generate a new session ID. You might want to use a more robust method.
#         session_id = get_random_string(length=32)
#         # Create a new UserSession object with table number and save it to the database.
#         session = cls(email=email, session_id=session_id, table=table)
#         session.save()
#         return session

#     def end_session(self):
#         # Method to end the session
#         self.is_active = False
#         self.save()

# class Order(models.Model):
#     PROCESSING_STATUS = "processing"
#     COMPLETED_STATUS = "completed"
#     SERVED_STATUS = "served"
#     PAID_STATUS = "paid"

#     STATUSES = (
#         (PROCESSING_STATUS, 'Processing'),
#         (COMPLETED_STATUS, 'Completed'),
#         (SERVED_STATUS, 'Served'),
#         (PAID_STATUS, 'Paid'),
#     )

#     place = models.ForeignKey(Place, on_delete=models.CASCADE)
#     table = models.CharField(max_length=2)
#     detail = models.TextField()
#     payment_intent = models.CharField(max_length=255)
#     amount = models.IntegerField()
#     status = models.CharField(max_length=20, choices=STATUSES, default=PROCESSING_STATUS)
#     created_at = models.DateTimeField(default=timezone.now)
#     session_id = models.CharField(max_length=255)  # Retained from previous version
#     email = models.EmailField()  # Retained from previous version

#     def __str__(self):
#         return "{}/{}/${}".format(self.place, self.table, self.amount)

# class Invoice(models.Model):
#     invoice_number = models.CharField(max_length=50, unique=True)
#     table = models.CharField(max_length=10)
#     customer_email = models.EmailField()
#     items = models.JSONField()  # Stores ordered items as JSON
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     issued_at = models.DateTimeField(default=timezone.now)
#     paid = models.BooleanField(default=False)
#     payment_details = models.TextField(blank=True)  # For any payment-related information

#     def __str__(self):
#         return "Invoice {} - Table {} - Total: ${}".format(self.invoice_number, self.table, self.total_amount)



# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.utils.crypto import get_random_string

# # Create your models here.
# class Place(models.Model):
#   owner = models.ForeignKey(User, on_delete=models.CASCADE)
#   name = models.CharField(max_length=255)
#   image = models.CharField(max_length=255)
#   number_of_tables = models.IntegerField(default=1)
#   font = models.CharField(max_length=100, blank=True)
#   color = models.CharField(max_length=100, blank=True)

#   def __str__(self):
#     return "{}/{}".format(self.owner.username, self.name)

# class Category(models.Model):
#   place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="categories")
#   name = models.CharField(max_length=255)

#   def __str__(self):
#     return "{}/{}".format(self.place, self.name)

# class Tag(models.Model):
#     name = models.CharField(max_length=100)


# class MenuItem(models.Model):
#     place = models.ForeignKey(Place, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     price = models.IntegerField(default=0)
#     image = models.CharField(max_length=255)
#     is_available = models.BooleanField(default=True)
#     tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relationship
#     is_drink = models.BooleanField(default=False)  # Add this line

#     def __str__(self):
#         return "{}/{}".format(self.category, self.name)



# class UserSession(models.Model):
#     email = models.EmailField()
#     session_id = models.CharField(max_length=255)
#     created_at = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)  # Existing field to indicate if the session is active
#     table = models.CharField(max_length=10)  # Renamed field for table number

#     def __str__(self):
#         return "{} - {}".format(self.email, self.session_id)

#     @classmethod
#     def create_session_for_email(cls, email, table):
#         # Generate a new session ID. You might want to use a more robust method.
#         session_id = get_random_string(length=32)
#         # Create a new UserSession object with table number and save it to the database.
#         session = cls(email=email, session_id=session_id, table=table)
#         session.save()
#         return session

#     def end_session(self):
#         # Method to end the session
#         self.is_active = False
#         self.save()

# class Order(models.Model):
#     PROCESSING_STATUS = "processing"
#     COMPLETED_STATUS = "completed"
#     SERVED_STATUS = "served"
#     PAID_STATUS = "paid"

#     STATUSES = (
#         (PROCESSING_STATUS, 'Processing'),
#         (COMPLETED_STATUS, 'Completed'),
#         (SERVED_STATUS, 'Served'),
#         (PAID_STATUS, 'Paid'),
#     )
    
#     menu_items = models.ManyToManyField(MenuItem, through='OrderItem')
#     place = models.ForeignKey(Place, on_delete=models.CASCADE)
#     table = models.CharField(max_length=2)
#     detail = models.TextField()
#     payment_intent = models.CharField(max_length=255)
#     amount = models.IntegerField()
#     status = models.CharField(max_length=20, choices=STATUSES, default=PROCESSING_STATUS)
#     created_at = models.DateTimeField(default=timezone.now)
#     session_id = models.CharField(max_length=255)  # Retained from previous version
#     email = models.EmailField()  # Retained from previous version

#     def __str__(self):
#         return "{}/{}/${}".format(self.place, self.table, self.amount)
    
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)


# class Invoice(models.Model):
#     invoice_number = models.CharField(max_length=50, unique=True)
#     table = models.CharField(max_length=10)
#     customer_email = models.EmailField()
#     items = models.JSONField()  # Stores ordered items as JSON
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     issued_at = models.DateTimeField(default=timezone.now)
#     paid = models.BooleanField(default=False)
#     payment_details = models.TextField(blank=True)  # For any payment-related information

#     def __str__(self):
#         return "Invoice {} - Table {} - Total: ${}".format(self.invoice_number, self.table, self.total_amount)



# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.utils.crypto import get_random_string

# # Create your models here.
# class Place(models.Model):
#   owner = models.ForeignKey(User, on_delete=models.CASCADE)
#   name = models.CharField(max_length=255)
#   image = models.CharField(max_length=255)
#   number_of_tables = models.IntegerField(default=1)
#   font = models.CharField(max_length=100, blank=True)
#   color = models.CharField(max_length=100, blank=True)

#   def __str__(self):
#     return "{}/{}".format(self.owner.username, self.name)

# class Category(models.Model):
#   place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="categories")
#   name = models.CharField(max_length=255)

#   def __str__(self):
#     return "{}/{}".format(self.place, self.name)

# class Tag(models.Model):
#     name = models.CharField(max_length=100)


# class MenuItem(models.Model):
#     place = models.ForeignKey(Place, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     price = models.IntegerField(default=0)
#     image = models.CharField(max_length=255)
#     is_available = models.BooleanField(default=True)
#     tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relationship
#     is_drink = models.BooleanField(default=False)  # Add this line

#     def __str__(self):
#         return "{}/{}".format(self.category, self.name)



# class UserSession(models.Model):
#     email = models.EmailField()
#     session_id = models.CharField(max_length=255)
#     created_at = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)  # Existing field to indicate if the session is active
#     table = models.CharField(max_length=10)  # Renamed field for table number

#     def __str__(self):
#         return "{} - {}".format(self.email, self.session_id)

#     @classmethod
#     def create_session_for_email(cls, email, table):
#         # Generate a new session ID
#         session_id = get_random_string(length=32)
#         # Create a new UserSession object with table number and save it to the database
#         session = cls(email=email, session_id=session_id, table=table)
#         session.save()

#         # Check if a UserProfile for this email already exists
#         user_profile, created = UserProfile.objects.get_or_create(email=email)
#         # If created is True, it means a new UserProfile was created. If False, the UserProfile already existed.

#         return session

#     def end_session(self):
#         self.is_active = False
#         self.save()

# class Order(models.Model):
#     PROCESSING_STATUS = "processing"
#     COMPLETED_STATUS = "completed"
#     SERVED_STATUS = "served"
#     PAID_STATUS = "paid"

#     STATUSES = (
#         (PROCESSING_STATUS, 'Processing'),
#         (COMPLETED_STATUS, 'Completed'),
#         (SERVED_STATUS, 'Served'),
#         (PAID_STATUS, 'Paid'),
#     )
    
#     menu_items = models.ManyToManyField(MenuItem, through='OrderItem')
#     place = models.ForeignKey(Place, on_delete=models.CASCADE)
#     table = models.CharField(max_length=2)
#     detail = models.TextField()
#     payment_intent = models.CharField(max_length=255)
#     amount = models.IntegerField()
#     status = models.CharField(max_length=20, choices=STATUSES, default=PROCESSING_STATUS)
#     created_at = models.DateTimeField(default=timezone.now)
#     session_id = models.CharField(max_length=255)  # Retained from previous version
#     email = models.EmailField()  # Retained from previous version

#     def __str__(self):
#         return "{}/{}/${}".format(self.place, self.table, self.amount)
    
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)


# class Invoice(models.Model):
#     invoice_number = models.CharField(max_length=50, unique=True)
#     table = models.CharField(max_length=10)
#     customer_email = models.EmailField()
#     items = models.JSONField()  # Stores ordered items as JSON
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     issued_at = models.DateTimeField(default=timezone.now)
#     paid = models.BooleanField(default=False)
#     payment_details = models.TextField(blank=True)  # For any payment-related information

#     def __str__(self):
#         return "Invoice {} - Table {} - Total: ${}".format(self.invoice_number, self.table, self.total_amount)
    

# class UserProfile(models.Model):
#     email = models.EmailField(max_length=255, unique=True)
#     tags = models.ManyToManyField('Tag', through='UserTagCount', blank=True)
#     # Other fields...

#     def __str__(self):
#         return self.email

# class UserTagCount(models.Model):
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     count = models.IntegerField(default=0)
    

#     def __str__(self):
#         return '{} - {} - {}'.format(self.user_profile.email, self.tag.name, self.count)
    
    




from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.db.models import Count, Prefetch, Avg, Sum, F
from itertools import product

# Create your models here.
class Place(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  number_of_tables = models.IntegerField(default=1)
  font = models.CharField(max_length=100, blank=True)
  color = models.CharField(max_length=100, blank=True)
  tax_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Added field

  def __str__(self):
    return "{}/{}".format(self.owner.username, self.name)

class Category(models.Model):
  place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="categories")
  name = models.CharField(max_length=255)

  def __str__(self):
    return "{}/{}".format(self.place, self.name)

class Tag(models.Model):
    name = models.CharField(max_length=100)


class MenuItem(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relationship
    is_drink = models.BooleanField(default=False)  # Add this line

    def __str__(self):
        return "{}/{}".format(self.category, self.name)



class UserSession(models.Model):
    email = models.EmailField()
    session_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)  # Existing field to indicate if the session is active
    table = models.CharField(max_length=10)  # Renamed field for table number

    def __str__(self):
        return "{} - {}".format(self.email, self.session_id)

    @classmethod
    def create_session_for_email(cls, email, table):
        # Generate a new session ID
        session_id = get_random_string(length=32)
        # Create a new UserSession object with table number and save it to the database
        session = cls(email=email, session_id=session_id, table=table)
        session.save()

        # Check if a UserProfile for this email already exists
        user_profile, created = UserProfile.objects.get_or_create(email=email)
        # If created is True, it means a new UserProfile was created. If False, the UserProfile already existed.

        return session

    def end_session(self):
        self.is_active = False
        self.save()

class Order(models.Model):
    PROCESSING_STATUS = "processing"
    COMPLETED_STATUS = "completed"
    SERVED_STATUS = "served"
    PAID_STATUS = "paid"

    STATUSES = (
        (PROCESSING_STATUS, 'Processing'),
        (COMPLETED_STATUS, 'Completed'),
        (SERVED_STATUS, 'Served'),
        (PAID_STATUS, 'Paid'),
    )
    
    menu_items = models.ManyToManyField(MenuItem, through='OrderItem')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    table = models.CharField(max_length=2)
    detail = models.TextField()
    payment_intent = models.CharField(max_length=255)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUSES, default=PROCESSING_STATUS)
    created_at = models.DateTimeField(default=timezone.now)
    session_id = models.CharField(max_length=255)  # Retained from previous version
    email = models.EmailField()  # Retained from previous version

    def __str__(self):
        return "{}/{}/${}".format(self.place, self.table, self.amount)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    table = models.CharField(max_length=10)
    customer_email = models.EmailField()
    items = models.JSONField()  # Stores ordered items as JSON
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_at = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)
    payment_details = models.TextField(blank=True)
    invoice_tax = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) 

    def __str__(self):
        return "Invoice {} - Table {} - Total: ${}".format(self.invoice_number, self.table, self.total_amount)

class UserProfile(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    tags = models.ManyToManyField('Tag', through='UserTagCount', blank=True)

    def __str__(self):
        return self.email

    def get_preferred_price_range(self):
        """Calculate the user's preferred price range based on past orders."""
        user_orders = Order.objects.filter(email=self.email)
        order_items = OrderItem.objects.filter(order__in=user_orders)
        avg_price = order_items.annotate(item_price=F('menu_item__price') * F('quantity')).aggregate(Avg('item_price'))['item_price__avg']
        if avg_price:
            lower_bound = avg_price * 0.8
            upper_bound = avg_price * 1.2
            return lower_bound, upper_bound
        return None, None

    def get_most_ordered_tags(self):
        """Identify the tags of the most ordered items."""
        most_ordered_items = OrderItem.objects.filter(order__email=self.email).values('menu_item').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')[:5]  # Top 5 items
        most_ordered_item_ids = [item['menu_item'] for item in most_ordered_items]
        tags = Tag.objects.filter(menuitem__id__in=most_ordered_item_ids).distinct()
        return tags

    def recommend_menu_food_items(self, top_n=10):
        # Get user's tag preferences
        user_tag_counts = self.usertagcount_set.all().order_by('-count')
        tag_preferences = {utc.tag_id: utc.count for utc in user_tag_counts}
        lower_bound, upper_bound = self.get_preferred_price_range()
        most_ordered_tags = self.get_most_ordered_tags()

        # Fetch all MenuItems with their related tags, excluding drinks
        menu_items = MenuItem.objects.filter(is_drink=False).prefetch_related('tags')

        # Calculate score for each MenuItem
        menu_item_scores = []
        for item in menu_items:
            score = 0
            # Increase score based on matching user tag preferences
            for tag in item.tags.all():
                if tag in most_ordered_tags:
                    score += tag_preferences.get(tag.id, 0) * 1.5  # Boost for most ordered tags
                else:
                    score += tag_preferences.get(tag.id, 0)

            # Adjust score based on preferred price range
            if lower_bound and upper_bound and lower_bound <= item.price <= upper_bound:
                score *= 1.2  # Increase score if within preferred price range

            if score > 0:  # Consider only items with a positive score
                menu_item_scores.append((item, score))

        # Sort by score in descending order and select top_n items
        recommended_items = sorted(menu_item_scores, key=lambda x: x[1], reverse=True)[:top_n]
        return [item[0] for item in recommended_items]  # Return MenuItem objects

    def recommend_menu_drink_items(self, top_n=10):
        # Get user's tag preferences
        user_tag_counts = self.usertagcount_set.all().order_by('-count')
        tag_preferences = {utc.tag_id: utc.count for utc in user_tag_counts}
        # Since this is for drinks, the preferred price range could optionally be recalculated or adjusted for drinks
        lower_bound, upper_bound = self.get_preferred_price_range()
        most_ordered_tags = self.get_most_ordered_tags()

        # Fetch all MenuItems with their related tags, including only drinks
        menu_items = MenuItem.objects.filter(is_drink=True).prefetch_related('tags')

        # Calculate score for each MenuItem
        menu_item_scores = []
        for item in menu_items:
            score = 0
            # Increase score based on matching user tag preferences
            for tag in item.tags.all():
                if tag in most_ordered_tags:
                    score += tag_preferences.get(tag.id, 0) * 1.5  # Boost for most ordered tags
                else:
                    score += tag_preferences.get(tag.id, 0)

            # Adjust score based on preferred price range, if applicable
            if lower_bound and upper_bound and lower_bound <= item.price <= upper_bound:
                score *= 1.2  # Increase score if within preferred price range

            if score > 0:  # Consider only items with a positive score
                menu_item_scores.append((item, score))

        # Sort by score in descending order and select top_n items
        recommended_items = sorted(menu_item_scores, key=lambda x: x[1], reverse=True)[:top_n]
        return [item[0] for item in recommended_items]  # Return MenuItem objects
    
    def recommend_combo_meals(self, top_n=10):
        # get up to 5 food and drink recommendations each
        recommended_foods = self.recommend_menu_food_items(top_n=10)
        recommended_drinks = self.recommend_menu_drink_items(top_n=10)

        # Use itertools.product to create all possible combinations of food and drink items
        all_combos = list(product(recommended_foods, recommended_drinks))

        # Limit the number of combos to the requested number (top_n), up to the total available
        combo_meals = all_combos[:top_n]

        return combo_meals


class UserTagCount(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    

    def __str__(self):
        return '{} - {} - {}'.format(self.user_profile.email, self.tag.name, self.count)
    
    




