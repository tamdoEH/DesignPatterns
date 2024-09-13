# Code for traffic light transition that contains too many if-elif-else statements
import time
def change_light(light):
    if light == "red":
        time.sleep(5)  # Red light lasts for 5 seconds
        return "Green Light - Go!"
    elif light == "green":
        time.sleep(5)  # Green light lasts for 5 seconds
        return "Yellow Light - Prepare to stop"
    elif light == "yellow":
        time.sleep(2)  # Yellow light lasts for 2 seconds
        return "Red Light - Stop!"
    else:
        return "Invalid light color"
    

         