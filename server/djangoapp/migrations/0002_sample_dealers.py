from django.db import migrations

def create_sample_dealers(apps, schema_editor):
    Dealer = apps.get_model('djangoapp', 'Dealer')
    Dealer.objects.create(name='Alpha Motors', city='New York', state='NY', address='123 Main St', zip_code='10001')
    Dealer.objects.create(name='Beta Autos', city='Los Angeles', state='CA', address='456 Sunset Blvd', zip_code='90001')
    Dealer.objects.create(name='Gamma Cars', city='Chicago', state='IL', address='789 Lake Shore Dr', zip_code='60601')

class Migration(migrations.Migration):
    dependencies = [
        ('djangoapp', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_sample_dealers),
    ]
