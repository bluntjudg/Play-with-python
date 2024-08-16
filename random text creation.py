#creating random text files from order 1 to 10

import os

# Create a directory to store the text files
directory = "ordered_text_files"
os.makedirs(directory, exist_ok=True)

# Generate and save 10 text files with content from 1 to 10
for i in range(1, 11):
    file_name = f"{directory}/file_{i}.txt"
    
    # Generate content in order from 1 to 10
    content = str(i)
    
    # Write content to the file
    with open(file_name, "w") as file:
        file.write(content)

print("Ordered text files created successfully in the directory:", directory)



#sirs code

import random 

for i in range(1, 11):
    filen=[chr(random.randint(65,91)) for i in range(4)]
    filen="".join(filen)
    data=open(filen+'.txt','w')
    data.write(str(i)+'/n')
    data.close()




