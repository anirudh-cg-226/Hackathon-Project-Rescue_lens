
import requests
from dateandwhatsapp import sendmessage
from telegram_notification import send_telegram_message, send_telegram_location
from getlocationinfo2 import getlocation

mylocation=getlocation()

# code to add data of the missing person to the data base using the node js API manually developed


#since name of the missing person can be same for many like shivam,ramesh in India ,hence data using adhaar card number after the name in form   (name_adhaarcardnumber) data has been split and added to data base 


def add_in_base(a):
    idx=0
    actual_name=""
    adhaar=""
    for i in range(len(a)-1, 0-1, -1):
        if(a[i]=='_'):
            idx=i
            break
    
    for i in range(0,idx):
        actual_name+=a[i]
    
    for i in range(idx+1,len(a)):
        adhaar+=a[i]

    # print(adhaar)
    # print(actual_name)

    dataval={
        "name":actual_name,
        "adhaar":adhaar,
        "locationval":mylocation
        }
    

    # headers={'Content-Type':'application/json'}
    # print(dataval)
    try:
        r= requests.post(url="http://localhost:5000/api/foundlocation/addlocation",json=dataval, timeout=5)
        r.raise_for_status()
        print(r.text)

        newr=requests.get(url=f"http://localhost:5000/api/missingpeople/getallpersons/{adhaar}", timeout=5)
        newr.raise_for_status()
        # print(newr.text['phonenumber'])
        newrdata=newr.json()
        phone = newrdata[0]['phonenumber']
        print(f"📞 Phone number: {phone}")
        
        # Send WhatsApp notification
        sendmessage(phone, actual_name, adhaar, mylocation)
        
        # Send Telegram notification (with location pin)
        send_telegram_location(phone, actual_name, adhaar, mylocation)
        
        print(f"✅ Successfully reported {actual_name} found at {mylocation}")
        print("📱 Notifications sent via WhatsApp and Telegram")
    except requests.exceptions.ConnectionError:
        print(f"⚠️  Warning: Could not report found person to backend server.")
        print(f"   Person detected: {actual_name} (Adhaar: {adhaar})")
        print(f"   Location: {mylocation}")
        print(f"   Backend server at localhost:5000 is not running.")
    except requests.exceptions.Timeout:
        print(f"⚠️  Warning: Backend server timed out while reporting found person.")
        print(f"   Person detected: {actual_name} (Adhaar: {adhaar})")
    except Exception as e:
        print(f"⚠️  Warning: Error reporting to backend: {e}")
        print(f"   Person detected: {actual_name} (Adhaar: {adhaar})")


