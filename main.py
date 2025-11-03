from dialog_system import Garfield
from bots.builtin import *
from bots.llm import SimpleLLMBot, LLMBot
from bots.cot import CoTBot
from bots.rag import RAGBot


if __name__ == '__main__':
    garfield = Garfield(1, 'list')
    garfield.add(HelloBot())
    garfield.add(GreetingBot())
    garfield.add(FavoriteColorBot())
    garfield.add(CalcBot('loop'))
    garfield.add(SimpleLLMBot('loop'))
    garfield.add(LLMBot())
    garfield.add(CoTBot())
    garfield.add(RAGBot())
    garfield.run()
