import myfitnesspal
import os
from dotenv import load_dotenv
from openai import OpenAI

recipe_list = []

client = myfitnesspal.Client()
recipes = client.get_recipes()
for recipe_id in recipes.keys():
    recipe = client.get_recipe(recipe_id)
    recipe_list.append(recipe)



load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a nutritionist helping to create meal plans the meet the clients macros."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)


print(recipe_list)
