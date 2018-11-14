### sensor_msgs/JointState ###

Il msg consiste in multiple arrays, una per ogni parte del joint state.
Lo scopo è quello di rendere ogni campo opzionale (es. il campo effort può essere tralasciato se non serve)
This message consists of a multiple arrays, one for each part of the joint state. 
Tutte le array del messaggio devono avere la stessa dimensione oppure essere vuoti.

Header header
string[] name
float64[] position
float64[] velocity
float64[] effort
