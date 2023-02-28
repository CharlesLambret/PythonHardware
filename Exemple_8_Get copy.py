import network   # import des fonction liées au wifi
import urequests    # import des fonction liées aux requêtes http
import utime    # import des fonction liées au temps
import ujson    # import des fonction liées à la conversion en Json
from machine import Pin, PWM

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'IIM_Private' # nom du réseau wifi
password = 'Creatvive_Lab_2023' # mot de passe du réseau wifi
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/1" # url de la page

arrayPin = [16,17, 18]
blue = PWM(Pin(arrayPin[0], mode=Pin.OUT))
green = PWM(Pin(arrayPin[1], mode=Pin.OUT))
red = PWM(Pin(arrayPin[2], mode=Pin.OUT))

blue.freq(1_000) # freq en hz
green.freq(1_000)
red.freq(1_000)



while not wlan.isconnected(): # tant que la raspi n'est pas connectée au réseau
    print('connecting...') # affiche "connecting..." dans le terminal
    utime.sleep(1) # attend 1 seconde

print('connected') # affiche "connected" dans le terminal

while(True): # boucle infinie
    try:
        print("GET")
        response = urequests.get(url)   # envoie une requête GET à l'url
        data = response.json() # convertit le contenu de la page en json
        types = data["types"] # récupère le contenu de la clé "types" dans le json
        type = types[0]["name"]
        print(type) # affiche le contenu de la page dans le terminal
        response.close() # ferme la connexion
        utime.sleep(0.5) # attend 5 secondes
        if type == "Plante":
            green.duty_u16(12000)

    except:
        print("Error") # affiche "Error" dans le terminal
        utime.sleep(0.5)
