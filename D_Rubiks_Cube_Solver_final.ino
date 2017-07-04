/***********************************************************
 * Don Dominic
 * MARCH 10, 2017
************************************************************ */

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ArduinoJson.h>

/******************ESP SERVER(SSID&PASSWORD)***************/
ESP8266WebServer server;
char* ssid = "HHG";
char* pass = "Chesscube";
/************************************************************/

/****************STEPPER & PINS*******************************
 * Stepper 0 - Front - GPIO01->(STEP[0])...GPIO03->(DIR[0])
 * Stepper 1 - Left - -GPIO15->(STEP[1])...GPIO13->(DIR[1])
 * Stepper 2 - Right - GPIO12->(STEP[2])...GPIO14->(DIR[2])
 * Stepper 3 - Up - - -GPIO02->(STEP[3])...GPIO00->(DIR[3])
 * Stepper 4 - Down - -GPIO04->(STEP[4])...GPIO05->(DIR[4])
 * Stepper 5 - Back - -GPIO09->(STEP[5])...GPIO11->(DIR[5])
 */
 int STEP[6]={1,15,12,2,4,9};
 int EN[6]= {3,13,14,0,5,10};
/************************************************************/

/*************DIRECTION*************************************
* Clockwise - - - Direction Pin =1/HIGH
* AntiClockwise - Direction Pin =0/LOW
*/
 //int CLK=1;  
 //int ANCLK=0;
/*************************************************************/ 

/*******************TURN MODE**************************************                                                      
 *  ###########NEMA 17 - 200 steps per revoultion=360 degree######
 *  Quarter Turn - 90 degree - 50 steps 
 *  Half Turn - - -180degree - 100 steps
 */
 int qtm=50;
 int htm=100;
 int q3tm=150;
/***************************************************************/

/***********************TURN SPEED******************************
 * Reduce turn delay(miccroseconds delay in between each step) to increase turn speed
 */
 int turn_delay=2;
/****************************************************************/

char command[60];

void Turn(int,int);

void setup()
{
  Serial.begin(9600);
  
  for(int i=0;i<=6;i++)
  {
    pinMode(STEP[i],OUTPUT);
    pinMode(EN[i],OUTPUT);
  }
  
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

void loop() 
{
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
   cube1.toCharArray(command,60);
   const char space[2]=" ";
   char* x;
   x=strtok(command,space);
   while(x!=NULL)
   {
    Serial.println(x);
   //................QUARTER CLOCKWISE TURNS...............
    if(strcmp(x,"F")==0)
     Turn(0,qtm+1);
    else if(strcmp(x,"L")==0)
     Turn(1,qtm);
    else if(strcmp(x,"R")==0)
     Turn(2,qtm);
    else if(strcmp(x,"U")==0)
     Turn(3,qtm);
    else if(strcmp(x,"D")==0)
     Turn(4,qtm);
    else if(strcmp(x,"B")==0)
     Turn(5,qtm);
   //..................................................
   //..............QUARTER ANTICLOCKWISE TURNS.........
    else if(strcmp(x,"F'")==0)
     Turn(0,q3tm);
    else if(strcmp(x,"L'")==0)
     Turn(1,q3tm);
    else if(strcmp(x,"R'")==0)
     Turn(2,q3tm);
    else if(strcmp(x,"U'")==0)
     Turn(3,q3tm);
    else if(strcmp(x,"D'")==0)
     Turn(4,q3tm);
    else if(strcmp(x,"B'")==0)
     Turn(5,q3tm);
   //....................................................
   //............HALF CLOCKWISE TURNS....................
    else if(strcmp(x,"F2")==0)
     Turn(0,htm);
    else if(strcmp(x,"L2")==0)
     Turn(1,htm);
    else if(strcmp(x,"R2")==0)
     Turn(2,htm);
    else if(strcmp(x,"U2")==0)
     Turn(3,htm);
    else if(strcmp(x,"D2")==0)
     Turn(4,htm);
    else if(strcmp(x,"B2")==0)
     Turn(5,htm);
   //....................................................
    x=strtok(NULL,space);
    delay(50);
   }
}

void Turn(int s,int mode)
{
      Serial.print("Turning Stepper: ");
      Serial.println(s);
      digitalWrite(EN[s],0);
      Serial.print("Step No.: ");
  for(int j=0;j<mode;j++)
  {
    digitalWrite(STEP[s],LOW);
    digitalWrite(STEP[s],HIGH);
    delay(turn_delay);
        Serial.print(j);
  }
      digitalWrite(EN[s],1);
      Serial.println();
}
