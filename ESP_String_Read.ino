#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ArduinoJson.h>




ESP8266WebServer server;
char* ssid = "HHG";
char* pass = "Chesscube";


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
WiFi.begin(ssid,pass);
while(WiFi.status()!=WL_CONNECTED)
{
  Serial.print(".");
  delay(500);
}
Serial.println();
Serial.print("IP ");
Serial.print(WiFi.localIP());

Serial.println();

server.on("/stepper",stepper);
server.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
server.handleClient();
}



void stepper()
{
  String data = server.arg("plain");
  StaticJsonBuffer<200> jBuffer;
  JsonObject& jObject = jBuffer.parseObject(data); 
  String cube = jObject["cube"];

server.send(204,"");
 solvecube(cube);
  
}

void solvecube(String cube1)
{
  char z[50];
  cube1.toCharArray(z,50);
  for(int i=0;i<50;i++)
  Serial.println(z[i]); 

  //Stepper control code here
}


