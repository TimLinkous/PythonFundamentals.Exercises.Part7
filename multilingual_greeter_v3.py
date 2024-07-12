from typing import Dict , List
import random

# Dictionaries for languages, name prompts, and greetings
lang_dict = {1: 'English', 2: 'Spanish', 3: 'Portuguese'}
name_prompt_dict = {1: 'What is your name?', 2: '¿Cómo te llamas?', 3: 'Qual é o seu nome?'}
greetings_dict = {
    1: ['Hello', 'Hi', "Hey there"],
    2: ['Hola', 'Buenos dias', 'Ey'],
    3: ['Olá', 'Oi', 'Bom dia']
}

def print_language_options(lang_options: Dict[int, str]) -> None:
    print("Please choose a language: ")
    for key, value in lang_options.items():
        print(f'{key}: {value}')
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """

def language_input() -> int:
    return int(input())
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """

def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    return lang_choice in lang_options
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """

def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    return name_prompt_options.get(lang_choice)
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """

def name_input(name_prompt: str) -> str:
    print(name_prompt)
    return input()
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """

def greet(name: str, greetings_options: Dict[int, List[str]], lang_choice: int) -> None:
    greeting = random.choice(greetings_options[lang_choice])
    print(f'{greeting} {name}')
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """

def add_language():
    new_id = max(lang_dict, default=0) + 1
    lang_dict[new_id] = input("Enter the name of the new language: ")
    name_prompt_dict[new_id] = input(f"Enter the name prompt for {lang_dict[new_id]}: ")
    greetings_dict[new_id] = input(f"Enter the greeting for {lang_dict[new_id]}: ")

def add_greeting():
    lang_id = int(input("Enter the language ID to update: "))
    if lang_id in greetings_dict:
        greetings_dict[lang_id] = input("Enter the new greeting: ")
    else:
        print("Language ID not found.")

def admin_mode():
    print("Admin Mode:")
    print("1: Add support for additional languages.")
    print("2: Update greetings for existing languages.")
    choice = input()

    if choice == '1':
        add_language()
    elif choice == '2':
        add_greeting()
    else:
        print("Not a valid option. Try again.")

def user_mode():
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while not language_choice_is_valid(lang_dict, chosen_lang):
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)}"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)

if __name__ == '__main__':
    user_input = input("Press 1 for Admin mode or 2 for User mode: ")
    try:  #try-except handles the "Value Error" if the input cannot be converted to an error 
        mode = int(user_input)
    except ValueError:
        print(f"Invalid input: {user_input}. Please enter 1 or 2.")
    else:
        if mode == 1:
            admin_mode()
        elif mode == 2:
            user_mode()
        else:
            print("Invalid mode selection.")
