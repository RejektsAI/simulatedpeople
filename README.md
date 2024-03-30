# SimulatedPerson
SimulatedPerson is a Python class that allows you to create a simulated conversation partner powered by OpenAI's language models. With just a few lines of code, you can engage in interactive conversations and explore the capabilities of AI-driven dialogue.

## Features
Easy to set up and use
Customizable context and memory length
Adjustable generation parameters (temperature, frequency penalty, presence penalty, max tokens)
Conversation history management using a deque
Integration with OpenAI's chat completion API
## Getting Started
1. Install the required dependencies:
```bash
pip install openai
```
2. Obtain an API key from OpenAI.
3. Create an instance of the **SimulatedPerson** class:
```python
from simulated_person import SimulatedPerson

api_key = "your_openai_api_key"
context = "You are a helpful assistant named Alice."
alice = SimulatedPerson("Alice", api_key, context=context)
```
```python
alice.listen("Hello, Alice! How are you today?")
response = alice.get_response()
alice.speak(response)
print(response)
```
4. Start conversing with the simulated person:
5. Continue the conversation by calling listen(), get_response(), and speak() as needed.
### Customization
You can customize the behavior of the simulated person by adjusting the following parameters:
* model: The OpenAI model to use for generating responses (default: "gpt-3.5-turbo").
* memory_length: The maximum number of conversation turns to keep in memory (default: 10).
* context: The initial context or system message to set the behavior of the simulated person.
* temperature: Controls the randomness of the generated responses (default: 0.7).
* frequency_penalty: Penalizes repeated words or phrases (default: 1).
* presence_penalty: Penalizes new topics or concepts (default: 0.3).
* max_tokens: The maximum number of tokens in the generated response (default: 256).
### Example
Here's an example of how to use SimulatedPerson to create a simple chatbot:
```python
from simulated_person import SimulatedPerson

api_key = "your_openai_api_key"
context = "You are a friendly chatbot named Buddy who loves to chat about movies and books."
buddy = SimulatedPerson("Buddy", api_key, context=context)

while True:
    user_input = input("You: ")
    buddy.listen(user_input)
    response = buddy.get_response()
    buddy.speak(response)
    print(f"Buddy: {response}")
```
This example creates a chatbot named Buddy who engages in conversations about movies and books. The conversation continues until you manually stop the program.
