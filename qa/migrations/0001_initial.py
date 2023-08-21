# Generated by Django 4.2.2 on 2023-08-20 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qa.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='qa.questioncategory'),
        ),
    ]
