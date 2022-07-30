import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
levis = cv2.CascadeClassifier("renklicakmak.xml")
camera = cv2.VideoCapture(0)
cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://chtdrone-default-rtdb.firebaseio.com'

})

while True:
    kontrol,cerceve = camera.read()
    gri = cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    sonuc = levis.detectMultiScale(gri,1.1,4)
    for (x,y,genislik,yukseklik) in sonuc:
        cv2.putText(cerceve,"Fire",(x,y),cv2.FONT_ITALIC,1,(255,0,0),2)
        cv2.rectangle(cerceve,(x,y),(x+genislik,y+yukseklik),(255,0,0),2)
        ref = db.reference('/')
        ref.set({

            'Fire':
                {
                    'Danger': {
                        'Warning': '1'


                    }

                }

        })
    ref = db.reference('/')
    ref.set({

        'Not Fire':
            {
                'Not Danger': {
                    'Warning': '0'

                }

            }

    })

    if cv2.waitKey(10) == 27:
        break
    cv2.imshow("Tespit",cerceve)