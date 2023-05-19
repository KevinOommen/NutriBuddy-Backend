from rest_framework.views import APIView
from rest_framework.response import Response
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
os.environ["OPENAI_API_KEY"] = "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"

class ChatBot:

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
    
class ChatBotView_FoodSearch(APIView):

    def post(self, request, format=None):
        chatbot = ChatBot()
        food = request.data.get('food')
        diet = request.data.get('diet')
        result = chatbot.get_result(food,diet)
        return Response({'response':result})
