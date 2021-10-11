def decode(arr, input_type = "int"):
    """Takes an array of varint converted numbers, returns original number"""
    if not arr:
        raise ValueError("Could not decode varint, empty values passed")
    decoded_val = 0
    shift = 0
    if input_type == "hex":
        arr = [int(ele,16) for ele in arr]
    for val in arr:
        #remove msb
        decoded_val += (val & 0x7f) << shift
        shift = shift + 7 #next loop value will be shifted left by 7, encode shifts right by 7
    return decoded_val