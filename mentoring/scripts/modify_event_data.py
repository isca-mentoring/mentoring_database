from mentoring.models import Event
from django.db import transaction


@transaction.atomic
def add_event(event_name, event_data):
    Event(name=event_name, additional_information=event_data).save()


@transaction.atomic
def delete_event(event_name):
    try:
        event = Event.objects.get(name=event_name)
        event.delete()
    except Event.DoesNotExist as e:
        raise e(f"Cannot find Event named `{event_name}`")


@transaction.atomic
def modify_event(event_name, event_data):
    try:
        event = Event.objects.get(name=event_name)
        event.additional_information = event_data
        event.save()
    except Event.DoesNotExist as e:
        raise e(f"Cannot find Event named `{event_name}`")

