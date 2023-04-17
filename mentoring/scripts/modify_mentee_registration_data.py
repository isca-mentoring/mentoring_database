from django.db import transaction
from external_data.mentee_forms import parse_isca_2022_mentee_form_1_to_1_from_csv, parse_isca_2022_mentee_form_round_table_from_csv
from mentoring.models import MenteeEventRegistration, Event


def populate_mentee_form_into_db(dataframe, event_name):
    """
    Expects valid dataframe and event_name.
    1) Gets valid Event whose name equals `event_name`.
    2) Delete all MenteeEventRegistration objects belonging to above Event.
    3) Add new MentorEventRegistration objects using dataframe.
    """
    try:
        event = Event.objects.select_for_update().get(name=event_name)
        existing_mentor_registrations_for_event = MenteeEventRegistration.objects.select_for_update().filter(event_pkey=event)
        existing_mentor_registrations_for_event.delete()
        for row_index in dataframe.index:
            try:
                registration_info = dataframe.iloc[row_index].to_dict()
                mentee_registration_obj = MenteeEventRegistration(event_pkey=event, registration_info=registration_info)
                mentee_registration_obj.save()
            except:
                continue
    except Event.DoesNotExist as e:
        raise e(f"Event named: {event_name} does not exist.")
    except Exception as e:
        raise e


# Map Mentor Registration form with corresponding Event name in DB.
dataframe_retrieval_dict = {
    'Interspeech-2022-one-to-one-mentoring': parse_isca_2022_mentee_form_1_to_1_from_csv,
    'Interspeech-2022-round-table-mentoring': parse_isca_2022_mentee_form_round_table_from_csv,
}



def main(form_name):
    if form_name == "Interspeech-2022-round-table-and-one-to-one-mentoring":
        round_table_df = dataframe_retrieval_dict.get('Interspeech-2022-round-table-mentoring')()
        one_to_one_df = dataframe_retrieval_dict.get('Interspeech-2022-one-to-one-mentoring')()
        with transaction.atomic():
            populate_mentee_form_into_db(round_table_df, "Interspeech-2022-round-table-mentoring")
            populate_mentee_form_into_db(one_to_one_df, "Interspeech-2022-one-to-one-mentoring")
    else:
        dataframe = dataframe_retrieval_dict.get(form_name)()
        with transaction.atomic():
            populate_mentee_form_into_db(dataframe, form_name)
