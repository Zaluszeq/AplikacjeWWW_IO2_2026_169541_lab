from decimal import Decimal

from events.models import Event


print("=== 1. Opublikowane wydarzenia (chronologicznie) ===")
published_events = Event.objects.filter(is_published=True).order_by('date')
for event in published_events:
    print(f"{event.date:%Y-%m-%d %H:%M} - {event.title}")


print("\n=== 2. Wydarzenia z limitem >= 50 miejsc ===")
big_events = Event.objects.filter(capacity__gte=50)
for event in big_events:
    print(f"{event.title} - limit: {event.capacity}")


print("\n=== 3. Liczba darmowych wydarzeń ===")
free_count = Event.objects.filter(price=Decimal('0.00')).count()
print(f"Darmowe wydarzenia: {free_count}")


print("\n=== 4. Zmiana statusu publikacji ===")
event = Event.objects.filter(is_published=True).first()
if event is None:
    print("Brak opublikowanych wydarzeń do zmiany.")
else:
    print(f"Przed: {event.title} -> is_published={event.is_published}")
    event.is_published = False
    event.save()
    event.refresh_from_db()
    print(f"Po:    {event.title} -> is_published={event.is_published}")