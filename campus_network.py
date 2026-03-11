# Peer-to-Peer Campus Network
# Data Structures Used:
# Hash Table, Graph, Binary Search Tree, Sorting

from collections import deque

# -------------------------------
# Student Class
# -------------------------------

class Student:
    def __init__(self, id, name, email, gpa):
        self.id = id
        self.name = name
        self.email = email
        self.gpa = gpa
        self.friends = []

# -------------------------------
# Hash Table (Student Registry)
# -------------------------------

students = {}   # key = id, value = Student object

def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    gpa = float(input("Enter GPA: "))

    students[id] = Student(id, name, email, gpa)

    print("Student added successfully")

# -------------------------------
# Graph (Friend Connections)
# -------------------------------

graph = {}

def add_friend():
    a = int(input("Enter Student ID 1: "))
    b = int(input("Enter Student ID 2: "))

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

    print("Friend connection added")

# -------------------------------
# BFS Shortest Path
# -------------------------------

def bfs(start, target):

    visited = set()
    queue = deque([[start]])

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node == target:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

# -------------------------------
# Binary Search Tree
# -------------------------------

class BSTNode:

    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

def insert_bst(root, student):

    if root is None:
        return BSTNode(student)

    if student.id < root.student.id:
        root.left = insert_bst(root.left, student)
    else:
        root.right = insert_bst(root.right, student)

    return root

def search_bst(root, id):

    if root is None:
        return None

    if root.student.id == id:
        return root.student

    if id < root.student.id:
        return search_bst(root.left, id)

    return search_bst(root.right, id)

# -------------------------------
# Leaderboard Sorting
# -------------------------------

def leaderboard():

    arr = list(students.values())

    arr.sort(key=lambda x: x.gpa, reverse=True)

    print("\nTop Students")
    for s in arr:
        print(s.name, "GPA:", s.gpa)

# -------------------------------
# Display Students
# -------------------------------

def display_students():

    for id, s in students.items():
        print(id, s.name, s.gpa)

# -------------------------------
# Menu System
# -------------------------------

root = None

while True:

    print("\n--- Campus Network ---")

    print("1 Add Student")
    print("2 Add Friend")
    print("3 Find Connection")
    print("4 Display Students")
    print("5 Leaderboard")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        add_student()

        root = None
        for s in students.values():
            root = insert_bst(root, s)

    elif choice == "2":

        add_friend()

    elif choice == "3":

        a = int(input("Start ID: "))
        b = int(input("Target ID: "))

        path = bfs(a, b)

        if path:
            print("Connection Path:", path)
        else:
            print("No connection found")

    elif choice == "4":

        display_students()

    elif choice == "5":

        leaderboard()

    elif choice == "6":

        break

    else:

        print("Invalid choice")