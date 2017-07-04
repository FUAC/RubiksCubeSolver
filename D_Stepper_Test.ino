int STEP=12;
int EN=13;
int DIR=9;

int turn_delay=5;

void setup() 
{
  pinMode(STEP,OUTPUT);
  pinMode(EN,OUTPUT);
  pinMode(DIR,OUTPUT);

  digitalWrite(DIR,LOW);
  
  digitalWrite(EN,0);
  for(int j=0;j<50;j++)
  {
    digitalWrite(STEP,LOW);
    digitalWrite(STEP,HIGH);
    delay(turn_delay);
  }
  digitalWrite(EN,1);
  
  delay(500);
  
  digitalWrite(DIR,HIGH);

  digitalWrite(EN,0);
  
  for(int j=0;j<50;j++)
  {
    digitalWrite(STEP,LOW);
    digitalWrite(STEP,HIGH);
    delay(turn_delay);
  }

  digitalWrite(EN,1);
}

void loop() 
{
  

}
