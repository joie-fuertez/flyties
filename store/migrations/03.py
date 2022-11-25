from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '02'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]