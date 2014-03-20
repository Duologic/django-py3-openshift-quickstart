from django.db import models
from django_extensions.db.models import TimeStampedModel

class Address(TimeStampedModel):
    mailaddress = models.EmailField()

class Account(TimeStampedModel):
    mailaddress = models.ForeignKey('Address')
    imapuri = models.URLField()
    imapport = models.PositiveSmallIntegerField()
    imapuser = models.CharField(max_length=200)
    imappasswd = models.CharField(max_length=200) # insecure, encrypt/decrypt unavoidable
    imapssl = models.BooleanField(max_length=200)

class HeaderInfo(TimeStampedModel):
    mail = models.ForeignKey('Mail')
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Mail(TimeStampedModel):
    account = models.ForeignKey('Account') # should this be manytomany to avoid duplicate mails?
    messageid = models.CharField(max_length=200)
    raw = models.TextField()
    sender = models.ForeignKey('Address', related_name='sender')
    delivered_to = models.ForeignKey('Address', related_name='delivered_to')
    receivers = models.ManyToManyField('Address', related_name='receivers')
    carboncopy = models.ManyToManyField('Address', related_name='carboncopy')
    date_sent = models.DateTimeField()
    date_delivered = models.DateTimeField() # multiple received dates in raw message?
    subject = models.CharField(max_length=200)
    text_body = models.TextField()
    html_body = models.TextField()
    # attachments?
