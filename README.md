
# Measure Lambda function
 
This AWS Lambda function is designed to predict the size of parts of body based on height and weight. 

If you want to develop the machine learning model and how to deploy the function to AWS, check [Deployment section](#Deployment-using-AWS-CDK-and-Python-Flask)  

If you just want to use the API, check [Endpoint section](#API-USAGE-GUIDE)





# Deployment using AWS CDK and Python Flask

### Prerequisites

Before deploying the Python API Service, ensure you have the following:

* AWS CLI installed and configured with the necessary permissions (run `aws configure`).
* Docker installed on your local machine.
* AWS CDK installed (`npm install -g aws-cdk`).

### Deployment Steps


1. Clone the Repository to local machine or server:

```bash
git clone https://github.com/your-repo/your-python-api.git
cd measureup-docker-aws
```

2. Develop Python machine learning pipeline

If you want to modify the Python code which is used for prediction, open the `image/` directory and you can find the `lambda_function.py` which handles the main ML project.

In the `image/src/` folder, you can find the models for predicting measurements in the `image/src/male` and `image/src/female` folders. These models are used in the `api_test.py` script and you can feel free to modify the script and add your own models.

3. Build the Docker Image:


The `image/Dockerfile` includes the instructions for turning the ML app into a Docker image. In the `image/` folder, you can run:

```bash
docker build -t  measureup-model:test .
```

To run the Docker image locally, run:

```bash
docker run -p 8080:8080 measureup-model:test
```


3. Create AWS infrascture

To configure the AWS lambda function, go to `lib/` and edit the `measureup_aws-stack.ts` file. In this file you can find how the Docker image function is defined.


4. Deploy using AWS CDK:

Before you deploy, please make sure you have your AWS CLI configured, since you will need that to interact with AWS with your account. To perform this step, you can run `aws sts get-caller-identity`, and you are supposed to get response that includes details about your AWS account. 

And make sure you run the boostrap command: `cdk bootstrap --region [your_region]`. Learn more about [Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)

Since we are using Typescript to work with AWS CDK, make sure you run `npm install` to install npm packages.

Now you can just run to deploy the Lambda function. 
```
cdk deploy
```
It is likely to take several minutes to run this command, after that you will find the URL for the function in the console.


# API USAGE GUIDE

To use this API, you can follow the instructions below. Make sure you obtain a valid api key from the project maintainer.

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

`curl -X POST -H "x-api-key: ${INSERT_YOUR_KEY}" "https://[endpoint].[region].amazonaws.com/v1/measure?height=179&weight=84&gender=male&part=waist"`

`curl -X POST -H "x-api-key: ${INSERT_YOUR_KEY}" "https://[endpoint].[region].amazonaws.com/v1/measure?height=155&weight=59&gender=female&part=chest"`

`curl -X POST -H "x-api-key: ${INSERT_YOUR_KEY}" "https://[endpoint].[region].amazonaws.com/v1/measure?height=161.9&weight=62.3&gender=female&part=chest"`

### Returned Object

The Lambda function returns an object with the following structure:

```json
{
  "result": {
    "prediction": 69.38572669366266
  }
}
```


