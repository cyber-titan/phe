import model
import phe as paillier
import json

def operations_on_encrypted_data(data):
	"""
	predicts salary for our client with data [24, 4, 6, 1] as age, healthy_eating, active_lifestyle, Gender respectively.
	returns results => <class 'phe.paillier.EncryptedNumber'>, public_key => <class 'phe.paillier.PaillierPublicKey'>
	"""
	model_coefficients = model.model_output()
	public_key = data['public_key']
	public_key = paillier.PaillierPublicKey(n = int(public_key['n']))
	enc_nums_rec = [paillier.EncryptedNumber(public_key, int(x[0], int(x[1]))) for x in data['values']]
	results = sum([model_coefficients[i] * enc_nums_rec[i] for i in range(len(enc_nums_rec))])
	return results, public_key

def store_encrypted_result(data):
	"""
	returns dictionary to be stored in result.json
	"""
	results, public_key = operations_on_encrypted_data(data)
	encrypted_data = {}
	encrypted_data['public_key'] = {'n': public_key.n}
	encrypted_data['values'] = (str(results.ciphertext()), results.exponent)
	return encrypted_data


data = {}
# 1. get encrypted user data from data.json
with open('/Users/cyber_titan/Desktop/VS Code/PHE Demo/data.json', 'r') as file: 
	data = json.load(file)

# 2. store encrypted result in result.json after performing prediction on encrypted data. (data is of type 'dict')
result = store_encrypted_result(data)
# result is of type 'dict'
with open('/Users/cyber_titan/Desktop/VS Code/PHE Demo/result.json', 'w') as file: 
	data = json.dump(result, file, indent = 2)

# Verification: If client data wasn't encrypted, will we get the same output? Uncomment below & run to verify.
data = [24, 4, 6, 1]
model_coefficients = model.model_output()
print("Prediction value:", sum([data[i] * model_coefficients[i] for i in range(len(data))]))