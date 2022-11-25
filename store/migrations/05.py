import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '04'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]