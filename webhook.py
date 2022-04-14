from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    '''
    Listens for webhook
    '''
    if request.method == 'POST':
        data = request.json
        print(data)

        gateway_id = data['uplink_message']['rx_metadata'][0]['gateway_ids']['gateway_id']
        gateway_eui = data['uplink_message']['rx_metadata'][0]['gateway_ids']['eui']
        time = data['received_at']
        temperature = data['uplink_message']['decoded_payload']['temperature']

        print('--------------------------------------')
        print('Gateway ID: ' + gateway_id)
        print('Gateway EUI: ' + gateway_eui)
        print('Time: ' + time)
        print('Temperature: ' + str(temperature))

        if temperature <= 15:
            print('It is cold')
        elif temperature > 15.1 and temperature < 20:
            print('It is warm')
        else:
            print('It is hot')

        print('--------------------------------------')

        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
