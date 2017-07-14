f1= open("my_output.txt", 'r')
f2= open("sample_output.txt", 'r')

lines1 = f1.readlines()
lines2 = f2.readlines()

for i,line in enumerate(lines1):
    if line != lines2[i]:
        print ("",line,lines2[i])









ehdegnmorgafrjxvksc


