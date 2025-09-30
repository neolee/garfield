from dialog_system import Garfield
from bots.builtin import *
from bots.llm import SimpleLLMBot, LLMBot


if __name__ == '__main__':
    garfield = Garfield(1, 'list')
    garfield.add(HelloBot())
    garfield.add(GreetingBot())
    garfield.add(FavoriteColorBot())
    garfield.add(CalcBot('looped'))
    garfield.add(SimpleLLMBot('looped'))
    garfield.add(LLMBot())
    garfield.run()
