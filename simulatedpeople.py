from collections import deque
from openai import OpenAI

class SimulatedPerson:
    def __init__(self, first_name, api_key, model="gpt-3.5-turbo", memory_length=10, context=""):
        self.first_name = first_name
        self.ai = OpenAI(api_key=api_key)
        self.model = model
        self.memory = deque(maxlen=memory_length)
        self.context = self.format("system", context)
        self.last_response = None

    def format(self, role, content):
        return {"role":role,"content":content}

    def get_response(self, temperature=0.7, frequency_penalty=1, presence_penalty=0.3,max_tokens=256):
        self.last_response = self.ai.chat.completions.create(
            model=self.model,
            messages=[self.context] + list(self.memory),
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            max_tokens=max_tokens,
        )
        response = self.last_response.choices[0].message.content
        return response
    
    def listen(self,content):
        self.memory.append(self.format("user", content))

    def speak(self,content):
        self.memory.append(self.format("assistant", content))

    def reset_memory(self):
        self.memory.clear()