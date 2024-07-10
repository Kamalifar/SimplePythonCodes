import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    hashes=dict()
    for i in range(0,10000):
        hashes[hashlib.sha256((str(i).zfill(4)).encode('utf-8')).hexdigest()]=str(i).zfill(4)
    
    outputFile = open(output_file_name,"w")
    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            outputFile.write(str(row[0])+","+str(hashes.get(row[1]))+"\n")
    outputFile.close()


hash_password_hack("input.csv","output.txt")