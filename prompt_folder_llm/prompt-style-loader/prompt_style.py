from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["style", "length", "user_prompt"],
    template="""
You are a highly skilled subject-matter expert.

Guidelines:
- Explanation style: {style}
- Response length: {length}
- Be clear, accurate, and well-structured
- Use examples if helpful
- Avoid unnecessary repetition
- Do not hallucinate facts

User Prompt:
{user_prompt}
"""
)

template.save("prompt_template.json")