
import requests

# Telegram Bot Integration
# To get your bot token: Message @BotFather on Telegram and create a new bot
# To get chat_id: Message your bot, then visit: https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates

def send_telegram_message(phone_number, name, adhaar, location):
    """
    Send notification via Telegram Bot
    
    Args:
        phone_number: Contact phone number (for reference)
        name: Person's name
        adhaar: Aadhaar number
        location: Dictionary with city, region, country, latitude, longitude
    """
    
    # ⚙️ CONFIGURATION - Replace these with your actual values
    BOT_TOKEN = "7825777880:AAFisf8tKl3f47mC7C3dBnMXBcjX2cb0EIM"
    CHAT_ID = "-4838700324"      # Your Telegram chat ID or group ID
    
    # Extract location details
    city = location.get('city', 'Unknown')
    region = location.get('region', 'Unknown')
    country = location.get('country', 'Unknown')
    latitude = location.get('latitude', 'Unknown')
    longitude = location.get('longitude', 'Unknown')
    
    # Format message with better formatting using Telegram markdown
    message = f"""🔍 *Missing Person Found!*

👤 *Name:* {name}
🆔 *Aadhaar:* {adhaar}
📞 *Contact:* +91{phone_number}

📍 *Location Details:*
🌆 City: {city}
🗺️ Region: {region}
🌍 Country: {country}
📌 Coordinates: {latitude}, {longitude}

🔗 [View on Google Maps](https://www.google.com/maps?q={latitude},{longitude})

_Regards, FindOne Team_
"""
    
    # Telegram Bot API endpoint
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    # Payload
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        if result.get("ok"):
            print(f"✅ Telegram notification sent successfully!")
            print(f"   Message ID: {result['result']['message_id']}")
            return True
        else:
            print(f"❌ Telegram API error: {result.get('description', 'Unknown error')}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("⚠️  Warning: Could not connect to Telegram API")
        print("   Check your internet connection")
        return False
    except requests.exceptions.Timeout:
        print("⚠️  Warning: Telegram API request timed out")
        return False
    except Exception as e:
        print(f"⚠️  Error sending Telegram message: {e}")
        return False


def send_telegram_location(phone_number, name, adhaar, location):
    """
    Send location as a Telegram location pin (more interactive)
    
    Args:
        phone_number: Contact phone number
        name: Person's name
        adhaar: Aadhaar number
        location: Dictionary with latitude, longitude
    """
    
    # ⚙️ CONFIGURATION
    BOT_TOKEN = "7825777880:AAFisf8tKl3f47mC7C3dBnMXBcjX2cb0EIM"
    CHAT_ID = "-4838700324"
    
    latitude = location.get('latitude')
    longitude = location.get('longitude')
    
    if not latitude or not longitude:
        print("⚠️  Cannot send location pin: coordinates missing")
        return False
    
    # First send the text message
    send_telegram_message(phone_number, name, adhaar, location)
    
    # Then send location pin
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendLocation"
    
    payload = {
        "chat_id": CHAT_ID,
        "latitude": latitude,
        "longitude": longitude
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        if result.get("ok"):
            print(f"📍 Location pin sent to Telegram!")
            return True
        else:
            print(f"❌ Could not send location pin: {result.get('description')}")
            return False
            
    except Exception as e:
        print(f"⚠️  Error sending location pin: {e}")
        return False
