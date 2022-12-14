#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char *SSID = "";
const char *password = ";

IPAddress serverAddr = IPAddress(192, 168, 178, 20); //<---- UDP DESTINATION IP
const int serverPort = 6969;

char message[] = "1";
const int messageLen = 1;

WiFiUDP Udp;

void setup() {
  // Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, password);
  while (WiFi.status() != WL_CONNECTED) {
    // Serial.print('.');
    delay(10);
  }
  // Serial.print("Connected! IP address: "); Serial.println(WiFi.localIP());
}

void loop() {
  Udp.beginPacket(serverAddr, serverPort);
  Udp.write(message, 1);
  Udp.endPacket();
}
