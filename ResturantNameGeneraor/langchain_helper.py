import os

from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

openai_api_key = os.environ.get("OPENAI_API_KEY")
print(openai_api_key)
llm = OpenAI(temperature=0.6)


def genearte_restro_menu(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    response = chain.invoke({'cuisine': cuisine})
    return response

if(__name__== "__main__"):
    print(genearte_restro_menu("indian"))




'''def genearte_restro_menu(cuisine):
    return {
        "restaurant_name":"curry_dlt",
        "menu_item":"samosa , paneer tikka"

    }'''
