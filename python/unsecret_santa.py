import os
from base64 import b64encode,b64decode
from Crypto.Cipher import AES, PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.PublicKey import RSA
import rsa

# prompt for private rsa key file
print("Ho ho ho! Time to decrypt your secret santa secret message!\n")

def decrypt_key():
	encoded_aes = input("Please paste your encrypted Base64 AES key: ")
	encrypted_aes = b64decode(encoded_aes)
	
	pem_path = input("\nPlease enter the file path to your private RSA key: ")
	
	with open(pem_path, 'r') as file:
		private_rsa = file.read()

	# keyDER = b64decode(private_rsa)
	keyPriv = RSA.importKey(private_rsa)
	cipher = Cipher_PKCS1_v1_5.new(keyPriv)
	
	plain_text = cipher.decrypt(encrypted_aes, None)
	
	print("Your AES key is: " + str(plain_text.decode('utf-8')))

def get_encrypted():
	file_path = input("Please enter the path to your secret message: ")
	
	with open(file_path, 'r') as file:
		encrypted_file = file.read()
	
	return encrypted_file
	
decrypt_key()

# prompt for encrypted aes key

# use private rsa file to decrypt aes key

# use aes key to decrypt message contents


