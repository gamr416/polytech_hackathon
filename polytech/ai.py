from openai import OpenAI


client = OpenAI(
  api_key='KEY-HERE'
)

def call_da_ai_for_word(call):
    
    completion = client.chat.completions.create(
    model='gpt-4o-mini',
    store=True,
    messages=[{'role': 'user', 'content': f'Что такое {call} на сленге. Представь краткий ответ как будто бы из толкового словаря'}]
    )
    return completion.choices[0].message.content


def call_da_ai_for_sentence(call):
    completion = client.chat.completions.create(
    model='gpt-4o-mini',
    store=True,
    messages=[{'role': 'user', 'content': f'Что означает сленговое предложение: {call}.'}]
    )
    return completion.choices[0].message.content



