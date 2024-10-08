title_mapping = {
    'all': {'title': 'Таблиця усього транспорту підрозділів поліції особливого призначення'},
    'Легковий': {'title': 'Таблиця усього легкового транспорту підрозділів поліції особливого призначення'},
    'Мікроавтобус': {'title':'Таблиця усіх мікроавтобусів підрозділів поліції особливого призначення'},
    'Автобус': {'title': 'Таблиця усіх автобусів підрозділів поліції особливого призначення'},
    'Пікап': {'title': 'Таблиця усіх пікапів підрозділів поліції особливого призначення'},
    'Вантажний': {'title': 'Таблиця усього вантажного транспорту підрозділів поліції особливого призначення'},
    'Бронетехніка': {'title': 'Таблиця усієї броньованої техніки підрозділів поліції особливого призначення'},
}


def table_title(title_name):
    # Перевірка, чи введений логін присутній в словнику
    title_info = title_mapping.get(title_name)

    # Перевірка, чи знайдено інформацію за введеним ключем
    if title_info:
        # Отримання значення 'title' зі словника
        title = title_info.get('title')
        return title
    else:
        # Обробка випадку, коли ключа немає в словнику
        return f"No information found for title: {title_name}"
