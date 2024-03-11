import PyPDF2


def add_watermark(super_pdf, wtrmrk_pdf, marked_pdf):
    with open(super_pdf, 'rb') as super_file:
        super_pdf_reader = PyPDF2.PdfFileReader(super_file)
        with open(wtrmrk_pdf, 'rb') as wtr_file:
            wtrmrk_pdf_reader = PyPDF2.PdfFileReader(wtr_file)
            marked_pdf_writer = PyPDF2.PdfFileWriter()
            wrtmrk_page = wtrmrk_pdf_reader.getPage(0)
            for page_num in range(super_pdf_reader.numPages):
                page = super_pdf_reader.getPage(page_num)
                page.mergePage(wrtmrk_page)
                marked_pdf_writer.addPage(page)
            with open(marked_pdf, 'wb') as marked_file:
                marked_pdf_writer.write(marked_file)


# Hardcoded file names
super_pdf = 'super.pdf'
wtrmrk_pdf = 'wtr.pdf'
marked_pdf = 'marked.pdf'

add_watermark(super_pdf, wtrmrk_pdf, marked_pdf)


# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')


# pdf_combiner(inputs)
