#!/usr/bin/env python3

def welcome():
    print("Welcome to the test")
    print("When you are ready press enter.")
    

def ask_questions(ask_color=False):
    name = input("Name: ")
    print(f"It's nice to meet you {name}")

    if ask_color:
        color = input("What is your favorti color? ")
        print(f"{color} is a wonderful color!")

def goodbye():
    print("Ciao.")

welcome()
ask_questions(ask_color=True)
goodbye()