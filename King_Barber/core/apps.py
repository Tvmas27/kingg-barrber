from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
import os
import json
from django.conf import settings

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        if not firebase_admin._apps:
            try:
                # Intentar obtener credenciales de variable de entorno
                firebase_creds = os.getenv('FIREBASE_CREDENTIALS')
                
                if firebase_creds and firebase_creds.startswith('{'):
                    # Si es un JSON string (Producción/Heroku)
                    cred_dict = json.loads(firebase_creds)
                    
                    # FIX: Asegurar que la clave privada tenga los saltos de línea correctos
                    if 'private_key' in cred_dict:
                        cred_dict['private_key'] = cred_dict['private_key'].replace('\\n', '\n')

                    cred = credentials.Certificate(cred_dict)
                    print("Firebase Admin SDK inicializado desde variable de entorno JSON")
                else:
                    # Si es una ruta de archivo (Desarrollo)
                    cred_path = firebase_creds or os.path.join(settings.BASE_DIR.parent, 'serviceAccountKey.json')
                    cred = credentials.Certificate(cred_path)
                    print(f"Firebase Admin SDK inicializado desde archivo: {cred_path}")

                firebase_admin.initialize_app(cred)
            except Exception as e:
                print(f"Error inicializando Firebase: {e}")
