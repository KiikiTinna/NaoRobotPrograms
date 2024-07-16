import qi
import argparse
import sys
import time

def main(session):
    """
    Walk and Turn - Example to make Nao walk and then turn
    This example is only compatible with NAO
    """
    # Get the services ALMotion & ALRobotPosture
    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")

    # Wake up robot
    motion_service.wakeUp()

    # Send robot to Stand
    posture_service.goToPosture("StandInit", 0.5)

    # Enable arms control by Motion algorithm
    motion_service.setMoveArmsEnabled(True, True)

    # Set foot contact protection
    motion_service.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

    # Walk forward
    X = 0.7  # forward speed
    Y = 0.0  # lateral speed
    Theta = 0.0  # rotation speed
    Frequency = 0.6  # moderate speed
    try:
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
    except Exception as errorMsg:
        print(str(errorMsg))
        print("This example is not allowed on this robot.")
        exit()

    time.sleep(4.0)  # Walk for 4 seconds

    # Stop walking
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motion_service.moveToward(X, Y, Theta)
    motion_service.waitUntilMoveIsFinished()

    # Turn 90 degrees
    Theta = 1.57  # 90 degrees in radians
    motion_service.moveTo(0, 0, Theta)
    motion_service.waitUntilMoveIsFinished()

    # Go to rest position
    motion_service.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.94",
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.0.94'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print("Can't connect to Naoqi at IP \"" + args.ip + "\" on port " + str(args.port) + ".\n"
              "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
