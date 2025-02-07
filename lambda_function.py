import json
import math
import requests

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum([d**power for d in digits]) == n

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fact available.")
    except:
        return "No fact available."
    
def classify_number(event, context):
    try:
        query_params = event.get("queryStringParameters", {})
        number_str = query_params.get("number", "")

        # Check if the input is a valid number (negative, float or integer)
        try:
            # Try to convert the number to a float (handles both integer and floating-point numbers)
            number = float(number_str)
        except ValueError:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"number": number_str, "error": True})
            }

        # Calculate properties for valid number inputs (including negative and float)
        properties = []
        if is_armstrong(abs(int(number))):  # Only check Armstrong for the absolute value
            properties.append("armstrong")
        
        properties.append("odd" if number % 2 != 0 else "even")

        response_body = {
            "number": number,
            "is_prime": is_prime(int(number)),
            "is_perfect": is_perfect(int(number)),
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(abs(int(number)))),  # Sum digits of the absolute value
            "fun_fact": get_fun_fact(int(number))  # Fun fact for the absolute value
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response_body)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Internal Server Error"})
        }

