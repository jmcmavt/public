import random
import string
import rsa
from langchain.llms import Ollama
from Crypto.Cipher import AES, PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.PublicKey import RSA
from base64 import b64encode,b64decode

ollama = Ollama(base_url="http://localhost:11434") # this is the default listening port for ollama

def get_participants():
	
	pairs = {}
	more_participants = "y"

	while more_participants == "y":
		get_participant = input("Enter participant name: ")
		pairs[get_participant] = None
		more_participants = input(get_participant + " added to the list! Add another? (y/n): ")
		# add input validation
	
	return pairs
	
def get_public_keys(participant_dict): # send the dict here to associate public key with participant

	print(f"Now, you'll provide the RSA public key for each participant.\n")

	for key in participant_dict:
		rsa_val = input("Please paste the RSA public key for " + key + ": ")
		participant_dict[key] = rsa_val
	
	return participant_dict

def assign_santa(plist):
	
	print("\n🎁🎁 Great, we're going to randomly assign each secret Santa. 🎁🎁\n")

	random.shuffle(plist)
	assignments = {plist[i]: plist[(i + 1) % len(plist)] for i in range(len(plist))}

	print("Mixing cocoa...")
	print("Buying shipping labels...")
	print("Reticulating splines...this may take a minute...\n\n")

	return assignments

def generate_message(assigned):
	
	messages = []
	
	for santa,recipient in assigned.items():
		message = ollama("write a fun and festive holiday message telling " + santa + " that they are the secret santa for " + recipient + " and that they should not spend more than $35 on their secret santa gift, exclusive of shipping")
		messages.append(message)
	
	return messages

def encrypt_message(plist, message):
	
	keys_plain = []
	
	print("\n\nNow encrypting secret messages and writing to files...\n")
	
	for p,m in zip(plist, message):
		
		key_plain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
		key_encoded = bytes(key_plain,'UTF-8')
		message_encoded = bytes(m,'UTF-8')
		
		# print(f"{key_plain} is the AES key for {p}\n") uncomment if you want to know the key, but what's the fun in that
		
		keys_plain.append(key_plain)
		cipher = AES.new(key_encoded, AES.MODE_EAX)
		nonce = cipher.nonce
		ciphertext, tag = cipher.encrypt_and_digest(message_encoded)
		
		filename = f"encrypted_for_{p}.txt"
		file_out = open(filename, "wb")
		[file_out.write(i) for i in (cipher.nonce, tag, ciphertext)]
		file_out.close()
		
		print(f"Secret message encrypted for {p} and written to file!")
	
	print('')
		
	return keys_plain

def encrypt_aes_with_rsa(aes_keys, this_keys_dict):
	
	rsak = list(this_keys_dict.values())
	part = list(this_keys_dict.keys())	
	
	for a,r,p in zip(aes_keys,rsak,part):
		
		keyDER = b64decode(r)
		keyPub = RSA.importKey(keyDER)
		cipher = Cipher_PKCS1_v1_5.new(keyPub)
		cipher_text = cipher.encrypt(a.encode())
		encrypted_aes = b64encode(cipher_text)
	
		print(f"Encrypted AES Key for {p}: {cipher_text}\n")

def main():
	print("\n🎄🎄 Welcome to AI-powered Secret Santa. First, we need to get the names of each Secret Santa participant. 🎄🎄\n")
	participants = get_participants() # get a dict of names of participants for the secret santa
	keys_dict = get_public_keys(participants) # using that dict, get their public keys for the value
	participant_list = list(participants.keys()) # just get the names from the dict and turn them into a list
	assigned_participants = assign_santa(participant_list) # shuffle the participants so each one has a secret santa
	messages_list = generate_message(assigned_participants) # use ollama to generate a message for each participant
	aes_keys_plaintext = encrypt_message(participant_list, messages_list) # get the list of keys in plain text so they can be encrypted
	encrypt_aes_with_rsa(aes_keys_plaintext, keys_dict) # print out the encrypted values of the AES keys

main()
