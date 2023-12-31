import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda"
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class MeasureupAwsStack extends cdk.Stack {
	constructor(scope: Construct, id: string, props?: cdk.StackProps) {
		super(scope, id, props);
		const dockerFunc = new lambda.DockerImageFunction(this, "DockerFunc", {
			code: lambda.DockerImageCode.fromImageAsset("./image"),
			memorySize: 256,
			timeout: cdk.Duration.seconds(10),
			// architecture: lambda.Architecture.ARM_64,
		})

		const functionUrl = dockerFunc.addFunctionUrl({
			authType: lambda.FunctionUrlAuthType.NONE,
			cors: {
				allowedMethods: [lambda.HttpMethod.ALL],
				allowedHeaders: ["*"],
				allowedOrigins: ["*"],
			}
		})

		new cdk.CfnOutput(this, "FunctionURLValue", {
			value: functionUrl.url,
		})
	}
}
