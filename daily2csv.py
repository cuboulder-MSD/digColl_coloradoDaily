import os
import re
import uuid
import glob
import xml.etree.ElementTree as ET
import csv
import xmltodict
from bs4 import BeautifulSoup
from lxml import etree
import datetime

from pathlib import Path
from os import listdir
from os.path import isfile, join
from xml.etree.ElementTree import Element, SubElement, Comment, tostring



basedir = '/Users/erra1244/Desktop/issues_XML/'
with open('ocrdata.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(("filename", "ocr"))

    for yeardir in os.listdir(basedir):
        if yeardir.startswith('.'):
            continue
        for issue in os.listdir(os.path.join(basedir,yeardir)):
            if issue.startswith('.'):
                continue
            myfiles = os.listdir(os.path.join(basedir, yeardir, issue))
            myfiles.sort()
            thing = ''
            for myfile in myfiles:
                if myfile.startswith('.'):
                    continue
                # print(os.path.join(basedir, yeardir, issue, myfile))
                if 'mets' not in myfile:

                    result = os.path.join(basedir, yeardir, issue, myfile)
                    xml = open(result, 'r')
                    tree = ET.parse(xml)
                    root = tree.getroot()
                    for tag in root.findall('.//*[@CONTENT]'):
                        x = tag.attrib['CONTENT'] + ' '
                        thing += x
                    # for tag in root.findall('.//fileName'):
                    #     print(tag.text)

            newmonth = issue.replace('_','-')
            date = yeardir + '-' + newmonth
            row=(date,thing)
            writer.writerow(row)

bibData = {}

# basedir = '/Users/erra1244/Desktop/issues_XML/'
# with open('ocrdata.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, lineterminator='\n')
#     writer.writerow(("filename", "ocr"))
    
#     for yeardir in os.listdir(basedir):
#         if yeardir.startswith('.'):
#             continue
#         for issue in os.listdir(os.path.join(basedir,yeardir)):
#             if issue.startswith('.'):
#                 continue
#             row = []
#             for myfile in os.listdir(os.path.join(basedir, yeardir, issue)):
#                 if myfile.startswith('.'):
#                     continue
#                 print(os.path.join(basedir, yeardir, issue, myfile))
#                 if 'mets' not in myfile:
                    
#                     result = os.path.join(basedir, yeardir, issue, myfile)
#                     xml = open(result, 'r')
#                     tree = ET.parse(xml)
#                     root = tree.getroot()
#                     thing = ''
#                     for tag in root.findall('.//*[@CONTENT]'):
#                         x = tag.attrib['CONTENT'] + ' '
#                         thing += x
#                     row=(myfile,thing)
                    
                    # print(row)
                    # bibData['filename'] =myfile
                    # bibData['ocr'] = thing

            
    # w = csv.DictWriter(f, bibData.keys())
    # w.writeheader()       
    # w.writerow(bibData)
# print(bibData)
                

        # for mydir in os.listdir(os.path.join(basedir, yeardir, issue)):
        #     print(mydir)
        #     if os.path.isdir(os.path.join(basedir, yeardir, issue, mydir)):
        #         row = []
        #         for myfile in os.listdir(os.path.join(basedir, yeardir, issue, mydir)):
        #             print(myfile)
        #             if 'mets' not in myfile:
        #                 result = os.path.join(basedir, mydir, myfile)
        #                 xml = open(result, 'r')
        #                 tree = ET.parse(xml)
        #                 root = tree.getroot()
        #                 thing = ''
        #                 for tag in root.findall('.//*[@CONTENT]'):
        #                     x = tag.attrib['CONTENT'] + ' '
        #                     thing += x
        #                 bibData['filename'] =myfile
        #                 bibData['ocr'] = thing
        #                 print(bibData)



# for yeardir in os.listdir(basedir):
#     for issue in os.listdir(os.path.join(basedir,yeardir)):
#         for mydir in os.listdir(basedir):
#             if os.path.isdir(os.path.join(basedir, mydir)):
#                 row = []
#                 for myfile in os.listdir(os.path.join(basedir, mydir)):
#                     if 'mets' not in myfile:
#                         result = os.path.join(basedir, mydir, myfile)
#                         xml = open(result, 'r')
#                         tree = ET.parse(xml)
#                         root = tree.getroot()
#                         thing = ''
#                         for tag in root.findall('.//*[@CONTENT]'):
#                             x = tag.attrib['CONTENT'] + ' '
#                             thing += x
#                         bibData['filename'] =myfile
#                         bibData['ocr'] = thing
#                         print(bibData)


# for mydir in os.listdir(basedir):
#     if os.path.isdir(os.path.join(basedir, mydir)):
#         row = []
#         for myfile in os.listdir(os.path.join(basedir, mydir)):
#             if 'mets' in myfile:
#                 # print(myfile)
#                 result = os.path.join(basedir, mydir, myfile)
                
#                 file = open(result,'r')
                


#                 ###########
#                 xml_data = file.read()
                
#                 soup = BeautifulSoup(xml_data, features='xml')
#                 # print(soup)
#                 titles = soup.find_all('MODS:dateIssued')
#                 for title in titles:
                   
#                     firstDate = title.text.replace('.','-')
#                     #converts dd-mm-yyyy to yyyy-mm-dd
#                     newDate=datetime.datetime.strptime(title.text, '%d.%m.%Y').strftime('%Y-%m-%d')
                    
#                     bibData['title'] = 'Colorado Daily, ' + newDate
#                     bibData['publisher'] = 'University of Colorado Boulder'
#     print(bibData)
                

            
