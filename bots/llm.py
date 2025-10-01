from bot import Bot
import models as m


system_message = "You are a helpful assistant."


class SimpleLLMBot(Bot):
    def __init__(self, runtype='looped'):
        super().__init__(runtype)
        self.q = "I'm now backed by the newest LLM. Let's talk."
        self.model = m.default
        self.system_message = system_message

    def _think(self, s):
        completion = self.model.create_chat_completion(
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": s}
            ]
        )
        return self.model.chat_completion_content(completion)


def stringify_messages(messages):
    import json
    
    s = f"\n{'-'*20} History dump {'-'*20}\n"
    s += json.dumps(messages,  ensure_ascii=False, indent=2)
    s += f"\n{'-'*55}"
    return s

class LLMBot(Bot):
    def __init__(self, runtype='custom', stream=True, verbose=False):
        super().__init__(runtype)
        self.q = "I'm now backed by the newest LLM. Let's talk."
        self.model = m.default
        self.stream = stream
        self.verbose = verbose
        self.system_message = system_message

    def _show_messages(self, messages):
        self._print(stringify_messages(messages), 'light_grey')

    # called after completion return from the model
    def _postprocessing(self, content):
        return content

    # called before provide context to the model
    def _preprocessing(self, q):
        return q

    def run(self):
        self._print(self.q)
        
        messages = [
            {"role": "system", "content": self.system_message}
        ]

        while True:
            q = input("> ")
            if self._is_command_quit(q): return Bot.EXIT_NORMAL
            if self._is_command_restart(q): return Bot.EXIT_RESTART
            context = self._preprocessing(q)
            self.model.append_message(messages, "user", context)
            
            new_message = {"role": "assistant", "content": ""}
            completion = self.model.create_chat_completion(messages, self.stream)
            if self.stream:
                for chunk in completion:
                    s = self.model.chat_completion_chunk_content(chunk)
                    if s:
                        print(self._format(s), end="", flush=True)
                        new_message["content"] += s # type: ignore
                print()
            else:
                response = self._postprocessing(self.model.chat_completion_content(completion))
                self._print(response)
                new_message["content"] = response

            messages.append(new_message)

            # print history if in verbose mode
            if self.verbose: self._show_messages(messages)
            else: print()
