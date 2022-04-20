import threading  #imports the threading library to utilize multithreading
import requests 
from time import perf_counter



threads = [] # creates an empty threads list for use later on
total_bytes = 0
total_time = 0.0
timer_start = perf_counter()



def download_flags(flag_name):
    global total_bytes
    local_req = requests.get(f"https://sciencekids.co.nz/images/pictures/flags680/{flag_name}.jpg")
    total_bytes = total_bytes + len(local_req.content)
    if local_req.status_code == 200:
        with open(f"./flag_images/{flag_name}.jpg", 'wb') as f:
            f.write(local_req.content)



with open("flag_names.txt", "r") as flag_names:
    for flag_name in flag_names:
        flag_name = flag_name.strip()
        if flag_name != "":
            thread = threading.Thread(target=download_flags, args=(flag_name,)) # instantiates the Thread class to create a new Thread
            threads.append(thread) #appends the newly instantiated thread to the threads list, to be closed (or join()) later on
            thread.start() # begins the operation of the thread

for thread in threads: # loops over all of the open threads appended to the threads list, and closes them (or joins them)
    thread.join()

 

with open("cia_c_output.txt", "w") as output:
    output.write(f"""
    Elapsed Time: {perf_counter()}
    {total_bytes} bytes downloaded
    """)