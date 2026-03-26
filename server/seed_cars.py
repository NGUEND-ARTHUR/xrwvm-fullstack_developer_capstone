from djangoapp.models import CarMake, CarModel

# Clear existing data
CarModel.objects.all().delete()
CarMake.objects.all().delete()

# Create car makes
make1 = CarMake.objects.create(name='Toyota', description='Japanese car manufacturer')
make2 = CarMake.objects.create(name='Ford', description='American car manufacturer')
make3 = CarMake.objects.create(name='BMW', description='German car manufacturer')

# Create car models
CarModel.objects.create(make=make1, name='Corolla', type='Sedan', year=2020)
CarModel.objects.create(make=make1, name='RAV4', type='SUV', year=2021)
CarModel.objects.create(make=make2, name='Mustang', type='Coupe', year=2022)
CarModel.objects.create(make=make2, name='F-150', type='WAGON', year=2023)
CarModel.objects.create(make=make3, name='X5', type='SUV', year=2021)
CarModel.objects.create(make=make3, name='3 Series', type='Sedan', year=2020)

print('Sample car makes and models added.')
