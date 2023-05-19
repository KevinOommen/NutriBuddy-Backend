import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
os.environ["OPENAI_API_KEY"] = "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"

def prompt():
    llm = OpenAI(temperature=0.5)  

    prompt = PromptTemplate(
        input_variables=["food", "diet", "instructions"],
        template="Hey! Please provide the main ingredients of {food} and their approximate calorie count. Also, mention if it's suitable for someone following a {diet} answer as points. Instructions: {instructions}",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def question(inputs):
    chain = prompt()
    return chain.run(inputs)



instructions = "answer in bulletins always like a friend who motivates you to eat healthy and stay fit ."

result = question({"food": "Shawarma", "diet": "keto", "instructions": instructions})
print(result)
