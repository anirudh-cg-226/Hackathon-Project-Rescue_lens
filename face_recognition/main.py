import streamlit as st
import requests
from streamlit_lottie import st_lottie
import cv2
# face-recognition imports may fail on systems without build tools (dlib/cffi).
# Try to import and fall back to a degraded mode if unavailable so Streamlit
# can still run for frontend/backend integration and image preview.
FACE_RECOG_AVAILABLE = True
face_import_error = None
try:
    from simple_facerec import SimpleFacerec
except Exception as e:
    FACE_RECOG_AVAILABLE = False
    face_import_error = e
from apicall import add_in_base
from imagesapi import getimages


getimages()
# lottie adder
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




# st.set_page_config(layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)





# sidebar

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title('Face Recognition App to Find Missing People')
st.sidebar.subheader('Parameters')


app_mode = st.sidebar.selectbox('Choose the App mode',
['Detection Mode','Further Process']
)

if app_mode =='Further Process':
    st.markdown("<h1 style='font-family:sans-serif; color:#282c34; font-size: 50px;font-weight:700'>Further Process</h1>",unsafe_allow_html=True)
    st.markdown('Here after detection from the web cam in the detection mode we can get the data related to the missing person with his current location and the time detected in the information section of the website ')
    st.markdown('If you want more information about the missing peoples please visit missing people on the website and click on tracked locations for getting information about missing persons that have been tracked or have been found somewhere through surveillance')
    st.image("assets//navbarscreenshot.PNG")
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 400px;
        margin-left: -400px;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    
else:
    use_webcam = st.sidebar.button('Use Webcam')
    original_title = '<p style="font-family:sans-serif; color:#282c34; font-size: 50px;text-align:center;font-weight:700">Face Recognition App</p>'
    st.markdown(original_title, unsafe_allow_html=True)


    lottie_url = "https://assets10.lottiefiles.com/packages/lf20_2szpas4y.json"
    lottie_face = load_lottieurl(lottie_url)

    if use_webcam == False:
        st_lottie(lottie_face, key='face recognition')
    else:
        if not FACE_RECOG_AVAILABLE:
            st.error("Face-recognition libraries are not installed on this system.\n"
                     "Install dlib/face_recognition (via Conda or MSVC build tools) to enable webcam detection.")
            if face_import_error:
                st.code(str(face_import_error))
            st.markdown("### Available images (preview mode)")
            import os, glob
            imgs = glob.glob(os.path.join("images", "*.*"))
            if len(imgs) == 0:
                st.info("No images found in `./images/`. Start the backend to fetch images or add images manually.")
            else:
                for p in imgs:
                    st.image(p, caption=os.path.basename(p), use_column_width=True)
        else:
            # encode faces from a folder
            FRAME_WINDOW = st.image([])

            # Provide a way to refresh encodings without restarting Streamlit
            try:
                if 'sfr' not in st.session_state:
                    st.session_state.sfr = SimpleFacerec()
                    st.session_state.sfr.load_encoding_images("images/")
            except Exception as e:
                st.error(f"Error initializing face recognizer: {e}")
                st.stop()

            # Sidebar control to refresh images from backend and reload encodings
            if st.sidebar.button('Refresh encodings'):
                getimages()
                st.session_state.sfr = SimpleFacerec()
                st.session_state.sfr.load_encoding_images("images/")
                st.sidebar.success('Encodings refreshed')

            sfr = st.session_state.sfr
            st.sidebar.write(f"Known encodings: {len(sfr.known_face_names)}")

            # load camera
            cap = cv2.VideoCapture(0)

            namesset = set()

            while True:
                ret, frame = cap.read()
                if not ret:
                    st.warning('Failed to read frame from camera.')
                    break

                # detect faces
                face_locations, face_names = sfr.detect_known_faces(frame)
                for face_loc, name in zip(face_locations, face_names):
                    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                    # Different colors for known vs unknown persons
                    if name != "Unknown":
                        # Known person - Blue color
                        color = (0, 0, 200)
                        flag = name in namesset
                        namesset.add(name)
                        if not flag:
                            add_in_base(name)
                            print(f"✅ Registered person detected: {name}")
                    else:
                        # Unknown person - Red color
                        color = (0, 0, 255)
                        print("⚠️  Unknown person detected - Not registered in database")

                    cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, color, 2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 4)

                # Display frame in Streamlit (cv2.imshow doesn't work in Streamlit)
                newframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FRAME_WINDOW.image(newframe)
                key = cv2.waitKey(1)
                if key == 27:
                    break

            cap.release()



