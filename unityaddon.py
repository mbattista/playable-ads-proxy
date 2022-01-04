from mitmproxy import http

import json

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.startswith("https://auction.unityads.unity3d.com/v6/games/"):
      json_given = json.loads(flow.request.content)

      json_payload = {
        'placements': {
          'defaultRewardedPlacement': {
            'adTypes': [
              'MRAID',
              'VIDEO'
            ],
            'allowSkip': False,
            'auctionType': 'cpm',
          },
          'defaultVideoAndPictureZone': {
            'adTypes': [
              'MRAID',
              'VIDEO'
            ],
            'allowSkip': True,
            'auctionType': 'cpm',
          },
          'rewardedVideo': {
            'adTypes': [
              'MRAID',
              'VIDEO'
            ],
            'allowSkip': False,
            'auctionType': 'cpm',
          },
          'video': {
            'adTypes': [
              'MRAID',
              'VIDEO'
            ],
            'allowSkip': True,
            'auctionType': 'cpm',
          }
        },
        'properties': json_given['properties'],
        'token': json_given['token'],
        'webviewUa': json_given['webviewUa'], 
      }
      flow.request.text = json.dumps(json_payload)

def response(flow: http.HTTPFlow) -> None:
  if flow.request.pretty_url.startswith("https://auction.unityads.unity3d.com/v6/games/"):
    json_given = json.loads(flow.response.content)
    content_change = {
      'dynamicMarkup': '',
      'markup': '%3Cscript%20src%3D%22mraid.js%22%3E%3C%2Fscript%3E%3Cscript%20type%3D%22text%2Fjavascript%22%3Efunction%20doReadyCheck%28%29%7Bif%20%28mraid.getState%28%29%3D%3D%22loading%22%29%7Bmraid.addEventListener%28%22ready%22%2C%20mraidIsReady%29%3B%7Delse%7BshowMyAd%28%29%3B%7D%7Dfunction%20showMyAd%28%29%7Bvar%20adContainer%3Ddocument.querySelector%28%22%23imageContainer%22%29%3B%7Dfunction%20mraidIsReady%28%29%7Bmraid.removeEventListener%28%22ready%22%2C%20mraidIsReady%29%3B%20showMyAd%28%29%3B%7Dfunction%20addEvent%28evnt%2C%20elem%2C%20func%29%7Bif%20%28elem.addEventListener%29%7Belem.addEventListener%28evnt%2C%20func%2C%20false%29%3B%7Delse%20if%20%28elem.attachEvent%29%7Belem.attachEvent%28%22on%22%20%2B%20evnt%2C%20func%29%3B%7Delse%7Belem%5Bevnt%5D%3Dfunc%3B%7D%7DdoReadyCheck%28%29%3B%3C%2Fscript%3E%3Cdiv%20id%3D%22imageContainer%22%3E%3Cdiv%20id%3D%22widgetmain%22%20style%3D%22text-align%3Aleft%3Boverflow-y%3Aauto%3Boverflow-x%3Ahidden%3Bwidth%3A1000px%3Bbackground-color%3A%23transparent%3B%20border%3A1px%20solid%20%23333333%3B%22%3E%3Cdiv%20id%3D%22rsswidget%22%20style%3D%22height%3A600px%3B%22%3E%3Ciframe%20src%3D%22http%3A%2F%2Fus1.rssfeedwidget.com%2Fgetrss.php%3Ftime%3D1641319246119%26amp%3Bx%3Dhttps%253A%252F%252Fwww.tagesschau.de%252Fxml%252Frss2%252F%26amp%3Bw%3D1000%26amp%3Bh%3D600%26amp%3Bbc%3D333333%26amp%3Bbw%3D1%26amp%3Bbgc%3Dtransparent%26amp%3Bm%3D20%26amp%3Bit%3Dtrue%26amp%3Bt%3D%28default%29%26amp%3Btc%3D333333%26amp%3Bts%3D15%26amp%3Btb%3Dtransparent%26amp%3Bil%3Dtrue%26amp%3Blc%3DE1E0FF%26amp%3Bls%3D16%26amp%3Blb%3Dtrue%26amp%3Bid%3Dtrue%26amp%3Bdc%3DF5F5F5%26amp%3Bds%3D14%26amp%3Bidt%3Dtrue%26amp%3Bdtc%3D284F2D%26amp%3Bdts%3D12%22%20border%3D%220%22%20hspace%3D%220%22%20vspace%3D%220%22%20frameborder%3D%22no%22%20marginwidth%3D%220%22%20marginheight%3D%220%22%20style%3D%22border%3A0%3B%20padding%3A0%3B%20margin%3A0%3B%20width%3A1000px%3B%20height%3A600px%3B%22%20id%3D%22rssOutput%22%3EReading%20RSS%20Feed%20...%3C%2Fiframe%3E%3C%2Fdiv%3E%3C%2Fdiv%3E%3C%2Fdiv%3E',
      'inlinedUrl': '',
    }
    for key in json_given['media']:
      json_given['media'][key]['content'] = json.dumps(content_change)
      json_given['media'][key]['adType'] = 'MRAID'
      json_given['media'][key]['contentType'] = 'programmatic/mraid'
      json_given['media'][key]['height'] = 320
      json_given['media'][key]['width'] = 480
      json_given['media'][key].pop('videoLength', None)

    flow.response.text = json.dumps(json_given)


