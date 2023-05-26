#include <Arduino.h>
#include <Wire.h>
#include "fiche.h"


 fiche::fiche(/* args */)
{
}

fiche::~fiche()
{
}

void fiche::Renvoi(){
// Initialisation de la communication série
  Serial.begin(115200);
  pinMode(MouvPin, INPUT);
  pinMode(LedVertPin,OUTPUT);
  pinMode(LedRedPin,OUTPUT);
  while (!Serial);

  // Initialisation de la communication I2C
  Wire.begin();
}

void fiche::requete(){
    Sen0017=digitalRead(MouvPin);

Serial.println(Sen0017);

  //valeur son

  Serial.println(SonPin);

  
     // read the value from the sensor:
 sensity_t = analogRead(sensityPin);
  // turn the ledPin on

 dist_t = sensity_t * MAX_RANG  / ADC_SOLUTION;//
 Serial.println(dist_t,0);
 

  if ( Sen0017==1 && SonPin>16 )
  {
   digitalWrite(LedRedPin,HIGH)  ;
    digitalWrite(LedVertPin,LOW);
  }
  else
  {
   digitalWrite(LedVertPin,HIGH)  ;
    digitalWrite(LedRedPin,LOW);
  }
  
  if (dist_t<60)
  {
    digitalWrite(LedRPin,HIGH);
    delay(20);
    digitalWrite(LedRPin,LOW);
    delay(20);
  }
  
}