import json, os
from api_test import User, SizePredictor, model_path_dict

def handler(event, context):
    result = {}
    
    try:
        height = event['queryStringParameters']['height']
        weight = event['queryStringParameters']['weight']
        try:
            height = float(height)
            weight = float(weight)
        except ValueError:
            return jsonify({"error": "'weight' and 'height' must be both be float"}), 400


        gender = str(event['queryStringParameters']['gender'])
        part = str(event['queryStringParameters']['part'])

        user_profile = User(
                _gender=gender,
                _weight=weight,
                _height=height
                )

        predictor = SizePredictor(model_path_dict=model_path_dict)

        if part != "all":
            prediction = predictor.predict(
                    body_part=part, 
                    gender=gender, 
                    user=user_profile
                    )
            result['prediction'] = prediction[0]

        elif part == "all":
            prediction = predictor.predict_all(
                    gender=gender, 
                    user=user_profile
                    )
            result['prediction'] = prediction

        else:
            result['prediction'] = None

    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Missing parameter: {str(e)}'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }


