#define PIN_A 8
#define PIN_D 7

void setup() {
  pinMode(PIN_A, OUTPUT);
  pinMode(PIN_D, INPUT);
}

void loop() {
  int val_D = digitalRead(PIN_D);
  
  if (val_D) { 
    digitalWrite(PIN_A, HIGH);
  } else  {
    digitalWrite(PIN_A, LOW);
  }
}
