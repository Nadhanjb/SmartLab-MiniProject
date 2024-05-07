import os
from datetime import datetime

from django.http import HttpResponse

from .models import *
import base64

# from src.dbcon import *



def index():
    return HttpResponse("okk")


def dw(request):
    path = request.GET["p"]
    file_path = "static/" + path
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{path}"'
        return response

def select(request):
    path = request.GET["p"]
    result = screenshot.objects.get(sid=path)

    if result:
        result.delete()
        return HttpResponse("ok")
    else:
        return HttpResponse("na")

def insprocess(request):
    lis = ['System Idle Process', 'System', 'Registry', 'smss.exe', 'wininit.exe', 'services.exe', 'lsass.exe', 'wsc_proxy.exe', 'Memory Compression', 'igfxCUIService.exe', 'AvastSvc.exe', 'aswToolsSvc.exe', 'dasHost.exe', 'spoolsv.exe', 'IntelCpHDCPSvc.exe', 'novapdfs.exe', 'SecurityHealthService.exe']
    sid = request.GET["p"]
    pr = request.GET["pr"]

    if pr not in lis:
        process.objects.filter(sid=sid, process=pr).delete()
        # Process.objects.create(sid=sid, process=pr)
        ob=process()
        ob.SYSTEM=system_table.objects.get(id=sid)
        return HttpResponse("ok")
    return HttpResponse("ok")

def process(request):
    path = request.GET["p"]
    result = command.objects.filter(sid=path)
    res = "#".join([item.process for item in result])

    command.objects.filter(sid=path).delete()
    return HttpResponse(res)

def sd(request):
    path = request.GET["p"]
    result = command.objects.filter(sid=path).first()
    res_str = "#".join(result.process)

    command.objects.filter(sid=path).delete()
    return HttpResponse(res_str)

def rs(request):
    path = request.GET["p"]
    result = command.objects.filter(sid=path).first()
    res_str = "#".join(result.process)

    command.objects.filter(sid=path).delete()
    return HttpResponse(res_str)

def bgp(request):
    path = request.GET["p"]
    result = command.objects.filter(sid=path).first()
    res_str = "#".join(result.process)

    command.objects.filter(sid=path).delete()
    return HttpResponse(res_str)

def up(request):
    fn = request.GET["fn"]
    path = request.GET["p"]
    id = request.GET["id"]

    image_string = path.decode('base64')
    file_path = "static/media/screenshot/" + fn

    with open(file_path, "wb") as fh:
        fh.write(image_string)

    screenshot.objects.filter(sid=id).delete()
    ob=screenshot()
    ob.SYSTEM=system_table.objects.get(id=id)
    ob.scrnsht=fn
    ob.date=datetime.today()
    ob.status='pending'


    return HttpResponse("ok")

def up1(request):
    fn = request.GET["fn"]
    path = request.GET["p"]

    image_string = path.decode('base64')
    file_path = "static/media/capture/" + fn

    with open(file_path, "wb") as fh:
        fh.write(image_string)

    return HttpResponse("ok")








# @app.route('/dw')
# def dw():
#     path=request.args.get("p")
#     return send_from_directory("static", path, as_attachment=True)
#
#
# @app.route('/select')
# def select():
#
#     path=request.args.get("p")
#
#
#     re = selectone("select * from screencaptrequest where sid=%s",path)
#     if re:
#         iud("delete from screencaptrequest where sid=%s",path)
#         return "ok"
#     else:
#         return "na"
#
#
# @app.route('/insprocess')
# def insprocess():
#     lis=['System Idle Process','System','Registry','smss.exe','wininit.exe','services.exe','lsass.exe','wsc_proxy.exe','Memory Compression','igfxCUIService.exe','AvastSvc.exe','aswToolsSvc.exe','dasHost.exe','spoolsv.exe','IntelCpHDCPSvc.exe','novapdfs.exe','SecurityHealthService.exe']
#     sid = request.args.get("p")
#     pr = request.args.get("pr")
#     if pr not in lis:
#
#
#
#         iud("delete from process where sid=%s and `process`=%s",str(sid))
#
#
#         iud("INSERT INTO `process` VALUES(NULL,'"+str(sid)+"',%s)",pr)
#     return "ok"
#
# @app.route('/process')
# def process():
#     path = request.args.get("p")
#
#
#     re = selectall2("SELECT * FROM `command` WHERE `sid`=%s",path)
#     res=[]
#     for i in re:
#         res.append(i['process'])
#     ress= "#".join(res)
#     iud("delete  from command where sid=%s",path)
#     return ress
#
#
#
#
# @app.route('/sd')
# def sd():
#     path = request.args.get("p")
#
#
#     re = selectone("select * from command where sid=%s",path)
#     res=[]
#     for i in re:
#         res.append(i['process'])
#     ress= "#".join(res)
#     iud.delete("delete  from command where sid=%s",path)
#     return ress
#
# @app.route('/rs')
# def rs():
#     path = request.args.get("p")
#
#
#     re = selectone("select * from command where sid=%s",path)
#     res=[]
#     for i in re:
#         res.append(i['process'])
#     ress= "#".join(res)
#     iud("delete  from command where sid=%s",path)
#     return ress
#
#
#
# @app.route('/bgp')
# def bgp():
#     path = request.args.get("p")
#
#
#     re = selectone("select * from command where sid=%s",path)
#     res=[]
#     for i in re:
#         res.append(i['process'])
#     ress= "#".join(res)
#     iud.delete("delete  from command where sid="+str(path))
#     return ress
#
#
#
# @app.route('/up',methods=['post','get'])
# def up():
#
#     fn=request.args.get("fn")
#
#     path=request.args.get("p")
#     id=request.args.get("id")
#
#
#
#     image_string = base64.b64decode(path)
#
#
#     path=r"E:\smart lab web\src\static\screenshot\\"+fn
#     fh = open(path, "wb")
#     fh.write(image_string)
#     fh.close()
#
#     re = selectone("select * from screenshot where sid=%s",str(id))
#     print("INSERT INTO `screenshot` VALUES(NULL,%s,'"+str(id)+"',now(),'pending')",fn)
#
#     iud("INSERT INTO `screenshot` VALUES(NULL,%s,'"+str(id)+"',now(),'pending')",fn)
#
#     return "ok"
#
#
#
# @app.route('/up1',methods=['post','get'])
# def up1():
#
#     fn=request.args.get("fn")
#
#     path=request.args.get("p")
#
#
#
#     image_string = base64.b64decode(path)
#
#     path=r"E:\smart lab web\src\static\capture\\"+fn
#     fh = open(path, "wb")
#     fh.write(image_string)
#     fh.close()
#
#     return "ok"





app.run(debug=True,port=5001,host="0.0.0.0")