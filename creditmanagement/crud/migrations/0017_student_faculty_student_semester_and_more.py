# Generated by Django 4.2.6 on 2024-01-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_remove_student_faculty_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('経済学部', '経済学部'), ('経営学部', '経営学部'), ('法学部', '法学部')], default='経済学科', max_length=10, verbose_name='学部'),
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('前期', '前期'), ('後期', '後期')], default='後期', max_length=5, verbose_name='現在の学期'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('経済学科', '経済学科'), ('国際経済学科', '国際経済学科'), ('総合経済政策学科', '総合経済政策学科')], default='経済学科', max_length=20, verbose_name='学科'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('1年', '1年'), ('2年', '2年'), ('3年', '3年'), ('4年', '4年')], default='4年', max_length=5, verbose_name='学年'),
        ),
    ]
