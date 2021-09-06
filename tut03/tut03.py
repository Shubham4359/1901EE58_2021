import os.path

def output_by_subject(tittle, heading_coloumns):
    path=r"C:\Users\DELL\Desktop\tut03solution\output_by_subject\\"        #setting the path
    topic=tittle[3]                    #  storing the topic of the file
    new_heading=heading_coloumn[0]+','+heading_coloumn[1]+','+heading_coloumn[3]+','+heading_coloumn[8]     #creating heading row to be pushed onto an empty file
    content_new_row=tittle[0]+','+tittle[1]+','+tittle[3]+','+tittle[8]     #creating new row to be pushed onto an empty file
    if os.path.exists(path+'%s.csv' %topic) == False:     # If file  already exists then appending only content otherwise
        with open(path+'%s.csv' %topic, 'a') as f:
            f.write(new_heading)                                #insert heading row
            f.write(content_new_row)                                #insert new row
    else :
        with open(path+'%s.csv' %topic, 'a') as f:
            f.write(content_new_row)                                #insert new row    
    return

def output_individual_roll(tittle, heading_coloumns):
    path=r"C:\Users\DELL\Desktop\tut03solution\output_individual_roll\\"                      #setting path
    topic=tittle[0]                    #  storing the name of the file
    new_heading=heading_coloumn[0]+','+heading_coloumn[1]+','+heading_coloumn[3]+','+heading_coloumn[8]     #creating heading row to be pushed onto an empty file
    content_new_row=tittle[0]+','+tittle[1]+','+tittle[3]+','+tittle[8]       #creating new row to be pushed onto an empty file
    if os.path.exists(path+'%s.csv' %topic) == False:                # If file  already exists then appending only content otherwise
        with open(path+'%s.csv' %topic, 'a') as f:
            f.write(new_heading)                                     #inserting heading row
            f.write(content_new_row)                                 #inserting content in it
    else :
        with open(path+'%s.csv' %topic, 'a') as f:
            f.write(content_new_row)                                 #inserting content
    return

f=open(r"C:\Users\DELL\Desktop\tut03solution\regtable_old.csv","r")     #opening dataset file
first_line = f.readline()                          #reading the 1st line(/the heading coloumns) of the dataset
new_heading_coloumns=first_line.split(',')         #spliting wrt comma and creating a list of heading coloumns
for line in f:
    changed_line=line.split(',')                   #spliting by using comma and creating a list of coloumns of the current row
    output_individual_roll(changed_line, new_heading_coloumns)    #implementing firsttask
    output_by_subject(changed_line, new_heading_coloumns)         #implementing secondtask
f.close()