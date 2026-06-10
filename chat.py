from openai import OpenAI

client= OpenAI()

response= client.responses.create(
    input= "What means CS50? ",
    model= "gpt-4"
)

print(response.output_text)

