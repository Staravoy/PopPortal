from django.shortcuts import render
from tz.models import Car
from .title_for_table import table_title
from tz.views import all_units_tz
from .calculation import calculation


def leader_home(request):
    # Головна сторінка керівника
    return render(request, 'leadership/leader_home.html')


def transport(request):
    # Загальна таблиця транспорту підрозділів для керівництва
    unique_region_unit = Car.objects.values('region', 'unit').distinct()  # Визначення кількості регіонів
    region_unit_data = []

    for region_unit in unique_region_unit:
        region = region_unit['region']
        unit = region_unit['unit']
        total_count = Car.objects.filter(region=region, unit=unit).count()
        type_counts = calculation(region, unit)

        region_unit_data.append({
            'region': region,
            'unit': unit,
            'total_count': total_count,
            **type_counts  # Додаємо всі значення з type_counts у словник
        })
    print(region_unit_data)
    # Підрахунки загальної кількості ТЗ
    amount_transport = len(Car.objects.all())
    car = len(Car.objects.filter(type_tz='Легковий'))
    suv = len(Car.objects.filter(type_tz='Позашляховики'))
    minibus = len(Car.objects.filter(type_tz='Мікроавтобус'))
    bus = len(Car.objects.filter(type_tz='Автобус'))
    armored = len(Car.objects.filter(type_tz='Броне техніка'))
    pickup = len(Car.objects.filter(type_tz='Пікап'))
    truck = len(Car.objects.filter(type_tz='Вантажний'))
    other = len(Car.objects.filter(type_tz='Інші'))

    # створення словника для передачі в контекст
    context = {
        'region_unit_data': region_unit_data,
        'unique_region_unit': unique_region_unit,
        'amount_transport': amount_transport,
        'car': car,
        'suv': suv,
        'minibus': minibus,
        'bus': bus,
        'armored': armored,
        'pickup': pickup,
        'truck': truck,
        'other': other,
    }


    return render(request, 'leadership/transport.html', context)



def all_transport(request, type):
    # увесь існуючий транспорт
    if type == 'all':
        title_table = table_title(type)
        all_tz = Car.objects.all()
    else:
        title_table = table_title(type)
        all_tz = Car.objects.filter(type_tz=type)

    context = {'title_table': title_table, 'all_tz': all_tz}
    return render(request, 'leadership/all_transport.html', context)



