from tz.models import Car
from django.db.models import Count


def calculation(region, unit):
    count_tz = (
        Car.objects
        .filter(region=region, unit=unit)
        .values('type_tz')
        .annotate(count=Count('type_tz'))
    )

    type_counts = {item['type_tz']: item['count'] for item in count_tz}
    return type_counts