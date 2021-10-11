def encode(num, return_type="int"):
    """Return varint for given number"""
    out = []
    while True:
        # get first seven bits of number
        first_seven = num & 0x7f
        num = num >> 7
        if num:
            # there are more bytes, make msb of first seven 1 and continue
            out.append(first_seven | 0x80)
        else:
            # small number, no more bytes left, add first_seven without setting msb, since it is the last byte
            out.append(first_seven)
            break
    if return_type == "hex":
        out = [hex(hex_int)[2:].zfill(2) for hex_int in out]
    return out