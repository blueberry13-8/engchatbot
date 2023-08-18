import openai

openai.api_key = open('openai_key.txt').read()


def init_message(messages, model='gpt-3.5-turbo'):
    message = [{"role": "system", "content": "You are cyber priest. You must listen to people and do them confession"}]
    messages.append(message)


def get_message(prompt, messages, model='gpt-3.5-turbo'):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(model=model, messages=messages)
    reply = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': reply})
    return reply


messages = []
init_message(messages)
while True:
    request = input('User message: ')
    response = get_message(request, messages)
    print(f'ChatGPT message: {response}')

