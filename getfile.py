import base64

INPUT = "something.txt"

output_file_path = "output_file.zip"

with open(INPUT, 'r') as code:
    base64_encoded = code.read()

decoded_data = base64.b64decode(base64_encoded)

# Write the binary data to an output file
with open(output_file_path, 'wb') as output_file:
    output_file.write(decoded_data)

print("Binary data decoded and saved as", output_file_path)

print("Finished")
