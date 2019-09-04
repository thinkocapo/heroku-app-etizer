import os
from flask import Flask, request, json, abort
from flask_cors import CORS

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://2ba68720d38e42079b243c9c5774e05c@sentry.io/1316515",
    integrations=[FlaskIntegration()],
    release=os.environ.get("VERSION")
)

app = Flask(__name__)
CORS(app)

@app.route('/handled', methods=['GET'])
def handled_exception():
    try:
        '2' + 2
    except Exception as err:
        sentry_sdk.capture_exception(err)
        abort(500)

    return 'Success'

@app.route('/unhandled', methods=['GET'])
def unhandled_exception():
    obj = {}
    obj['keyDoesntExist']

Inventory = {
    'wrench': 1,
    'nails': 1,
    'hammer': 1
}

def process_order(cart):
    global Inventory
    tempInventory = Inventory
    for item in cart:
        if Inventory[item['id']] <= 0:
            raise Exception("Not enough inventory for " + item['id'])
        else:
            tempInventory[item['id']] -= 1
            print 'Success: ' + item['id'] + ' was purchased, remaining stock is ' + str(tempInventory[item['id']])
    Inventory = tempInventory 

@app.before_request
def sentry_event_context():

    if (request.data):
        order = json.loads(request.data)
        with sentry_sdk.configure_scope() as scope:
                scope.user = { "email" : order["email"] }
        
    transactionId = request.headers.get('X-Transaction-ID')
    sessionId = request.headers.get('X-Session-ID')
    global Inventory

    with sentry_sdk.configure_scope() as scope:
        scope.set_tag("transaction_id", transactionId)
        scope.set_tag("session-id", sessionId)
        scope.set_extra("inventory", Inventory)

@app.route('/checkout', methods=['POST'])
def checkout():

    order = json.loads(request.data)
    print "Processing order for: " + order["email"]
    cart = order["cart"]
    
    process_order(cart)

    return 'Success'