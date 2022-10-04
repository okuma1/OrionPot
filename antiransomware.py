import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
from datetime import date, datetime
from psutil import *
from sklearn import tree

data = date.today()
data = datetime.now()
data = data.strftime('%d/%m/%Y %H:%M')
import numpy as np

processos = []
processos2 = []
pid_process = []
pid_process2 = []


class eventoshandler(FileSystemEventHandler):
        def on_modified(self, event):
            print("{} - Arquivo modificado".format(data))
            for newprocess in process_iter(['pid', 'name', 'username']):
                processos2.append(newprocess) 

                if newprocess not in processos:
                    #print(newprocess)
                    newprocess.kill()

while True: 
    for process in process_iter(['pid', 'name', 'username']):
        processos.append(process)
        pid = pids()

        #print(data)
    for ids in pid:
        pids = pid_exists(ids)
        pid_process.append(ids)
    print(pid_process2)

    eventos = eventoshandler
   
    break
path = "/home"
event_handler = eventoshandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
