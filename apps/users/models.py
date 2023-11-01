from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.users.managers import UserManager
from django.db import models
from apps.users import constants

class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=45, verbose_name="Имя")
    lastname = models.CharField(max_length=45, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Эл. почта")
    image = models.ImageField(blank=True, verbose_name="Аватар", upload_to="media/avatar/", default="media/avatar/avatar.jpg")
    birthday = models.DateField(null=True, blank=True, verbose_name="День рождения")
    gender = models.CharField(choices=constants.GENDER, verbose_name="Пол", max_length=20)
    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Персонал", default=False)
    data_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def get_full_name(self):
        full_name = "%s %s" % (self.firstname, self.lastname)
        return full_name.strip()

    def __str__(self):
        return f"{self.firstname}, {self.lastname} {self.email}"


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.user}, {self.token}"