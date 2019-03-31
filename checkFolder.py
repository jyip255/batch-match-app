import os
import requests
from PIL import Image
import pyzbar.pyzbar as pyzbar
import wand.image

def checkFolder(check,temp,error,scanned,nomatch):
    files = [file for file in os.listdir(check) if file[0] != "."]
    for file in files:
        returned = scanQR(check,temp,error,scanned,file)
        if returned[0]:
            handleCall(returned[1],returned[2],nomatch)
    tmpfiles = [file for file in os.listdir(temp) if file[0] != "."]
    for file in tmpfiles:
    	os.remove(temp+file)
    return len(files) > 0

def handleCall(filepath,reqid,nomatch):
    data = {"filepath" : filepath, "reqid" : reqid}
    ret = requests.post(url="http://127.0.0.1:8080/attach", json=data)
    if ret.status_code == 400:
        os.rename(filepath,nomatch+os.path.basename(filepath))

def scanQR(check,temp,error,scanned,filename):
    if allowed_file(filename):
        notypename = filename[:-4]
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            os.rename(check+filename,temp+filename)
            img = wand.image.Image(filename=temp+filename)
            converted = img.convert('pdf')
            converted.save(filename=check+notypename+".pdf")
        if filename.endswith('.pdf'):
            img = wand.image.Image(filename=check+filename)
            converted = img.convert('jpg')
            converted.save(filename=temp+notypename+".jpg")
        imgfilename = temp+notypename+".jpg"
        if pyzbar.decode(Image.open(imgfilename)) != []:
            decodedImg = pyzbar.decode(Image.open(imgfilename))[0].data.decode("utf-8")
            reqId = decodedImg.split('/')[-1]
            os.rename(check+notypename+".pdf",scanned+notypename+".pdf")
            return [True, scanned+notypename+".pdf", reqId]
        else:
            os.rename(check+notypename+".pdf",error+notypename+".pdf")
            return [False]
    else:
        os.rename(check+filename,error+filename)
        return [False]

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in set(['pdf','jpg'])