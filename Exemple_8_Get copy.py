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

arrayPin = [16,17, 18]
blue = PWM(Pin(arrayPin[0], mode=Pin.OUT))
green = PWM(Pin(arrayPin[1], mode=Pin.OUT))
red = PWM(Pin(arrayPin[2], mode=Pin.OUT))

blue.freq(1_000)
green.freq(1_000)
red.freq(1_000)

while not wlan.isconnected():
    print('connecting...')
    utime.sleep(1)

print('connected')

endLoop = False

types_colors = {
        "Plante": green,
        "Feu": red,
        "Eau": blue
    }

while True:
    print("Entrez un nom de Pokémon")
    url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/" + input()
    
    for color in types_colors.values():
        color.freq(200)
        color.duty_u16(0)

    
    try:
        print("GET")
        response = urequests.get(url)
        data = response.json()
        types = data["types"]
        type = types[0]["name"]
        print(type)
        if type in types_colors:
            types_colors[type].duty_u16(12000)

        response.close()
        utime.sleep(0.5)
        endLoop = True
    except:
        print("Error")
        utime.sleep(0.5)


    if endLoop :
        print("Entrez un nom de Pokémon")
        url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/"+input()
        endLoop = False
    
