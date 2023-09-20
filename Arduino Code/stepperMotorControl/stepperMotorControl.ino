// Define the stepper motor connections
int motor1StepPin = 3;
int motor1DirPin = 2;
int motor2StepPin = 7;
int motor2DirPin = 6;
int dirPin;
int stepPin;
int stepsPerRevolution = 800;

void setup() {
  // Set the pin modes for the motors
  pinMode(motor1StepPin, OUTPUT);
  pinMode(motor1DirPin, OUTPUT);
  pinMode(motor2StepPin, OUTPUT);
  pinMode(motor2DirPin, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');

    // Parse the command
    int motorID = command.charAt(1) - '0';
    char dir = command.charAt(4);
    float rotations = command.substring(7).toFloat();

    // Control the motor based on the command
    if (motorID == 1) {
      controlMotor(dir, rotations, motorID);
    } else if (motorID == 2) {
      controlMotor(dir, rotations, motorID);
    }
  }
}

void controlMotor(char dir, float rotations, int motorID) {
  // Specify which motor is being controlled
  if (motorID == 1) {
    dirPin = motor1DirPin;
    stepPin = motor1StepPin;
  } else if (motorID ==2) {
    dirPin = motor2DirPin;
    stepPin = motor2StepPin;
  }
  
  // Set the direction of the motor
  if (dir == 'U') {
    digitalWrite(dirPin, HIGH);
  } else if (dir == 'D') {
    digitalWrite(dirPin, LOW);
  }
 
  // Convert rotations to steps
  int steps = rotations * stepsPerRevolution;

  // Move the motor by the specified number of steps
  for (int i = 0; i < steps; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(500);
  }
}
