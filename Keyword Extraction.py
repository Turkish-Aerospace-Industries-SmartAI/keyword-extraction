# importing required modules
import PyPDF2

import json

# creating a pdf file object
pdfFileObj = open('osra-defence-technology-taxonomy.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
total_pages = pdfReader.numPages

page_num = 6
acronym_dict = {}
keywords_dict = {}
while(page_num < total_pages):
    digits = "0123456789"
    if page_num == 6:
        # creating a page object
        pageObj = pdfReader.getPage(page_num)

        # extracting text from page
        text = pageObj.extractText()
        text = text.split('\n')
        count = 0
        while(count < len(text)):
            if count >= 8:
                if text[count] != '' or text[count] != ' ':
                    if text[count-1][0] in digits:
                        count += 1
                        continue
                    # find the full word from the line with ... in it or  ..... in it
                    if '...' in text[count]:
                        full_word = text[count].split('...')[0]
                    elif ' ...' in text[count]:
                        full_word = text[count].split(' ...')[0]
                    elif ' .' in text[count]:
                        full_word = text[count].split(' .')[0]
                    else:
                        full_word = text[count].split('.. ..')[0]
                    if full_word == 'Command Control Communications Computers ':
                        full_word += text[count+1].split('.. ..')[0]
                        acronym_dict[text[count - 1]] = full_word
                        count += 3
                    elif full_word == 'Computer Aided Logistics Support  ':
                        acronym_dict[text[count - 1]] = full_word
                        count += 2
                        accronym = text[count -
                                        1].split('.. ..')[0].split('  ')[0]
                        full_word = text[count -
                                         1].split('.. ..')[0].split('  ')[1]
                        acronym_dict[accronym] = full_word
                    elif full_word == 'Chemical Biological Radiological Nuclear and ' or full_word == 'Common Infrastructure for Battlefield ' or full_word == 'Computer Integration of Requirement ' or full_word == 'Consequence Management  ':
                        full_word += text[count+1].split(' ..')[0]
                        acronym_dict[text[count - 1]] = full_word
                        count += 2
                    else:
                        acronym_dict[text[count - 1]] = full_word
                        count += 1
            count += 1

    elif page_num == 7:
        # creating a page object
        pageObj = pdfReader.getPage(page_num)

        # extracting text from page
        text = pageObj.extractText()
        text = text.split('\n')
        count = 0
        while(count < len(text)):
            if count >= 6:
                if text[count] != '':
                    if count == 6:
                        full_word = text[count].split('...')[0]
                        acronym_dict['DAG'] = full_word
                        count += 1
                    else:
                        # find the full word from the line with ... in it or  ..... in it
                        if '...' in text[count]:
                            full_word = text[count].split('...')[0]
                        elif ' ...' in text[count]:
                            full_word = text[count].split(' ...')[0]
                        else:
                            full_word = text[count].split('....')[0]
                        if full_word == 'Electromagnetic Compatibility  ':
                            accronym = text[count - 1].split(' ..')[0]
                            acronym_dict[accronym] = full_word
                            count += 1
                        elif 'EMO' in text[count-1]:
                            full_word = text[count -
                                             1].split('EMO')[1].split(' ..')[0]
                            acronym_dict['EMO'] = full_word
                            count += 2
                        elif full_word == 'Gaussian Process Regression  ':
                            full_word += text[count+1].split(' ..')[0]
                            acronym_dict[text[count - 1]] = full_word
                            count += 2
                        else:
                            acronym_dict[text[count - 1]] = full_word
                            count += 1
            count += 1

    elif page_num == 8:
        # creating a page object
        pageObj = pdfReader.getPage(page_num)

        # extracting text from page
        text = pageObj.extractText()
        text = text.split('\n')
        count = 0
        while(count < len(text)):
            if count >= 6:
                if text[count] != '':
                    if count == 6:
                        full_word = text[count].split('...')[0]
                        acronym_dict['HMI'] = full_word
                        count += 1
                    else:
                        # find the full word from the line with ... in it or  ..... in it
                        if '...' in text[count]:
                            full_word = text[count].split('...')[0]
                        elif ' ...' in text[count]:
                            full_word = text[count].split(' ...')[0]
                        elif ' . ' in text[count]:
                            full_word = text[count].split(' . ')[0]
                        else:
                            full_word = text[count].split('  .. ')[0]
                        if full_word == 'Integrated Circuit  ' or full_word == 'Intelligence, Surveillance, Target Acquisition & ' or full_word == 'Mine Counter Measure  ' or full_word == 'Monolithic Microwave Integrated Circuit ' or full_word == 'Maintenance and Repair Organizations  ':
                            if full_word == 'Mine Counter Measure  ':
                                full_word += text[count+1].split(' . ')[0]
                            elif full_word == 'Monolithic Microwave Integrated Circuit ':
                                full_word += text[count+1].split('55')[0]
                            elif full_word == 'Maintenance and Repair Organizations':
                                full_word += text[count+1].split('85')[0]
                            else:
                                full_word += text[count+1].split(' ..')[0]
                            acronym_dict[text[count - 1]] = full_word
                            count += 2
                        elif full_word == 'Intelligence Surveillance and Target Acquisition':
                            acronym_dict[text[count - 1]] = full_word
                            count += 2
                        elif 'LED' in text[count-1]:
                            full_word = text[count].split(' ..')[0]
                            acronym_dict['LED'] = full_word
                            count += 1
                            acronym_dict['LEO'] = text[count].split(' ..')[0]
                            count += 1
                        elif 'MIPPS' in text[count-1]:
                            acronym_dict[text[count - 1]] = full_word
                            count += 2
                        else:
                            acronym_dict[text[count - 1]] = full_word
                            count += 1
            count += 1

    elif page_num == 9:
        # creating a page object
        pageObj = pdfReader.getPage(page_num)

        # extracting text from page
        text = pageObj.extractText()
        text = text.split('\n')
        count = 0
        while(count < len(text)):
            if count >= 7:
                if text[count] != '':
                    # find the full word from the line with ... in it or  ..... in it
                    if '...' in text[count]:
                        full_word = text[count].split('...')[0]
                    elif ' ...' in text[count]:
                        full_word = text[count].split(' ...')[0]
                    else:
                        full_word = text[count].split('....')[0]
                    if full_word == 'Radio Frequency  ' or full_word == 'Spatial -Temporal Graph Concolutional Networks' or full_word == 'Unmanned Underwater Vehicle  ':
                        full_word += text[count+1].split(' ..')[0]
                        if 'Radio Frequency  ' in full_word:
                            full_word = full_word.split('53')[0]
                        elif 'Unmanned Underwater Vehicle  ' in full_word:
                            full_word = full_word.split('47')[0]
                        acronym_dict[text[count - 1]] = full_word
                        count += 2
                    elif 'SCS' in text[count-1]:
                        full_word = text[count -
                                         1].split('SCS')[1].split(' ..')[0]
                        acronym_dict['SCS'] = full_word
                        count += 2
                    else:
                        acronym_dict[text[count - 1]] = full_word
                        count += 1
            count += 1

    elif page_num == 10:
        # creating a page object
        pageObj = pdfReader.getPage(page_num)

        # extracting text from page
        text = pageObj.extractText()
        text = text.split('\n')
        count = 0
        while(count < len(text)):
            if count >= 6:
                if text[count] != '':
                    if count == 6:
                        full_word = text[count].split('...')[0]
                        acronym_dict['VTOL'] = full_word
                        count += 1
                    else:
                        # find the full word from the line with ... in it or  ..... in it
                        if '...' in text[count]:
                            full_word = text[count].split('...')[0]
                        elif ' ...' in text[count]:
                            full_word = text[count].split(' ...')[0]
                        else:
                            full_word = text[count].split('....')[0]
                        if full_word == 'Wide Area Surveillance and Automatic Detection':
                            full_word += text[count+1].split(' ..')[0]
                            acronym_dict[text[count - 1]] = full_word
                            count += 2
                            text[count] = text[count].split('  ..')[0]
                            acronym_dict['WLP'] = text[count]
                            count += 1
                        else:
                            acronym_dict[text[count - 1]] = full_word
                            count += 1
            count += 1
    elif page_num >= 12 and page_num <= 15 or page_num >= 39 and page_num <= 43 or page_num >= 67 and page_num <= 69 or page_num >= 77 and page_num <= 79 or page_num == 89:
        # creating a page object
        pageObj = pdfReader.getPage(page_num)

        # extracting text from page
        text = pageObj.extractText()
        text = text.split('\n')
        count = 0
        word = None
        while(count < len(text)):
            if count >= 8:
                if text[count] != '':
                    keyword = text[count].split('–')[1].split(' ..')[0]
                    if keyword[0] == ' ' and keyword[-1] == ' ':
                        keyword = keyword[1:len(keyword)-1]
                    elif keyword[-1] == ' ':
                        keyword = keyword[:len(keyword)-1]
                    elif keyword[0] == ' ':
                        keyword = keyword[1:]
                    header = text[count].split('–')[0].split('.')[
                        0].split(' ')[0]
                    keywords_dict[keyword] = []
                    count += 1
                    while(count < len(text)):
                        if header in text[count]:
                            if 'Symbolic,' in text[count]:
                                word = 'Symbolic, Logic-based and Knowledge-based'
                            elif 'Connectionist' in text[count]:
                                word = 'Connectionist - Artificial Neural Networks (ANN)'
                            else:
                                word = text[count].split(
                                    '–')[1].split(' ..')[0]
                                word = word[1:len(word)-1]
                                if 'Meteoro' in word:
                                    word = 'Meteorology'
                            keywords_dict[keyword].append(word)
                            count += 1
                        else:
                            break
                if word == 'Electromagnetic Railguns' or word == 'Procurement and Contracting Processes':
                    break
            count += 1
    page_num += 1

new_dict = {}
for key, value in acronym_dict.items():
    if key[0] == ' ' and key[-1] == ' ':
        key = key[1:len(key)-1]
    if key[:2] == '  ':
        key = key[2:]
    if key[-2:] == '  ':
        key = key[:len(key)-2]
    if key[-1] == ' ':
        key = key[:len(key)-1]
    if key[0] == ' ':
        key = key[1:]
    if value[0] == ' ' and value[-1] == ' ':
        value = value[1:len(value)-1]
    if value[:2] == '  ':
        value = value[2:]
    if value[-2:] == '  ':
        value = value[:len(value)-2]
    if value[-1] == ' ':
        value = value[:len(value)-1]
    if value[0] == ' ':
        value = value[1:]
    new_dict[key] = value

with open('osra_keywords.json', 'w') as fp:
    json.dump(keywords_dict, fp)
with open('osra_acronyms.json', 'w') as fp:
    json.dump(new_dict, fp)

print("Number of acronyms: ", len(new_dict.keys()))
print("Number of keywords: ", len(keywords_dict.keys()))

# closing the pdf file object
pdfFileObj.close()
