import http.client
import json
import sys

import re


def shorterURL(url):
    # API load
    f = open('./shortUrlAPI','r')
    lines = f.readlines()
    api=[]
    for line in lines:
        api.append(line)
    api_key=api[0]
    pattern = re.compile(r'\s+')
    api_key = re.sub(pattern, '', api_key)
    print(api_key)
    f.close

    conn = None
    s_url = ''
    try:
        data = json.dumps({'longUrl' : str(url)}).encode('utf-8')
        content_length = len(data)
        uri = '/urlshortener/v1/url?key=%s' % api_key
        conn = http.client.HTTPSConnection('www.googleapis.com', 443)
        conn.connect()
        conn.putrequest('POST', uri)
        conn.putheader('Content-Type', 'application/json')
        conn.putheader('Content-Length', str(content_length))
        conn.endheaders()
        conn.send(data)
        resp = conn.getresponse().read()
        resp = resp.decode('utf-8')
        s_url = json.loads(resp)['id']
    except Exception as exc:
        print('Error', exc)
    finally:
        if conn is not None:
            conn.close()
    return s_url

if __name__ == '__main__':
    d=shorterURL('http://board.sejong.ac.kr/viewcount.do?rtnUrl=/boardview.do?pkid=110237^currentPage=1^searchField=ALL^siteGubun=19^menuGubun=1^bbsConfigFK=333^searchLowItem=ALL&searchValue=&gubun=&tableName=SJU_BBSDATA&fieldName=VIEWCOUNT&viewNum=82&whereCon=PKID=110237')  

# import json
# import urllib.parse
# import urllib.request

# class GooglException (Exception):
#     def __init__(self, message, code, errors):
#         super().__init__(message)
#         self.code = code
#         self.errors = errors

# def shortenURL (url_to_shorten):
#     """
#     Given a URL, return a goo.gl shortened URL
#     Arguments
#     ---------
#         url_to_shorten : string
#             The URL you want to shorten
#     Returns
#     -------
#         Shortened goo.gl URL string
#     Raises
#     ------
#         GooglException
#             If something goes wrong with the HTTP request
#     """

#     # The goo.gl API URL
#     api_url = 'https://www.googleapis.com/urlshortener/v1/url'
#     # Construct our JSON dictionary
#     data = json.JSONEncoder().encode({'longUrl': url_to_shorten})
#     # Encode to UTF-8 for sending
#     data = data.encode('utf-8')
#     # HTTP header
#     headers = {"Content-Type": "application/json"}
#     # Construct the request
#     request = urllib.request.Request(api_url, data=data, headers=headers)

#     # Make the request and get the response to read from
#     try:
#         response = urllib.request.urlopen(request)
#         success = True
#     # If a HTTPError occurs, we will be reading from the error instead
#     except urllib.error.HTTPError as err:
#         response = err
#         success = False
#     # Read the response object, decode from utf-8 and convert from JSON
#     finally:
#         data = json.loads(response.read().decode('utf8'))

#     # Return our shortened URL
#     if success:
#         return data['id']
#     # Or raise an Exception
#     else:
#         raise GooglException(data['error']['message'], data['error']['code'], data['error']['errors'])

# if __name__ == '__main__':
#     d=shortenURL('http://board.sejong.ac.kr/viewcount.do?rtnUrl=/boardview.do?pkid=110237^currentPage=1^searchField=ALL^siteGubun=19^menuGubun=1^bbsConfigFK=333^searchLowItem=ALL&searchValue=&gubun=&tableName=SJU_BBSDATA&fieldName=VIEWCOUNT&viewNum=82&whereCon=PKID=110237')  
