
![alt text](https://github.com/andreagavazzi/ros_training/blob/master/data/D23D2A98-7AD6-4566-AF74-CE00F2298B5E.jpeg)
# ros_training

### Elementi del filesystem

Package
ROS packages are the individual units, or the atomic units, of ROS software. All source code, data files, build files, dependencies, and other files are organized in packages.

Package manifest
A package manifest is an XML file placed inside a ROS package. It has all the primary information of a ROS package, including the name of the package, description, author, dependencies, and so forth.

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


