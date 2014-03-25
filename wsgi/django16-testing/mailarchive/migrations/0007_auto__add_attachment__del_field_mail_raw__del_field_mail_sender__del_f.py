# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attachment'
        db.create_table('mailarchive_attachment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('mail', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailarchive.Mail'])),
            ('ctype', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('cencoding', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('cdisposition', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('payload', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mailarchive', ['Attachment'])

        # Deleting field 'Mail.raw'
        db.delete_column('mailarchive_mail', 'raw')

        # Deleting field 'Mail.sender'
        db.delete_column('mailarchive_mail', 'sender_id')

        # Deleting field 'Mail.account'
        db.delete_column('mailarchive_mail', 'account_id')

        # Deleting field 'Mail.messageid'
        db.delete_column('mailarchive_mail', 'messageid')

        # Adding field 'Mail.raw_mail'
        db.add_column('mailarchive_mail', 'raw_mail',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)

        # Adding field 'Mail.message_id'
        db.add_column('mailarchive_mail', 'message_id',
                      self.gf('django.db.models.fields.CharField')(max_length=200, default=1),
                      keep_default=False)

        # Adding field 'Mail.inreplyto_id'
        db.add_column('mailarchive_mail', 'inreplyto_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['mailarchive.Mail']),
                      keep_default=False)

        # Adding field 'Mail.inreplyto_text'
        db.add_column('mailarchive_mail', 'inreplyto_text',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Mail.sender_address'
        db.add_column('mailarchive_mail', 'sender_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', null=True, to=orm['mailarchive.Address']),
                      keep_default=False)

        # Adding field 'Mail.from_address'
        db.add_column('mailarchive_mail', 'from_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='from', null=True, to=orm['mailarchive.Address']),
                      keep_default=False)

        # Removing M2M table for field receivers on 'Mail'
        db.delete_table(db.shorten_name('mailarchive_mail_receivers'))

        # Removing M2M table for field carboncopy on 'Mail'
        db.delete_table(db.shorten_name('mailarchive_mail_carboncopy'))

        # Adding M2M table for field account on 'Mail'
        m2m_table_name = db.shorten_name('mailarchive_mail_account')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mail', models.ForeignKey(orm['mailarchive.mail'], null=False)),
            ('account', models.ForeignKey(orm['mailarchive.account'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mail_id', 'account_id'])

        # Adding M2M table for field receivers_to on 'Mail'
        m2m_table_name = db.shorten_name('mailarchive_mail_receivers_to')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mail', models.ForeignKey(orm['mailarchive.mail'], null=False)),
            ('address', models.ForeignKey(orm['mailarchive.address'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mail_id', 'address_id'])

        # Adding M2M table for field carboncopy_to on 'Mail'
        m2m_table_name = db.shorten_name('mailarchive_mail_carboncopy_to')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mail', models.ForeignKey(orm['mailarchive.mail'], null=False)),
            ('address', models.ForeignKey(orm['mailarchive.address'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mail_id', 'address_id'])


        # Changing field 'Mail.date_sent'
        db.alter_column('mailarchive_mail', 'date_sent', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Mail.delivered_to'
        db.alter_column('mailarchive_mail', 'delivered_to_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['mailarchive.Address']))

        # Changing field 'Mail.subject'
        db.alter_column('mailarchive_mail', 'subject', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Mail.date_delivered'
        db.alter_column('mailarchive_mail', 'date_delivered', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Mail.html_body'
        db.alter_column('mailarchive_mail', 'html_body', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Mail.text_body'
        db.alter_column('mailarchive_mail', 'text_body', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting model 'Attachment'
        db.delete_table('mailarchive_attachment')


        # User chose to not deal with backwards NULL issues for 'Mail.raw'
        raise RuntimeError("Cannot reverse this migration. 'Mail.raw' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Mail.raw'
        db.add_column('mailarchive_mail', 'raw',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Mail.sender'
        raise RuntimeError("Cannot reverse this migration. 'Mail.sender' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Mail.sender'
        db.add_column('mailarchive_mail', 'sender',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['mailarchive.Address']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Mail.account'
        raise RuntimeError("Cannot reverse this migration. 'Mail.account' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Mail.account'
        db.add_column('mailarchive_mail', 'account',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailarchive.Account']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Mail.messageid'
        raise RuntimeError("Cannot reverse this migration. 'Mail.messageid' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Mail.messageid'
        db.add_column('mailarchive_mail', 'messageid',
                      self.gf('django.db.models.fields.CharField')(max_length=200),
                      keep_default=False)

        # Deleting field 'Mail.raw_mail'
        db.delete_column('mailarchive_mail', 'raw_mail')

        # Deleting field 'Mail.message_id'
        db.delete_column('mailarchive_mail', 'message_id')

        # Deleting field 'Mail.inreplyto_id'
        db.delete_column('mailarchive_mail', 'inreplyto_id_id')

        # Deleting field 'Mail.inreplyto_text'
        db.delete_column('mailarchive_mail', 'inreplyto_text')

        # Deleting field 'Mail.sender_address'
        db.delete_column('mailarchive_mail', 'sender_address_id')

        # Deleting field 'Mail.from_address'
        db.delete_column('mailarchive_mail', 'from_address_id')

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

        # Removing M2M table for field account on 'Mail'
        db.delete_table(db.shorten_name('mailarchive_mail_account'))

        # Removing M2M table for field receivers_to on 'Mail'
        db.delete_table(db.shorten_name('mailarchive_mail_receivers_to'))

        # Removing M2M table for field carboncopy_to on 'Mail'
        db.delete_table(db.shorten_name('mailarchive_mail_carboncopy_to'))


        # User chose to not deal with backwards NULL issues for 'Mail.date_sent'
        raise RuntimeError("Cannot reverse this migration. 'Mail.date_sent' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Mail.date_sent'
        db.alter_column('mailarchive_mail', 'date_sent', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Mail.delivered_to'
        raise RuntimeError("Cannot reverse this migration. 'Mail.delivered_to' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Mail.delivered_to'
        db.alter_column('mailarchive_mail', 'delivered_to_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailarchive.Address']))

        # User chose to not deal with backwards NULL issues for 'Mail.subject'
        raise RuntimeError("Cannot reverse this migration. 'Mail.subject' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Mail.subject'
        db.alter_column('mailarchive_mail', 'subject', self.gf('django.db.models.fields.CharField')(max_length=200))

        # User chose to not deal with backwards NULL issues for 'Mail.date_delivered'
        raise RuntimeError("Cannot reverse this migration. 'Mail.date_delivered' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Mail.date_delivered'
        db.alter_column('mailarchive_mail', 'date_delivered', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Mail.html_body'
        raise RuntimeError("Cannot reverse this migration. 'Mail.html_body' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Mail.html_body'
        db.alter_column('mailarchive_mail', 'html_body', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Mail.text_body'
        raise RuntimeError("Cannot reverse this migration. 'Mail.text_body' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Mail.text_body'
        db.alter_column('mailarchive_mail', 'text_body', self.gf('django.db.models.fields.TextField')())

    models = {
        'mailarchive.account': {
            'Meta': {'object_name': 'Account', 'ordering': "('-modified', '-created')"},
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
            'Meta': {'object_name': 'Address', 'ordering': "('-modified', '-created')"},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailaddress': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'names_json': ('django.db.models.fields.TextField', [], {})
        },
        'mailarchive.attachment': {
            'Meta': {'object_name': 'Attachment', 'ordering': "('-modified', '-created')"},
            'cdisposition': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'cencoding': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'ctype': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Mail']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'payload': ('django.db.models.fields.TextField', [], {})
        },
        'mailarchive.headerinfo': {
            'Meta': {'object_name': 'HeaderInfo', 'ordering': "('-modified', '-created')"},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailarchive.Mail']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mailarchive.mail': {
            'Meta': {'object_name': 'Mail', 'ordering': "('-modified', '-created')"},
            'account': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mailarchive.Account']", 'symmetrical': 'False'}),
            'carboncopy_to': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'carboncopy'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['mailarchive.Address']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_delivered': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'delivered_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'delivered_to'", 'null': 'True', 'to': "orm['mailarchive.Address']"}),
            'from_address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from'", 'null': 'True', 'to': "orm['mailarchive.Address']"}),
            'html_body': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inreplyto_id': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['mailarchive.Mail']"}),
            'inreplyto_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'raw_mail': ('django.db.models.fields.TextField', [], {}),
            'receivers_to': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'receivers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['mailarchive.Address']"}),
            'sender_address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'null': 'True', 'to': "orm['mailarchive.Address']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'text_body': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['mailarchive']