from rest_framework.views import APIView
from rest_framework.response import Response
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
os.environ["OPENAI_API_KEY"] = "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"

class ChatBot_FoodSearch:

    def prompt(self):
        llm = OpenAI(temperature=0.5)  

        prompt = PromptTemplate(
            input_variables=["food", "diet", "instructions"],
            template="Hey! Please provide the main ingredients of {food} and their approximate calorie count. Also, mention if it's suitable for someone following a {diet} answer as points. Instructions: {instructions}",
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        return chain

    def question(self,inputs):
        chain = self.prompt()
        return chain.run(inputs)
    def get_result(self,food,diet):
        instructions = "answer in bulletins always like a friend who motivates you to eat healthy and stay fit ."
        result = self.question({"food": food, "diet": diet, "instructions": instructions})
        return result

class ChatBot_DietSelector:

    def prompt(self):
        llm = OpenAI(temperature=0.5)  

        prompt = PromptTemplate(
            input_variables=["age", "sex", "height" ,"weight","to_gain_or_loose" , "vegan_or_non" ,"instructions"],
            template="Hey! Please suggest me a diet plan.I am a {sex} who is {age} year old with height {height} and weight {weight} I am a {vegan_or_non} and I want to {to_gain_or_loose} Instructions: {instructions}",
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        return chain

    def question(self,inputs):
        chain = self.prompt()
        return chain.run(inputs)
    def get_result(self,age,sex,height,weight,to_gain_or_loose,vegan_or_non):
        instructions = "answer in bulletins always like a friend who motivates you to eat healthy and stay fit also give a one diet name like keto,low-carb etc at last and also points to follow in it ."
        result = self.question({"age": age, "sex": sex,"height":height,"weight":weight,"to_gain_or_loose":to_gain_or_loose,"vegan_or_non":vegan_or_non, "instructions": instructions})
        return result
    
class ChatBotView_FoodSearch(APIView):

    def post(self, request, format=None):
        chatbot = ChatBot_FoodSearch()
        food = request.data.get('food')
        diet = request.data.get('diet')
        result = chatbot.get_result(food,diet)
        return Response({'response':result})

class ChatBotView_DietSelector(APIView):

    def post(self, request, format=None):
        chatbot = ChatBot_DietSelector()
        #get all the data from the request to pass to the chatbot_dietselector
        age = request.data.get('age')
        sex = request.data.get('sex')
        height = request.data.get('height')
        weight = request.data.get('weight')
        to_gain_or_loose = request.data.get('to_gain_or_loose')
        vegan_or_non = request.data.get('vegan_or_non')
        result=chatbot.get_result(age,sex,height,weight,to_gain_or_loose,vegan_or_non)
        return Response({'response':result})

    

