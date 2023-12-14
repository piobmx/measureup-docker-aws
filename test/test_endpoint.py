import requests

API_ENDPOINT = "https://zt3bzz6d525nlp7tw2lq2foq6m0slqvb.lambda-url.eu-central-1.on.aws/"

def test_predict_body_part():
    # Test predicting the size of a body part for a male individual (e.g., arm)
    response = requests.post(API_ENDPOINT, params={'height': 179, 'weight': 84, 'gender': 'male', 'part': 'arm'})
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Parse the response data as JSON
    data = response.json()
    
    # Check if the response has the expected structure
    assert 'result' in data
    assert 'prediction' in data['result']
    
    # Check if the prediction value is a number
    assert isinstance(data['result']['prediction'], (int, float))

def test_predict_body_part_female():
    # Test predicting the size of a body part for a female individual (e.g., ankle)
    response = requests.post(API_ENDPOINT, params={'height': 163, 'weight': 63.5, 'gender': 'female', 'part': 'ankle'})
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Parse the response data as JSON
    data = response.json()
    
    # Check if the response has the expected structure
    assert 'result' in data
    assert 'prediction' in data['result']
    
    # Check if the prediction value is a number
    assert isinstance(data['result']['prediction'], (int, float))

def test_invalid_gender():
    # Test predicting the size of a body part with an invalid gender
    response = requests.post(API_ENDPOINT, params={'height': 163, 'weight': 63.5, 'gender': 'invalid_gender', 'part': 'ankle'})
    
    # Check if the response status code is 400 (Bad Request) or another appropriate error status code
    assert response.status_code == 400

    # Parse the response data as JSON
    data = response.json()

    # Check if the response contains an error message or appropriate error structure
    assert 'error' in data

def test_missing_parameters():
    # Test predicting the size of a body part with missing parameters
    response = requests.post(API_ENDPOINT, params={'height': 163, 'gender': 'female', 'part': 'ankle'})
    
    # Check if the response status code is 400 (Bad Request) or another appropriate error status code
    assert response.status_code == 400

    # Parse the response data as JSON
    data = response.json()

    # Check if the response contains an error message or appropriate error structure
    assert 'error' in data

