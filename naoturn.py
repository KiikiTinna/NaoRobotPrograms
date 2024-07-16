import qi
import argparse
import sys
import time

def main(session):
    """
    Turn - Small example to make Nao turn
    This example is only compatible with NAO
    """
    # Get the services ALMotion & ALRobotPosture.
    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")

    # Wake up robot
    motion_service.wakeUp()

    # Send robot to Stand
    posture_service.goToPosture("StandInit", 0.5)

    #####################
    ## Enable arms control by Motion algorithm
    #####################
    motion_service.setMoveArmsEnabled(True, True)
    # motion_service.setMoveArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #motion_service.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motion_service.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.8  # Adjust the angular velocity to control the turning speed
    Frequency = 0.6  # Adjust the frequency as desired
    try:
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
    except Exception as errorMsg:
        print(str(errorMsg))
        print("This example is not allowed on this robot.")
        exit()

    # Keep turning for 4 seconds
    time.sleep(4.0)

    #####################
    ## End Turn
    #####################
    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motion_service.moveToward(X, Y, Theta)

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
