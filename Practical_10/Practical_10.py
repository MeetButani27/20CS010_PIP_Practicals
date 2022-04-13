# 20CS010 - Meet Butani
# Generate a PDF file of your 3rd Semester Mark-sheet
# ----------------------------------------------------

# importing FPDF from fpdf
from fpdf import FPDF

# creating an object of FPDF class
pdf = FPDF()

# adding/creating one page in our PDF file
pdf.add_page()

# setting font-style and font-size
pdf.set_font("Arial", size = 10)

# opening the 'marksheet' file, which contains the marks
file = open('F:\Semester -4\marksheet.txt', 'r')

# adding the content of 'marksheet' file into PDF line by line
for line in file:
    pdf.cell(200, 10, txt=line, ln=1, align='C')

# naming the newly generated PDF file
pdf.output('20CS010 - Marksheet.pdf')
