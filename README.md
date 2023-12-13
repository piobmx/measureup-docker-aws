
# Measure Lambda function

This AWS Lambda function is designed to predict the size of parts of body based on height and weight.

Parameters
1. Gender 
Description: gender of the target t he individual
Type: string
Possible Values: ["male", "female"]

2. part  
Description: indicate which part of the body needs to be predicted
Type: string
Possible Values:
	* chest
	* waist
	* hip
	* thigh
	* ankle
	* arm
	* outseam

3. weight
Description: weight of the individual in kilogram
Type: float 

4. height
Description: height of the individual in centimeter
Type: float


The Lambda function is triggered by a URL with the following structure:

https://[endpoint].on.aws/?height=[height]&weight=[weight]&gender=[gender]&part=[part]
**Note:** Parameters are case-sensitive. Ensure correct casing when providing values for parameters.
*Example* : 
*`https://[endpoint].on.aws/?height=179&weight=84&gender=male&part=arm`
*`https://[endpoint].on.aws/?height=163&weight=63.5&gender=female&part=ankle`

## Returned Object

The Lambda function returns an object with the following structure:

```json
{
  "result": {
    "prediction": 69.38572669366266
  }
}

# Measure Lambda function

This AWS Lambda function is designed to predict the size of parts of body based on height and weight.

Parameters
1. Gender 
Description: gender of the target t he individual
Type: string
Possible Values: ["male", "female"]

2. part  
Description: indicate which part of the body needs to be predicted
Type: string
Possible Values:
	* chest
	* waist
	* hip
	* thigh
	* ankle
	* arm
	* outseam

3. weight
Description: weight of the individual in kilogram
Type: float 

4. height
Description: height of the individual in centimeter
Type: float


The Lambda function is triggered by a URL with the following structure:

https://[endpoint].on.aws/?height=[height]&weight=[weight]&gender=[gender]&part=[part]
**Note:** Parameters are case-sensitive. Ensure correct casing when providing values for parameters.
*Example* : 
*`https://[endpoint].on.aws/?height=179&weight=84&gender=male&part=arm`
*`https://[endpoint].on.aws/?height=163&weight=63.5&gender=female&part=ankle`

## Returned Object

The Lambda function returns an object with the following structure:

```json
{
  "result": {
    "prediction": 69.38572669366266
  }
}
