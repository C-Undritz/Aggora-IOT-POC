import websockets
import asyncio
import json
import datetime
from modules.hex_to_bytes import decoder


async def listen():
    '''
    Function to listen and receive message from a websocket URL
    '''
    url = "wss://eu4pro.loriot.io/app?token=vgEGwgAAABBldTRwcm8ubG9yaW90Lmlv_CRMgdeGghpfxY0ZXJWq9Q=="

    async with websockets.connect(url) as uplink:
        while True:
            data = await uplink.recv()
            json_data = json.loads(data)
            cmd = json_data['cmd']

            if cmd == 'gw':
                gateway_eui = json_data['gws'][0]['gweui']
                sensor_eui = json_data['EUI']
                count = json_data['fcnt']
                time = json_data['gws'][0]['time']
                sensor_data = json_data['data']

                temperature = decoder(sensor_data)["temperature"]
                humidity = decoder(sensor_data)["humidity"]
                uplink_time = time.replace("T", " ").replace("Z", " ")
                recorded_time = datetime.datetime.now()

                print('Gateway ID: ' + gateway_eui)
                print('Sensor ID: ' + sensor_eui)
                print('Uplink Count: ' + str(count))
                print('Uplink Time: ' + str(uplink_time))
                print('temperature: ' + str(temperature))
                print('humidity: ' + str(humidity))
                print('Recorded_time: ' + str(recorded_time))


asyncio.get_event_loop().run_until_complete(listen())
