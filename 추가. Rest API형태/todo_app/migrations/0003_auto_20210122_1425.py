# Generated by Django 3.1.5 on 2021-01-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20210122_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='schedule',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='city',
            field=models.CharField(choices=[('busan', '부산'), ('ulsan', '울산'), ('daegu', '대구,경북'), ('gwangju', '광주'), ('gyeonggi', '경기'), ('incheon', '인천'), ('daejeon', '대전,충청'), ('seoul', '서울')], max_length=80, null=True),
        ),
    ]
