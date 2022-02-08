import requests
import threading

url = 'https://wordscankillpeople.000webhostapp.com/login.php'

test = {'email':'Icreate','password':'devs}
def loop():
    o = requests.post(url, data = test)
    print(o.text)

threads = []
for i in range(50):
        x = threading.Thread(target=loop)
        x.daemon = True
        threads.append(x)
for i in range(50):
                 threads[i].start()
                
for i in range(50):
             threads[i].join()
             