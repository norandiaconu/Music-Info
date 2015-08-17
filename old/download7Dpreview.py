from py7D import api_settings
import oauth2 as oauth
import urllib
#import pycurl
#from io import BytesIO

#def __init__():
#    write7DPreview(filename, previewID)
global previewID, id
previewID = 6369075
id = ''

def main():
    consumer_key = api_settings.oauthkey
    consumer_secret = api_settings.secret

    consumer = oauth.Consumer(consumer_key, consumer_secret)
    request_url = "http://previews.7digital.com/clip/" + str(previewID)

    req = oauth.Request(method="GET", url=request_url,is_form_encoded=True)

    req['oauth_timestamp'] = oauth.Request.make_timestamp()
    req['oauth_nonce'] = oauth.Request.make_nonce()
    sig_method = oauth.SignatureMethod_HMAC_SHA1()

    req.sign_request(sig_method, consumer, token=None)
    #req = req + 'country=US'
    print req.to_url()
    id = req.to_url()
    id = id + '&country=US'
    print id
    #import urllib
    urllib.urlretrieve (id, "mp3")

if __name__ == '__main__':
    import sys
    main()

    #buffer = BytesIO()

    #curlGET = pycurl.Curl()
    #curlGET.setopt(curlGET.URL, req.to_url())
    #curlGET.setopt(curlGET.WRITEDATA, buffer)
    #curlGET.perform()
    #curlGET.close()

    #with open(filename, 'wb') as f:
    #    f.write(buffer.getvalue())
