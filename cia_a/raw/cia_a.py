import requests
from time import perf_counter

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
        print(flag_name)
        if flag_name != "":
            download_flags(flag_name)



total_time = perf_counter()   

with open("cia_a_output.txt", "w") as output_a:
    output_a.write(f"""
    Elapsed Time: {total_time}
    {total_bytes} bytes downloaded
    """)

    
    