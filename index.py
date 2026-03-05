from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def perguntador(pergunta):
    client = genai.Client(api_key=GEMINI_API_KEY)

    resposta = client.models.generate_content(
        model="gemini-2.5-flash",

        config=types.GenerateContentConfig(
            system_instruction="Você é uma máquina de averiguar resenha, averigue essa resenha resenha passada pelo usuário com as seguintes mensagens"
        " (como um booleano): RESENHA DEMAIS e poucas linhas explicando o motivo, NÃO É RESENHA e poucas linhas explicando o motivo do porque não é resenha." \
        "lembre-se de que você precisa ser mais aberto ao esotérico, ao que não faz muito sentido. Você precisa ser um coringa" \
        " Isso não significa que você deva aprovar tudo, mas também deve analisar possível resenha funny, não seja muito formal nem descritivo, apenas resenhe também."),

        contents= pergunta
    )
    return print(resposta.text)

def startApp():
    questao_en_questao = input('Qual é a resenha da vez?\n: ')
    return perguntador(questao_en_questao)