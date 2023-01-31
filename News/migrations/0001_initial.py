# Generated by Django 4.1.5 on 2023-01-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000)),
                ('subtitle', models.TextField()),
                ('description', models.TextField()),
                ('tag', models.CharField(choices=[('Recent-Posts', 'Recent-Posts'), ('Popular', 'Popular'), ('Most-Read', 'Most-Read'), ('Hot-Stuff', 'Hot-Stuff'), ('Top-of-the-week', 'Top-of-the-week'), ('Must-Read', 'Must-Read')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Home', 'Home'), ('Kitchen', 'Kitchen'), ('Garden', 'Garden'), ('Cars', 'Cars'), ('Travel', 'Travel'), ('Pets', 'Pets'), ('Office', 'Office'), ('Electronics', 'Electronics'), ('Hobby', 'Hobby'), ('Baby', 'Baby'), ('Holiday', 'Holiday'), ('Software', 'Software'), ('Health', 'Health'), ('Appliences', 'Appliences'), ('Money', 'Money'), ('Books', 'Books'), ('Home-&-Garden', 'Home-&-Garden'), ('Fashion', 'Fashion')], default='', max_length=1000)),
                ('image', models.ImageField(default='', upload_to='cover')),
            ],
        ),
    ]