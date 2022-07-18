import tello
import time

def main():
    print ("====================================")
    print ("Engaging Drone")
    drone = tello.Tello('', 8889, False, 1, '192.168.10.1', 8889, False)  
    battery = drone.get_battery()
    print (f"Battery is {battery}")
    print ("Taking off")
    reply = drone.takeoff()
    print (reply)
    time.sleep(2)
    print ("Rotating CW")
    reply = drone.rotate_cw(90)
    print (reply)
    time.sleep(2)
    height = drone.get_height()
    print (f"Height is {height}")
    print ("Moving Forward")
    reply = drone.move('forward', 0.25)
    print (reply)
    time.sleep(2)
    print ("Landing")
    reply = drone.land()
    print (reply)
    time.sleep(2)
    drone.End_Video()
    drone.__del__()

if __name__ == "__main__":
    main()
