# ros_training

### Elementi

- package: I programmi ROS. Racchiudono, oltre un manifest.xml descrittivo, codice, file, dipendenze, ecc..
- node: Processi che eseguono operazioni
- topic: bus in cui i nodi mandano o ricevono messaggi
- message: i messaggi che arrivano o partono dai nodi  

- master: mette in comunicazione i nodi
- parameter server: programma che può memorizzare i parametri o valori dai nodi
- service: funzioni chiamate dal nodo client (request/reply)

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

### Creazione di un package
```
cd ~catkin_ws/src
catkin_create_pkg package_name std_msgs rospy roscpp
gedit package.xml    # per customizzare il file package
cd ..
catkin_make
```

# Publisher e Subscriber templates


### Publisher
Il nodo pubblica un messaggio su un topic
```python
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():    
    pub = rospy.Publisher('chatter', String, queue_size=10)    # definisce il publisher, il topic su cui pubblica e il msg che porta
    
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
Il nodo sottoscrive un dato topic che pubblica un dato messaggio. Quando il nodo riceve un messaggio viene chiamata la funzione di callback che contiene il messaggio stesso come primo argomento.
```python
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    print data.data
    
def listener():
    rospy.init_node('listener', anonymous=True)    # crea il nodo

    rospy.Subscriber('chatter', String, callback)    # sottoscrive il topic e rimanda alla funzione callback

    rospy.spin()    # tiene il processo vivo

if __name__ == '__main__':
    listener()
```

___
![alt text](https://gavazzionline.files.wordpress.com/2014/01/img_6916.jpg?w=200)
