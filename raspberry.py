from machine import Pin, ADC # importe dans le code la librairie qui permet de gréer les Pin de sortie & de réception de signaux analogiques 
import time #importe dans le code la lib qui permet de gérer le temps

adc = ADC(Pin(26, mode=Pin.IN)) # crée un objet adc qui va lire le signal analogique sur le pin 26
adc.atten(ADC.ATTN_11DB) # réglage de la sensibilité de l'adc
adc.width(ADC.WIDTH_12BIT) # réglage de la résolution de l'adc

