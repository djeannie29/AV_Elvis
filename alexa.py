#ASSISTENTE VIRTUAL - V 1.0
import speech_recognition as sr
import wikipedia
import pywhatkit
import openai
import pyttsx3

from get_env import print_env

env = print_env(['app_key'])
# configurando o ambiente
openai.api_key = env['app_key']

model_engine = 'text-davinci-003'  # engine

audio = sr.Recognizer()
maquina = pyttsx3.init()# object creation


def listen_command():
    comando = ""
    try:
        with sr.Microphone() as source:
            print ("Escutando...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz,language='pt-br')
            comando =  comando.lower()
            if 'alexa' in comando:
                comando = comando.replace('alexa','')
                maquina.say (comando)
                maquina.runAndWait()
    except Exception as e:
        print(f"Microfone não está ok {e}")
    return comando

def execute_command():
    comando = listen_command()
    if "procure por" in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif "pesquise por" in comando:
        procurar = comando.replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif "toque" in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f"tocando {musica} no youtube")
        maquina.runAndWait()
    elif 'responda' in comando or 'fale sobre' in comando or 'crie' or 'o que você acha sobre' in comando or 'cite in comando':
        prompt = comando.replace('responda', '')
        prompt = comando.replace('fale sobre', '')
        prompt = comando.replace('crie', '')
        prompt = comando.replace('o que você acha sobre', '')
        prompt = comando.replace('cite', '')


        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=100,
            temperature=0.5,
        )
        response = completion.choices[0].text
        print(response)
        maquina.say(response)
        maquina.runAndWait()
    else:
        pass

while True:
    execute_command()
    saida=input("Deseja sair?")
    if saida == 'sim':
        break