# ros_training

### Elementi

- package: le unità dei programmi ROS. Racchiudono il codice, i file, dipendenze, ecc...
- package manifest: file xml nel package. Contiene info base come autore, licenza, dipendenze,...
- nodes: Processi che eseguono operazioni
- master: mette in comunicazione i nodi
- parameter server: programma che può memorizzare i parametri o valori dai nodi
- topics: bus in cui i nodi mandano o ricevono messaggi 
- message: i messaggi che arrivano o partono dai nodi
- service: funzioni chiamate dal nodo client (request/reply)

### Creazione di un package
```
cd ~catkin_ws/src
catkin_create_pkg package_name std_msgs rospy roscpp
gedit package.xml    # per customizzare il file package
cd ..
catkin_make
```

### Comandi utili

| Area | Comando | Descrizione |
| :--- | :--- | :--- |
| Filesystem | roscd [package_name] | porta alla cartella del package |
| | roscd log | porta ai file log |
| | rosls [package_name] | ls del package |
| Package | rospack find [package_name] | trova la cartella del package |
| | rospack depends1 [package_name] | trova le dipendenze del package |
| Node | rosnode list | elenco nodi |
| | rosnode info [node_name] | info sul nodo |
| Topic | rostopic list | elenco topic |
| | rostopic echo /topic | echo dei dati |
| | rostopic pub /topic msg_type data| pubblica il dato sul topic |

# Publisher e Subscriber templates

### Publisher

```python
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():    
    pub = rospy.Publisher('chatter', String, queue_size=10)
    
    rospy.init_node('talker', anonymous=True)     # crea il nodo
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():        
        pub.publish('Hello World')    # pubblica la stringa
        rate.sleep()

if __name__ == '__main__':    # Funzione principale
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
```

### Subscriber
This declares that your node subscribes to the chatter topic which is of type std_msgs.msgs.String. When new messages are received, callback is invoked with the message as the first argument.
```python
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    rospy.init_node('listener', anonymous=True)    # crea il nodo

    rospy.Subscriber('chatter', String, callback)    # sottoscrive il topic e rimanda alla funzione callback

    rospy.spin()    # tiene il processo vivo

if __name__ == '__main__':
    listener()
```

___
![alt text](https://gavazzionline.files.wordpress.com/2014/01/img_6916.jpg?w=200)
