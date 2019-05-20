import re
import pandas as pd
import os.path as path
import csv


def get_email_list(lines):

    line_data = ""

    for line in lines:
        line_data= line_data+line+'\n'


    email_list=[]

    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

    matches = pattern.findall(line_data)
    for match in matches:
        email_list.append(match)

    return email_list

def get_linked_in_profiles(lines):

    profile_list=[]

    for line in lines:
        if line.startswith("https://bd.linkedin.com/in"):
            profile_list.append(line)

    return profile_list

def get_emails(data):
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    matches = pattern.findall(data)

    emails=''
    for match in matches:
        emails = emails+match+'|'
    
    if len(emails)>0:
        emails = emails[:-1]
    
    return emails


def is_valid_url(url):
    if '??' in url:
        return False
    else:
        return True
    # regex = re.compile(
    #         r'^(?:http|ftp)s?://' # http:// or https://
    #         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    #         r'localhost|' #localhost...
    #         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    #         r'(?::\d+)?' # optional port
    #         r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # return re.match(regex, url) is not None

def is_valid_linkedin_url(url):
    p = re.compile(r'((http(s?)://)*([a-zA-Z0-9\-])*\.|[linkedin])[linkedin/~\-]')
    # p = re.compile(r'((http(s?)://)*([a-zA-Z0-9\-])*\.|[linkedin])[linkedin/~\-]+\.[a-zA-Z0-9/~\-_,&=\?\.;]+[^\.,\s<]')

    return re.match(p,url) is not None


def get_email_and_id(block):
    lines = block.split('\n')
    
    url = lines[0]

    if is_valid_url(url):
        parts = url.split('/')
        
        if '?' in parts[4]:
            parts[4] = parts[4].split('?')[0]
            # print(parts[4])

        new_parts=parts[:5]

        url = '/'.join(new_parts)
        
        data_lines = lines[1:]
        data = ' '.join(data_lines)
        
        emails = get_emails(data)
        
        return url,emails


def get_block_list(filename):
    block_list=[]

    with open(filename, 'r') as myfile:
        lines = myfile.readlines()
        block = ''

        for line in lines:
            line = line.replace('\n','')

            # print(len(line))
            
            if len(line) == 0:
                # print('Y')
                block_list.append(block)
                block =''
            else:
                # print('N')
                # print(line)
                
                if len(block)==0:
                    block = block+line
                else:
                    block = block+'\n'+line

    return block_list



def extract_and_save(filename):
    block_list = get_block_list(filename)

    data_list = []
    for block in block_list:
        data ={}


        # Check Block Size
        if len(block) >10:
            if get_email_and_id(block) != None:
                try:
                    (url,email) = get_email_and_id(block)
                    # print(url,email)
                    # counter = counter+1
                    # print(counter)
                    data['url']=url
                    data['email'] = email

                    data_list.append(data)
                except:
                    pass

    


    df = pd.DataFrame(data_list)

    name = path.splitext(filename)[0]


    df.to_csv('./output/'+name+'.csv',index=False)


def get_url_list(file):
    list =[]

    with open(file,'r') as f:
        reader = csv.DictReader(f,delimiter=',')
        for x in reader:
            list.append(x['url'])

    return list








if __name__ == "__main__":
    list = get_url_list('./output/data1.csv')

    for x in list:
        print(x)
    
    





   
        



