#include <Arduino.h>
#include <Wire.h>
#include <fiche.h>

void setup() {
  fiche Objet;
  Objet.Renvoi();
}

void loop() {
  
fiche Objet;
Objet.requete();

  delay(120000);
}
