
# Measure Lambda function

This AWS Lambda function is designed to predict the size of parts of body based on height and weight.

### Parameters


| Name  | Type | Description | Allowed values | 
| ------------- | ------------- | ------------- | ------------- |
| gender  | string  | gender of the target t he individual | ["male", "female"] |
| part  | string  | indicate which part of the body needs to be predicted | ["chest", "waist", "hip", "thigh", "ankle", "arm", "outseam",] |
| weight  | float  |weight of the individual in kilogram| |
| height  | float  |height of the individual in centimeter | |


### Usage 

The Lambda function is triggered by a URL with the following structure:

https://[endpoint].on.aws/?height=[height]&weight=[weight]&gender=[gender]&part=[part]

**Note:** Parameters are case-sensitive. Ensure correct casing when providing values for parameters.

*Example* : 

`curl -XPOST https://[endpoint].on.aws/?height=179&weight=84&gender=male&part=arm`

`curl -XPOST https://[endpoint].on.aws/?height=163&weight=63.5&gender=female&part=ankle`

### Returned Object

The Lambda function returns an object with the following structure:

```json
{
  "result": {
    "prediction": 69.38572669366266
  }
}
```


