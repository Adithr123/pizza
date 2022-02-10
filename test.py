# Import ability to use enums
from enum import Enum

# Create a dictionary for each language, with each message translation inside
english = dict(
    Welcome="Welcome to Adith Pizzeria\n",
    Name="What would you like your order name to be?",
)
spanish = dict(
    Welcome="Bienvenidos a Adith Pizzeria.\n",
    Name="Qual es tu nombre? "
)


# Create an enum to hold the available languages in the program
class AvailableLanguages(Enum):
    English = 1,
    Spanish = 2


# Create a class to get the specified language by AvailableLanguage enum value
class Languages:
    @staticmethod
    def get(language):
        if language == AvailableLanguages.English:
            return english
        if language == AvailableLanguages.Spanish:
            return spanish
        raise Exception("Language is not defined")


# Create a messages class to get the specific message for a given language.
class Messages:
    def __init__(self, language):
        self.language = Languages.get(language)

    def get(self, key):
        return self.language[key]


# Creates an instance of the Messages class, asking it for only english messages
messages = Messages(AvailableLanguages.English)

# Prints out the english version of the welcome message
print(messages.get("Welcome"))