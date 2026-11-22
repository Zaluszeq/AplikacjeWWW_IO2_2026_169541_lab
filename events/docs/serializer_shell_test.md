{'id': 4, 'title': 'Darmowy Webinar Django', 'slug': 'darmowy-webinar-django', 'category_id': 1, 'organizer_id': 1, 'description': 'temp', 'location': 'http://127.0.0.1:8000/admin', 'date': '2026-11-25T18:00:00Z', 'capacity': 500, 'price': '0.00', 'is_published': False, 'created_at': '2026-11-22T16:02:54.955656Z'}
b'{"id":4,"title":"Darmowy Webinar Django","slug":"darmowy-webinar-django","category_id":1,"organizer_id":1,"description":"temp","location":"http://127.0.0.1:8000/admin","date":"2026-11-25T18:00:00Z","capacity":500,"price":"0.00","is_published":false,"created_at":"2026-11-22T16:02:54.955656Z"}'

Dane są poprawne!
{'title': 'Nowe Warsztaty Pythona', 'slug': 'nowe-warsztaty-pythona', 'category': <Category: Technologia>, 'organizer': <User: bartek>, 'description': 'temp', 'location': 'http://127.0.0.1:8000/admin', 'date': datetime.datetime(2026, 11, 25, 18, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')), 'capacity': 500, 'price': Decimal('0.00'), 'is_published': False}
Utworzono wydarzenie o id=5
5

Czy poprawne? False
Błędy: {'title': [ErrorDetail(string='This field may not be blank.', code='blank')], 'slug': [ErrorDetail(string='This field is required.', code='required')], 'category_id': [ErrorDetail(string='This field is required.', code='required')], 'organizer_id': [ErrorDetail(string='This field is required.', code='required')], 'description': [ErrorDetail(string='This field is required.', code='required')], 'location': [ErrorDetail(string='This field is required.', code='required')], 'date': [ErrorDetail(string='This field is required.', code='required')], 'capacity': [ErrorDetail(string='Ensure this value is greater than or equal to 1.', code='min_value')]}

Czy poprawne? False
Błędy: {'title': [ErrorDetail(string='This field is required.', code='required')], 'category_id': [ErrorDetail(string='This field is required.', code='required')], 'date': [ErrorDetail(string='Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z].', code='invalid')]}
