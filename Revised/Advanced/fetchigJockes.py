from urllib import request
import json

url = 'https://official-joke-api.appspot.com/jokes/ten'
r = request.urlopen(url)

print(r.getcode())  # Check the response code

data = r.read()
jsondata = json.loads(data)  # Parse the JSON data

class Joke:
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f'Setup: {self.setup}, Punchline: {self.punchline}'

# Initialize an empty list to store joke objects
jokes = []

for j in jsondata:
    setup = j['setup']
    punchline = j['punchline']

    # Create a Joke object and append it to the jokes list
    joke_obj = Joke(setup, punchline)
    jokes.append(joke_obj)

# Print the number of jokes
print(f'Total jokes: {len(jokes)}')

# Print each joke
for joke in jokes:
    print(joke)
