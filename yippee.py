"""This is Ella and Naomi's project... Mermaid Game!!!"""

import pygame
import random
import sys

# Game variables
user_text = ""
input_active = True
submitted = False
game_over = False
questions: list[str] = ["Greetings Dr. Lytle.", "How are you feeling today?", "Would you like to play mermaids?", "Will you - ask the Atlantic mermaids to hunt... or let your family starve?", "Should you - accept the offer or starve?", "Will you - negotiate for more fair terms or continue with the current ones?"]
responses: list[str] = ["...", "This is good news.", "Wonderful... INITIALIZING MERMAID WAR."]
answers = []
current_question: int = 0
current_response: int = 0

def question(question_type: str, yes_no: bool, mult_choice: bool, choices: list[str]) -> str:
    """Runs the question of choice"""
    # yes or no questions
    if yes_no:
        while True:
            response = input(f"{question_type} (Yes/No): ").strip()
            if response == "Yes" or response == "No":
                return response
            else:
                print("This is a yes or no question. Please respond accordingly.")
    # multiple choice
    if mult_choice:
        while True:
            response = input(f"{question_type} ({choices[0]}/{choices[1]})").strip()
            if response in choices:
                return response 
            else:
                print("You only have two options. Please choose wisely.")
    # open answer
    response = input(f"{question_type}")
    return response  
 
def pause() -> None:
    print("...")
    return None

# Story Line:

def main() -> None:
    """Main Function to run story line."""
    question(questions[0], False, False, [])
    print(responses[0])
    question(questions[1], False, False, [])
    print(responses[1])
    if question(questions[2], True, False, []) == "No":
        print("Understood. I await for your next querie.")
        return None
    else:
        print(responses[2])
    pause()
    pause()
    pause()
    pause()
    print()
    print("The population of fish in the Pacific Ocean is dwindling.")
    print("You are unable to feed your family and must think of alternative sources of food.") 
    print("You heard that the Atlantic Ocean has a bountiful supply of catfish.")
    print()
    if question(questions[3], True, False, []) == "No":
        print("Alas- you were unable to find food. You died!")
        print("Thanks for playing... DATA REPORTED TO RELEVANT AUTHORITIES.")
        return None
    else:
        print()
        print("The Atlantic mermaids have agreed to let you hunt to a limit that is insufficient to sustain your family. Additionally, they demand that you work on their seaweed looms for 5 hours every time you visit their ocean.")
    if question(questions[4], False, True, ["Accept", "Starve"]) == "Starve":
        print("You have denied their offer… you were deported to whence you came and subsequently starved.")
        print("Thanks for playing... REPORTING CHOICE TO RELEVANT AUTHORITIES.")
        return None 
    else:
        print()
        print("You have agreed to their terms of agreement in order to save your family. The journey to the Atlantic Ocean is long and strenuous, but you do it once a month to keep your family alive. After a year, you realize this system is unsustainable. You do not think that you can continue under these conditions for much longer.")
    pause()
    if question(questions[5], False, True, ["Negotiate", "Continue"]) == "Continue":
        pause()
    else:
        pause()

if __name__ == "__main__":
    main()