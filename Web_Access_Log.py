import re

def main():
    content = readLogFile(r'C:\Users\Owner\PycharmProjects\log_analysis\Web_Access.log')
#    print content
    text = '91.205.189.15 - - [19/Feb/2018:00:35:01] "GET /product.screen?productId=WC-SH-A01&JSESSIONID=SD6SL5FF3ADFF41065 HTTP 1.1" 200 2832 "http://www.buttercupgames.com/category.screen?categoryId=ACCESSORIES" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; InfoPath.1; MS-RTC LM 8)" 447'
    print parseLog(text)

def readLogFile(log_file):
    with open(log_file) as file:
        content = file.read()
    return content

def parseLog(text):
    lst = []
    lst.append(getIPAddress(text))
    lst.append(getST(text))
    lst.append(getMethod(text))
    lst.append(getUrl(text))
    lst.append(getHttp(text))
    lst.append(getStatusCode(text))
    lst.append(getSize(text))
    lst.append(getSrcURL(text))
    lst.append(getUserAgent(text))
    lst.append(getOther(text))
    return lst
#1
def getIPAddress(text):
    regex = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    list = re.findall(regex, text)
    return list[0]
#2
def getST(text):
    regex = '\d{2}\/\w{3}\/201[0-9]:\d{2}:\d{2}:\d{2}'
    list = re.findall(regex, text)
    return list[0]
#3
def getMethod(text):
    regex = 'GET|POST'
    list = re.findall(regex, text)
    return list[0]
#4
def getUrl(text):
    regex = '(?<=GET )\/\w+\.\w+\??[\w=&-]+'
    list = re.findall(regex, text)
    return list[0]
#5
def getHttp(text):
    regex = 'HTTP\s\d.\d'
    list = re.findall(regex, text)
    return list[0]
#6
def getStatusCode(text):
    regex = '(?<=HTTP ..." )[1-5]0[0-9]'
    lst = re.findall(regex, text)
    return lst[0]
#7
def getSize(text):
    regex = '(?<=HTTP ...\" \d{3} )\d+'
    list = re.findall(regex, text)
    return list[0]
#8
def getSrcURL(text):
    regex = '"http[s]?:\/\/[\w.\/?=-]+\"'
    lst = re.findall(regex, text)
    return lst[0]
#9
def getUserAgent(text):
    regex = '(?<=\" \")[\w\":/;,()\s.-]+(?=\" )'
    lst = re.findall(regex, text)
    return lst[0]
#10
def getOther(text):
    regex = '(?<!HTTP \d.\d\" )(?<=\" )\d+'
    lst = re.findall(regex, text)
    return lst[0]

if __name__ == '__main__':
    main()