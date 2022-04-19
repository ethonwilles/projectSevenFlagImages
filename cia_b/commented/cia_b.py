from multiprocessing import Process, Queue
from functools import reduce
import requests
from time import perf_counter


q = Queue()
total_bytes_array = []
total_bytes = 0
total_time = 0.0
processes = []

timer_start = perf_counter()



def download_flags(flag_name, queue):
    global total_bytes_array
    local_req = requests.get(f"https://sciencekids.co.nz/images/pictures/flags680/{flag_name}.jpg")
    queue.put(len(local_req.content))
        
    
    if local_req.status_code == 200:
        with open(f"./flag_images/{flag_name}.jpg", 'wb') as f:
            f.write(local_req.content)



with open("flag_names.txt", "r") as flag_names:
    for flag_name in flag_names:
        flag_name = flag_name.strip()
        if flag_name != "" and __name__ == "__main__":
            
            process = Process(target=download_flags, args=(flag_name, q))
            process.start()
            processes.append(process)
            

for process in processes:
    total_bytes_array.append(q.get())
    process.join()


if total_bytes_array != []:
    total_bytes = reduce((lambda x1,x2: x1 + x2), total_bytes_array)

with open("cia_b_output.txt", "w") as output:
    output.write(f"""
    Elapsed Time: {perf_counter()}
    {total_bytes} bytes downloaded
    """)