# Functional Prompt

def ascending_sort(array):
    arr = []
    for item in array:
        if type(item) == list:
            for i in item:
                arr.append(i)
        else:
            arr.append(item)
    return sorted(arr)

print(ascending_sort([1,2,3,[6,5,9],[4,7,8]]))

"""
1.This function accepts an array and returns a new array without changing the original array. 

2. This function is a pure function. It always returns the same output for the same input, and it has no side effects. It doesn't interact with any external state or data.

3. No, this solution is not a higher-order function. A higher-order function is a function that takes another function as an argument or returns a function. This function takes a list as argument and returns a new list.

4. Not sure. Comparing with OOP for this problem. I feel functional programming is more flexible and easier to manipulate.

5. Functional programming ensures data immutability. This function doesn't alter the original array.

"""

# Object oriented Prompt

class Podracer:
    def __init__ (self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    def repair(self):
        self.condition = "repaired"
    
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed = self.max_speed * 2
    
class SebulbasPod(Podracer):
    def flame_jet(self, other):
        other.condition = "trashed"

Anakins_pod = AnakinsPod(300, "good", 5000)
print(f"Anakin's pod max speed: {Anakins_pod.max_speed}")
Anakins_pod.boost()
print(f"Anakin's pod max speed after boost: {Anakins_pod.max_speed}")
SebulbasPod = SebulbasPod(280, "excellent", 10000)
SebulbasPod.flame_jet(Anakins_pod)
print(f"Anakin's pod condition after flame jet: {Anakins_pod.condition}")

"""
1.a.Encapsulation: Using classes, it bundles data(max_speed, condition, price,etc) and functions(__init__, repair, boost, etc) into a single unit(class).

1.b.Abstraction: Using classes hides the details of the implementation and provides a simplified interface to the user. Users only need to use the methods provided in the class, and not the implementation details.

1.c.Inheritance: AnakinsPod and SebulbasPod both inherit from the Podracer class, demonstrating inheritance. They inherit attributes like max_speed, condition, and price, as well as methods like repair. 

1.d.Polymorphism: All child classes' objects can be treated as if they were instances of their superclass when there is only __init__ method is used.


2. Not sure. Feel like OOP is more efficient for this problem. It allows child classes to inherit attributes and methods from their parent class, which make the codes more concise and reusable. It also make it easier to create new objects from the existing classes. For users, it is easier to understand and use.

3.Each class encapsulates data and methods into a single unit. Each child class inherits attributes and methods from its parent class.

"""