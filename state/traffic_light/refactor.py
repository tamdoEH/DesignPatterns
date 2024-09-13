# refactor the code to use state pattern

from abc import ABC, abstractmethod
import time

# State interface
class TrafficLightState(ABC):
    @abstractmethod
    def change(self, traffic_light):
        pass

    @abstractmethod
    def display(self):
        pass

# Concrete States
class RedState(TrafficLightState):
    def change(self, traffic_light):
        time.sleep(5)  # Red light lasts for 5 seconds
        traffic_light.change_state(GreenState())

    def display(self):
        return "Red Light - Stop!"

class YellowState(TrafficLightState):
    def change(self, traffic_light):
        time.sleep(2)  # Yellow light lasts for 2 seconds
        traffic_light.change_state(RedState())

    def display(self):
        return "Yellow Light - Prepare to stop"

class GreenState(TrafficLightState):
    def change(self, traffic_light):
        time.sleep(5)  # Green light lasts for 5 seconds
        traffic_light.change_state(YellowState())

    def display(self):
        return "Green Light - Go!"

# Context class
class TrafficLight:
    def __init__(self):
        self._state = GreenState()

    def change_state(self, state):
        self._state = state

    def display(self):
        return self._state.display()


# Usage example
if __name__ == "__main__":
    traffic_light = TrafficLight()
    print(traffic_light.display())
    traffic_light.change_state(YellowState())
    print(traffic_light.display())
    traffic_light.change_state(RedState())
    print(traffic_light.display())