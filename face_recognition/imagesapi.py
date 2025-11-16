from PIL import Image
from io import BytesIO
import io
import requests
import json
from images_update import makenew


# Using Api to add all photos fron database to folder to use for encoding to match 

def getimages():
  url="http://localhost:5000/api/missingpeople/getallpersons"
  try:
    mydata=requests.get(url, timeout=5)
    mydata.raise_for_status()
    finaldata=mydata.json()
    # delete all previous photos using make new
    makenew()
    for i  in range(0,len(finaldata)):
      fdata = finaldata[i]['image']['data']['data']
      # `fdata` is returned as a list/iterable of integers from the backend.
      # Convert to bytes correctly so PIL can open it.
      newobj = bytes(fdata)

      # the name of image is followed by (name_adhaarnumber) as there amy be multiple people with same adhaar number
      newname=finaldata[i]['name']+'_'+finaldata[i]['adhaar_number']
      img=Image.open(io.BytesIO(newobj))
      img.save("./images/"+newname+".png")
    # print(newname)
  except requests.exceptions.ConnectionError:
    print("⚠️  Warning: Backend server at localhost:5000 is not running.")
    print("   The app will use existing images in the ./images/ folder.")
    print("   To fetch latest images, start the Node.js server first.")
  except requests.exceptions.Timeout:
    print("⚠️  Warning: Backend server timed out.")
    print("   The app will use existing images in the ./images/ folder.")
  except Exception as e:
    print(f"⚠️  Warning: Could not fetch images from backend: {e}")
    print("   The app will use existing images in the ./images/ folder.")

