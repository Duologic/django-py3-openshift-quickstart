# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Mail.delivered_to'
        db.add_column('mailarchive_mail', 'delivered_to',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['mailarchive.Address'], related_name='delivered_to'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Mail.delivered_to'
        db.delete_column('mailarchive_mail', 'delivered_to_id')


    models = {
        'mailarchive.account': {
            'Meta': {'object_name': 'Account', 'ordering': "('-modified', '-created')"},
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
            'Meta': {'object_name': 'Address', 'ordering': "('-modified', '-created')"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailaddress': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'mailarchive.headerinfo': {
            'Meta': {'object_name': 'HeaderInfo', 'ordering': "('-modified', '-created')"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Mail']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mailarchive.mail': {
            'Meta': {'object_name': 'Mail', 'ordering': "('-modified', '-created')"},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Account']"}),
            'carboncopy': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'carboncopy'", 'to': "orm['mailarchive.Address']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_delivered': ('django.db.models.fields.DateTimeField', [], {}),
            'date_sent': ('django.db.models.fields.DateTimeField', [], {}),
            'delivered_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Address']", 'related_name': "'delivered_to'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'raw': ('django.db.models.fields.TextField', [], {}),
            'receivers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'receivers'", 'to': "orm['mailarchive.Address']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Address']", 'related_name': "'sender'"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mailarchive']