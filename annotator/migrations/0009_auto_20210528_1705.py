# Generated by Django 3.1.5 on 2021-05-28 11:35

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0008_auto_20210528_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='my_field',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='ques1',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='rating',
        ),
        migrations.AlterField(
            model_name='survey',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='Page5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques1', models.CharField(choices=[('choice1', 'choice1'), ('choice2', 'choice2'), ('choice3', 'choice3'), ('choice4', 'choice4')], max_length=250, null=True)),
                ('my_field', multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3')], max_length=29, null=True)),
                ('comment', models.CharField(max_length=250, null=True)),
                ('rating', models.CharField(max_length=20, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='annotator.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Page4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques1', models.CharField(choices=[('choice1', 'choice1'), ('choice2', 'choice2'), ('choice3', 'choice3'), ('choice4', 'choice4')], max_length=250, null=True)),
                ('my_field', multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3')], max_length=29, null=True)),
                ('comment', models.CharField(max_length=250, null=True)),
                ('rating', models.CharField(max_length=20, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='annotator.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Page3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques1', models.CharField(choices=[('choice1', 'choice1'), ('choice2', 'choice2'), ('choice3', 'choice3'), ('choice4', 'choice4')], max_length=250, null=True)),
                ('my_field', multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3')], max_length=29, null=True)),
                ('comment', models.CharField(max_length=250, null=True)),
                ('rating', models.CharField(max_length=20, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='annotator.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Page2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques1', models.CharField(choices=[('choice1', 'choice1'), ('choice2', 'choice2'), ('choice3', 'choice3'), ('choice4', 'choice4')], max_length=250, null=True)),
                ('my_field', multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3')], max_length=29, null=True)),
                ('comment', models.CharField(max_length=250, null=True)),
                ('rating', models.CharField(max_length=20, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='annotator.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Page1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques1', models.CharField(choices=[('choice1', 'choice1'), ('choice2', 'choice2'), ('choice3', 'choice3'), ('choice4', 'choice4')], max_length=250, null=True)),
                ('my_field', multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3')], max_length=29, null=True)),
                ('comment', models.CharField(max_length=250, null=True)),
                ('rating', models.CharField(max_length=20, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='annotator.survey')),
            ],
        ),
    ]
