PROJECT_ID = 'mantanz-blog-2a3a8'

IS_EXTERNAL_PLATFORM = True # False if using Cloud Functions

firebase_app = None

def init_firebase():
    global firebase_app
    if firebase_app:
        return firebase_app

    import firebase_admin
    from firebase_admin import credentials

    if IS_EXTERNAL_PLATFORM:
        cred = credentials.Certificate('/Users/mantanz/Downloads/git_rep/domhain/key.json')
    else:
        cred = credentials.ApplicationDefault()

    firebase_app = firebase_admin.initialize_app(cred, {
        # 'projectId': PROJECT_ID,
        'storageBucket': f"{PROJECT_ID}.appspot.com"
    })

    return firebase_app

import sys
from firebase_admin import storage

init_firebase()

bucket = storage.bucket()
blob = bucket.blob('covid-19/'+sys.argv[1])

# upload
# blob.upload_from_string('hello world')
# upload via file
blob.upload_from_filename('./data_csv/'+sys.argv[1])

# download
# output = blob.download_as_string()
# download to file
# blob.download_to_filename('/Users/mantanz/Downloads/output_new.csv')
