# Messages #

L'utilizzo dei messaggi è paragonabile a quello delle classi. Contengono infatti attributi propri che ne caratterizzano gli elementi

### sensor_msgs/JointState ###

Il msg consiste in multiple arrays (liste in python), una per ogni parte del joint state.
Lo scopo è quello di rendere ogni campo opzionale (es. il campo effort può essere tralasciato se non serve)
Tutte le liste del messaggio devono avere la stessa dimensione oppure essere vuote. In questo ultimo caso l'elemento non viene considerato.  

Elementi:  
Header header  
string[] name  
float64[] position  
float64[] velocity  
float64[] effort  

Es.
```python
...
pub = rospy.publisher('/cmd_joints', JointState)
...
servo_command = JointState()
servo_command.name = ['head_pan_joint', 'head_pan_tilt']
servo_command.position = [0.03, -1]
servo_command.effort = [0.5, 1]
...
pub.publish(servo_command)
...
```
