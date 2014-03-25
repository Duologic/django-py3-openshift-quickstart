from django.db import models
from django_extensions.db.models import TimeStampedModel

class Address(TimeStampedModel):
    mailaddress = models.EmailField()
    names_json = models.TextField() # json array with possible names for the owner, update on check if exists

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
    account = models.ManyToManyField('Account') # should this be manytomany to avoid duplicate mails?
    raw_mail = models.TextField()
    message_id = models.CharField(max_length=200)
    inreplyto_id = models.ForeignKey('Mail', null=True) # if found, use this
    inreplyto_text = models.CharField(max_length=200, null=True)
    sender_address = models.ForeignKey('Address', related_name='sender', null=True)
    from_address = models.ForeignKey('Address', related_name='from', null=True)
    delivered_to = models.ForeignKey('Address', related_name='delivered_to', null=True)
    receivers_to = models.ManyToManyField('Address', related_name='receivers', null=True)
    carboncopy_to = models.ManyToManyField('Address', related_name='carboncopy', null=True)
    date_sent = models.DateTimeField(null=True)
    date_delivered = models.DateTimeField(null=True) # multiple received dates: use most recent date? 
    subject = models.CharField(max_length=200, null=True)
    text_body = models.TextField(null=True, blank=True)
    html_body = models.TextField(null=True, blank=True)

class Attachment(TimeStampedModel):
    mail = models.ForeignKey('Mail')
    ctype = models.CharField(max_length=200, null=True)
    cencoding = models.CharField(max_length=200, null=True)
    cdisposition = models.CharField(max_length=200, null=True)
    payload = models.TextField()
