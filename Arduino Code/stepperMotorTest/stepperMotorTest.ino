int stepPerRev = 6400;
int stepPin = 3;
int dirPin = 2; 

void setup() {
  // put your setup code here, to run once:
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(dirPin, HIGH);

  for (int i = 0; i < 2 * stepPerRev; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(800);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(800);
  }

    digitalWrite(dirPin, LOW);

  for (int i = 0; i < 2 * stepPerRev; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(800);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(800);
  }
}
