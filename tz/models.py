from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Car(models.Model):
    region = models.CharField(max_length=50, default=False)
    unit = models.CharField(max_length=50, default=False)
    type_tz = models.CharField(max_length=50)
    brand_tz = models.CharField(max_length=50)
    model_tz = models.CharField(max_length=50)
    year_tz = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    numer_tz = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    color_tz = models.CharField(max_length=20)
    balanser_tz = models.CharField(max_length=50)
    condition_tz = models.CharField(max_length=50)
    liable_tz = models.CharField(max_length=200)
    use_tz = models.CharField(max_length=20, default=False)
    radio_on_tz = models.CharField(max_length=20, default=False)
    refit_tz = models.CharField(max_length=50, default=False)    # Нові поля в БД
    run_tz = models.IntegerField(default=False)
    sgu_tz = models.CharField(max_length=20, default="Не обладнано")
    seats_tz = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(100)], default=False)
    modified_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f"{self.id}, {self.type_tz}, {self.brand_tz}, {self.model_tz}, {self.year_tz}, {self.numer_tz},"
                f"{self.fuel_type}, {self.color_tz}, {self.condition_tz}, {self.use_tz}, {self.radio_on_tz},{self.balanser_tz}, {self.liable_tz}")

    def edit_car(self, new_data):
        # Оновіть дані моделі на основі нових даних
        for field, value in new_data.items():
            setattr(self, field, value)

        # Збережіть оновлену модель
        self.save()
