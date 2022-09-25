from flask import Flask, request
app = Flask(__name__)

in_memory_datastore = {
   "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
   "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
   "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
   "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
                "contribution": "class/object split, subclassing, protected attributes"},
   "Pascal": {"name": "Pascal", "publication_year": 1970,
              "contribution": "modern unary, binary, and assignment operator syntax expectations"},
   "CLU": {"name": "CLU", "publication_year": 1975,
           "contribution": "iterators, abstract data types, generics, checked exceptions"},
}
'''
@app.get('/programming_languages')
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}
'''

@app.route('/')
def hello_world():
    return "Fuck off"
@app.route('/programming_languages/<programming_language_name>')
def get_programming_language(programming_language_name):
   return in_memory_datastore[programming_language_name]


# @app.get('/programming_languages')
# def list_programming_languages():
#    before_year = request.args.get('before_year') or '30000'
#    after_year = request.args.get('after_year') or '0'
#    qualifying_data = list(
#        filter(
#            lambda pl: int(before_year) > pl['publication_year'] > int(after_year),
#            in_memory_datastore.values()
#        )
#    )

#    return {"programming_languages": qualifying_data}



# import requests 
# import base64
# user='clevercart-c4a68e29f9afcc45f2e56902f0151c991072864823612119086'
# passw = '25MY35fFo7Uh7fZJfzdrB17OJ42VC4rnFTd4jhI4'
# code_it = user+':'+passw
# message_bytes = code_it.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
# code_it = "Basic "+base64_message
# #print(code_it)
# def get_me_the_fuck_in():
#     headers = {"Content-Type":"application/x-www-form-urlencoded","Authorization":code_it}
#     data = {"grant_type":"client_credentials","scope":"product.compact"}
#     #resp = requests.get(curl -X POST 'https://api.kroger.com/v1/connect/oauth2/token' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Authorization: Basic Y2xldmVyY2FydC1jNGE2OGUyOWY5YWZjYzQ1ZjJlNTY5MDJmMDE1MWM5OTEwNzI4NjQ4MjM2MTIxMTkwODY6Qm1Da2lKTU1vaWx3MVFaZVpUS2ZLMGt3MHh0WW1JTkxpSzZBZDNjQQ==' -d 'grant_type=client_credentials&scope=product.compact')
#     resp = requests.post('https://api.kroger.com/v1/connect/oauth2/token', headers=headers,data = data)
#     print("first code",resp.status_code)
#     #print(resp.json()['access_token'])
#     #print("curl -X POST 'https://api.kroger.com/v1/connect/oauth2/token' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Authorization:"+ code_it+"' -d 'grant_type=client_credentials&scope=product.compact' ")
#     response_data = resp.json()
#     return response_data['access_token']
# def get_me_the_fuck_locations(access_token):
#     header_locations = {"Accept": "application/json","Authorization": "Bearer "+access_token}
#     res = requests.get('https://api.kroger.com/v1/locations?filter.zipCode.near=47408&filter.radiusInMiles=15&filter.chain=Kroger',headers=header_locations)
#     chain_loc = res.json()
#     print("locations ",res.status_code)
#     #print(chain_loc["data"])
#     ids = []
#     for i in chain_loc["data"]:
#         #print(i.keys())
#         #print(i['locationId'],i['address'])
#         ids.append(i['locationId'])
#     return ids

# def get_me_the_fuck_cheap(locations,access_token,term,brand):
#     res = ''
#     for id in locations:
#         header_cheap = {"Accept": "application/json","Authorization": "Bearer "+access_token}
#         get_me_the_url="https://api.kroger.com/v1/products?filter.brand="+brand+"&filter.term="+term+"&filter.locationId="+str(id)
#         #print(get_me_the_url)
#         #print("curl -X GET '"+get_me_the_url+"' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Authorization: Bearer "+ access_token)
#         res = requests.get(get_me_the_url,headers=header_cheap)
#         print("cheapo ",res.status_code)
#     data = res.json()
#     return data["data"][0]["productId"]
# #curl -X GET \
# #  'https://api.kroger.com/v1/locations?filter.zipCode.near=47408&filter.radiusInMiles=15&filter.chain=Kroger' \
# #  -H 'Accept: application/json' \
# #  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoiWjRGZDNtc2tJSDg4aXJ0N0xCNWM2Zz09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJjbGV2ZXJjYXJ0LWM0YTY4ZTI5ZjlhZmNjNDVmMmU1NjkwMmYwMTUxYzk5MTA3Mjg2NDgyMzYxMjExOTA4NiIsImV4cCI6MTY2Mjk0MzI5NywiaWF0IjoxNjYyOTQxNDkyLCJpc3MiOiJhcGkua3JvZ2VyLmNvbSIsInN1YiI6IjlkZWYyZDU5LTQwMTMtNWYyOS04NGRhLTU0YTRjMDY1OTNhMSIsInNjb3BlIjoicHJvZHVjdC5jb21wYWN0IiwiYXV0aEF0IjoxNjYyOTQxNDk3MjI2MzE5NjgxLCJhenAiOiJjbGV2ZXJjYXJ0LWM0YTY4ZTI5ZjlhZmNjNDVmMmU1NjkwMmYwMTUxYzk5MTA3Mjg2NDgyMzYxMjExOTA4NiJ9.pKmK0jLYfJoKQzVEGrTHWYtWinjH5ffNWTmS8Mx5vYsMdnbetAWr8ziYC-qVAQwSgXq9EkjD_itPvmfUkaqIiazoAAHBlIfg5ebAletA06Rsj4SoIWgXZjFfGMViYjKYcn6kjJARZzzkSQGv7yHFxpn2BJNtjxuSPStCJ4PAGl_ruw0njQclzK_9dl8xLX2wYeX9h0OkkIGRuKArHbsMkwb4HPud2Ufg994VkyKJXYFPyxbJuvXHdGTCt_7Dt1vNTgFTIGMg9zMn3IcEbocIyRXDRK15JZlUshA5wHWEZ9FwM1UkGOl2cSTN0rCutmFUAr_ceQ6UXt-rrduoVG3SyQ'
# def fuckin_cheap_value(prod,access_token,location):
#     # https://api.kroger.com/v1/products/{{ID}}?filter.locationId={{LOCATION_ID}}' \
#     header_cheap = {"Accept": "application/json","Authorization": "Bearer "+access_token}
#     get_me_the_url="https://api.kroger.com/v1/products/"+str(prod)+"?filter.locationId="+str(location)
#         #print(get_me_the_url)
#         #print("curl -X GET '"+get_me_the_url+"' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Authorization: Bearer "+ access_token)
#     res = requests.get(get_me_the_url,headers=header_cheap)
#     print("priceo ",res.status_code)
#     data = res.json()
#     #print(data["data"]["items"][0]["price"])
#     return data["data"]["items"][0]["price"]
#     #return data["data"]["items"]
#     #return data["data"][0]["productId"]
# access_token=get_me_the_fuck_in()
# locs = get_me_the_fuck_locations(access_token)
# print(locs)
# productid = get_me_the_fuck_cheap(locs,access_token,'chocolate','Kroger')
# print(fuckin_cheap_value(productid,access_token,locs[0]))

# @app.get('/kroger')
# def list_of_items():
#    item = request.args.get('item')
#    #access_token=get_me_the_fuck_in()
#    #locs = get_me_the_fuck_locations(access_token)
#    productid = get_me_the_fuck_cheap(locs,access_token,item,'Kroger')
#    return_value = fuckin_cheap_value(productid,access_token,locs[0])
#    return {"programming_languages":list(return_value.values())}
#    #return {"cost": list(productid)}
# print()
# #print("curl -X POST 'https://api.kroger.com/v1/connect/oauth2/token' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Authorization:"+ code_it+"' -d 'grant_type=client_credentials&scope=product.compact' ")