import json
from src import *
height = 183.4
weight = 79
try:
    height = float(height)
    weight = float(weight)
except ValueError:
    print("ERROR!!!")


gender = "male"
part = "arm_model"

user_profile = User(
        _gender=gender,
        _weight=weight,
        _height=height
        )

predictor = SizePredictor(model_path_dict=model_path_dict)
prediction = predictor.predict(
        body_part=part, 
        gender=gender, 
        user=user_profile
        )
print(prediction)
