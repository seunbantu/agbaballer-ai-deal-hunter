from flight_search import search_flight
from ai_filter import is_good_deal
from whatsapp_alert import send_alert
from config import TARGET_PRICE

ORIGIN = "NYC"
DESTINATION = "LON"

flight = search_flight(ORIGIN, DESTINATION)

if is_good_deal(flight["price"], TARGET_PRICE):
    message = f"""
✈️ AGBABALLER AI ALERT ✈️

{flight['origin']} → {flight['destination']}
Date: {flight['date']}
Airline: {flight['airline']}
Price: ${flight['price']} 🔥

Book fast!
"""
    send_alert(message.strip())
    print("✅ Deal found. WhatsApp alert sent.")
else:
    print("❌ No good deal found yet.")
