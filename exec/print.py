from PIL import Image
from fpdf import FPDF


def create_pdf():
    image = Image.open('exec/scatter_plot.png')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 10, 'Beautiful Plot', 0, 1, 'C')
    pdf.image('exec/scatter_plot.png', x=20, y=20, w=200, h=150)
    pdf.output('exec/plot.pdf', 'F')

if __name__ == '__main__':
    create_pdf()