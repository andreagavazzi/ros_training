# ros_training

### Elementi del filesystem

- package: le unitá dei programmi ROS. Racchiudono il codice, i file, dipendenze, ecc..
- package manifest: file xml nel package. Contiene info base come autore, licenza, dipendenze,..
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
cd ..
catkin_make
```


___
![alt text](https://gavazzionline.files.wordpress.com/2014/01/img_6916.jpg?w=300)
