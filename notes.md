# ros_training

### Elementi

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
cat package.xml    # per customizzare il file package
cd ..
catkin_make
```

### Comandi utili

| Comando | Descrizione |
| :--- | :--- |
| rospack find [package_name] | trova la cartella del package |
| rospack depends1 [package_name] | trova le dipendenze del package |
| roscd [package_name] | porta alla cartella del package |




___
![alt text](https://gavazzionline.files.wordpress.com/2014/01/img_6916.jpg?w=300)
