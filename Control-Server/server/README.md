## Note
We are using Django `1.11.11`. The current version of Django uses several different functions and method names, so attempting to reference this version of the documentation will not be accurate. So please note that to view docuentation for this release on the Django site requires the use of the specific `1.11` docs found [here](https://docs.djangoproject.com/en/1.11/)

## DB Mockup
Please see the image below as a mockup of the SQLite DB.

## All Endpoints
*All are PUT/POST requests as the purpose of this application is to interact with a device, by sending it commands*

### Variables
Maps to *variables -- value*

- Deflecting Voltage -- PUT (50V - 250V)
- Deflecting Switch -- PUT (0 - 2)
- Accelerating Voltage -- PUT (0V - 250V)
- Magnetizing Current -- PUT (0A - 3A)
- Magnetic Arc -- PUT (0 - 2)

### Queue
*This is for the queue of the users in line to access the device.*
Maps to *ip*(string) and *place*(int)

- Users -- POST (ip, place)
- Users -- DELETE (id)
- Users -- PUT (id, place)

### Stretch Goal Endpoints
- Power -- POST (0, 1)

## Pip Dependencies
*Make sure to run `python -m pip install --upgrade pip` to ensure you have the latest version of pip. Alternitavely use the quickstart files in the dependencies folder. There are install scripts for all dependencies inside these scripts for Windows CMD and macOS Terminal. Please also ensure that you have Python installed on your machine, or else these scripts will fail.*
- [django](https://www.djangoproject.com/)
- [TastyPie](https://django-tastypie.readthedocs.io/en/latest/)
- django-cors-headers - *Auth Headers for RESTful requests*
- pip install django-nose - *Coverage Reports*
- pip install coverage - *Code Coverage*

## Note
Please note that the URL for containing the IP for the server for the API will be different in PROD. It is set to localhost so that it can be easily tested on your machine. If we were to redo this I would include the queue logic within the API or the server itself instead of trusting that the client itself can host it within the browser.
