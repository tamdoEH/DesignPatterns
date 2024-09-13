from abc import ABC, abstractmethod

# State interface
class WarriorState(ABC):
    @abstractmethod
    def move(self, warrior):
        pass

    @abstractmethod
    def attack(self, warrior):
        pass

    @abstractmethod
    def interact(self, warrior):
        pass

# Concrete States
class NormalState(WarriorState):
    def move(self, warrior):
        return "Walking normally"

    def attack(self, warrior):
        warrior.change_state(BattleState())
        return "Transitioning to battle state"

    def interact(self, warrior):
        return "Interacting with NPC"

class BattleState(WarriorState):
    def move(self, warrior):
        return "Moving in combat stance"

    def attack(self, warrior):
        return "Attacking the enemy"

    def interact(self, warrior):
        return "Can't interact during battle"

class StunnedState(WarriorState):
    def move(self, warrior):
        return "Can't move while stunned"

    def attack(self, warrior):
        return "Can't attack while stunned"

    def interact(self, warrior):
        return "Can't interact while stunned"

class StealthState(WarriorState):
    def move(self, warrior):
        return "Moving silently"

    def attack(self, warrior):
        warrior.change_state(BattleState())
        return "Sneak attack! Transitioning to battle state"

    def interact(self, warrior):
        warrior.change_state(NormalState())
        return "Exiting stealth mode to interact"

# Context class
class Warrior:
    def __init__(self):
        self._state = NormalState()

    def change_state(self, state):
        self._state = state

    def move(self):
        return self._state.move(self)

    def attack(self):
        return self._state.attack(self)

    def interact(self):
        return self._state.interact(self)

# Usage example
if __name__ == "__main__":
    warrior = Warrior()

    print("Initial state (Normal):")
    print(warrior.move())
    print(warrior.interact())
    print(warrior.attack())

    print("\nAfter attacking (should transition to Battle state):")
    print(warrior.move())
    print(warrior.attack())
    print(warrior.interact())

    print("\nChanging to Stunned State:")
    warrior.change_state(StunnedState())
    print(warrior.move())
    print(warrior.attack())
    print(warrior.interact())

    print("\nChanging to Stealth State:")
    warrior.change_state(StealthState())
    print(warrior.move())
    print(warrior.attack())

    print("\nAfter stealth attack (should transition to Battle state):")
    print(warrior.move())
    print(warrior.attack())