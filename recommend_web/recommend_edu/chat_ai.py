import openai
import os

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())

openai.api_key = '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'


def get_completion(question, model="gpt-3.5-turbo", temperature=0.5):

    prompt = f"""
    Format everything as HTML that can be used in a website. 
    Place the description in a <div> element.

    Try to make an answer for a future University student: ```{question}```
    """

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )

    return response.choices[0].message["content"]


def get_bot_response(user_message):
    response = get_completion(user_message, temperature=1)

    return response
