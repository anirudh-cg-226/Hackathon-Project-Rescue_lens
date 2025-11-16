#!/bin/bash
# Script to add a missing person via API

# Example: Add a test person
curl -X POST http://localhost:5000/api/missingpeople/addperson \
  -F "name=Test Person" \
  -F "email=test@example.com" \
  -F "Gender=Male" \
  -F "identification=Scar on left hand" \
  -F "nationality=Indian" \
  -F "height=5.8" \
  -F "datemissing=2024-11-01" \
  -F "address=123 Test Street, Delhi" \
  -F "adhaar_number=123456789012" \
  -F "phonenumber=9876543210" \
  -F "image=@/path/to/photo.jpg"

# Replace /path/to/photo.jpg with actual path to person's photo
echo -e "\n\n✅ Person added! Check: http://localhost:5000/api/missingpeople/getallpersons"
