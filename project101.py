import dropbox
import os
class TransferData:
    def _init_(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'dc9204w5c84meo0'
    transferData = TransferData(access_token)

    for root, dirs, files in os.walk(file_from):
        relative_path = os.path.replath(local_path,file_from)
        dropbox_path = os.path.join(file_to, relevant_path)
    file_from = input("Enter the path to transfer:- ")
    file_to = input("enter the full path to upload to dropbox:- ")

    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(),dropbox_path, mode = WriteMode('overwrite'))

