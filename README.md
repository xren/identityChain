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
-F "image_url=https://specials-images.forbesimg.com/imageserve/59d657a9a7ea436b47b37bfc/416x416.jpg?background=000000&cropX1=1277&cropX2=3651&cropY1=1191&cropY2=3565"

# add face
curl -X POST "https://api-us.faceplusplus.com/facepp/v3/faceset/addface" \
-F "api_key=J2WKF74Tb9d2ilM0PZDG6TQCiYulVbdW" \
-F "api_secret=ewUvvuO8yanG9fTb2HI9PzKPNNi92Amu" \
-F "faceset_token=d73b8dff7aceb173137627124d8eba21" \
-F "face_tokens=57d2cf41e7d89ac379923285bb2e877b"


# search
curl -X POST "https://api-us.faceplusplus.com/facepp/v3/search" \
-F "api_key=J2WKF74Tb9d2ilM0PZDG6TQCiYulVbdW" \
-F "api_secret=ewUvvuO8yanG9fTb2HI9PzKPNNi92Amu" \
-F "face_token=3c8639996c852697b9c5996cb5e7b9c3" \
-F "faceset_token=d73b8dff7aceb173137627124d8eba21"
