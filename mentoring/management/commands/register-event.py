from django.core.management.base import BaseCommand, CommandError
from mentoring.models import Event
from mentoring.scripts.modify_event_data import add_event, delete_event, modify_event

import json


class Command(BaseCommand):
    help = 'Register event data into DB'

    def add_arguments(self, parser):
        parser.add_argument('--operation', default='add', const='add', nargs='?', choices=['add', 'delete', 'modify'], help="Choose an operation to perform for selected Event: ['add', 'delete', 'modify']")
        parser.add_argument('--name', type=str, help="Enter the Event's name to perform operation on.")
        parser.add_argument('--event_data', type=str, help="Enter Event data as a valid json string")

    def handle(self, *args, **options):
        try:
            event_name = options.get("name")
            operation = options.get("operation")
            event_data = options.get("event_data")

            if not operation:
                raise CommandError("Enter a valid operation.")
            if not event_name:
                raise CommandError("Enter the Event's name to perform operation on.")

            if event_data:
                event_data = json.loads(event_data)

            if operation=="add":
                if event_data is None:
                    raise CommandError("Enter Event data as a valid json string")
                add_event(event_name, event_data)

            elif operation=="delete":
                delete_event(event_name)

            elif operation=="modify":
                if event_data is None:
                    raise CommandError("Enter Event data as a valid json string")
                modify_event(event_name, event_data)

            self.stdout.write(self.style.SUCCESS(f'Successfully performed `{operation}` operation on `{event_name}` Event.'))

        except Event.DoesNotExist:
            self.stdout.write(self.style.NOTICE(f"Event named `{event_name}` does not exist. First register Event named `{event_name}`, before proceeding."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Exception while performing operation on Event: {e}'))
