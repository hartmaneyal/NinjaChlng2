from djitellopy import Tello
import time, cv2
from threading import Thread

tello = Tello('192.168.10.1')
keepRecording = [True]

def runCommands():
    print("Running commands")

    battery = tello.get_battery()
    print (f"Battery is {battery}")

    tello.takeoff()

    tello.move_forward(50)
    tello.move_back(50)

    tello.rotate_counter_clockwise(25)
    tello.move_forward(70)
    tello.move_back(70)

    tello.move_right(50)
    tello.rotate_clockwise(25)

    tello.move_forward(30)
    tello.move_forward(30)

    tello.land()

    print("Commands completed")
    time.sleep(5)
    keepRecording[0] = False

if __name__ == "__main__":
    try:
        print("============= STARTING =============")

        tello.connect()
        
        tello.streamon()
        frame_read = tello.get_frame_read()

        cv2.namedWindow("Tello", cv2.WINDOW_NORMAL)

        commands = Thread(target=runCommands, daemon=True).start()

        print("Starting Video feed")
        while keepRecording[0]:
            cv2.imshow('Tello',frame_read.frame)
            cv2.waitKey(100)
        print("Video feed closed")

        cv2.destroyAllWindows()
        tello.streamoff()

        print("============= COMPLETED =============")
    except BaseException as err:
        print(f"An exception occurred: {err}")