from pandas import read_csv
from Isca_Mentoring.external_configuration import mentee_form_import_dir
from os.path import join


columns_rename = {
    "ï»¿ID": "id",
    "Hora de inÃ­cio": "start",
    "Hora de conclusÃ£o": "end",
    "E-mail": "email",
    "Nome": "name",
    "Surname": "surname",
    "First name": "first name",
    "Email address - your institution/work address is preferred": "preferred email",
    "Institution/company where you are based":"based in company or institute",
    "In which city is your institution/company?":"city of base",
    "In which country is your institution/company?":"country of base",
    "If you selected 'Other', please state the country in which your institution/company is located.":"other city of base",
    "What is your nationality?":"nationality",
    "If you selected 'Other', please state your nationality":"other nationality",
    "Gender identity":"gender",
    "At which career stage are you? If you are outside academia, please pick to closest equivalent level to your current role.":"stage of career",
    "In which sector are you studying or working?":"work sector",
    "Will you be attending the mentoring events online or in person in Korea?":"attending online or offline",
    "Which type of mentoring are you interested in attending? (select all that apply)":"interested_type_of_mentoring",
    "Defining research questions for your PhD":"PhD research questions",
    "Handling setbacks in your PhD":"PhD setbacks",
    "Everyday tips for a PhD student":"PhD tips",
    "Managing the supervisor - student relationship":"supervisor relationship",
    "Handling disagreement & conflict in research":"handling conflict",
    "Why was my paper rejected? Insights from reviewers":"paper rejection reason",
    "Under pressure: how to navigate the competitive academic environment":"handling competition",
    "The research-life juggle: time management, productivity and work-life balance":"research life juggle",
    "Reaching out: Growing your network and creating new collaborations":"reaching out",
    "Contributing to your academic community: mentoring, supporting, and being a good peer":"contributing to community",
    "Research integrity and being a responsible researcher":"research integrity",
    "The future of speech startups; where next?":"speech startups",
    "Research in academia versus industry: Which is right for me?":"academia vs industry research",
    "Planning your career in speech: strategies for success":"planning career in speech",
    "Writing your first grant proposal: tips for beginners":"grant proposal writing",
    "First steps: Tips for new group leaders and PIs":"leading groups",
    "Are there other mentoring topics you would like to discuss?":"other topics to discuss",
    "Is there a specific question you would like to ask a mentor or raise for discussion at the round table? You will still have the opportunity to ask other questions during the event, but providing q...":"post round table questions",
    "Do you have a strong preference for a particular kind of mentor? E.g. a particular gender, nationality or work sector. Please give reasons where possible. While we are developing mentoring at ISCA...":"mentor preference",
    "We are making arrangements for one-on-one mentoring by senior ISCA members at any time, outside of Interspeech. Is this something you would be interested in?":"mentoring outside of Interspeech",
    "Is there anything else you want to tell us?":"anything else",
}

def parse_isca_2022_mentee_form_round_table_from_csv():
    df = read_csv(join(mentee_form_import_dir, "Interspeech-2022-round-table-and-one-to-one-mentoring.csv"), dtype=str, encoding='latin-1')

    df.rename(columns=columns_rename, inplace=True)
    df.fillna("", inplace=True)
    df = df[df["interested_type_of_mentoring"].str.contains('Round table', regex=False)]
    return df

def parse_isca_2022_mentee_form_1_to_1_from_csv():
    df = read_csv(join(mentee_form_import_dir, "Interspeech-2022-round-table-and-one-to-one-mentoring.csv"),
                  dtype=str, encoding='latin-1')
    df.rename(columns=columns_rename, inplace=True)
    df.fillna("", inplace=True)
    df = df[df["interested_type_of_mentoring"].str.contains('One-on-one', regex=False)]
    return df
