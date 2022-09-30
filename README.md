# ISCA Mentoring and Mentee Database 
Initiative of ISCA-SAC and the ISCA's Mentoring Committee.
This repository maintains the database storing Mentoring and Mentee registrations.

### Recommended software versions
P.S. The version numbers are recommendations only.

* PgAdmin 4
* PostgreSQl 14
* Python 3.9

### Create new virtual environment 
```
Navigate to repository directory:
$ pip install virtualenv
# Create new virtual env
$ python -m virtualenv venv_Isca_Mentoring (on Windows)
# Activate virtual env

```



### Command line interface reference
CAUTION: When you delete an Event, all Mentor-Registrations and Mentee-Registrations associated with that Event are also removed.
```
Add Event
$ python manage.py register-event --operation add --name Interspeech-2022-one-to-one-mentoring --event_data "{\"dates\":[\"18-09-2022\",\"19-09-2022\",\"20-09-2022\",\"21-09-2022\",\"22-09-2022\"],\"location\":[\"Remote\",\"Incheon,SouthKorea\"],\"description\":\"One to One mentoring between students and researchers. This event is conducted during Interspeech 2022\"}
$ python manage.py register-event --operation add --name Interspeech-2022-round-table-mentoring --event_data "{\"dates\":[\"21-09-2022\",\"22-09-2022\"],\"location\":[\"Incheon,SouthKorea\"],\"description\":\"Round table mentoring betweenstudentsandresearchers.ThiseventisconductedduringInterspeech2022\"}" 

Modify Event
$ python manage.py register-event --operation modify --name Interspeech-2022-round-table-mentoring --event_data "{\"dates\":[\"21-09-2022\"],\"location\":[\"Incheon,SouthKorea\"],\"description\":\"Round table mentoring betweenstudentsandresearchers.ThiseventisconductedduringInterspeech2022\"}" 

Delete Event
$ python manage.py register-event --operation delete --name Interspeech-2022-one-to-one-mentoring
$ python manage.py register-event --operation delete --name Interspeech-2022-round-table-mentoring

Register Mentors for an Event (This deleted existing mentor registrations for that event)
$ python manage.py register-mentors --form_name Interspeech-2022-one-to-one-mentoring
$ python manage.py register-mentors --form_name Interspeech-2022-round-table-mentoring

Register Mentees for an Event (This deleted existing mentee registrations for that event)
$ python manage.py register-mentees --form_name Interspeech-2022-round-table-and-one-to-one-mentoring

Export Mentor-Registrations for an Event into a CSV file
$ python manage.py export-mentors --event_name Interspeech-2022-round-table-mentoring --fields "affiliation" "mode of attendance" "topics intersted in hosting" "professional-title"
```

### Resources
JSON to String converter: https://jsontostring.com/
(Sometimes spaces are removed from strings while doig this. Have to manually add.)
