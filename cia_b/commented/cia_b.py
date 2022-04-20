from multiprocessing import Process, Queue #imports the Process and Queue classes from multiprocessing
from functools import reduce #imports the reduce function to add all of the bytes later on
import requests
from time import perf_counter


q = Queue() #instantiates the Queue class, so we can share data between processes
total_bytes_array = [] 
total_bytes = 0
total_time = 0.0
processes = [] #similar to threads = [] from cia_c.py

timer_start = perf_counter()



def download_flags(flag_name, queue):
    global total_bytes_array
    local_req = requests.get(f"https://sciencekids.co.nz/images/pictures/flags680/{flag_name}.jpg")
    queue.put(len(local_req.content)) #puts the bytes into the shared memory of the Queue
        
    
    if local_req.status_code == 200:
        with open(f"./flag_images/{flag_name}.jpg", 'wb') as f:
            f.write(local_req.content)



with open("flag_names.txt", "r") as flag_names:
    for flag_name in flag_names:
        flag_name = flag_name.strip()
        if flag_name != "" and __name__ == "__main__":
            
            process = Process(target=download_flags, args=(flag_name, q)) # instantiates the Process class, similar to how Threads was instantiated in cia_c.py. Also, the target parameter is set to the name of the function you wish to run, and args is set to the parameter you wish/need to supply to the corresponding function.
            process.start()#begins the process
            processes.append(process) 
            

for process in processes: 
    total_bytes_array.append(q.get()) #calls the get() method within the instantied Queue class to retrieve the bytes we stored, and appends them to total_bytes_array
    process.join() #ends the process


if total_bytes_array != []:
    total_bytes = reduce((lambda x1,x2: x1 + x2), total_bytes_array) # these are somewhat complex operations, of which I cannot explain here. If you wish to delve further, I recommend reviewing the documentation for functools.reduce() and lamba/anonymous functions within python.

with open("cia_b_output.txt", "w") as output:
    output.write(f"""
    Elapsed Time: {perf_counter()}
    {total_bytes} bytes downloaded
    """)