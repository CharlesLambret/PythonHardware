import network
import urequests
import utime
import ujson
from machine import Pin, PWM

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'IIM_Private'
password = 'Creatvive_Lab_2023'
wlan.connect(ssid, password)
url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/"

arrayPin = [20,21, 22]

ledB = PWM(Pin(arrayPin[0], mode=Pin.OUT)) 
ledG = PWM(Pin(arrayPin[1], mode=Pin.OUT)) 
ledR = PWM(Pin(arrayPin[2], mode=Pin.OUT)) 

ledB.freq(1_000) 
ledG.freq(1_000)
ledR.freq(1_000)

while not wlan.isconnected():
    print('connecting...')
    utime.sleep(1)

print('connected')

endLoop = False

types_colors = {
        "Normal": (255, 255, 255), # Blanc
        "Feu": (255, 0, 0), # Rouge
        "Eau": (0, 0, 255), # Bleu
        "Plante": (0, 255, 0), # Vert
        "Insecte": (139, 69, 19), # Marron
        "Vol": (255, 255, 255), # Blanc
        "Électrik": (255, 255, 0), # Jaune
        "Sol": (255, 165, 0), # Orange
        "Roche": (128, 128, 128), # Gris foncé
        "Combat": (139, 0, 0), # Rouge foncé
        "Psy": (128, 0, 128), # Violet
        "Spectre": (128, 0, 128), # Violet foncé
        "Glace": (255, 255, 255), # Blanc
        "Dragon": (75, 0, 130), # Violet foncé
        "Ténèbres": (0, 0, 0), # Noir
        "Acier": (192, 192, 192), # Gris métallique
        "Fée": (255, 0, 255) # Rose
    }






print("Entrez un nom de Pokémon") # Demande le nom du pokemon
url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/" + input() # Création de l'url avec le nom du pokemon
    
    
try:
        print("GET") 
        response = urequests.get(url) # On récupère les données de l'API
        data = response.json() # On récupère les données de l'API sous forme de dictionnaire
        types = data["types"] # On récupère les types du pokemon
        type = types[0]["name"] # On récupère le premier type du pokemon
        print(type) # On affiche le type du pokemon
        color = types_colors.get(type, (0, 0, 0)) # On récupère la couleur du type du pokemon dans le dictionnaire 
        ledR.freq(1000) # Fréquence de 1 kHz 
        ledG.freq(1000) # Fréquence de 1 kHz 
        ledB.freq(1000) # Fréquence de 1 kHz 
        ledR.duty_u16(color[0] * 256) # Rouge
        ledG.duty_u16(color[1] * 256) # Vert
        ledB.duty_u16(color[2] * 256) # Bleu
        response.close() # On ferme la connexion
        utime.sleep(0.5) # On attend 0.5 secondes
        endLoop = True # On passe la variable endLoop à True
except:
        print("Error")
        utime.sleep(0.5)


if endLoop :
        print("Entrez un nom de Pokémon")
        url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/"+input()
        endLoop = False
    
