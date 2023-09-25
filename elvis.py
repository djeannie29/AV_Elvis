import speech_recognition as sr
import wikipedia
import pywhatkit
import openai
import pyttsx3


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
            if 'elvis' in comando:
                comando = comando.replace('elvis','')
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
    else:
        pass

while True:
    execute_command()