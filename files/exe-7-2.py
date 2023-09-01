# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:

# X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

import subprocess


def list_dir():
    """List the files in the particular directory"""
    
    subprocess.run(['ls', '-lh', '*.txt'])

def avg_spam_confidence(file_path):
    '''Counting the average of spam confidence'''
    count = 0
    sum = 0
    try:
        fhand = open(file_path)
        for line in fhand:
            if line.startswith("X-DSPAM-Confidence:"):
                data = line.strip()
                colon_pos = data.find(":")
                float_num = float(data[colon_pos+2:])
                # print(float_num)
                count += 1
                sum = sum + float_num
        print(f"Count: {count}, Total: {sum}, Avg: {sum/count}")
    except:
        print(f"The following directory is not listed in your file. \nSigning off......")
        exit()

list_dir()

file_name = input("Choose a file >>> ")
file_path = f"{file_name}.txt"

avg_spam_confidence(file_path)

