# !/usr/bin/python3
# pip install fitz
# pip install PyMuPDF

import fitz
import os
import os.path as path

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(THIS_FOLDER,"acta.pdf")
output_file = os.path.join(THIS_FOLDER,"acta-firmada.pdf")
image_file = os.path.join(THIS_FOLDER,"firma.png")

def firmar(archivo):
    # define the position (upper-right corner)
    # image_rectangle = fitz.Rect(450,20,550,120)
    image_rectangle_vertical = fitz.Rect(250,760,350,860)
    image_rectangle_horizontal = fitz.Rect(520,400,620,500)

    # retrieve the first page of the PDF
    pdf = fitz.open(archivo)
    print(pdf)
    for i in range(pdf.pageCount):
        try:
            page = pdf[i]
            pix = page.getPixmap()
            pdf_width = pix.width

            # add the image 
            # ancho Rolando 596
            if pdf_width > 620:
                page.insertImage(image_rectangle_horizontal, filename=image_file, rotate=90)
                print('Firmando... Página: '+str(i+1)+' Ancho: '+str(pdf_width)+' (horizontal)')
            else:
                page.insertImage(image_rectangle_vertical, filename=image_file)
                print('Firmando... Página: '+str(i+1)+' Ancho: '+str(pdf_width)+' (vertical)')
        except:
            print('### Error ###')
            break

    pdf.save('f'+archivo)

listaArchivo = os.listdir(THIS_FOLDER)
if listaArchivo:
    for fileName in listaArchivo:
        print('Leyendo '+str(fileName))
        if fileName.endswith(".pdf"):
            firmar(fileName)