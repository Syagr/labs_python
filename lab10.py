""" 2 """
""" import random


class DeckOfCards:
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    suits = ('♠', '♣', '♦', '♥')

    def __init__(self):
        self.cards = [(rank, suit)
                      for rank in self.ranks for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("No cards left in the deck.")
            return None

    def reset(self):
        self.cards = [(rank, suit)
                      for rank in self.ranks for suit in self.suits]


deck = DeckOfCards()

deck.shuffle()

card = deck.deal()
if card:
    print(f"received card: {card[0]}{card[1]}")


deck.reset()

 """

""" 3 """
""" class TemperatureSensor:
    def __init__(self, temperature):
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_temperature(self, unit='Celsius'):
        if unit == 'Celsius':
            return self.temperature
        elif unit == 'Fahrenheit':
            return self.celsius_to_fahrenheit(self.temperature)
        elif unit == 'Kelvin':
            return self.celsius_to_kelvin(self.temperature)
        else:
            print("Invalid unit. Please choose Celsius, Fahrenheit, or Kelvin.")

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32


sensor = TemperatureSensor(25)


print("Temperature in Celsius:", sensor.get_temperature())


print("Temperature in Fahrenheit:", sensor.get_temperature('Fahrenheit'))


print("Temperature in Kelvin:", sensor.get_temperature('Kelvin'))


sensor.set_temperature(32)


print("Updated temperature in Celsius:", sensor.get_temperature())
 """

""" 4 """
""" class MazeGame:
    def __init__(self, maze):
        self.maze = maze
        self.player_position = (0, 0)

    def move_up(self):
        row, col = self.player_position
        if row > 0 and self.maze[row-1][col] != '#':
            self.player_position = (row-1, col)
        else:
            print("Cannot move up. Hit a wall.")

    def move_down(self):
        row, col = self.player_position
        if row < len(self.maze)-1 and self.maze[row+1][col] != '#':
            self.player_position = (row+1, col)
        else:
            print("Cannot move down. Hit a wall.")

    def move_left(self):
        row, col = self.player_position
        if col > 0 and self.maze[row][col-1] != '#':
            self.player_position = (row, col-1)
        else:
            print("Cannot move left. Hit a wall.")

    def move_right(self):
        row, col = self.player_position
        if col < len(self.maze[0])-1 and self.maze[row][col+1] != '#':
            self.player_position = (row, col+1)
        else:
            print("Cannot move right. Hit a wall.")

    def check_win(self):
        row, col = self.player_position
        if self.maze[row][col] == 'E':
            print("Congratulations! You reached the exit!")
            return True
        else:
            return False

    def print_maze(self):
        for row in self.maze:
            print(' '.join(row))

maze = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', 'E', ' ', '#'],
    ['#', '#', '#', '#', '#']
]

game = MazeGame(maze)

game.print_maze()

game.move_down()
game.move_down()
game.move_right()
game.move_right()
game.move_up()
game.move_up()

game.check_win()

game.print_maze()
"""

""" 5 """
""" class RestaurantMenu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item_name, item_price):
        if item_name not in self.menu_items:
            self.menu_items[item_name] = item_price
            print(f"Added '{item_name}' to the menu with price ${item_price}.")
        else:
            print(f"Item '{item_name}' already exists in the menu.")

    def remove_item(self, item_name):
        if item_name in self.menu_items:
            del self.menu_items[item_name]
            print(f"Removed '{item_name}' from the menu.")
        else:
            print(f"Item '{item_name}' not found in the menu.")

    def compute_total_cost(self, items_ordered):
        total_cost = 0
        for item in items_ordered:
            if item in self.menu_items:
                total_cost += self.menu_items[item]
            else:
                print(f"Item '{item}' not found in the menu.")
        return total_cost

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")
 
menu = RestaurantMenu()

menu.add_item("Pizza", 12.99)
menu.add_item("Burger", 9.99)
menu.add_item("Salad", 7.99)

menu.print_menu()

items_ordered = ["Pizza", "Burger", "Fries"]
total_cost = menu.compute_total_cost(items_ordered)
print(f"Total cost of items ordered: ${total_cost}")

menu.remove_item("Salad")

menu.print_menu()
"""

""" 6 """
""" from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            print(f"Vertex '{vertex}' already exists in the graph.")

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            # Remove vertex from edges
            for v in self.edges:
                self.edges[v] = [(u, w) for u, w in self.edges[v] if u != vertex]
            print(f"Vertex '{vertex}' removed from the graph.")
        else:
            print(f"Vertex '{vertex}' not found in the graph.")

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.edges[vertex1].append((vertex2, weight))
            self.edges[vertex2].append((vertex1, weight))
        else:
            print(f"One or both vertices '{vertex1}', '{vertex2}' not found in the graph.")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.edges[vertex1] = [(u, w) for u, w in self.edges[vertex1] if u != vertex2]
            self.edges[vertex2] = [(u, w) for u, w in self.edges[vertex2] if u != vertex1]
        else:
            print(f"One or both vertices '{vertex1}', '{vertex2}' not found in the graph.")

    def dijkstra(self, start_vertex, end_vertex):
        distances = {v: float('inf') for v in self.vertices}
        distances[start_vertex] = 0
        queue = [(0, start_vertex)]
        visited = set()

        while queue:
            dist, vertex = heapq.heappop(queue)

            if vertex == end_vertex:
                return distances[end_vertex]

            if vertex not in visited:
                visited.add(vertex)

                for neighbor, weight in self.edges[vertex]:
                    new_dist = dist + weight

                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(queue, (new_dist, neighbor))

        return float('inf')

    def print_graph(self):
        print("Vertices:")
        print(self.vertices)
        print("Edges:")
        for vertex, edges in self.edges.items():
            print(f"{vertex}: {edges}")


graph = Graph()


graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")


graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 1)
graph.add_edge("C", "E", 3)
graph.add_edge("D", "E", 4)


start_vertex = "A"
end_vertex = "E"
shortest_path = graph.dijkstra(start_vertex, end_vertex)

if shortest_path == float('inf'):
    print(f"There is no path between '{start_vertex}' and '{end_vertex}' in the graph.")
else:
    print(f"The shortest path between '{start_vertex}' and '{end_vertex}' is {shortest_path} units.")
"""

""" 7 """
""" class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Cat(Animal):
    def __init__(self, name, species, sound, fur_color):
        super().__init__(name, species, sound)
        self.fur_color = fur_color

    def meow(self):
        print("Meow!")

animal = Animal("Lion", "Mammal", "Roar")
print(animal.name)  
print(animal.species)  
animal.make_sound()  


cat = Cat("Fluffy", "Felis catus", "Meow", "Orange")
print(cat.name)  
print(cat.species)  
print(cat.fur_color) 
cat.make_sound()  
cat.meow()  
"""

""" 8 """
""" class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass  # Placeholder for calculating area


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

shape = Shape("Generic Shape")
print(shape.name) 
shape.calculate_area() 

rectangle = Rectangle("Rectangle 1", 5, 10)
print(rectangle.name)  
print(rectangle.width)  
print(rectangle.height)  
print(rectangle.calculate_area()) 
print(rectangle.calculate_perimeter())
"""

""" 9 """
""" class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print("Hello, I am", self.name)


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def calculate_grade(self):
        
        pass

person = Person("John", 30, "Male")
print(person.name) 
print(person.age)  
print(person.gender)  
person.say_hello()  

# Create a Student object
student = Student("Alice", 20, "Female", "123456")
print(student.name) 
print(student.age) 
print(student.gender)  
print(student.student_id)  
student.calculate_grade()  
"""

""" 10 """
""" class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")


class Truck(Vehicle):
    def __init__(self, make, model, year, max_payload):
        super().__init__(make, model, year)
        self.max_payload = max_payload

    def calculate_fuel_efficiency(self):
    
        pass

vehicle = Vehicle("Toyota", "Camry", 2022)
print(vehicle.make)  
print(vehicle.model)  
print(vehicle.year)  
vehicle.start_engine() 
vehicle.stop_engine()  


truck = Truck("Ford", "F-150", 2021, 5000)
print(truck.make)  
print(truck.model)  
print(truck.year)  
print(truck.max_payload) 
truck.calculate_fuel_efficiency()

"""

""" 11 """
""" from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")
dog = Dog()
cat = Cat()

dog.speak() 
cat.speak()
"""

""" 12 """
""" from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
rectangle = Rectangle(5, 10)
circle = Circle(5)

print(rectangle.calculate_area())  
print(circle.calculate_area())
"""