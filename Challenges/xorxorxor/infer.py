#!/usr/bin/python3
import os
import binascii

# We know that (plaintext) XOR (cipheredText) = key  

class XOR:

	def encrypt(self, data, key):

		key_length = int((len(hex(key))-2)/2)
		key_bytes = key.to_bytes(key_length, 'big')

		data_length = int((len(hex(data))-2)/2)
		data_bytes = data.to_bytes(data_length, 'big')

		decrypted_data = 0
		for i in range(data_length):
			decrypted_data += (data_bytes[i] ^ (key_bytes[i % key_length])) << 8*(data_length-i-1)

		return decrypted_data


def main():
    
	crypto_handler = XOR()

	plain_text = "HTB{"
	plain_bytes = plain_text.encode("utf-8")
	plain_flag = int(binascii.hexlify(plain_bytes), 16)
	print("Plain string is:", plain_text, "Hex: ", hex(plain_flag))

	key = 0x134af6e1
	print("Key is", hex(key))

	inferred_key = crypto_handler.encrypt(plain_flag, key)
	print("Inferred XOR key is", hex(inferred_key))

########################

	encrypted_data = 0x134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9
	l_payload = int((len(hex(encrypted_data))-2)/2)
	decrypted_flag = crypto_handler.encrypt(encrypted_data, inferred_key)

	print("The flag is", decrypted_flag.to_bytes(l_payload, 'big'))


if __name__ == '__main__':
    main()
