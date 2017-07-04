#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ArduinoJson.h>

/******************ESP SERVER(SSID&PASSWORD)***************/
ESP8266WebServer server;
char* ssid = "don123";
char* pass = "abcd1234";
/************************************************************/

/****************STEPPER & PINS*******************************
 * Stepper 0 - Front - 
 * Stepper 1 - Left - -
 * Stepper 2 - Right - 
 * Stepper 3 - Down - -
 * Stepper 4 - Up - - -
 * Stepper 5 - Back - -
 */
 int EN[6]={13,15,12,2,4,10};
 //.........F..L..R..D.U..B
 int STEP= 3;
 int DIR=14;
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
 int error=45;
/***************************************************************/

/***********************TURN SPEED******************************
 * Reduce turn delay(miccroseconds delay in between each step) to increase turn speed
 */
 int turn_delay=10;
/****************************************************************/

char command[60];

void Turn(int,int);


void initialize()
{
  pinMode(STEP,OUTPUT);
  pinMode(DIR,OUTPUT);
  digitalWrite(DIR,LOW);
  for(int i=0;i<=6;i++)
  {
   //Serial.print("hi");
   pinMode(EN[i],OUTPUT);
    digitalWrite(EN[i],HIGH);
  }  
}


void setup()
{
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

initialize();
  

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
//char z[20];
  //cube1.toCharArray(z,20);
  //or(int i=0;i<20;i++)
  //Serial.print(z[i]); 


  
  cube1.toCharArray(command,60);
   const char space[2]=" ";
   char* x;
   x=strtok(command,space);
   while(x!=NULL)
   {
    Serial.println(x);
   //................QUARTER CLOCKWISE TURNS...............
    if(strcmp(x,"F")==0)
     Turn(0,qtm);
    else if(strcmp(x,"L")==0)
     Turn(1,qtm);
    else if(strcmp(x,"R")==0)
     Turn(2,qtm);
    else if(strcmp(x,"D")==0)
     Turn(3,qtm);
    else if(strcmp(x,"U")==0)
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
    else if(strcmp(x,"D'")==0)
     Turn(3,q3tm);
    else if(strcmp(x,"U'")==0)
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
    else if(strcmp(x,"D2")==0)
     Turn(3,htm);
    else if(strcmp(x,"U2")==0)
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
      digitalWrite(DIR,HIGH);
      digitalWrite(EN[s],0);
      for(int j=0;j<error;j++)
  {
    digitalWrite(STEP,HIGH);
    delay(turn_delay);
    digitalWrite(STEP,LOW);
    
    delay(turn_delay);
        Serial.print(j);
  }
  digitalWrite(DIR,LOW);
      Serial.print("Step No.: ");
  for(int j=0;j<mode+error;j++)
  {
    digitalWrite(STEP,HIGH);
    delay(turn_delay);
    digitalWrite(STEP,LOW);
    
    delay(turn_delay);
        Serial.print(j);
  }
      digitalWrite(EN[s],1);
      Serial.println();
}

