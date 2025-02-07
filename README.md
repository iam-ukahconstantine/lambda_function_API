# Number Classifier API

This is a Python-based API that classifies a given number based on its mathematical properties. It is hosted on AWS Lambda and accessible through AWS API Gateway. The API returns the number's classification, prime status, perfect number status, Armstrong status, digit sum, and a fun fact fetched from the Numbers API.

## Table of Contents
- [Technology Stack](#technology-stack)
- [API Endpoint](#api-endpoint)
- [Response Format](#response-format)
- [Installation](#installation)
- [Deployment](#deployment)
- [Usage](#usage)
- [License](#license)

## Technology Stack
- **Programming Language**: Python 3.x
- **Cloud Service**: AWS Lambda, AWS API Gateway
- **External Dependencies**:
  - `requests` (for fetching fun facts from Numbers API)
  
## API Endpoint
The API is publicly accessible through the following endpoint:

```
GET https://{api-gateway-id}.execute-api.{region}.amazonaws.com/api/classify-number?number={number}
```

### Query Parameters
- `number` (required): The number to classify (an integer).

## Response Format

### 200 OK
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### 400 Bad Request (Invalid Input)
```json
{
    "number": "abc",
    "error": true
}
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/iam-ukahconstantine/lambda_function_API.git
   cd number-classifier-api
   ```

2. Install required dependencies:
   - Run the following command to install `requests`:
   ```bash
   pip install requests -t .
   ```

3. Create a zip file containing your Python script and dependencies:
   ```bash
   zip -r lambda_function.zip .
   ```

4. Upload the `.zip` file to AWS Lambda via the AWS Console.
    ```bash
   aws s3 cp lambda_function.zip s3://{your s3 BucketName}/
   ```

## Deployment

### Deploy to AWS Lambda

1. **Create a new AWS Lambda function**.
2. Choose **Python 3.x** as the runtime.
3. Upload the `lambda_function.zip` file to AWS Lambda.
4. Set the **Handler** to `lambda_function.classify_number`.
5. Deploy the function and create a new **API Gateway**.
6. Make sure to configure **CORS** for the API Gateway.

### Enable CORS

If you plan to use this API in a front-end application, enable CORS in API Gateway by adding the following headers:

```json
"Access-Control-Allow-Origin": "*",
"Access-Control-Allow-Headers": "Content-Type"
"Access-Control-Allow-Methods": "Get"
```

### Test the Endpoint

Once the API Gateway is deployed, you can test the Lambda function by providing test events directly in the AWS Console by inputting a sample event like this:
```
{
    "queryStringParameters": {
        "number": "371"
    }
}

```

Also, test it by sending a GET request with a `number` query parameter:
```
GET https://{api-gateway-id}.execute-api.{region}.amazonaws.com/api/classify-number?number={number}
curl "<your-api-url>/api/classify-number?number=371"
curl -X GET "https://{api-gateway-id}.execute-api.{region}.amazonaws.com/api/classify-number?number=371"

```

## Usage

1. Make a `GET` request to the API endpoint.
2. Provide a number as a query parameter, for example:
   ```bash
   GET https://{api-gateway-id}.execute-api.{region}.amazonaws.com/api/classify-number?number=371
   ```
3. The API will return the classification of the number, its mathematical properties, and a fun fact.

