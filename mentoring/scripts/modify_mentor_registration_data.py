from django.db import transaction
from external_data.mentor_forms import parse_isca_2022_mentor_form_1_to_1_from_csv, parse_isca_2022_mentor_form_rounf_table_from_csv
from mentoring.models import MentorEventRegistration, Event


def populate_mentor_form_into_db(dataframe, event_name):
    """
    Expects valid dataframe and form_name.
    1) Gets valid Event whose name equals `form_name`.
    2) Delete all MentorEventRegistration objects belonging to above Event.
    3) Add new MentorEventRegistration objects using dataframe.
    """
    try:
        event = Event.objects.select_for_update().get(name=event_name)
        existing_mentor_registrations_for_event = MentorEventRegistration.objects.select_for_update().filter(event_pkey=event)
        existing_mentor_registrations_for_event.delete()

        for row_index in dataframe.index:
            registration_info = dataframe.iloc[row_index].to_dict()
            mentor_registration_obj = MentorEventRegistration(event_pkey=event, registration_info=registration_info)
            mentor_registration_obj.save()
    except Event.DoesNotExist as e:
        raise e(f"Event named: {event_name} does not exist.")
    except Exception as e:
        raise e


# Map Mentor Registration form with corresponding Event name in DB.
dataframe_retrieval_dict = {
    'Interspeech-2022-one-to-one-mentoring': parse_isca_2022_mentor_form_1_to_1_from_csv,
    'Interspeech-2022-round-table-mentoring': parse_isca_2022_mentor_form_rounf_table_from_csv,
}


def main(form_name):
    dataframe = dataframe_retrieval_dict.get(form_name)()
    with transaction.atomic():
        populate_mentor_form_into_db(dataframe, form_name)
