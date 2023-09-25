import openai
from get_env import print_env

env = print_env(['app_key'])
# configurando o ambiente
openai.api_key = env['app_key']

model_engine = 'text-davinci-003'  # engine
while True:
    print(50*'-')
    prompt = input('Escreva algo:')
    print('.')
    print('..')
    print('...')
    print('O ChatGPT está processando sua mensagem!')
    print(50 * '-')
    # gera resposta
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
    )
    response = completion.choices[0].text.strip()
    print(response)

    saida =  input('Você deseja sair do chat?')
    if saida == sim:
        break
