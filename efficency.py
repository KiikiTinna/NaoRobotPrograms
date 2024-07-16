import qi
import argparse
import sys
import time
import math

def main(session):
  
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

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    motion_service.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    Frequency = 1.2  # moderate speed

    try:
        # Turn to the left
        X = 0.0
        Y = 0.0
        Theta = -0.4  # Negative value for left turn
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(3.0)  # Wait for the turn to complete

        # Move straight for 1 meter
        X = 0.9# forward
        Y = 0.0
        Theta = 0.0
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(3.0)  # Wait for the movement to complete

        # Turn to the left again
        X = 0.0
        Y = 0.0
        Theta = 0.4 # Negative value for left turn
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(4.0)  # Wait for the turn to complete

        # Move straight for 1 meters
        X = 1.0  # forward
        Y = 0.0
        Theta = 0.0
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(3.0)  # Wait for the movement to complete
        
        # Move straight for 1 meters
        X = 1.0  # forward
        Y = 0.0
        Theta = 0.0
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(3.0)  # Wait for the movement to complete
        
        # Move straight for 1 meters
        X = 1.0  # forward
        Y = 0.0
        Theta = 0.0
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(3.0)  # Wait for the movement to complete
                
        # Move straight for 1 meters
        X = 1.0  # forward
        Y = 0.0
        Theta = 0.0
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(2.0)  # Wait for the movement to complete
        
        # Move straight for 1 meters
        X = 0.5 # forward
        Y = 0.0
        Theta = 0.0
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(3.0)  # Wait for the movement to complete
        
        
        # Turn left 
        X = 0.0  # forward
        Y = 0.0
        Theta = -0.5
        motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        time.sleep(3.0)  # Wait for the movement to complete

    except Exception as errorMsg:
        print(str(errorMsg))
        print("This example is not allowed on this robot.")
        exit()

    #####################
    ## End Walk
    #####################
    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motion_service.moveToward(X, Y, Theta)

    motion_service.waitUntilMoveIsFinished()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.161",
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
