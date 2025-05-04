int kirmizi = 25;
int yesil = 26;
int mavi = 27;
void setup(){
  Serial.begin(9600);
  for(int i = 25; i<=27; i++){
    pinMode(i,OUTPUT);
  }
}
void loop(){
  if(Serial.available()){
    String duygu = Serial.readStringUntil('\n');
    duygu.trim();

    if(duygu == "mutlu")
      setColor(255,255,0); 
    else if(duygu == "selam")
      setColor(255,255,0);
    else if (duygu == "uzgun")
      setColor(0,0,255); 
    else if (duygu == "sinirli")
      setColor(255,0,0); 
    else if (duygu == "notr")
      setColor(0,255,0);
    else if (duygu == "asik")
      setColor(255,0,255);
    else if(duygu == "merakli")
      setColor(128,128,0);
    else if (duygu == "korkmus")
      setColor(128,128,128);
    else if (duygu == "sasirmis")
      setColor(0,255,255);
    else
      setColor(255,255,255); 
  }
}

void setColor(int kirmiziDeg, int yesilDeg, int maviDeg){
  analogWrite(kirmizi, kirmiziDeg);
  analogWrite(yesil, yesilDeg);
  analogWrite(mavi,maviDeg);
}