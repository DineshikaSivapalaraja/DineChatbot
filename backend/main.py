from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

import db_connection

app = FastAPI()

# @app.get("/")
# async def get():
#     return "Welcome to DineChatbot!"
#
@app.post("/")
async def handle_request(request: Request):
    #retrieve the JSON data from the request
    payload = await request.json()

    #extract the necessary info from the payload
    #based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "track.order - context: ongoing-tracking":
        track_order(parameters)

def track_order(parameters: dict):
    order_id = parameters['order_id']

    #call db--. it will occur in separte file
    order_status = db_connection.get_order_status(order_id)

    if order_status:
        fulfillment_text = f"The order status for order id {order_id} is {order_status}"
    else:
        fulfillment_text = f"No order found with order id: {order_id}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })




