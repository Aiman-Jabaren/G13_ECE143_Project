import PyPDF2
import argparse
import os
import pycountry
import re
if __name__=="__main__":
    
    p = './pdfs/'
    file_list = os.listdir(path=p)
    file_list.sort()
    for fi in file_list:
        # creating a pdf file object
        pdfFileObj = open(p+fi, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        text = pageObj.extractText()
        lines = text.splitlines()
        
        # Parsing for keywords
        for i,line in enumerate(lines):
            if re.search('Total',line) and re.search('population',line):
                country = lines[i-1].strip()
            if re.search('Diabetes',line):
                if re.search('Overweight',lines[i+4]):
                    dia_male = lines[i+1].strip()
                    dia_female = lines[i+2].strip()
                    dia_total = lines[i+3].strip()
                    ov_male = lines[i+5].strip()
                    ov_female = lines[i+6].strip()
                    ov_total = lines[i+7].strip()
                elif re.match(r'Diabetes $',line):
                    pro_mort = lines[i+2].strip()
            if re.search('Obesity',line):
                ob_male = lines[i+1]
                ob_female = lines[i+2]
                ob_total = lines[i+3]
        # set the delimiter
        dl = ',' 
        # try to get country codes. Leave blank if not found
        try: 
            country_code2 = pycountry.countries.get(name=country).alpha_2
            country_code3 = pycountry.countries.get(name=country).alpha_3
        except AttributeError:
            country_code2 = ''
            country_code3 = ''
        # write to output file
        with open('final_data.csv','a',1) as f:
            li = country+dl+dia_total+dl+dia_male+dl+dia_female+dl+ob_total+dl+ob_male+dl+ob_female+dl+ov_total+dl+ov_male+dl+ov_female+dl+pro_mort+dl+country_code2+dl+country_code3+'\n'
            f.write(li)

        # closing the pdf file object
        pdfFileObj.close()
