from django.db import models
# import uuid

# def generate_default_username(first_name: str, last_name: str) -> str:
#     return f"{first_name.lower()}_{last_name.lower()}_{uuid.uuid4().hex[:4]}"

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100, null=False, default="first_name")
    last_name = models.CharField(max_length=100, null=False, default="last_name")
    age = models.IntegerField(null=False, default=18)

    class Meta:
        ordering = ['first_name', 'last_name']
    
    # def save(self, *args, **kwargs):
    #     if not self.username:
    #         self.username = generate_default_username(self.first_name, self.last_name)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.id} - {self.username}"
