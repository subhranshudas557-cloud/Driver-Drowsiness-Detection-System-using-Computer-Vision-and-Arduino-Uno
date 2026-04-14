// Motor Driver Pins (L293D)
int ENA = 5;   // Enable (PWM)
int IN1 = 2;
int IN2 = 3;

// Output Devices
int buzzer = 6;
int led = 7;

char data;

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(led, OUTPUT);

  Serial.begin(9600);

  // Start motor (normal running)
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 200);   // speed (0–255)
}

void loop() {

  if (Serial.available() > 0) {
    data = Serial.read();

    // SLEEP DETECTED
    if (data == 'S') {
      analogWrite(ENA, 0);        // Stop motor
      digitalWrite(buzzer, HIGH); // Buzzer ON

      // LED blinking
      digitalWrite(led, HIGH);
      delay(300);
      digitalWrite(led, LOW);
      delay(300);
    }

    // AWAKE
    else if (data == 'A') {
      digitalWrite(buzzer, LOW);
      digitalWrite(led, LOW);

      // Motor runs again
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, 200);
    }
  }
}
