# Remote Physics Lab
_Senior Development Project_

## About This Project 
This project is meant to help explore the possibilities of creating a fully remote lab experience for students at FGCU. Several professors at the university are invested and involved with the development of this service. This project is meant to act as a proof-of-concept for both the Physics department as well as other departments on campus who might benefit from a fully remote lab experience. 
This project is aimed at addressing the concern of university leaders for that of class sizes, and the number of classes required to meet each week in order for the university to adhere to the size requirements. With a remote system, students can complete their assignments in a timely fashion, instructors can lecture other students during that time that they would otherwise be attending to a lab section, and classrooms can be booked only for instruction. This is a great opportunity, as the number of available classrooms on campus continue to decline, and as new students attend the university each semester. In effect nearly doubling the effective capacity of the department. 

### Software Architecture
The Software will be comprised of 3 major parts
1. **Command & Control Server** - _For interacting with the hardware devices and controlling the Pi_
2. **Raspberry Pi** - _The main objective of the Pi is to stream the live video to the client but also host the web service_
3. **Client** - _Issuing commands to the server on the interface and from there will be interpreted as an instruction on the device_


## Sponsors
- Dr. Alexander Sakharuk - Associate Professor of Physics
- Dr. Janusz Zalewski - Professor of Software Engineering

### Other Sponsors
- USAF Academy in Colorodo Springs, CO

## Testing
- DjangoTest for Unit Testing the API with automated unit tests within the Travis CI builds

*Running API Tests* - run `python manage.py test RPL/tests`
