char command[60];

void setup() 
{
  Serial.begin(9600);

}

void loop() 
{
  if(Serial.available()>0)
  {
   String command_s=Serial.readString();
   command_s.toCharArray(command,60);
   const char space[2]=" ";
   char* x;
   x=strtok(command,space);
   while(x!=NULL)
   {
    Serial.println(x);
    x=strtok(NULL,space);
   }
  }

}
