#include <Servo.h>
#include "defines.h"
#include "Booth.h"

Machine machine;
Pump spraypump;

void setup(){
  Serial.begin(9600);
}
void loop(){
  long h = machine.AnimalHeight();
  Serial.println(h);
  if
  (machine.DetectAnimal()){
    machine.OpenEntry();
    delay(2000);
  }
  if
  (machine.AnimalInside()){
    machine.CloseEntry();
    delay(2000);

    spraypump.on();
    machine.Spray();
    delay(10000);

    spraypump.off();
    delay(1000);

    machine.OpenExit();
    delay(20000);

    if
    (!machine.AnimalInside()){
      machine.CloseExit();
    }
    else
    {
      delay(10000);
    }
  }
}