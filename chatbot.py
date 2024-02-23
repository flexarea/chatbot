import re
from typing import List
import random

class ChatBot:
    def make_reply(self, text: str) -> str:
        replies = {r"\b(hello|hi|hey|what up|what's up|yo|good morning)\b": "hey, how are you today?",
                   r"\b(well|fine|good|chilling)\b": "Glad to hear that! How old are you?",
                   r"^(i |i'm |i am )?\d{1,2}.*?$": "As Pierre Corneille said, value doesn't wait the number of years. You can still be anything you want.",
                   r"(failing|tired|lost|life|give up)": "You are not everything you could be, and you know it.",
                   r"\b(joke|Tell me)\b": "Why was Cinderella so bad at soccer?\n She kept running from the ball.",
                   r"^(what).*(your|name)\?$": "I'm artemisx.\nWhat about you?",
                   r"\b(productive|better|be)\b": "If you fulfill your obligations every day you don’t need to worry about the future.",
                   r"\b(wtf)|f.[ck]\b": "No cursing, please :)",
                   r"\b(heartbroken)\b": "Letting go means to come to the realization that some people are a part of your history but not a part of your destiny"
                   }

        for i in replies:
            if re.search(i,text.lower()) != None:
                return replies[i]
            
        return "Sorry! That's beyond my knowledge."
        raise NotImplementedError

    @staticmethod
    def get_name() -> str:
        return "artemisx"
        raise NotImplementedError


    @staticmethod
    def examples() -> List[str]:
        lst = ["How do I make my time productive", "I am tired of failing", "What's the purpose of life", "How can I be better?", " I am heartbroken ", "Tell me a joke", "I give up"]
        return lst
        raise NotImplementedError


def get_user_statement() -> str:
    return input("you: ").lower().strip()


def main():
    bot = ChatBot()

    print(f"You're chatting with {bot.get_name()}")
    you_said = get_user_statement()
    while you_said.lower().strip() != "exit":
        if you_said == "examples":
            print("Examples: ", bot.examples())
        else:
            bot_said = bot.make_reply(you_said)
            print("bot: " + bot_said)
        you_said = get_user_statement()
    print("Bye!")


if __name__ == "__main__":
    main()

# Discover NLP course materials authored by Julie Medero, Xanda Schofield, and Richard Wicentowski
# This work is licensed under a Creative Commons Attribution-ShareAlike 2.0 Generic License# https://creativecommons.org/licenses/by-sa/2.0/
