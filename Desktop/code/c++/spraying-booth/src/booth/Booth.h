#include "defines.h"
#ifndef BOOTH_H
#define BOOTH_H
class Pump{
  public:
    uint8_t relay;
    Pump(){
       this->relay = pump;
       pinMode(relay,OUTPUT);
    }
    void on(){
      digitalWrite(this->relay,HIGH);
    }
    void off(){
      digitalWrite(this->relay,LOW);
    }
};
class Machine{
  public:
    Machine(){
      uint8_t inputs[] = {echoPin,pir};
      uint8_t outputs[] = {pump,servoL,servoR,entryServo,exitServo};
      int i,j;
      for
      ( i =0; i<2; i++){
        pinMode(inputs[i],INPUT);
      }
      for
      (j = 0; i<8; j++){
        pinMode(outputs[j],OUTPUT);
      }
    }
    void OpenEntry(){
      analogWrite(entryServo,180);
    }
    void CloseEntry(){
      analogWrite(entryServo,0);
    }
    void OpenExit(){
      analogWrite(exitServo,180);
    }
    void CloseExit(){
      analogWrite(exitServo,0);
    }
    void Spray(){
      analogWrite(servoL,180);
      analogWrite(servoR,180);
      delay(1000);
      analogWrite(servoL,180);
      analogWrite(servoR,180);
    }
    bool DetectAnimal(){
      if
      (digitalRead(pir)==HIGH){
        return true;
      }
      else
      {
        return false;
      }
    }
    bool AnimalInside(){
      if
      (digitalRead(IR1)==HIGH && digitalRead(IR2)==HIGH){
        return true;
      }
      else
      {
        return false;
      }
    }
    void buzz(){
      digitalWrite(buzzer,HIGH);
      delay(2000);
      digitalWrite(buzzer,LOW);
    }
    long AnimalHeight(){
      digitalWrite(triggerPin,HIGH);
      delayMicroseconds(1);
      digitalWrite(triggerPin,LOW);
      unsigned long duration = pulseIn(echoPin,HIGH);
      long distance = duration*0.034/2;
      long height = 15-distance;
      return height;      
    }
};
#endif