import model

# Verification: If client data wasn't encrypted, will we get the same output?
data = [24, 4, 6, 1]
model_coefficients = model.model_output()
print("Prediction value:", sum([data[i] * model_coefficients[i] for i in range(len(data))]))