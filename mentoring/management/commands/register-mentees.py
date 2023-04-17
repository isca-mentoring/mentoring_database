from django.core.management.base import BaseCommand, CommandError
from Isca_Mentoring.external_configuration import mentee_form_import_dir
from mentoring.models import Event
from mentoring.scripts.modify_mentee_registration_data import main
from os.path import exists, join


class Command(BaseCommand):
    help = 'Register mentee form data into DB'

    def add_arguments(self, parser):
        parser.add_argument('--form_name', type=str)

    def handle(self, *args, **options):
        try:
            form_name = options.get('form_name', '')
            expected_file = join(mentee_form_import_dir, f"{form_name}.csv")

            if not exists(expected_file):
                raise CommandError(f'csv-file named: {form_name} missing-')

            main(form_name)

            self.stdout.write(self.style.SUCCESS(f'Successfully registered `{form_name}` data.'))

        except Event.DoesNotExist:
            self.stdout.write(self.style.NOTICE(f"Event named `{form_name}` does not exist. First register Event named `{form_name}`, before proceeding."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Exception while registering mentors for event: {e}'))
