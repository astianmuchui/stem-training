#include <Servo.h>
#define pump  2
#define servoL 12
#define servoR 13
#define echoPin 20 
#define triggerPin 21
#define entryServo 22
#define exitServo 36
#define pir 7
#define IR1 8
#define IR2 9
#define buzzer 19
#pragma 1

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