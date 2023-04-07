import os
import re
import uuid
import glob
import openai
import xml.etree.ElementTree as ET

from pathlib import Path
from os import listdir
from os.path import isfile, join
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

openai.api_key = ''

metadata = []
basedir = '/Users/erra1244/Desktop/issues_XML/'
rows = ['test']

for mydir in os.listdir(basedir):
    if os.path.isdir(os.path.join(basedir, mydir)):
        row = []
        for myfile in os.listdir(os.path.join(basedir, mydir)):
            if 'mets' not in myfile:
                result = os.path.join(basedir, mydir, myfile)
                xml = open(result, 'r')
                tree = ET.parse(xml)
                root = tree.getroot()
                thing = ''
                for tag in root.findall('.//*[@CONTENT]'):
                    x = tag.attrib['CONTENT'] + ' '
                    thing += x
                    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": "can you clean this text:" + thing}]
                    )
                    print(completion.choices[0].message.content)
                    # print(thing)

        		
            # if myfile.endswith('xml'):
            # 	print(myfile)
    #              result = process_xml(os.path.join(basedir, mydir, myfile))
    #              row[i_dont_know_what_you_are_doing] = do_something_with_result(result)
    #     rows.append(row)


# write_csv(rows)

# path = Path("/Users/erra1244/Desktop/issues_XML/")
# for file in path.glob("./*"):
# 	print(file)
        # with open(file,'r') as xmlFile:
        #     tree = ET.parse(xmlFile)
        #     root = tree.getroot()

# p = Path("/Users/erra1244/Desktop/Issues_XML/")

# file_list = [f for f in p.iterdir() if f.is_file()]


# for folder in p.glob('*'):
# 	print (folder)


	# file = sys.argv[1]
	# ns = {'alto':'http://www.loc.gov/standards/alto/ns-v2#'}







	
