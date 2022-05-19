import websockets
import asyncio
import json
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
            print(json_data)
            cmd = json_data['cmd']

            if (cmd == 'gw'):
                sensor_eui = json_data['EUI']
                count = json_data['fcnt']
                sensor_data = json_data['data']
                uplink_time = json_data['gws'][0]['time']
                gateway = json_data['gws'][0]['gweui']

                print('Sensor ID: ' + sensor_eui)
                print('Uplink Count: ' + str(count))
                print('Data: ' + sensor_data)
                environmental_data = decoder(sensor_data)
                print('temperature: ' + str(environmental_data["temperature"]))
                print('humidity: ' + str(environmental_data["humidity"]))
                print('uplink time: ' + str(uplink_time))
                print('Gateway ID: ' + gateway)


asyncio.get_event_loop().run_until_complete(listen())
