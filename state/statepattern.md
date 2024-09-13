# Problem Statement
Consider this Python code for a warrior character in an RPG:

```python
class Warrior:
    def __init__(self):
        self.state = "normal"

    def move(self):
        if self.state == "normal":
            return "Walking normally"
        elif self.state == "battle":
            return "Moving in combat stance"
        elif self.state == "stunned":
            return "Can't move while stunned"
        elif self.state == "stealth":
            return "Moving silently"

    def attack(self):
        if self.state == "normal":
            return "Can't attack in normal state"
        elif self.state == "battle":
            return "Attacking the enemy"
        elif self.state == "stunned":
            return "Can't attack while stunned"
        elif self.state == "stealth":
            return "Performing sneak attack"

    def interact(self):
        if self.state == "normal":
            return "Interacting with NPC"
        elif self.state == "battle":
            return "Can't interact during battle"
        elif self.state == "stunned":
            return "Can't interact while stunned"
        elif self.state == "stealth":
            return "Can't interact in stealth mode"
```

This code has several issues:

- It's hard to read and maintain due to numerous if-else statements.
- Adding a new state requires modifying multiple methods.
- The state logic is scattered across different methods.
- It violates the Open-Closed Principle: the class needs modification every time a new state is added.
  
# The Solution: State Pattern
The State Pattern can help us resolve these issues. But what exactly is it?

## 1. What is the State Pattern?
The State Pattern allows an object to alter its behavior when its internal state changes. It's as if the object changes its class.
This pattern is closely related to [Finite State Machine](https://en.wikipedia.org/wiki/Finite-state_machine#:~:text=A%20finite%2Dstate%20machine%20(FSM,states%20at%20any%20given%20time)) (FSM) concept. In the FSM, the object can be in one of a finite number of states, and its behavior changes based on the current state. The State Pattern is a way to implement FSMs in object-oriented programming. 

## 2. How does the State Pattern work?

- We create a separate class for each state.
- Each state class implements a common interface.
- The main object holds a reference to the current state object.
- When the state changes, we simply swap out the state object.
  
## 3. Implementing the Solution
Let's refactor our Warrior class using the State Pattern:
```python
from abc import ABC, abstractmethod

# State interface
class WarriorState(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def interact(self):
        pass

# Concrete States
class NormalState(WarriorState):
    def move(self):
        return "Walking normally"

    def attack(self):
        return "Can't attack in normal state"

    def interact(self):
        return "Interacting with NPC"

class BattleState(WarriorState):
    def move(self):
        return "Moving in combat stance"

    def attack(self):
        return "Attacking the enemy"

    def interact(self):
        return "Can't interact during battle"

class StunnedState(WarriorState):
    def move(self):
        return "Can't move while stunned"

    def attack(self):
        return "Can't attack while stunned"

    def interact(self):
        return "Can't interact while stunned"

class StealthState(WarriorState):
    def move(self):
        return "Moving silently"

    def attack(self):
        return "Performing sneak attack"

    def interact(self):
        return "Can't interact in stealth mode"

# Warrior class
class Warrior:
    def __init__(self):
        self.state = NormalState()

    def change_state(self, state):
        self.state = state

    def move(self):
        return self.state.move()

    def attack(self):
        return self.state.attack()

    def interact(self):
        return self.state.interact()

# Usage example
if __name__ == "__main__":
    warrior = Warrior()

    print("Normal State:")
    print(warrior.move()) # Output: Walking normally
    print(warrior.attack()) # Output: Can't attack in normal state
    print(warrior.interact()) # Output: Interacting with NPC

    print("\nChanging to Battle State:")
    warrior.change_state(BattleState())
    print(warrior.move()) # Output: Moving in combat stance
    print(warrior.attack()) # Output: Attacking the enemy
    print(warrior.interact()) # Output: Can't interact during battle

    print("\nChanging to Stunned State:")
    warrior.change_state(StunnedState())
    print(warrior.move()) # Output: Can't move while stunned
    print(warrior.attack()) # Output: Can't attack while stunned
    print(warrior.interact()) # Output: Can't interact while stunned

    print("\nChanging to Stealth State:")
    warrior.change_state(StealthState())
    print(warrior.move()) # Output: Moving silently
    print(warrior.attack()) # Output: Performing sneak attack
    print(warrior.interact()) # Output: Can't interact in stealth mode
```

Benefits of this approach:

- Each state's behavior is encapsulated in its own class.
- Adding a new state is as simple as creating a new class.
- The Warrior class doesn't need to change when adding new states.
- The code is more organized and easier to understand.

Downsides of this approach:

- Maybe overkill for small projects with few states.
- The number of classes can grow quickly if there are many states.

# Resources
- [State Pattern on Refactorguru](https://refactoring.guru/design-patterns/state/python/example#lang-features)
- [State Pattern using on Shoppee shipping status](https://techmaster.vn/posts/38155/state-pattern-ap-dung-lam-phan-quan-ly-trang-thai-don-hang-shopee)
- [Geeksforgeeks](https://www.geeksforgeeks.org/state-design-pattern/)
  
