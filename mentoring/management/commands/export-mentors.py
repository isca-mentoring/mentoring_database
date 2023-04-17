from django.core.management.base import BaseCommand, CommandError
from Isca_Mentoring.external_configuration import mentor_form_export_dir
from mentoring.models import MentorEventRegistration, Event
from os.path import join

import csv


class Command(BaseCommand):
    help = 'Export mentor registration data from DB into CSV'

    def add_arguments(self, parser):
        parser.add_argument('--event_name', type=str, help="Event name whose mentor registrations to output.")
        parser.add_argument('--fields', nargs='+', help='Enter which data fields you want in output')

    def handle(self, *args, **options):
        event_name = options.get('event_name')
        fields = options.get('fields')
        try:
            event = Event.objects.get(name=event_name)
        except:
            raise CommandError(f'No event named: {event_name}')

        export_file = join(mentor_form_export_dir, f"{event_name}.csv")
        mentor_registrations = MentorEventRegistration.objects.filter(event_pkey_id=event)

        fields = ['primary_key'] + fields

        self.stdout.write(f"{fields}")
        with open(export_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fields)
            writer.writeheader()
            for mentor in mentor_registrations:
                mentor_dict = dict()
                mentor_dict['primary_key'] = mentor.mentor_event_registration_pkey
                for field in fields[1::]:
                    value = mentor.registration_info.get(field)
                    mentor_dict[field] = value
                writer.writerow(mentor_dict)
