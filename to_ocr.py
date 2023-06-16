import os
import pytesseract 
from PIL import Image
num = int(input("Total Images? "))
os.system('clear')
for x in range(1,num+1):
    f = open('data.txt','a')
    f.write('\n'+'###### Image '+str(x)+' Data #####'+'\n')
    file = "image 1 "+"("+str(x)+")"+'.jpg'
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    f = open('data.txt','a')
    f.write(text+'\n')
    f.write('######Image '+str(x)+' Data END #####'+'\n')
    os.system('clear')
    print('Progress: '+str(int((x/num)*100))+'%')
f.close()
print("Completed")
a = input("Press Enter to Exit :)")
