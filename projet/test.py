import urequests
import utime
import ujson
from machine import Pin, PWM, I2C
import ssd1306
import usocket as socket


# Configuration de la LED RGB
ledR = PWM(Pin(22, mode=Pin.OUT))
ledG = PWM(Pin(21, mode=Pin.OUT))
ledB = PWM(Pin(20, mode=Pin.OUT))

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

# Configuration de l'écran OLED
i2c = I2C(0, sda=Pin(8), scl=Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configuration du socket
addr = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('En attente de connexions sur le port 3000')

while True:
    conn, addr = s.accept()
    print('Connexion depuis', addr)
    data = conn.recv(1024)
    request = str(data, 'utf8')
    print('Requête :', request)
    pokemon_name = request.split('/')[-1]
    print('Nom du Pokémon :', pokemon_name)
    try:
        response = urequests.get("https://api-pokemon-fr.vercel.app/api/v1/pokemon/" + pokemon_name)
        if response.status_code == 200:
            print("Requête en cours...")
            pokemon_type = response.json()["types"][0]['name']
            oled.fill(0)
            oled.text(pokemon_name, 0, 0)
            oled.text(pokemon_type, 0, 10)
            oled.show()
            color = colors.get(pokemon_type, (0,