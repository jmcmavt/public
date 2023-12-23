import os
from base64 import b64encode,b64decode
from Crypto.Cipher import AES, PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.PublicKey import RSA
import rsa

print("Ho ho ho! Time to decrypt your secret santa secret message!\n") # prompt for private rsa key file

def decrypt_key():
	encoded_aes = input("Please paste your encrypted Base64 AES key: ")
	encrypted_aes = b64decode(encoded_aes)
	
	pem_path = input("\nPlease enter the file path to your private RSA key: ")
	
	with open(pem_path, 'r') as file:
		private_key_file = file.read()

	private_key = RSA.importKey(private_key_file)
	cipher = Cipher_PKCS1_v1_5.new(private_key)
	encoded_key = cipher.decrypt(encrypted_aes, None)
	
	print("Your AES key is: " + str(encoded_key.decode('utf-8')))
	
	return encoded_key

def get_message(key):
	file_path = input("Please enter the path to your secret message: ") # should be the bath to the encrypted file
	file_in = open(file_path, "rb")
	
	nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)] # decryption operation
	cipher = AES.new(key, AES.MODE_EAX, nonce)
	message = cipher.decrypt_and_verify(ciphertext, tag)
	
	print(str(message.decode('utf-8')))	

def main():	
	aes_key = decrypt_key()
	get_message(aes_key)

main()