from pandas import read_csv
from Isca_Mentoring.external_configuration import mentor_form_import_dir
from os.path import join


columns_rename = {
    "ï»¿ID": "id",
    "Hora de inÃ­cio":"start",
    'Hora de conclusÃ£o':"end",
    "E-mail":"email",
    "Nome":"nome",
    "Email":"email",
    "Surname":"surname",
    "Given name":"first-name",
    'Alternative email address (Your email address/es will allow you to sign in to our database. If you provided an institutional email above that may expire and you have another email you would like tâ¦': 'alternative-email',
    "Please provide your ISCA membership number":"isca-id",
    "Current affiliation":"current-affiliation",
    "Professional title(s)":"titles",
    "Nationality":"nationality",
    "Country of residence\n":"residence",
    "In which city are you based ?":"city",
    "Gender identity":"gender",
    "Research area(s)":"research-areas",
    "In which sector(s) do you have experience?\n":"sectors-of-experience",
    "Total experience (after doctoral studies, if applicable)\n":"post-doctoral-experience",
    "How many mentees would you be willing to work with ?":"number-of-mentees",
    "What would be your preferred language(s) for 1:1 mentoring sessions ?":"language-preference",
    "If you have any time-zone preference, please select one":"time-zone",
    "Topics your mentee could request advice on may include career planning, academic writing, managing work relationships, time management, unethical behaviour and working with a disability/chronic il...":"topics-mentees-cannot-ask-about",
    "Are you planning to attend Interspeech 2022 ...":"interspeech-22-attending",
    "Is there anything else you would like to tell us?":"anything-else",
}

def parse_isca_2022_mentor_form_1_to_1_from_csv():
    df = read_csv(join(mentor_form_import_dir, "Interspeech-2022-one-to-one-mentoring.csv"), dtype=str, encoding='latin-1')
    df.rename(columns=columns_rename, inplace=True)
    df.fillna("", inplace=True)
    return df
