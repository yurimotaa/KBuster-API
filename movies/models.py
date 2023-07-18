from django.db import models


class Movie(models.Model):
    CHOICES = [
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
    ]
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=CHOICES, default="G", null=True)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
    orders = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="movies_orders"
    )


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="order_movies"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_order_movies"
    )
