from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
    
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Game(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='games')
    igdb_id = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    rating = models.IntegerField(null=True, blank=True)
    total_hours = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'igdb_id'], name='unique game')
        ]

    def __str__(self):
        return self.igdb_id