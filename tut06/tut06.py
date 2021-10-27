import re
import os
import shutil 





os.system('cls')

def regex_renamer():
   
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    s_padding = int(input("Enter the Season Number Padding: "))
    e_padding = int(input("Enter the Episode Number Padding: "))
    name_of_series = ""
    if webseries_num==1:
        name_of_series = "Breaking Bad"
    elif webseries_num ==2:
        name_of_series="Game of Thrones"
    else:
        name_of_series ="Lucifer"
       
    if name_of_series=='Breaking Bad':
        files_series= os.listdir(os.getcwd()+"\\wrong_srt\\"+name_of_series)
        for series in files_series:
            series_sub= re.split(' ',series)
            info_series=re.split('[se]',series_sub[2])
            newpath=os.getcwd()
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+name_of_series+"\\"+series,newpath+"\\corrected_srt\\Breaking Bad\\Breaking Bad - Season "+str('{:' + '0' + '>' + str(s_padding) + '}').format(info_series[1])+" Episode "+str('{:' + '0' + '>' + str(e_padding) + '}').format(info_series[2])+"."+re.split('\.',series_sub[3])[3]) 
    
    elif name_of_series=='Game of Thrones':
        files_series= os.listdir(os.getcwd()+"\\wrong_srt\\"+name_of_series)
        for series in files_series:
            series_main= re.split('.WEB',series)
            series_sub=re.split("-",series_main[0])
            info_series=re.split('[x]',series_sub[1])
            newpath=os.getcwd()
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+name_of_series+"\\"+series,newpath+"\\corrected_srt\\Game of Thrones\\Game of Thrones - Season "+str('{:' + '0' + '>' + str(s_padding) + '}').format(info_series[0].strip())+" Episode "+str('{:' + '0' + '>' + str(e_padding) + '}').format(info_series[1])+"-"+series_sub[2]+"."+re.split('\.',series_main[1])[4])          
    
    elif name_of_series=='Lucifer':
        files_series= os.listdir(os.getcwd()+"\\wrong_srt\\"+name_of_series)
        for series in files_series:
            series_main= re.split('.HDTV',series)
            series_sub=re.split("-",series_main[0])
            info_series=re.split('[x]',series_sub[1])
            newpath=os.getcwd()+"\\corrected_srt\\Lucifer\\Lucifer - Season "
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+name_of_series+"\\"+series,newpath+str('{:' + '0' + '>' + str(s_padding) + '}').format(info_series[0].strip())+" Episode "+str('{:' + '0' + '>' + str(e_padding) + '}').format(info_series[1])+"-"+series_sub[2]+"."+re.split('\.',series_main[1])[3])          

if os.path.isdir("corrected_srt") == 0:
    os.mkdir("corrected_srt")
if os.path.isdir("corrected_srt\Breaking Bad") == 0:
	os.mkdir("corrected_srt\Breaking Bad")	    
if os.path.isdir("corrected_srt\Game of Thrones") == 0:
    os.mkdir("corrected_srt\Game of Thrones")
if os.path.isdir("corrected_srt\Lucifer") == 0:
	os.mkdir("corrected_srt\Lucifer")

            

regex_renamer()