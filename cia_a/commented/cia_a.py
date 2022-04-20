import requests # requests library needed to make basic CRUD(create, read, update, delete ) requests
from time import perf_counter # counter needed to time the application

total_bytes = 0        #reference of total bytes downloaded
timer_start = perf_counter()  #begin timer



def download_flags(flag_name): #function declaration named download_flags and accepting flag_name as a parameter
    global total_bytes #making total bytes available to a function with the 'global' keyword
    local_req = requests.get(f"https://sciencekids.co.nz/images/pictures/flags680/{flag_name}.jpg") #request to get the image using HTTP verb GET
    total_bytes = total_bytes + len(local_req.content) # retrieving total bytes, then reassigning it to be itself plus the length of the requests content. len() returns the length of a string or list as an int. could also use total_bytes += len(local_req.content)
    if local_req.status_code == 200:  #if statement to check if the status code of the request is equal to 200, or in other words, successful
        with open(f"./flag_images/{flag_name}.jpg", 'wb') as f: # with statement to open the flag_images folder, with permissions set to write binary (wb), create a file named '{flag_name}.jpg', where flag_name is equal to the string supplied to parameter flag_name
            f.write(local_req.content) #write the downloaded jpg to the file


with open("flag_names.txt", "r") as flag_names: # with statement to open flag_names.txt with read permissions (r) and assign it an alias of flag_names
    for flag_name in flag_names: # for loop to loop over all of the imported lines within flag_names
        flag_name = flag_name.strip() #strip the whitespace from the flag_name string currently being handled in the loop
        if flag_name != "": #check to make sure that flag_name does not equal an empty string
            download_flags(flag_name) #call the download_flags function and supply the string flag_name as a parameter



  

with open("cia_a_output.txt", "w") as output_a: #opens output text file with write permissions (w) and assigns it an alias of output_a
    #the three quotation form of a string in python is known as a Heredoc, and I use it here. However you could just do individual strings with an escape operator (\)
    #the following code writes our elapsed time and total bytes downloaded to the opened file
    output_a.write(f"""
    Elapsed Time: {perf_counter()}      
    {total_bytes} bytes downloaded
    """)

    
    