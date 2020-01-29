#!/usr/bin/python3

import os
import sys
import json

def init_app():
    print("Welcome to your tabletop RPG companion app.")
    print("Please type what you want to do.")
    print("You can CREATE a character, LOAD an existing one, access the SETTINGS or EXIT the app.")

def check_menu_sel():
    print("> ", end="")
    sys.stdout.flush()
    try:
        selection = sys.stdin.readline()
    except ValueError: 
        print("Error in value")

    selection = selection.lower()[:-1]
    print(selection)
    
    if (selection == "create"):
        create_character()
    elif (selection == "load"):
        load_character()
    elif (selection == "settings"):
        display_settings()
    elif (selection == "exit"):
        exit();
        
if __name__ == "__main__":
    init_app()
    menu = check_menu_sel()


    