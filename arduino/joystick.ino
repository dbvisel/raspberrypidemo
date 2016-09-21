const int SW_pin = 2;
const int X_pin = 1;
const int Y_pin = 0;

void setup() {
  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  Serial.begin(115200);
}

void loop() {
  Serial.print("Switch: ");
  Serial.print(digitalRead(SW_pin));
  Serial.print("\n");
  Serial.print("x-axis: ");
  Serial.print(analogRead(X_pin));
  Serial.print("\n");
  Serial.print("y-axis: ");
  Serial.print(analogRead(Y_pin));
  Serial.print("\n");
  delay(200);
}
