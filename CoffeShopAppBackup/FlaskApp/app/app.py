import boto3 as sdk
from flask import Flask, render_template,request,jsonify
from dotenv import load_dotenv
import os
#########################################
# DYNAMO DB CONNECTION AND CONFIGURATION#
#########################################

# we load the environment variables
load_dotenv()

# then we access and instantiate them
aws_id = os.getenv('ID')
aws_key = os.getenv('ACCESS_KEY')
aws_region = os.getenv('REGION')

# Now we can open a session four our connection
session = sdk.Session(
    aws_access_key_id=aws_id,
    aws_secret_access_key=aws_key,
    region_name=aws_region
)

# Then we configure our client
client = session.client('dynamodb', 
                        endpoint_url=f'https://dynamodb.{aws_region}.amazonaws.com')



#######################
#   FLASK API CONFIG  #
#######################
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/update_button_active', methods=['POST'])
def update_button_active():
    data = request.get_json()
    bActive = data.get('bActive')
    print(jsonify({"content":bActive,"value":bActive}))
    return jsonify({"htmlFlag": bActive})

# DRINKS ENDPOINTS
@app.route('/')
def getDrinks():
    # this retrieves a json
    request_drinks = client.scan(TableName='drinks')
    # this converts the request in a list of dictionaries, removing the
    # unnecessary information given by the json
    response_drinks = request_drinks['Items']
    # now we can access its elements, the last S is the type of the value S=string
    # and it is something added by dynamoDB automaticaly
    first_item = response_drinks[0]["name"]["S"]
    return render_template("index.html",
                           htmlCheckDrinks=first_item)


# # FOODS ENDPOINTS
# @app.route('/getFoods')
# def getFoods():
#     response = client.scan(TableName='foods')
#     return response['Items']


# # BOOKS ENDPOINTS
# @app.route('/getBooks')
# def getBooks():
#     response = client.scan(TableName='books')
#     return response['Items']


@app.route("/employee")
def employee():
    emplo_greeting = "Hey you are on the employee's page"

    return render_template("employee.html",
                           htmlEmploGreeting=emplo_greeting)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

