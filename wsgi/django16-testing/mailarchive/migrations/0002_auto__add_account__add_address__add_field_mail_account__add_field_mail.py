# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table('mailarchive_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('mailaddress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailarchive.Address'])),
            ('imapuri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('imapport', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('imapuser', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imappasswd', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imapssl', self.gf('django.db.models.fields.BooleanField')(max_length=200)),
        ))
        db.send_create_signal('mailarchive', ['Account'])

        # Adding model 'Address'
        db.create_table('mailarchive_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('mailaddress', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('mailarchive', ['Address'])

        # Adding field 'Mail.account'
        db.add_column('mailarchive_mail', 'account',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailarchive.Account'], default=1),
                      keep_default=False)

        # Adding field 'Mail.sender'
        db.add_column('mailarchive_mail', 'sender',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['mailarchive.Address'], default=1),
                      keep_default=False)

        # Adding field 'Mail.date_sent'
        db.add_column('mailarchive_mail', 'date_sent',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Mail.date_delivered'
        db.add_column('mailarchive_mail', 'date_delivered',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Mail.subject'
        db.add_column('mailarchive_mail', 'subject',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding M2M table for field receivers on 'Mail'
        m2m_table_name = db.shorten_name('mailarchive_mail_receivers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mail', models.ForeignKey(orm['mailarchive.mail'], null=False)),
            ('address', models.ForeignKey(orm['mailarchive.address'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mail_id', 'address_id'])

        # Adding M2M table for field carboncopy on 'Mail'
        m2m_table_name = db.shorten_name('mailarchive_mail_carboncopy')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mail', models.ForeignKey(orm['mailarchive.mail'], null=False)),
            ('address', models.ForeignKey(orm['mailarchive.address'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mail_id', 'address_id'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table('mailarchive_account')

        # Deleting model 'Address'
        db.delete_table('mailarchive_address')

        # Deleting field 'Mail.account'
        db.delete_column('mailarchive_mail', 'account_id')

        # Deleting field 'Mail.sender'
        db.delete_column('mailarchive_mail', 'sender_id')

        # Deleting field 'Mail.date_sent'
        db.delete_column('mailarchive_mail', 'date_sent')

        # Deleting field 'Mail.date_delivered'
        db.delete_column('mailarchive_mail', 'date_delivered')

        # Deleting field 'Mail.subject'
        db.delete_column('mailarchive_mail', 'subject')

        # Removing M2M table for field receivers on 'Mail'
        db.delete_table(db.shorten_name('mailarchive_mail_receivers'))

        # Removing M2M table for field carboncopy on 'Mail'
        db.delete_table(db.shorten_name('mailarchive_mail_carboncopy'))


    models = {
        'mailarchive.account': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Account'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imappasswd': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'imapport': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'imapssl': ('django.db.models.fields.BooleanField', [], {'max_length': '200'}),
            'imapuri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'imapuser': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mailaddress': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Address']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'})
        },
        'mailarchive.address': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Address'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailaddress': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'})
        },
        'mailarchive.mail': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Mail'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Account']"}),
            'carboncopy': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'carboncopy'", 'to': "orm['mailarchive.Address']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_delivered': ('django.db.models.fields.DateTimeField', [], {}),
            'date_sent': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'raw': ('django.db.models.fields.TextField', [], {}),
            'receivers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'receivers'", 'to': "orm['mailarchive.Address']", 'symmetrical': 'False'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': "orm['mailarchive.Address']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mailarchive']
