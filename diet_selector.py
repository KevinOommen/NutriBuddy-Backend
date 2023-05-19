import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
os.environ["OPENAI_API_KEY"] = "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"

def prompt():
    llm = OpenAI(temperature=0.5)  

    prompt = PromptTemplate(
        input_variables=["age", "sex", "height" ,"weight","to_gain_or_loose" , "vegan_or_non" ,"instructions"],
        template="Hey! Please suggest me a diet plan.I am a {sex} who is {age} year old with height {height} and weight {weight} I am a {vegan_or_non} and I want to {to_gain_or_loose} Instructions: {instructions}",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def question(inputs):
    chain = prompt()
    return chain.run(inputs)



instructions = "answer in bulletins always like a friend who motivates you to eat healthy and stay fit also give a one diet name like keto,low-carb etc at last and also points to follow in it ."

result = question({"age": "25", "sex": "man","height":"170 cm","weight":"120 kg ","to_gain_or_loose":"loose 2 kg","vegan_or_non":"vegan", "instructions": instructions})
print(result)
