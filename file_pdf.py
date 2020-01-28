# how to create a pdf file
from fpdf import FPDF
f1=open("new.txt",'r')
ss=f1.readline()
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=12)
pdf.cell(200,10,txt=ss ,ln=1,align="C")
pdf.cell(200,10,txt="big boss",ln=2,align="C")
pdf.output("6.pdf")
f1.close()