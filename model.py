import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def model_output():
    # read input from file
    input_data = pd.read_csv('C:/Users/hp/OneDrive/Desktop/PHE Demo/phe/employee_data.csv')
    # dependent variable 'salary' along Y-axis
    y = input_data.salary
    # dropping salary column and using independent variables 'age, healthy_eating, active_lifestyle, Gender' along X-axis
    X = input_data.drop('salary', axis = 1)
    # train the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    reg = LinearRegression().fit(X_train, y_train)
    # return coefficients/weights for age, healthy_eating, active_lifestyle, Gender
    return reg.coef_


print(model_output())