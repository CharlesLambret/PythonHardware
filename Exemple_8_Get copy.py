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

if wlan.isconnected():
        print("Appuyez sur une touche pour chercher un Pokemon")
        if input():
            print("Entrez un nom de Pokémon")
            url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/"+input()

while True:
    try:
        print("GET")
        response = urequests.get(url)
        data = response.json()
        types = data["types"]
        type = types[0]["name"]
        print(type)
        response.close()
        utime.sleep(0.5)
        if type == "Plante":
            green.duty_u16(12000)
        if type == "Feu":
            red.duty_u16(12000)
        if type == "Eau":
            blue.duty_u16(12000)
    except:
        print("Error")
        utime.sleep(0.5)

   