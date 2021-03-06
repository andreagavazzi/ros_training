
### General  

Come prima cose deve essere sempre chiamata la libreria
```C++
#include <ros.h>
```

Per attivare la comunicazione tra Arduino e ros devo eseguire
```C++
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

### Publisher template  
```C++
#include <ros.h> //carico la libreria
#include <std_msgs/String.h> //tipo di messaggio

ros::NodeHandle nh; //istanza del nodehandle che gesisce la comunicazione tra nodi

std_msgs::String str_msg; 
ros::Publisher chatter("chatter", &str_msg);

char hello[13] = "hello world!";

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
}

void loop()
{
  str_msg.data = hello;
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1000);
}
```
### Subscriber template 
```C++
#include <ros.h>
#include <std_msgs/Empty.h>

ros::NodeHandle nh;

void messageCb( const std_msgs::Empty& toggle_msg){
  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
}

ros::Subscriber<std_msgs::Empty> sub("toggle_led", &messageCb );

void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
```

### LCD Subscriber  

```C++
/*
* Sottoscrive L'LCD ad un toplic che pubblica testo
*/

#include <ros.h>
#include <std_msgs/Empty.h>

ros::NodeHandle nh;

//Creo la funzione callback per il subscriber. 

void messageCb( const std_msgs::Empty& toggle_msg)
{
  digitalWrite(13, HIGH-digitalRead(13));   // blink the led codice LCD
}

// Istanziamo il subscriber con il topic name "toggle_led" e tipo std_msgs::Empty. 
// Its two arguments are the topic it will be subscribing to (toggle_led) and the callback function it will be using.
ros::Subscriber<std_msgs::Empty> sub("toggle_led", &messageCb );

//In the Arduino setup function you then need to initialize your ROS node handle, advertise any topics being published, and subscribe to any topics you wish to listen to

void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

//in the loop function we call ros::spinOnce() where all of the ROS communication callbacks are handled
void loop()
{
  nh.spinOnce();
  delay(1);
}
```
