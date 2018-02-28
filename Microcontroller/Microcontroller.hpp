#ifndef STEPPER_MOTOR_HPP
#define STEPPER_MOTOR_HPP

#include <wiringPi.h>

/**
 * uses <http://wiringpi.com/> for GPIO pin standard
 * This is for local invocation of RPI controlling methods.
 * RPC implementation for client-server interactions currently under development
 */
class Microcontroller {
public:

	enum Motor {deflect, accel, mag};

	Microcontroller(const unsigned int accel1, const unsigned int accel2, const unsigned int accel3,
		const unsigned int accel4, const unsigned int deflect1, const unsigned int deflect2, const unsigned int deflect3,
		const unsigned int deflect4, const unsigned int mag1, const unsigned int mag2, const unsigned int mag3,
		const unsigned int mag4, const unsigned int relay1, const unsigned int relay2, const unsigned int relay3,
		const unsigned int relay4, const unsigned int gearRatio, const unsigned int stepDuration, const unsigned int potentiometerDegrees);

	
	void step(int voltage, Motor motor);


	// The motor sequence for the full step stepping method.
	static const bool FULL_STEP_MOTOR_SEQUENCE[][4];

	// The current step duration in milliseconds. 3ms is a minimum
	int stepDuration;

	/** Holds the Raspberry Pi pin numbers for pins A though D of the stepper motor. **/
	int inputPins[16];

	// The motor being stepped by the Caller
	Motor motor;

	//Holds the maximum steps the motor should turn based on
	//gear ratio of pulleys and degrees of potentiometer turn radius
	double maxSteps;
	
	//Holds the current position of accelerating potentiometer
	int accelValue;

	//Holds the current position of deflecting potentiometer
	int deflectValue;

	//Holds the current position of magnetizing potentiometer
	int magValue;

	//Holds the size of steps of accelerating potentiometer for 1v change
	double accelStepSize;

	//Holds the size of steps of deflecting potentiometer for 1v change
	double deflectStepSize;

	//Holds the size of steps of magnetizing current potentiometer for .01a change.
	double magStepSize;

	void writeSequence(const unsigned int sequenceNo);
	

	//activates or deactivates the relay for switches. 
	//passes [0,0,0,0] for each of the 4 switches as low
	void writeRelay(int[] relay);
};

#endif
