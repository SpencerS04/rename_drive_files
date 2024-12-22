from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "trashed=false"}).GetList()
for file1 in file_list:
  title = file1['title']
  new_title = title.lower().replace(' ', '_').replace('-', '_')
  file1['title'] = new_title
  file1.Upload()