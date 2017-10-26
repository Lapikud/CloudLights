# CloudLights
Lights that can be controlled over wifi

## Üldine ülesehitus

Meil on:
* Odavad wifi relee moodulid mille peal jookseb Python
* WebSocket tehnoloogia abil andmevahetus relee moodulite ja veebi vahel
* HTML/JS Frontend valgustite sisse ja välja lülitamiseks


## Riistvara

Kasutusel on ESP8266 mikrokontroller koos relee mooduliga.

ESP8266 on ~1$ maksev mikrokontroller mis sisaldab endas 80MHz RISC CPU-d,
~100Kb RAM-i ja 2.Ghz WiFi riistvara

ESP kivi peal jookseb MicroPython mis on mikrokontrolleritele mõeldud
Python 3 implementatsioon.

ESP peal jookseb väike pythoni script mis ühendub ws://iot.wut.ee/ws/<ID>
aadressile ja hakkab sealt sõnumeid vastu võtma. <ID> asendatakse lambi
identifikaatoriga.

## Frontend

todo
