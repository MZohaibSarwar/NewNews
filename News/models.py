from django.db import models

CATEGORY_CHOICES = [
    ('Home', 'Home'),
    ('Kitchen', 'Kitchen'),
    ('Garden', 'Garden'),
    ('Cars', 'Cars'),
    ('Travel', 'Travel'),
    ('Pets', 'Pets'),
    ('Office', 'Office'),
    ('Electronics', 'Electronics'),
    ('Hobby', 'Hobby'),
    ('Baby', 'Baby'),
    ('Holiday', 'Holiday'),
    ('Software', 'Software'),
    ('Health', 'Health'),
    ('Appliences', 'Appliences'),
    ('Money', 'Money'),
    ('Books', 'Books'),
    ('Home-&-Garden', 'Home-&-Garden'),
    ('Fashion', 'Fashion'),
]
TAG_CHOICES = [
    ('Recent-Posts', 'Recent-Posts'),
    ('Popular', 'Popular'),
    ('Most-Read', 'Most-Read'),
    ('Hot-Stuff', 'Hot-Stuff'),
    ('Top-of-the-week', 'Top-of-the-week'),
    ('Must-Read', 'Must-Read'),
]


class News(models.Model):
    date = models.DateField(null=True)
    title = models.CharField(max_length=1000, default="")
    subtitle = models.TextField()
    description = models.TextField()
    tag = models.CharField(max_length=1000, choices=TAG_CHOICES, default="")
    category = models.CharField(max_length=1000, choices=CATEGORY_CHOICES, default="")
    image = models.ImageField(upload_to='cover', default="")

    def __str__(self):
        return f'{self.title} {self.tag} {self.category} {self.date}'


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}'


class Contact(models.Model):
    name = models.CharField(max_length=1000, default="")
    tel = models.IntegerField()
    email2 = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.name}'
