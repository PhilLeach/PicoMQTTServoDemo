import uasyncio as asyncio
from mqtt_as import MQTTClient, config
from servo_as import Servo_SG90 as Servo
from secrets import SERVER, SSID, PW

def servo_setup():
    s1 = Servo('Servo1',0,Servo.CENTER)
    s2 = Servo('Servo2',0,Servo.CENTER)
    servos = {'Servo1' : s1, 'Servo2' : s2}
    return servos



def callback(topic, msg, retained):
    message = msg.decode("utf-8").split() 
    print(f'{message[0]} {message[1]}')
    asyncio.create_task(servos[message[0]].move_to_poistion(int(message[1])))

async def conn_han(client):
    await client.subscribe('/PicoMQTTServoDemo/command', 1)

async def main(client, servos):
    await client.connect()
    while True:
        await asyncio.sleep(5)
        print(f"Servo 1 Position: {servos['Servo1'].position}, Servo 2 Position: {servos['Servo2'].position} ")
        await client.publish('/PicoMQTTServoDemo/status', f"Servo 1 Position: {servos['Servo1'].position}, Servo 2 Position: {servos['Servo2'].position} ", qos = 1)
        
config['subs_cb'] = callback
config['connect_coro'] = conn_han
config['server'] = SERVER
config['ssid'] = SSID
config['wifi_pw'] = PW

MQTTClient.DEBUG = True  # type: ignore # Optional: print diagnostic messages
client = MQTTClient(config)
servos = servo_setup()
try:
    asyncio.run(main(client, servos))
finally:
    client.close()  