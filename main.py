import pytesseract
import cv2
import fitz
import os
import sys


def text_from_image(image_file,config_mode=r' --psm 6 --oem 3'):
    """
    Takes file path, config_mode(default set to '--psm 6 --oem 3')
    returns text extracted from the image. Uses Open-cv module to read the image
    and pytesseract to extract the text from image
    """
    print(image_file)
    img = cv2.imread(image_file)
    # print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config=config_mode)
    return text
    


def text_from_pdf(pdf_file,config_mode=r' --psm 3 --oem 3'):
    """
    Takes pdf file as argument and converts the pdf to images using PyMuPDF.
    return the text extracted from the file.
    """
            
    pdf = fitz.open(pdf_file)
    total_text = []
    pdf_length = len(pdf)
    # Loop through each page of the PDF
    for i in range(len(pdf)):
        # Select the current page
        file_name = pdf.name[:-4]
        
        # print(file_path)
        page = pdf[i]
        pix = page.get_pixmap(alpha=False)
        pix.save(f"{file_name}_{i}.png")
    pdf.close()
        
        
        
       
    for i in range(pdf_length):
        
        file_path = os.path.realpath(f"{file_name}_{i}.png")
        text = text_from_image(file_path,config_mode=config_mode)
        # print(text)
        total_text.append(text)
        
        # with open(f"{file_name}{i}.txt", "w", encoding="utf-8") as f:
        #     f.write(text)
        os.remove(file_path)
    # print(total_text)
    output = "\n".join(total_text)
    with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
        f.write(output)    
    return output

#class to extract text from files
def extract_text(file_name):
    # print(file_name[-3::-1])
    if file_name[-3:] == 'pdf':
        text = text_from_pdf(file_name)
        print(text)
    else:
        
        text = text_from_image(file_name)
        print(text)
        

if __name__ == '__main__':
    
    _,file_name= sys.argv
    
    extract_text(file_name)
    
    
        
        
        
    
    
# with open("1.txt", "a", encoding="utf-8") as f:
#     f.write(text)    

# instance = ExtractText()
# print(instance.text_from_image("1.jpg",config_mode=r' --psm 6 --oem 3'))















# pdf_reader = PdfReader(pdf_file)
        # text_list = []
        # pages = pdf_reader.pages

        # for num in range(len(pages)):
        #     page = pdf_reader.pages[num]

        #     text = page.extract_text()
        #     text_list.append(text)

        # output = "\n".join(text_list)