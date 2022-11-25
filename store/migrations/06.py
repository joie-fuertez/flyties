from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '05'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]