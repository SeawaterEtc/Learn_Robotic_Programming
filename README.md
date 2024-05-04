# Learning ROS1

This is for learning and Reviewing ROS1. I will put everything in here. Basically everything about what I have learnt!

### ROS Basic concept

-> ROS master <-

<- Node -> Publishing -> Topic -> Callback -> Node -> subscribing ->

![alt text](image-2.png)


# Turtlesim_ws
create ws
```
mkdir -p turtlesim_ws/src
```


go to the dir, for my machine
```
cd ros1_workspaces/turtlesim_ws/src
```


## create pkg
```
catkin_create_pkg controller rospy roscpp turtlesim 
```
then catkin_make on ws


## create script node
```
cd controller 
mkdir script 
cd script
touch first_node.py
chmod +x first_node.py
```

Inside the first_node.py is the script that print out some messages
```
#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")
    rospy.loginfo("Hello from test node")
    rospy.logwarn("This is a warning")
    rospy.logerr("This is an error")
    rospy.sleep(1.0)
    rospy.loginfo("End of program")
```

create script to display message continously. in script dir
```
touch dmc_node.py
chmod +x dmc_node.py
```

inside dmc_node.py
```
#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")
    rospy.loginfo("Test node has been started")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()
```

running the script, don't forget to source and stay inside the ws
```
rosrun controller first_node.py
```

```
rosrun controller dmc_node.py
```
go to the script dir
```
python3 first_node.py
```

```
python3 dmc_node.py
```
![alt text](image.png)

### checking information 
rostopic list, rostopic info, rosmsg show, rostopic echo, rqt --clear-config
![alt text](image-1.png)

## Ros1 Publisher and Subscriber

### create Publisher
it is just a file (node in a pkg) in script but it publish some message to the topic
in script
```
touch draw_circle.py
chmod +x draw_circle.py
```

in the draw_circle.py, because when checking rostopic list, rostopic info /turtle1/cmd_vel, rosmsg show /geometry_msg/Twist, there are two information
```
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```
so we will use it to create a publisher.

inside the draw_circle.py
```
#!/usr/bin/env python3
import rospy
from geometry_msgs import Twist 

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started.")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        pub.publish(msg)
        rate.sleep()
```

ensure that in package.xml file there is this line. It sure that the package will run based on the topic. (I am not so sure why, but If I don't include the package won't run I think)
```
<build_depend>geometry_msg</build_depend>
```



```

```
# Turtlebot3_ws



# Smb_ws

```

```

```

```

```

```