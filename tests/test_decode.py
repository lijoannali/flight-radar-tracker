def_extract_icao(message: bytes) -> str: 
    return message[1:4].hex().upper()

message = bytes.fromhex("8D40621D58C382D690C8AC2863A7")
assert extract_icao(message) = "40621D"
print("Decoded ICAO")