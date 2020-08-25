from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

def handler_function(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            inc_label = 1
            if filename != "benjaminlewis":
                new_name = filename
                split_name = filename.split('.')
                file_exists = os.path.isfile((folder_destination + '/' + new_name))
                while file_exists:
                    inc_label += 1
                    new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(inc_label) \
                               + os.path.splitext(folder_to_track + '/' + new_name)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(folder_destination + '/' + new_name)

                src = folder_to_track + "/" + filename
                new_name = folder_destination + "/" + new_name
                os.rename(src, new_name)


folder_to_track = '/Users/benjaminlewis/Desktop'
folder_destination = '/Users/benjaminlewis/Desktop/jamin'
event_handler = handler_function()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()



