import requests
import json

def attempt():
  s = requests.Session()
  url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/' 
  cookies = {
    'ig_did': '73BA5476-FCF9-40E2-B51E-1BC08E78E28B',
    'ig_nrcb': '1',
    'csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
    'mid': 'YS5chQAEAAF3m0_fNMUWgYMz5df7',
  } 
  data = {
      'email': 'hello@yandex.ru',
      'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1630432041:AQpQAK2NpjpV6rUaB/XL/4Wio/cRGlY5mJ3Esqb6ZDYqn3kPPgZm/zgw5pw7eP6bxyS/gWzgv8ypFVJSi8fhNJKztuP7ih5MVAWHzzve/A7PBY8XLpH6ELPiHK4RjZsmcsaLTKsJcdMC',
      'username': 'hello',
      'first_name': 'dmitry someone',
      'opt_into_one_tap': False,
  }
  headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=73BA5476-FCF9-40E2-B51E-1BC08E78E28B; ig_nrcb=1; csrftoken=WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw; mid=YS5chQAEAAF3m0_fNMUWgYMz5df7',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'x-asbd-id': '437806',
    'x-csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '23b9dbae7fad',
    'x-requested-with': 'XMLHttpRequest',
  }

  r = s.post(url, cookies=cookies, data=data, headers=headers)
  print(r.content)
  return r.content

def add_one(number):
  return number + 1
