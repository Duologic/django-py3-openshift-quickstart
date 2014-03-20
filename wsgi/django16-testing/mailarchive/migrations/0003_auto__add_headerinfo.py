# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HeaderInfo'
        db.create_table('mailarchive_headerinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('mail', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailarchive.Mail'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mailarchive', ['HeaderInfo'])


    def backwards(self, orm):
        # Deleting model 'HeaderInfo'
        db.delete_table('mailarchive_headerinfo')


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
            'carboncopy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mailarchive.Address']", 'symmetrical': 'False', 'related_name': "'carboncopy'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_delivered': ('django.db.models.fields.DateTimeField', [], {}),
            'date_sent': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'raw': ('django.db.models.fields.TextField', [], {}),
            'receivers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mailarchive.Address']", 'symmetrical': 'False', 'related_name': "'receivers'"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Address']", 'related_name': "'sender'"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mailarchive']