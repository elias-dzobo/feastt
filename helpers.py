import os 
from datetime import datetime 
from dotenv import dotenv_values
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain_openai import ChatOpenAI
from openai import OpenAI


from langchain.output_parsers import ResponseSchema, StructuredOutputParser


#_ = load_dotenv(find_dotenv())

env = dotenv_values('.env')
os.environ['OPENAI_API_KEY'] = env.get("OPENAI_API_KEY")

meals = ResponseSchema(
        name="meals",
        description="a list of meal-recipe combos",
        type="list"
    )

response_schema = [meals]

parser = StructuredOutputParser.from_response_schemas(response_schema)


def generate_recipe(items, preferences):
    prompt_template = """
    
    Given the list of ingredients {items}, provide exactly four meals that can be prepared using mainly the mentioned ingredients.

    The meal should adhere strictly to the user's preferences {preferences}. 

    For each meal provided, provide a clear step by step recipe showing how said meal is prepared. 

    You are allowed to add few ingredients that can be used to complete the meal and provide alternatives for ingredients where needed based on the users preference.

    create a dictionary for each meal, with the keys 'meal' for the name of the meal, 'ingredients' for the ingredients used and 'recipe' for the instructions on how to prepare the meal.
    Your final output should be a json output with the key being "meals" and the value being the list

    """
    prompt = PromptTemplate(
        input_variables= ["items", "preferences"],
        template= prompt_template,
        partial_variables= {"format_instructions": parser.get_format_instructions()}
    )

    llm_chain = LLMChain(
        llm= ChatOpenAI(model_name='gpt-4o', temperature=0.8),
        prompt=prompt
    )

    res = llm_chain.run(items=items, preferences=preferences)

    res = parser.parse(res) 
    

    return res

def identify_ingredients(image):

    # Convert the image to bytes
    #img_bytes = io.BytesIO()
    #image.save(img_bytes, format='PNG')
    #img_bytes = img_bytes.getvalue()

    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "What’s ingredients are in this image?"},
            {
            "type": "image",
            "image_url": {
                "url": image
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    return response.choices[0]

""" items = ['potato', 'eggs', 'oil', 'chicken breast', 'seasoning']
preferences = 'A protein rich high caloric meal'

res = generate_recipe(items, preferences)

print(type(res))
print()
print(res)
print()

for meal in res['meals']:
    print(meal['meal'])
    print()
    print('\n'.join(meal['ingredients']))
    print()
    print('\n'.join(meal['recipe']))  """

#ing = identify_ingredients('temp_upload/ing.jpeg')
#print(ing)

