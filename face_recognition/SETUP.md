# Face Recognition App - Setup Guide

## ✅ Environment Setup Complete

Your Python environment is ready with all dependencies installed!

### Prerequisites
- Python 3.11 (installed via Homebrew)
- Virtual environment at `.venv311`

### Installed Packages
- ✅ streamlit 1.28.0
- ✅ streamlit-lottie 0.0.5
- ✅ opencv-python 4.11.0
- ✅ face-recognition 1.3.0
- ✅ requests 2.32.5
- ✅ imutils 0.5.4
- ✅ All other dependencies

## 🚀 How to Run

### 1. Activate the virtual environment
```bash
cd /Users/akhleshyadav/Desktop/aa/detect/face_recognition
source .venv311/bin/activate
```

### 2. Run the Streamlit app
```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501` or `http://localhost:8502`

### 3. Deactivate when done
```bash
deactivate
```

## 📡 Backend Server (Optional)

The app tries to connect to a Node.js backend server at `http://localhost:5000` for:
- Fetching missing persons images from database
- Reporting found persons
- Sending WhatsApp notifications

### ⚠️ Backend Not Running?
**No problem!** The app now includes error handling and will:
- Show a warning message in the console
- Continue running using existing images in the `./images/` folder
- Still perform face recognition on those images

### Starting the Backend Server
If you want full functionality (database integration, notifications):

```bash
cd /Users/akhleshyadav/Desktop/aa/Node-js-server-MS
npm install
npm start
```

The server should start on `http://localhost:5000`

## 📁 Project Structure
```
detect/face_recognition/
├── main.py                 # Main Streamlit app
├── simple_facerec.py       # Face recognition logic
├── imagesapi.py           # Fetch images from backend API
├── apicall.py             # Report found persons to backend
├── dateandwhatsapp.py     # WhatsApp notification integration
├── getlocationinfo2.py    # Get current location
├── images_update.py       # Manage image folder
├── images/                # Folder for face recognition images
├── assets/                # UI assets
├── .venv311/             # Virtual environment (don't commit)
└── requirements.txt       # Original package list
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** Make sure you've activated the virtual environment:
```bash
source .venv311/bin/activate
```

### Issue: "Connection refused" error
**Solution:** This is expected if the backend server isn't running. The app will work with existing images.

### Issue: Camera access denied
**Solution:** Grant camera permissions to your terminal/IDE in macOS System Settings > Privacy & Security > Camera

### Issue: No images in ./images/ folder
**Solution:** 
1. Start the Node.js backend server
2. Restart the Streamlit app to fetch images from database
3. Or manually add images to the `./images/` folder (name format: `Name_AdhaarNumber.png`)

## 📝 Notes

- The app uses newer package versions than `requirements.txt` for compatibility with Python 3.11
- Original `requirements.txt` was for Python 3.9/3.10 and had version conflicts
- All core functionality remains the same
- If you need to freeze current dependencies: `pip freeze > requirements-311.txt`

## 🎯 Next Steps

1. **Test the app** without backend:
   ```bash
   source .venv311/bin/activate
   streamlit run main.py
   ```

2. **Set up the backend** (if needed):
   - Navigate to `Node-js-server-MS/`
   - Install dependencies: `npm install`
   - Configure MongoDB connection
   - Start server: `npm start`

3. **Add test images** to `./images/` folder if database is empty

---

**Created:** November 2, 2025  
**Python Version:** 3.11.13  
**Environment:** `.venv311`
