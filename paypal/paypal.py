import paypalrestsdk
import logging

###################
# # CONFIGURATION #
###################
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AdBEXpTl7isOqzXphRzogdnntjZsXRIZggbMBUk7iQdvhNFsoQe4UNYguPnt4Y86T_u9Kk_PnKCfSx8C",
  "client_secret": "EGwr3k_JvT_tthd-CUX4TQAtvOczlTNfV2Hmbk0Nz1C81vmVceahmCgthEeiqyCbYaMKFOciLIfq8rQN" })

###################
# #CREATE PAYMENT #
###################
payment = paypalrestsdk.Payment({
  "intent": "sale",
  "payer": {
    "payment_method": "credit_card",
    "funding_instruments": [{
      "credit_card": {
        "type": "visa",
        "number": "4417119669820331",
        "expire_month": "11",
        "expire_year": "2018",
        "cvv2": "874",
        "first_name": "Joe",
        "last_name": "Shopper" }}]},
  "transactions": [{
    "item_list": {
      "items": [{
        "name": "item",
        "sku": "item",
        "price": "1.00",
        "currency": "USD",
        "quantity": 1 }]},
    "amount": {
      "total": "1.00",
      "currency": "USD" },
    "description": "This is the payment transaction description." }]})

if payment.create():
  print("Payment created successfully")
else:
  print(payment.error)

#######################
# GET PAYMENT DETAILS #
#######################
# Fetch Payment
payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")

# Get List of Payments
payment_history = paypalrestsdk.Payment.all({"count": 10})
payment_history.payments
