from .models import Car


logins_mapping = {
    'Vinniza_bat_tz': {'region': 'Вінницька область', 'unit': 'БПОП'},
    'Volin_rota_tz': {'region': 'Волинська область', 'unit': 'РПОП'},
    'Volin_Svityz_tz': {'region': 'Волинська область', 'unit': 'РПОП "Світязь" '},
    'Dnipro_polk_tz': {'region': 'Дніпропетровська область', 'unit': 'ППОП'},
    'Donezk_rota_tz': {'region': 'Донецька область', 'unit': 'РПОП'},
    'Zhitomir_rota_tz': {'region': 'Житомирська область', 'unit': 'РПОП'},
    'Zakarpatty_rota_tz': {'region': 'Закарпатська область', 'unit': 'РПОП'},
    'Zaporigya_bat_tz': {'region': 'Запорізька область', 'unit': 'БПОП'},
    'Zaporigya_Skif_tz': {'region': 'Запорізька область', 'unit': 'БПОП "Скіф" '},
    'Ivano_Frankivsk_rota_tz': {'region': 'Івано-Франківська область', 'unit': 'РПОП'},
    'Kyiv_region_polk_tz': {'region': 'Київська область', 'unit': 'ППОП'},
    'Kyiv_polk1_tz': {'region': 'Київ', 'unit': 'ППОП №1'},
    'Kyiv_polk2_tz': {'region': 'Київ', 'unit': 'ППОП №2'},
    'Kropik_rota_tz': {'region': 'Кіровоградська область', 'unit': 'РПОП'},
    'Lugansk_bat_tz': {'region': 'Луганська область', 'unit': 'БПОП'},
    'Lviv_bat_tz': {'region': 'Львівська область', 'unit': 'БПОП'},
    'Mikolaiv_rota_tz': {'region': 'Миколаївська область', 'unit': 'РПОП'},
    'Odesa_bat_tz': {'region': 'Одеська область', 'unit': 'БПОП'},
    'Poltava_bat_tz': {'region': 'Полтавська область', 'unit': 'БПОП'},
    'Rivne_rota_tz': {'region': 'Рівненська область', 'unit': 'РПОП'},
    'Sumi_bat_tz': {'region': 'Сумська область', 'unit': 'БПОП'},
    'Ternopil_rota_tz': {'region': 'Тернопільська область', 'unit': 'РПОП'},
    'Kharkiv_polk_tz': {'region': 'Харківська область', 'unit': 'ППОП'},
    'Kherson_rotz_tz': {'region': 'Херсонська область', 'unit': 'РПОП'},
    'Khmelnytsk_rota_tz': {'region': 'Хмельницька область', 'unit': 'РПОП'},
    'Khmelnytsk_Bogdan_tz': {'region': 'Хмельницька область', 'unit': 'РПОП "Богдан" '},
    'Cherkasy_bat_tz': {'region': 'Черкаська область', 'unit': 'БПОП'},
    'Chernivtsi_rota_tz': {'region': 'Чернівецька область', 'unit': 'РПОП'},
    'Chernihivska_bat_tz': {'region': 'Чернігівська область', 'unit': 'БПОП'},
}


def variable_user(login_name):
    # Перевірка, чи введений логін присутній в словнику
    if login_name in logins_mapping:
        # Отримання значення регіону та підрозділу для введеного логіну
        region_txt = logins_mapping[login_name]['region']
        unit_txt = logins_mapping[login_name]['unit']
        return region_txt, unit_txt
    else:
        region_txt = "Ви ввели не правильний логін"
        unit_txt = "Це є помилкою"
        return region_txt, unit_txt
