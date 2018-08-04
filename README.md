Onboarding steps:

1. install dependencies: `pip install -r requirements.txt`
2. run: gunicorn app:app

FACE++
faceset token: d73b8dff7aceb173137627124d8eba21

# create face set
curl -X POST "https://api-us.faceplusplus.com/facepp/v3/faceset/create" \
-F "api_key=J2WKF74Tb9d2ilM0PZDG6TQCiYulVbdW" \
-F "api_secret=ewUvvuO8yanG9fTb2HI9PzKPNNi92Amu"

# detect face and get face_id
curl -X POST "https://api-us.faceplusplus.com/facepp/v3/detect" -F "api_key=J2WKF74Tb9d2ilM0PZDG6TQCiYulVbdW" \
-F "api_secret=ewUvvuO8yanG9fTb2HI9PzKPNNi92Amu" \
-F "image_url=https://s1.ax1x.com/2018/08/04/PBbuAf.png"

# add face
curl -X POST "https://api-us.faceplusplus.com/facepp/v3/faceset/addface" \
-F "api_key=J2WKF74Tb9d2ilM0PZDG6TQCiYulVbdW" \
-F "api_secret=ewUvvuO8yanG9fTb2HI9PzKPNNi92Amu" \
-F "faceset_token=d73b8dff7aceb173137627124d8eba21" \
-F "face_tokens=955908f21856a8ba3af0ac7362143fcb"


# search
curl -X POST "https://api-us.faceplusplus.com/facepp/v3/search" \
-F "api_key=J2WKF74Tb9d2ilM0PZDG6TQCiYulVbdW" \
-F "api_secret=ewUvvuO8yanG9fTb2HI9PzKPNNi92Amu" \
-F "face_token=3c8639996c852697b9c5996cb5e7b9c3" \
-F "faceset_token=d73b8dff7aceb173137627124d8eba21"
