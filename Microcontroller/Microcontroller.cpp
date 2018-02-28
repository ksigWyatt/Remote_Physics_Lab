#include <iostream>
#include <ctime>
#include <stdlib.h>
#include “Microcontroller.hpp"

using namespace std;


const bool Microcontroller::FULL_STEP_MOTOR_SEQUENCE[][4] = {
		{ 1,  1,  0,  0 },
		{ 0,  1,  1,  0 },
		{ 0,  0,  1,  1 },
		{ 1,  0,  0,  1 },
		{ 1,  1,  0,  0 },
		{ 0,  1,  1,  0 },
		{ 0,  0,  1,  1 },
		{ 1,  0,  0,  1 }
};



Microcontroller::Microcontroller(const unsigned int accel1, const unsigned int accel2, const unsigned int accel3,
		const unsigned int accel4, const unsigned int deflect1, const unsigned int deflect2, const unsigned int deflect3,
		const unsigned int deflect4, const unsigned int mag1, const unsigned int mag2, const unsigned int mag3,
		const unsigned int mag4, const unsigned int relay1, const unsigned int relay2, const unsigned int relay3,
		const unsigned int relay4, const unsigned int gearRatio, const unsigned int stepDuration, const unsigned int potentiometerDegrees)
{
	inputPins[0] = accel1;
	inputPins[1] = accel2;
	inputPins[2] = accel3;
	inputPins[3] = accel4;
	inputPins[4] = deflect1;
	inputPins[5] = deflect2;
	inputPins[6] = deflect3;
	inputPins[7] = deflect4;
	inputPins[8] = mag1;
	inputPins[9] = mag2;
	inputPins[10] =mag3;
	inputPins[11] =mag4;
	inputPins[12] =relay1;
	inputPins[13] =relay2;
	inputPins[14] =relay3;
	inputPins[15] =relay4;
	for (int i = 0; i < 16; i++) {
		pinMode(inputPins[i], OUTPUT);
	}

	this->stepDuration = stepDuration;
	maxSteps = ((2036.8*potentiometerDegrees)/360)*gearRatio;
	
	accelValue = 0;
	deflectValue = 0;
	magValue = 0;
	
	accelStepSize = maxSteps/250;
	deflectStepSize = maxSteps/200;
	magStepSize = maxSteps/300;
}




void Microcontroller::step(int voltage, Motor motor) {
	this->motor = motor;
	//multiplies 3amps by 100 because we use hundredths place i.e. .01amp
	//if(motor == mag)
	//voltage=voltage*100;   //handle *100 on html side?

	switch(motor){
	case accel:
	if (voltage > accelValue) {
		
		for (int step = round((voltage-accelValue)*accelStepSize); step > 0; step--) {
			int currentSequenceNo = step % 8;
			writeSequence(currentSequenceNo);
		}
	} 
	else {
		for (int step = 0; step < abs(round((voltage-accelValue)*accelStepSize)); step++) {
			int currentSequenceNo = currentStep % 8;
			writeSequence(currentSequenceNo);
		}
	}
	accelValue=voltage;
	break;

	case deflect:
	if (voltage > deflectValue) {
		
		for (int step = round((voltage-deflectValue)*deflectStepSize); step > 0; step--) {
			int currentSequenceNo = step % 8;
			writeSequence(currentSequenceNo);
		}
	} 
	else {
		for (int step = 0; step < abs(round((voltage-deflectValue)*deflectStepSize)); step++) {
			int currentSequenceNo = currentStep % 8;
			writeSequence(currentSequenceNo);
		}
	}
	deflectValue=voltage;
	break;

	case mag:
	if (voltage > magValue) {
		
		for (int step = round((voltage-magValue)*magStepSize); step > 0; step--) {
			int currentSequenceNo = step % 8;
			writeSequence(currentSequenceNo);
		}
	} 
	else {
		for (int step = 0; step < abs(round((voltage-magValue)*magStepSize)); step++) {
			int currentSequenceNo = currentStep % 8;
			writeSequence(currentSequenceNo);
		}
	}
	magValue=voltage;
	break;
	}


}

void Microcontroller::writeSequence(const unsigned int sequenceNo) {
	
	
	for (int i = 0; i < 4; i++){
		switch(motor){
		case deflect:
			digitalWrite(inputPins[i], FULL_STEP_MOTOR_SEQUENCE[sequenceNo][i]);
			break;
		case accel:
			digitalWrite(inputPins[i+4], FULL_STEP_MOTOR_SEQUENCE[sequenceNo][i]);
			break;
		case mag:
			digitalWrite(inputPins[i+8], FULL_STEP_MOTOR_SEQUENCE[sequenceNo][i]);
			break;
		}

	}
	delay(stepDuration);
	for (int i = 0; i < 4; i++) {
		switch(motor){
		case deflect:
			digitalWrite(inputPins[i], 0);
			break;
		case accel:
			digitalWrite(inputPins[i+4], 0);
			break;
		case mag:
			digitalWrite(inputPins[i+8], 0);
			break;
		}
	}
}

void Microcontroller::writeRelay (int[] relay){
	for(int i=0; i<4; i++)
		digitalWrite(inputPins[i+12], relay[i]);
	
} 
