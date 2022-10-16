#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
#from Percent.msg import completed
PI = 3.1415926535897

def rotate(distance):
    #Starts a new node
    rospy.init_node('draw_triangle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    vel_msg = Twist()

    #percentage_publisher = rospy.Publisher('/draw_percent', completed, queue_size = 10)
    #complete_info = completed()
    #complete_info.completed = 0

    # Receiveing the user's input
    paramSpeed = rospy.get_param("/turtle_speed") #2.0
    speed = paramSpeed * 30
    lSpeed = speed/30
    angle = 120
    clockwise = True


    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360


    # Setting the current time for distance calculus
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0   #-abs(angular_speed)

    current_angle = 0
    current_distance = 0 


    for i in range(3):

        paramSpeed = rospy.get_param("/turtle_speed")
        speed = paramSpeed * 30
        lSpeed = speed/30
        angle = 120
        clockwise = True

        t0 = rospy.Time.now().to_sec()

        while(current_angle <= relative_angle):
            paramSpeed = rospy.get_param("/turtle_speed")
            speed = paramSpeed * 30
            angle = 120
            angular_speed = speed*2*PI/360
            relative_angle = angle*2*PI/360
            clockwise = True
            vel_msg.angular.z = -abs(angular_speed)
            print("))) moving angular")

            velocity_publisher.publish(vel_msg)
            

            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)


        vel_msg.angular.z = 0
        current_angle = 0

        while(current_distance <= distance):
            paramSpeed = rospy.get_param("/turtle_speed")
            speed = paramSpeed * 30
            lSpeed = speed/30
            vel_msg.linear.x = lSpeed
            print(">>> moving linear")
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance = lSpeed*(t1-t0)
            #complete_info.completed = current_distance/distance*3
            #percentage_publisher.publish(complete_info)
    	    
        vel_msg.linear.x = 0
        current_distance = 0
        velocity_publisher.publish(vel_msg)
        print("*********end of line**********")
    
    
        
    #Forcing our robot to stop
    vel_msg.angular.z = 0
    vel_msg.linear.x = 0
    print("error 1")
    velocity_publisher.publish(vel_msg)
    print("error2")
    #return None
    return

    rospy.spin()
    print("error3")


if __name__ == '__main__':
    try:
        # Testing our function

        print("Let's rotate your robot")
        distance = input("please enter distance: (or enter 0 (zero) to exit.)")

        if(distance == 0):
            print("Exiting now...")
            exit(1)

    	while(distance != 0):
            rotate(distance)
            distance = input("please enter distance: (or enter 0 to exit.)")

    except rospy.ROSInterruptException:
        pass
