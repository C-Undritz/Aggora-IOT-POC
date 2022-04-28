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

            cmd = json_data['cmd']

            if (cmd == 'rx'):
                sensor_eui = json_data['EUI']
                count = json_data['fcnt']
                sensor_data = json_data['data']

                print('Sensor ID: ' + sensor_eui)
                print('Uplink Count: ' + str(count))
                print('Data: ' + sensor_data)
                environmental_data = decoder(sensor_data)
                print('Environmental Data: ', environmental_data)


asyncio.get_event_loop().run_until_complete(listen())
