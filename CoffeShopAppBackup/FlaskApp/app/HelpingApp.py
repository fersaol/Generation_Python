from flask import Flask, render_template, jsonify
#import sys
#import os


# IMPORTANT NOTE:
#Flask es un framework síncrono y no soporta async y await de forma nativa. 
#para utilizar programación asíncrona en una app web de Python debería usar
#un framework que soporte asyncio, como Quart o FastAPI


# This is a way of adding the current path into the system path for retrieving libraries
# Get the current file's directory
#current_file_directory = os.path.dirname(os.path.realpath(__file__))

# Add the current file's directory to the system path
#sys.path.append(current_file_directory)


app = Flask(__name__) # start of the app


bActive = "No option chosen" # we set up a global variable

@app.route('/update_button_active', methods=['POST'])
def update_button_active():
    data = request.get_json()
    global bActive
    bActive = data.get('bActive')
    print(jsonify({'message': 'OK',"content":bActive}), 200)
    return bActive 

@app.route('/',methods=["POST","GET"])  
def customer():

    """
    this is the function to handle the store
    ---------------
    - ARGS:
        - no args
    """

    flag = bActive
    
    #Checks if all the required packages for the software are installed if not
    #it install them:
    skip = True
    if skip:
        packs_feedback = autoPackagesInstaller()
    else:
        packs_feedback = "auto installments skipped"

    # Welcomes the user
    dataGathering = request.form.get("form_first_name")
    to_send_greeting = "Welcome to Python Rangers Cafe, I am very happy to get you here!!!"
    greeting = chatMessage(to_send_greeting)
    name = chatMessage("Enter your name, please")
    first_response = f"{dataGathering} we offer drinks & a selection of delicious foods"
    response = chatMessage(first_response)   
        
    return render_template('index.html',
                           htmlGreeting=greeting,
                           htmlName = name,
                           htmlPackFeedback = packs_feedback,
                           htmlFirstRes = response,
                           htmlFlag=flag)




if __name__ == '__main__': # end of the app
    app.run(debug=True,port=5000) # to activate debug allow to view changes live

