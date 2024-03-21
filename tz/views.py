from django.shortcuts import render, redirect
from .forms import CarForm
from .user_variable import variable_user
from django.shortcuts import get_object_or_404
from .models import Car


def index(request):
    # Головна сторінка
    return render(request, 'tz/index.html')


def tz_unit(request):
    user_login = request.user.username
    if user_login == 'Boss':
        return redirect('leadership:leader_home')
    else:
        region_txt, unit_txt = variable_user(user_login)
    # Головна сторінка інспектора з ТЗ в підрозділі
    cars_count = len(Car.objects.filter(region=region_txt, unit=unit_txt))
    car = Car.objects.filter(type_tz='Легковий', region=region_txt, unit=unit_txt)
    minibus = Car.objects.filter(type_tz='Мікроавтобус', region=region_txt, unit=unit_txt)
    bus = Car.objects.filter(type_tz='Автобус', region=region_txt, unit=unit_txt)
    armored = Car.objects.filter(type_tz='Бронетехніка', region=region_txt, unit=unit_txt)
    pickup = Car.objects.filter(type_tz='Пікап', region=region_txt, unit=unit_txt)
    suv = Car.objects.filter(type_tz='Позашляховик', region=region_txt, unit=unit_txt)
    truck = Car.objects.filter(type_tz='Вантажівка', region=region_txt, unit=unit_txt)

    context = {}
    context['region'] = region_txt
    context['unit'] = unit_txt
    context['cars_count'] = cars_count
    context['car'] = len(car)
    context['minibus'] = len(minibus)
    context['bus'] = len(bus)
    context['armored'] = len(armored)
    context['pickup'] = len(pickup)
    context['suv'] = len(suv)
    context['truck'] = len(truck)

    return render(request, 'tz/main_p_tz.html', context)


def all_units_tz(request, region_txt=None, unit_txt=None):
    # Сторінка усього транспорту одного підрозділу
    if region_txt is not None and unit_txt is not None:
        all_tz = Car.objects.filter(region=region_txt, unit=unit_txt)
        context = {'all_tz': all_tz, 'region': region_txt, 'unit': unit_txt}
        return render(request, 'tz/all_units_tz.html', context)
    else:
        user_login = request.user.username
        name_table = "Таблиця всього транспорту"
        region_txt, unit_txt = variable_user(user_login)
        all_tz = Car.objects.filter(region=region_txt, unit=unit_txt)
        context = {'all_tz': all_tz, 'region': region_txt, 'unit': unit_txt, 'name_table': name_table}
        return render(request, 'tz/all_units_tz.html', context)


def all_car(request):
    # Сторінка усього легкового транспорту
    user_login = request.user.username
    region_txt, unit_txt = variable_user(user_login)
    all_car = Car.objects.filter(type_tz='Легковий', region=region_txt, unit=unit_txt)
    name_table = 'Таблиця усього легкового транспорту'
    context = {'all_tz': all_car, 'name_table': name_table, 'region': region_txt, 'unit': unit_txt}
    return render(request, 'tz/general_table.html', context)


def all_minibus(request):
    # Сторінка усіх мікроавтобусів
    user_login = request.user.username
    region_txt, unit_txt = variable_user(user_login)
    all_minibus = Car.objects.filter(type_tz='Мікроавтобус', region=region_txt, unit=unit_txt)
    name_table = 'Таблиця усіх мікроавтобусів'
    context = {'all_tz': all_minibus,'name_table': name_table, 'region': region_txt, 'unit': unit_txt}
    return render(request, 'tz/general_table.html', context)


def all_bus(request):
    # Сторінка усіх автобусів
    user_login = request.user.username
    region_txt, unit_txt = variable_user(user_login)
    all_bus = Car.objects.filter(type_tz='Автобус', region=region_txt, unit=unit_txt)
    name_table = 'Таблиця усіх автобусів'
    context = {'all_tz': all_bus, 'name_table': name_table, 'region': region_txt, 'unit': unit_txt}
    return render(request, 'tz/general_table.html', context)


def all_truck(request):
    # Сторінка усіх вантажівок
    user_login = request.user.username
    region_txt, unit_txt = variable_user(user_login)
    all_truck = Car.objects.filter(type_tz='Вантажівка', region=region_txt, unit=unit_txt)
    name_table = 'Таблиця усіх вантажівок'
    context = {'all_tz': all_truck, 'name_table': name_table, 'region': region_txt, 'unit': unit_txt}
    return render(request, 'tz/general_table.html', context)

def all_armored(request):
    # Сторінка усієї броньованої техніки
    user_login = request.user.username
    region_txt, unit_txt = variable_user(user_login)
    all_armored = Car.objects.filter(type_tz='Бронетехніка', region=region_txt, unit=unit_txt)
    name_table = 'Таблиця усієї бронетехніки'
    context = {'all_tz': all_armored, 'name_table': name_table, 'region': region_txt, 'unit': unit_txt}
    return render(request, 'tz/general_table.html', context)


def all_pickup(request):
    # Сторінка усіх пікапів
    user_login = request.user.username
    region_txt, unit_txt = variable_user(user_login)
    all_pickup = Car.objects.filter(type_tz='Пікап', region=region_txt, unit=unit_txt)
    name_table = 'Таблиця усіх пікапів'
    context = {'all_tz': all_pickup, 'name_table': name_table, 'region': region_txt, 'unit': unit_txt}
    return render(request, 'tz/general_table.html', context)


def all_suv(request):
    # Сторінка усіх позашляховиків
    user_login = request.user.username
    region_txt, unit_txt = variable_user(user_login)
    all_suv = Car.objects.filter(type_tz='Позашляховик', region=region_txt, unit=unit_txt)
    name_table = 'Таблиця позашляховиків'
    context = {'all_tz': all_suv, 'name_table': name_table,  'region': region_txt, 'unit': unit_txt}
    return render(request, 'tz/general_table.html', context)


def add_tz(request):
    # Додавання транспортного засобу
    user_login = request.user.username
    region_txt, unit_txt = variable_user(user_login)
    if request.method == 'POST':
        brand_tz = request.POST.get('brand_tz')
        type_tz = request.POST.get('type_tz')
        model_tz = request.POST.get('model_tz')
        year_tz = request.POST.get('year_tz')
        numer_tz = request.POST.get('numer_tz')
        fuel_type = request.POST.get('fuel_type')
        color_tz = request.POST.get('color_tz')
        condition_tz = request.POST.get('condition_tz')
        balanser_tz = request.POST.get('balanser_tz')
        liable_tz = request.POST.get('liable_tz')
        use_tz = request.POST.get('use_tz')
        radio_on_tz = request.POST.get('radio_on_tz')
        refit_tz = request.POST.get('refit_tz')
        run_tz = request.POST.get('run_tz')
        sgu_tz = request.POST.get('sgu_tz')
        seats_tz = request.POST.get('seats_tz')
        new_car = Car.objects.create(region=region_txt, unit=unit_txt, type_tz=type_tz, brand_tz=brand_tz, model_tz=model_tz,
                           year_tz=year_tz, numer_tz=numer_tz, fuel_type=fuel_type, color_tz=color_tz, balanser_tz=balanser_tz,
                           condition_tz=condition_tz, liable_tz=liable_tz, use_tz=use_tz, radio_on_tz=radio_on_tz, refit_tz=refit_tz,
                           run_tz=run_tz, sgu_tz=sgu_tz, seats_tz=seats_tz)
        request.session['title_txt'] = "Ви додали транспортний засіб з наступними даними:"
        return redirect('tz:one_tz', tz_id=new_car.id)
    return render(request, 'tz/add_tz.html')


def edit_tz(request, tz_id):
    # Отримати екземпляр Car за допомогою id
    edit_car = get_object_or_404(Car, id=tz_id)
    # визначення перемінних
    name_table = "Ви бажаєте внести зміни до наступного транспортного засобу:"
    if request.method == 'POST':
        edit_car.run_tz = request.POST.get('run_tz')
        edit_car.use_tz = request.POST.get('use_tz')
        edit_car.liable_tz = request.POST.get('liable_tz')
        edit_car.condition_tz = request.POST.get('condition_tz')
        edit_car.refit_tz = request.POST.get('refit_tz')
        edit_car.numer_tz = request.POST.get('numer_tz')
        edit_car.radio_on_tz = request.POST.get('radio_on_tz')
        edit_car.sgu_tz = request.POST.get('sgu_tz')
        edit_car.color_tz = request.POST.get('color_tz')

        edit_car.save()
        request.session['title_txt'] = "Ви внесли зміни до наступного запису:"
        return redirect('tz:one_tz', tz_id=edit_car.id)  # Замініть це на вашу сторінку після успішного редагування
    else:
        # Якщо це GET-запит, просто відобразити форму з поточними даними
        form = CarForm(instance=edit_car)

    context = {'form': form, 'tz': edit_car, 'name_table': name_table}
    return render(request, 'tz/edit_tz.html', context)


def one_tz(request, tz_id):
    name_table = request.session['title_txt']
    car_data = get_object_or_404(Car, id=tz_id)

    context = {'one_car': tz_id, 'tz': car_data, 'name_table': name_table}
    return render(request, 'tz/one_tz.html', context)
