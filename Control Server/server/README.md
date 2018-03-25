## Note
We are using Django `1.11.11`. The current version of Django uses several different functions and method names, so attempting to reference this version of the documentation will not be accurate. So please note that to view docuentation for this release on the Dgango site requires the use of the specific `1.11` docs found [here](https://docs.djangoproject.com/en/1.11/) 

## All Endpoints
*All are POST requests as the purpose of this application is to interact with a device, by sending it commands*

- Deflecting Voltage -- POST (50V - 250V)
- Deflecting Switch -- POST (0, 1, 2)
- Accelerating Voltage -- POST (0V - 250V)
- Magnetizing Current -- POST (0A - 3A)
- Current Switch -- POST (0, 1, 2)

### Stretch Goal Endpoints
- Power -- POST (0, 1)

## Pip Dependencies
*Make sure to run `python -m pip install --upgrade pip` to ensure you have the latest version of pip. Alternitavely use the quickstart files in the dependency folder. There are install scripts for all dependencies inside these scripts for Windows CMD and macOS Terminal. Please also ensure that you have Python installed on your machine, or else these scripts will fail.*
- [django](https://www.djangoproject.com/)
- [djangorestframework](http://www.django-rest-framework.org/)
- coreapi -- *Must be installed for schema support*