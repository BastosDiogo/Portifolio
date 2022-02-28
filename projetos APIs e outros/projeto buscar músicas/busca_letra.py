import requests
import time

artist = input('Digite o nome do Artista desejado:\nArtista: ')
artist = artist.title()
song = input('Digite o nome da Música desejado:\nMúsica: ')

# Exemplo de variáveis
# artist = "Fleetwood Mac"
# song   = "dreams"

sufixo = 'key={key}'
restante = f'art={artist}&mus={song}&api'

string = restante+sufixo # <------ Devolve = art=U2&mus=one&apikey={key}

api = requests.get(f'https://api.vagalume.com.br/search.php?{string}')
api = api.json()
nome_artista = api['art']['name']
nome_musica = api['mus'][0]['name']
fonte = api['art']['url']
letra = api['mus'][0]['text']
letra = str(letra).rsplit('\n')
print('Música: ',f'{nome_musica}'.upper(),f'\nArtista: {nome_artista}\n'.title(),sep='')
print(letra)
print(api)

for linha in range(0, len(letra)):
    time.sleep(1)
    print(letra[linha])
