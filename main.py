import configparser
import openai

# Lee la clave de API desde config.properties
config = configparser.ConfigParser()
config.read('config.properties')
openai.api_key = config.get('API', 'api_key')

def transform_number(number, to_binary=True):
    if to_binary:
        return bin(number)[2:]  # Cortamos el prefijo '0b' en la representación binaria
    else:
        return str(int(number, 2))  # Convertimos la cadena binaria a entero y luego a cadena

# Loop principal
while True:
    user_input = input("Ingrese una pregunta o solicitud ('adiós' para salir): ")

    if user_input.lower() == 'adios':
        print("¡Hasta luego!")
        break  # Sale del bucle si el usuario ingresa 'adiós'

    # Ajuste de temperatura
    temperature = 0.7  # Puedes ajustar este valor según tus preferencias

    # Simulación del profesor con el rol 'user'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un profesor que se especializa en números binarios"},
            {"role": "user", "content": user_input}
        ],
        temperature=temperature
    )

    # Imprimir la respuesta del modelo
    print(response['choices'][0]['message']['content'].strip())
