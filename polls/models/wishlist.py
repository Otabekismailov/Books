from django.db import models


class WishList(models.Model):
    user = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="wish_lists", verbose_name="Foydalanuvchi"
    )
    products = models.ForeignKey("polls.Product", on_delete=models.CASCADE, verbose_name="Mahsulot")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "products"]

    def __str__(self):
        return f"{self.user.username} - {self.products.title}"
