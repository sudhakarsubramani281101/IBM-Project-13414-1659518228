void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(2000); // Wait for 2000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  tone(4, 29, 5000); // play tone 10 (A#0 = 29 Hz)
  delay(5000); // Wait for 5000 millisecond(s)
  tone(12, 523, 1000); // play tone 60 (C5 = 523 Hz)
  delay(1000); // Wait for 1000 millisecond(s)
}