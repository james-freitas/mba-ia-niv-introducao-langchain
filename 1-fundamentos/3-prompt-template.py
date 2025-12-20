from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell a joke with my name!"
)

text = template.format(name="James")
print(text)