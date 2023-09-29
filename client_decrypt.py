import json
import phe as paillier

def get_encrypted_result():
	# gets encrypted result which is stored in result.json i.e., the encrypted data on which we performed predictions
	# return type is a dictionary
    with open('C:/Users/hp/OneDrive/Desktop/PHE Demo/phe/result.json', 'r') as file: 
        data = json.load(file)
        return data
    
def get_keys():
	"""
	Gets public and private keys stored in keys.json
	returns: public & private keys returned are object of type <class 'phe.paillier.PaillierPublicKey'>, 
	<class 'phe.paillier.PaillierPrivateKey'>.
	Public key has attribute 'n'; private key has attributes 'p', 'q'
	"""
	with open('C:/Users/hp/OneDrive/Desktop/PHE Demo/phe/keys.json', 'r') as file: 
		keys = json.load(file)
		public_key = paillier.PaillierPublicKey(n = int(keys['public_key']['n']))
		private_key = paillier.PaillierPrivateKey(public_key, keys['private_key']['p'], keys['private_key']['q'])
		return public_key, private_key


# 1. After running server.py i.e., server predictions/operations on encrypted data, decrypt it
res = get_encrypted_result()

# encrypted_result_public_key is an object of type <class 'phe.paillier.PaillierPublicKey'>
encrypted_result_public_key = paillier.PaillierPublicKey(n = int(res['public_key']['n']))

# encrypted_result_public_key is an object of type <class 'phe.paillier.EncryptedNumber'>
answer = paillier.EncryptedNumber(encrypted_result_public_key, int(res['values'][0]), int(res['values'][1]))

# 2. Decryption: Decrypting only when we make sure the public_key client has & public_key sent from server is same i.e., -
# unmodified during transit (or) at rest.
public_key, private_key = get_keys()

if (encrypted_result_public_key == public_key):
    print("Decrypted Result:", private_key.decrypt(answer))