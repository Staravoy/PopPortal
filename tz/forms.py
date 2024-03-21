from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'region': 'Область',
            'unit': 'Підрозділ',
            'type_tz': 'Тип ТЗ',
            'brand_tz': 'Марка',
            'model_tz': 'Модель',
            'year_tz': 'Рік виробництва',
            'numer_tz': 'Номерний знак',
            'fuel_type': 'Вид палива',
            'color_tz': 'Колір',
            'balanser_tz': 'Балансоутримувач',
            'condition_tz': 'Стан',
            'liable_tz': 'Відповідальний за ТЗ',
            'use_tz': 'Застосування ',
            'radio_on_tz': 'Наявність радіостанції',
            'refit_tz': 'Дата останнього ремонту',
            'sgu_tz': 'Наявність СГУ',
            'seats_tz': 'Кількість посадочних місць',
        }
