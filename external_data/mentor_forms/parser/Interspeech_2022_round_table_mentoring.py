from pandas import read_csv
from Isca_Mentoring.external_configuration import mentor_form_import_dir
from os.path import join


columns_rename = {
    "ID": "id",
    "Start time": "start-time",
    "Completion time": "end-time",
    "Email": "email",
    "Name": "name",
    "Email address (your work email address is preferred)": "email",
    "Surname": "surname",
    "Given name": "first-name",
    "Professional title(s), if applicable": "professional-title",
    "Current affiliation": "affiliation",
    "In which sector(s) do you have experience?\n": "sectors-of-experience",
    "How will you be attending Interspeech this year?": "mode of attendance",
    "On which of the following topics would you be happy to host a round table? Select all that apply.": "topics intersted in hosting",
    "Is there anything else you would like to tell us?": "additional info",
}

def parse_isca_2022_mentor_form_rounf_table_from_csv():
    df = read_csv(join(mentor_form_import_dir, "Interspeech-2022-round-table-mentoring.csv"), dtype=str, encoding='latin-1')
    df.rename(columns=columns_rename, inplace=True)
    df.fillna("", inplace=True)
    return df
