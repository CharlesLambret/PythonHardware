import network   #import des fonction lier au wifi
import urequests    #import des fonction lier au requetes http
import utime    #import des fonction lier au temps
import ujson    #import des fonction lier aà la convertion en Json
from machine import Pin, PWM, I2C
import ssd1306




# Configuration de la LED RGB
ledR = PWM(Pin(22, mode=Pin.OUT))
ledG = PWM(Pin(21, mode=Pin.OUT))
ledB = PWM(Pin(20, mode=Pin.OUT))


ledR2 = PWM(Pin(18, mode=Pin.OUT))
ledG2 = PWM(Pin(17, mode=Pin.OUT))
ledB2 = PWM(Pin(16, mode=Pin.OUT))



# Dictionnaire des couleurs
colors = {
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

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'IIM_Private'
password = 'Creatvive_Lab_2023'
wlan.connect(ssid, password) # connecte la raspi au réseau

while not wlan.isconnected():
    print("attente de connexion")
    utime.sleep(1)

fronturl = "localhost3000/"
pokemon_name = fronturl.split("/")[-1]

while True :
    
    try:
        response = urequests.get("https://api-pokemon-fr.vercel.app/api/v1/pokemon/" + pokemon_name) # lance une requete sur l'url

        if response.status_code == 200:
            print("requête en cours...")
            print(response.json()["types"][0]['name']) # traite sa reponse en Json
            pokemon_type = response.json()["types"][0]['name']
            pokemon_type2 = response.json()["types"][1]['name']
            texte_encode = pokemon_type.encode('utf-8')
            
            
            # Configuration de l'écran OLED pour afficher le nom du Pokémon
            i2c = I2C(0, sda=Pin(8), scl=Pin(9))
            oled = ssd1306.SSD1306_I2C(128, 64, i2c)
            oled.fill(0)
            oled.text(pokemon_name, 0, 0)
            oled.text(texte_encode, 0, 10)
            oled.text(pokemon_type2, 0, 20)
            
            oled.show()


            color = colors.get(pokemon_type, (0, 0, 0))
            color2 = colors.get(pokemon_type2, (0, 0, 0)) 
            ledR.freq(1000) # Fréquence de 1 kHz 
            ledG.freq(1000) # Fréquence de 1 kHz 
            ledB.freq(1000) # Fréquence de 1 kHz
            ledR2.freq(1000) # Fréquence de 1 kHz 
            ledG2.freq(1000) # Fréquence de 1 kHz 
            ledB2.freq(1000) # Fréquence de 1 kHz 
            ledR.duty_u16(color[0] * 256) # Rouge
            ledG.duty_u16(color[1] * 256) # Vert
            ledB.duty_u16(color[2] * 256) # Bleu
            ledR2.duty_u16(color2[0] * 256) # Rouge
            ledG2.duty_u16(color2[1] * 256) # Vert
            ledB2.duty_u16(color2[2] * 256) # Bleu
            response.close() # ferme la demande
            utime.sleep(1)
    except Exception as e:
        print("pokemon introuvable ou information introuvable" )
        print(e)

