
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_auto_20200526_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
