
#define LED_PIN 9
String message;  // Хранит вводимые данные

void setup() {
    pinMode(LED_PIN, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    while (Serial.available()) { 
        char incomingChar = Serial.read();
        
        if (incomingChar != '\n') {
            message += incomingChar; // Собираем строку из символов
        } 
        else { 
            message.toLowerCase(); // Приводим строку к нижнему регистру

            if (message == "on") {
                digitalWrite(LED_PIN, HIGH); // Включаем светодиод
                Serial.println("Светодиод включён");
            } 
            else if (message == "off") {
                digitalWrite(LED_PIN, LOW); // Выключаем светодиод
                Serial.println("Светодиод выключен");
            } 
            else {
                Serial.println("Ошибка: неизвестная команда. Введите 'on' или 'off'");
            }

            message = ""; // Очищаем строку перед следующим вводом
        }
    }
}