String incomingByte;
int incomingCmd;

// Motor A connections
#define enA 16  //(D2)
#define in1 13  //(D7)
#define in2 12  //(D6)

// Motor B connections
#define enB 14  //(D5)
#define in3 4   //(D3)
#define in4 5   //(D4)

#define BREAK 0
#define FOR 1
#define BACK 2
#define RIGHT 3
#define LEFT 4

void motors_backward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}
void motors_forward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}
void motors_break() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, HIGH);
}
void motors_left() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, HIGH);
}
void motors_right() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}
void right_speed(int speed) {
  analogWrite(enA, speed);
}
void left_speed(int speed) {
  analogWrite(enB, speed);
}

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  //start from speed of 100 (0<speed<255) and not moving
  motors_break();
  right_speed(255);
  left_speed(255);
  //starts with led turned off
  digitalWrite(LED_BUILTIN, HIGH);
}
void loop() {
if (Serial.available() > 0) {

    //incomingByte = Serial.readStringUntil('\n');
    incomingCmd = Serial.parseInt();

    switch (incomingCmd) {
      case BREAK:
        Serial.write("stopping\n");
        motors_break();
        break;
      case FOR:
        Serial.write("moving forward\n");
        motors_forward();
        break;
      case BACK:
        Serial.write("moving backwards\n");
        motors_backward();
        break;
      case RIGHT:
        Serial.write("moving right\n");
        motors_right();
        break;
      case LEFT:
        Serial.write("moving left\n");
        motors_left();
        break;
      default:
        Serial.write("invalid command\n");
        break;
    }
  }
}