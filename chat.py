from openai import OpenAI

client= OpenAI()

user_prompt= input("Prompt: ")
sys_prompt= "Solo una oración.a"

response= client.responses.create(
    input= user_prompt,
    instructions= sys_prompt,
    model= "gpt-4"
)

print(response.output_text)

