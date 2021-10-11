### Question 1 -
# What's the version of pipenv you installed?
# pipenv --version
# Ans: pipenv, version - 2021.5.29

### Question 2 -
# Use Pipenv to install Scikit-Learn version 1.0
# pipenv install scikit-learn==1.0
# What's the first hash for scikit-learn you get in Pipfile.lock?
# Ans. "sha256:121f78d6564000dc5e968394f45aac87981fcaaf2be40cfcd8f07b2baa1e1829"

### Question 3 -
import requests

url = 'http://localhost:9696/predict'

# sample customer details in JSON format -

customer_id = 'xyz-123'
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}

# sending this customer in a POST request to our web service - using post() function:
# To see the body of the response: takes the JSON response and converts it into a Python dictionary -
response = requests.post(url, json=customer).json()

print(response)


# sending a promo if response is churn:
if response['churn'] == True:
 print('sending promo email to %s' % customer_id)
else:
 print('not sending promo email to %s' % customer_id)

# Ans 3: {'churn': False, 'churn_probability': 0.2520966052686487}
# not sending promo email to xyz-123

# Ans 4: {'churn': False, 'churn_probability': 0.4032045646359045}
# not sending promo email to xyz-123

# Ans 5-  docker build -t agrigorev/zoomcamp-model:3.8.12-slim .
#  IMAGE ID - ff46fa3432cb
# sha256:ff46fa3432cb07e9b08160d847c1e1e6e49ba11c40d022685f9675a917d64568


# Ans 6 -
# {'churn': False, 'churn_probability': 0.2455399531372233}
# not sending promo email to xyz-123