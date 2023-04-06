from bs4 import BeautifulSoup
import cv2
import os
import time 
def remove_items(test_list, item):     
    res = [i for i in test_list if i != item] 
    return res
total_dict  = {}
def xml_img(xml_path):
    with open('Annotation-20230224T041327Z-001//Annotation//Annotation 1//'+xml_path, 'r') as f:
        data = f.read()        
    
    tmp = data.splitlines()
    
    for i in range(len(tmp)):        
        if("<name>"in tmp[i]):            
            name_tmp = tmp[i][tmp[i].index("<name>")+6:tmp[i].index("</name>")]   
            if name_tmp in total_dict.keys():
                total_dict[name_tmp] = total_dict[name_tmp]+1
            else:
                total_dict[name_tmp] = 1
    f.close()
path = "D://python//upwork project//vibu//Annotation-20230224T041327Z-001//Annotation//Annotation 1"
dir_list = os.listdir(path)    
for i in range (len(dir_list)):
    print(dir_list[i])
    print(i)
    xml_img(dir_list[i])
print(total_dict)