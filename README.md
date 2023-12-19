
# Measure Lambda function

This AWS Lambda function is designed to predict the size of parts of body based on height and weight.

### Endpoints

**Base URL**: `https://[endpoint].[region].amazonaws.com/v1`

**URL**: `/measure`

**Method**: `POST`

**Authentication**: All requests to the API must include the `x-api-key` header with a valid API key.

**Parameters**:
| Name  | Type | Description | Allowed values | 
| ------------- | ------------- | ------------- | ------------- |
| `gender`  | `string`  | gender of the target t he individual | `["male", "female"]` |
| `part`  | `string`  | indicate which part of the body needs to be predicted | `["chest", "waist", "hip", "thigh", "ankle", "arm", "outseam",]` |
| `weight`  | `float`  |weight of the individual in kilogram| |
| `height`  | `float`  |height of the individual in centimeter | |



The Lambda function is triggered by a URL with the following structure:

`https://[endpoint].on.aws/?height=[height]&weight=[weight]&gender=[gender]&part=[part]`


**Note:** Parameters are case-sensitive. Ensure correct casing when providing values for parameters.

*Example* : 

`curl -X POST -H "x-api-key: {INSERT_YOUR_KEY}" "https://[endpoint].[region].amazonaws.com/v1/measure?height=179&weight=84&gender=male&part=waist"`

`curl -X POST -H "x-api-key: {INSERT_YOUR_KEY}" "https://[endpoint].[region].amazonaws.com/v1/measure?height=155&weight=59&gender=female&part=chest"`

`curl -X POST -H "x-api-key: {INSERT_YOUR_KEY}" "https://[endpoint].[region].amazonaws.com/v1/measure?height=161.9&weight=62.3&gender=female&part=chest"`

### Returned Object

The Lambda function returns an object with the following structure:

```json
{
  "result": {
    "prediction": 69.38572669366266
  }
}
```


