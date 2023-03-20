#encode-decode

import base64

# String to encode
name = input('Enter your name:')

# Convert the string to its byte equivalent using 'ascii'
name_bytes = name.encode("ascii")

# Encode the string bytes using b64encode
base64_bytes = base64.b64encode(name_bytes)

# Decode the encoded b64encode bytes using 'ascii'
base64_string = base64_bytes.decode("ascii")

print(base64_string)