from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.


class Person(models.Model):
	user = models.OneToOneField(User, on_delete=CASCADE)
	pay_to = models.DateField()

	def __str__(self):
		return f"{self.user.username} - {self.user.first_name} {self.user.last_name}"


class Genre(models.Model):
	name = models.CharField(max_length=32, unique=True)

	class Meta:
		verbose_name_plural = "Genres"
		ordering = ["name"]

	def __str__(self):
		return f"{self.name}"


class Author(models.Model):
	name = models.CharField(max_length=32, null=False)
	birth_date = models.DateField(null=True, blank=True)
	country = models.CharField(max_length=32, null=True, blank=True)
	biography = models.TextField

	class Meta:
		ordering = ["name", "birth_date"]

	def __str__(self):
		return f"{self.name} - {self.country} ({self.birth_date})"


class Language(models.Model):
	language = models.CharField(max_length=32, unique=True)

	def __str__(self):
		return f"{self.language}"


class Book(models.Model):
	name = models.CharField(max_length=64, null=False, blank=False)
	original_name = models.CharField(max_length=64, null=False, blank=False)
	genre = models.ManyToManyField(Genre)
	year = models.PositiveIntegerField(null=True, blank=True)
	language = models.ManyToManyField(Language)
	author = models.ManyToManyField(Author)
	image = models.CharField(max_length=256, blank=True, null=True)
	description = models.TextField()
	page = models.PositiveIntegerField()
	isbn = models.CharField(max_length=32, null=False)
	amount = models.PositiveIntegerField()

	def get_author(self):
		return self.author.first().name

	def get_author_id(self):
		return self.author.first().id

	def get_language(self):
		return self.language.first().language

	def get_genre(self):
		return self.genre.first().name

	def __str__(self):
		return f"{self.name} - {self.get_author()} ({self.year})"


class Rented(models.Model):
	id_book = models.ForeignKey(
		Book, on_delete=models.SET_NULL, null=True, blank=True, default=None
	)
	id_user = models.ForeignKey(
		Person, on_delete=models.SET_NULL, null=True, blank=True, default=None
	)
	rent_date = models.DateField(blank=True, null=True)
	reservation_date = models.DateField(auto_now_add=True)
	return_date = models.DateField(blank=True, null=True)
	returned = models.BooleanField(default=False, null=True, blank=True)
	canceled = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.id_book.name} - {self.id_user}"





class Comment(models.Model):
	id_book = models.ForeignKey(
		Book, on_delete=models.SET_NULL, null=True, blank=True, default=None
	)
	id_user = models.ForeignKey(
		Person, on_delete=models.SET_NULL, null=True, blank=True, default=None
	)
	comment = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Order(models.Model):
	user = models.ForeignKey(Person, on_delete=CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, blank=True, null=True)

	@property
	def total_items(self):
		order_items = self.orderitem_set.all()
		total = len(order_items)
		return total

	def __str__(self):
		return f"{self.user} - {self.id}"


class OrderItem(models.Model):
	cart = models.ForeignKey(Order, on_delete=CASCADE)
	book = models.ForeignKey(Book, on_delete=CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	canceled = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.cart.id} - {self.book} - {self.cart.user}"


class Reserved(models.Model):
	id_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	id_user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	reservation_date = models.DateField(auto_now_add=True)
	email_sent = models.BooleanField(default=False, null=True, blank=True)

	def __str__(self):
		return f"{self.id_book.name} - {self.id_user}"

	class Meta:
		verbose_name_plural = "Reserved"
class Rating(models.Model):
	id_order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	id_book = models.ForeignKey(
		Book, on_delete=models.SET_NULL, null=True, blank=True, default=None
	)
	id_user = models.ForeignKey(
		Person, on_delete=models.SET_NULL, null=True, blank=True, default=None
	)
	rating = models.PositiveIntegerField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)