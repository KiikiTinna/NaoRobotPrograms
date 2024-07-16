import qi


# Connect to the robot
session = qi.Session()
session.connect("tcp://192.168.1.161") # Robot IP

# TextToSpeech service
tts = session.service("ALTextToSpeech")
tts.say("Hi")

session.close()