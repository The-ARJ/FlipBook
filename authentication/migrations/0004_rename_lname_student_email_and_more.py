# Generated by Django 4.0.2 on 2022-02-04 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_student_delete_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='lname',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='roll',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sclass',
        ),
    ]
