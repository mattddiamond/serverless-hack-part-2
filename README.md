# Serverless Hack-a-thon 
### Solution Part I

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- src - source code for app.py
- events - there are no events. You can ignore.
- tests - there are no tests. You can ignore.
- template.yaml - A template that defines the application's AWS resources. Let's be honest, this is a template.

The application uses several AWS resources, including Lambda functions that calls Textract. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Deploy the sample application - Part I

For the Serverless hack-a-thon, you can deploy this application, which will call an S3 bucket, send a sample license to textract.  Textract will return a JSON object which the applicaiton which will then create key value pairs and return the name and license ID.

First steps, let's clone the repo from Github:
```bash
git clone git@github.com:mattddiamond/serverless-hack-part-1.git
cd serverless-hack-part-1
```
The first command will clone this git repo. To run the second command, you'll need to change directories.

You will need to create a new S3 bucket and copy the file 'washington-drivers-license.jpeg' to the bucket.
To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam local invoke
```


## Next steps
Remember, the CTO asked for this data to persist in a database.  You can add to the app.py now to have it write out the key value pairs (kvs) to a Serverless Database (ala Dynamo). Check out this link for an example of how to code this: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.02-write-data.html


