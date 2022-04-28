def decoder(data):
    '''
    Decodes the data array into dictionary containing the temperature and
    humidity data.
    '''
    decoded = {}
    j = 0
    while j < len(data):
        channel_id = data[j]
        channel_type = data[j+1]
        j += 2
        # Battery
        if (int(channel_id) == 0x01 and int(channel_type) == 0x75):
            decoded["battery"] = data[j]
            j += 1
        # Temperature
        elif (int(channel_id) == 0x03 and int(channel_type) == 0x67):
            required_slice = slice(j, j+2)
            # required_data = data[required_slice]
            # test_var = readInt16LE(data[required_slice]) / 10
            decoded["temperature"] = readInt16LE(data[required_slice]) / 10
            j += 2
        # Humidity
        elif (int(channel_id) == 0x04 and int(channel_type) == 0x68):
            decoded["humidity"] = data[j] / 2
            j += 1
        else:
            break

    return decoded


def readUInt16LE(gerbil):
    value = (gerbil[1] << 8) + gerbil[0]
    return value & 0xffff


def readInt16LE(hamster):
    ref = readUInt16LE(hamster)
    return ref - 0x10000 if ref > 0x7fff else ref


def hex_to_byte_array(hexdata):
    '''
    Converts hex data to byte array for the decode function. 
    '''
    if len(hexdata) % 2 != 0:
        print("Error: There must be an even number of hex digits to convert to bytes")
    else:
        num_bytes = len(hexdata) / 2
        byte_array = []
        i = 0
        while i < num_bytes:
            hex_value = hexdata[i*2:i*2+2]
            byte = bytes.fromhex(hex_value)
            byte_array.append(byte[0])
            i += 1
        return byte_array


original_data = "0367e00004684b"
final_data = decoder(hex_to_byte_array(original_data))

print(final_data)
print(final_data["temperature"])
print(final_data["humidity"])
