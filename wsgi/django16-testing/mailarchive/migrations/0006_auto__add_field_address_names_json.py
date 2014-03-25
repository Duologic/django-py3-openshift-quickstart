# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Address.names_json'
        db.add_column('mailarchive_address', 'names_json',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Address.names_json'
        db.delete_column('mailarchive_address', 'names_json')


    models = {
        'mailarchive.account': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Account'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imappasswd': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'imapport': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'imapssl': ('django.db.models.fields.BooleanField', [], {'max_length': '200'}),
            'imapuri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'imapuser': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mailaddress': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Address']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'mailarchive.address': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Address'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailaddress': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'names_json': ('django.db.models.fields.TextField', [], {})
        },
        'mailarchive.headerinfo': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'HeaderInfo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Mail']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mailarchive.mail': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Mail'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Account']"}),
            'carboncopy': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'carboncopy'", 'symmetrical': 'False', 'to': "orm['mailarchive.Address']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_delivered': ('django.db.models.fields.DateTimeField', [], {}),
            'date_sent': ('django.db.models.fields.DateTimeField', [], {}),
            'delivered_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'delivered_to'", 'to': "orm['mailarchive.Address']"}),
            'html_body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'raw': ('django.db.models.fields.TextField', [], {}),
            'receivers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'receivers'", 'symmetrical': 'False', 'to': "orm['mailarchive.Address']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': "orm['mailarchive.Address']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text_body': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['mailarchive']