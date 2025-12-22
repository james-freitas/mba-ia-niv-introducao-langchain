from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

question_template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name!"
)

model = ChatOpenAI(temperature=0.5, model_name="gpt-5-mini")

chain = question_template | model

result = chain.invoke({"name": "James"})

print(result.content)