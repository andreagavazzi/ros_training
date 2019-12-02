```python
#!/usr/bin/env python

# Crea un nodo che pubblica per l'lcd

import rospy
from std_msgs.msg import String

def lcd():    
    pub = rospy.Publisher('lcd_msg', String, queue_size=10)    # definisce il publisher, il topic su cui pubblica e il msg che porta
    
    rospy.init_node('to_lcd', anonymous=True)     # crea il nodo
    
    pub.publish('LCD ACTIVE')    # pubblica la stringa
        
if __name__ == '__main__':    # Funzione principale
    try:
        lcd()
    except rospy.ROSInterruptException:
        pass
```
