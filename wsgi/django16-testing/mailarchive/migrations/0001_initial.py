# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mail'
        db.create_table('mailarchive_mail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('messageid', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('raw', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mailarchive', ['Mail'])


    def backwards(self, orm):
        # Deleting model 'Mail'
        db.delete_table('mailarchive_mail')


    models = {
        'mailarchive.mail': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Mail'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'raw': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['mailarchive']