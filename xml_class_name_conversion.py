from bs4 import BeautifulSoup
import cv2
import os

def remove_items(test_list, item):
     
    res = [i for i in test_list if i != item]
 
    return res



def xml_img(xml_path):
    with open('Anotation-20230131T113530Z-001//Anotation//Anotation xml//'+xml_path, 'r') as f:
        data = f.read()        
    
    tmp = data.splitlines()
    for i in range(len(tmp)):
        if("<name>"in tmp[i]):            
            name_tmp = tmp[i][tmp[i].index("<name>")+6:tmp[i].index("</name>")]   
            if ("britannia" in name_tmp.lower()):
                tmp[i] = "<name>"+"BRITANNIA"+"</name>"
            if ("unibic" in name_tmp.lower()):
                tmp[i] = "<name>"+"UNIBIC"+"</name>"
            if ("cadbury" in name_tmp.lower()):
                tmp[i] = "<name>"+"CADBURY"+"</name>"
            if ("itc_" in name_tmp.lower()):
                tmp[i] = "<name>"+"ITC"+"</name>"
            if ("parle" in name_tmp.lower()):
                tmp[i] = "<name>"+"PARLE"+"</name>"
            if ("amul" in name_tmp.lower()):
                tmp[i] = "<name>"+"AMUL"+"</name>"
            
    xml_data = '\n'.join(tmp)

    
    


    


    f.close()

    
        
        
    
    f =  open("new_xml\\"+xml_path, "wb")
    f.write(xml_data.encode())
    f.close()


path = "D://python//upwork project//vibu//Anotation-20230131T113530Z-001//Anotation//Anotation xml"
dir_list = os.listdir(path)    
for i in range (len(dir_list)):
    print(dir_list[i])
    xml_img(dir_list[i])