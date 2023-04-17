from django.db import models
from django.db.models import CASCADE

from mentoring.constants import MEETING_ROLES_CHOICES


def default_person_contact_info():
    return {
        "verified_emails": [],
        "unverified_emails": [],
    }


def default_person_personal_info():
    return {
        "name": None,
        "date_of_birth": None,
        "gender": None,
    }


def default_event_additional_info():
    return {
        "dates": [],
        "description": None,
    }


class Person(models.Model):
    person_pkey = models.BigAutoField(primary_key=True)
    contact_information = models.JSONField(default=default_person_contact_info)
    personal_information = models.JSONField(default=default_person_personal_info)
    industry_information = models.JSONField(default=dict)
    educational_information = models.JSONField(default=dict)


class Event(models.Model):
    event_pkey = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, blank=False, max_length=255)
    additional_information = models.JSONField(default=default_event_additional_info)


class Meeting(models.Model):
    meeting_pkey = models.BigAutoField(primary_key=True)
    additional_info = models.TextField()


class MentorEventRegistration(models.Model):
    mentor_event_registration_pkey = models.BigAutoField(primary_key=True)
    event_pkey = models.ForeignKey(Event, on_delete=CASCADE)
    registration_info = models.JSONField(default=dict)


class MenteeEventRegistration(models.Model):
    mentee_event_registration_pkey = models.BigAutoField(primary_key=True)
    event_pkey = models.ForeignKey(Event, on_delete=CASCADE)
    registration_info = models.JSONField(default=dict)


class AdminEventRegistration(models.Model):
    admin_event_registration_pkey = models.BigAutoField(primary_key=True)
    event_pkey = models.ForeignKey(Event, on_delete=CASCADE)
    registration_info = models.JSONField(default=dict)


class MeetingPersonRole(models.Model):
    meeting_pkey = models.ForeignKey(Meeting, on_delete=CASCADE)
    mentor_pkey = models.ForeignKey(MentorEventRegistration, on_delete=CASCADE)
    mentee_pkey = models.ForeignKey(MenteeEventRegistration, on_delete=CASCADE)
    admin_pkey = models.ForeignKey(AdminEventRegistration, on_delete=CASCADE)
    role = models.CharField(choices=MEETING_ROLES_CHOICES, max_length=13)