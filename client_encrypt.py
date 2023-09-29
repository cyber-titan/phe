import phe as paillier
import json

def generate_keys():
	"""
	generates a pair of public and private keys and store it in keys.json
	public_key => <class 'phe.paillier.PaillierPublicKey'>; private_key => <class 'phe.paillier.PaillierPrivateKey'>
	"""
	public_key, private_key = paillier.generate_paillier_keypair()
	keys = {}
	keys['public_key'] = {'n' : public_key.n}
	keys['private_key'] = {'p' : private_key.p, 'q' : private_key.q}
	with open('C:/Users/hp/OneDrive/Desktop/PHE Demo/phe/keys.json', 'w') as file: 
		json.dump(keys, file, indent = 2)

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

def encrypt_data(public_key, data):
	"""
	public & private keys returned are both object of type <class 'phe.paillier.PaillierPublicKey'>.
	public key has attribute 'n'; private key has attributes 'p', 'q'

	Using encrypt() method of public_key, remember it is an object of type <class 'phe.paillier.PaillierPublicKey'>.
	After next line executes, encrypted_list will have 4 objects of type <class 'phe.paillier.PaillierPublicKey'>, which will also
	have an attribute of 'exponent'. Hence, x.exponent in line 43 ;)
	returns a dictionary
	"""
	encrypted_list = [public_key.encrypt(x) for x in data]
	encrypted_data = {}
	# here public_key is an object of type <class 'phe.paillier.PaillierPublicKey'> which has an attribute of 'n'
	encrypted_data['public_key'] = {'n': public_key.n}
	encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_list]
	return encrypted_data

def get_encrypted_result():
	# gets encrypted result which is stored in result.json i.e., the encrypted data on which we performed predictions
	# return type is a dictionary
    with open('C:/Users/hp/OneDrive/Desktop/PHE Demo/phe/result.json', 'r') as file: 
        data = json.load(file)
        return data


# 1. To generate public & private keys. NOTE: EACH TIME NEW KEYS ARE GENERATED.
generate_keys()

# 2. encrypt client or user data
public_key, private_key = get_keys()
# here each element is a column which corresponds to a client's age, healthy_eating, active_lifestyle, Gender respectively.
# for which we will perform prediction after encrypting the data first
user_data = [24, 4, 6, 1]
res = encrypt_data(public_key, user_data)

# 3. store encrypted user or client data into data.json. Remember no operations/predictions are performed yet
with open('C:/Users/hp/OneDrive/Desktop/PHE Demo/phe/data.json', 'w') as file: 
    json.dump(res, file, indent = 2)