import requests

'''
url = "https://buscacepinter.correios.com.br/app/endereco/carrega-cep-endereco.php"

payload = {
   "documentId":"FACDDFE0F80FA9FF529EF26FD449D2BE",
   "documentLifecycle":"active",
   "frameId":0,
   "frameType":"outermost_frame",
   "initiator":"https://buscacepinter.correios.com.br",
   "method":"POST",
   "parentFrameId":-1,
   "requestHeaders":[
      {
         "name":"sec-ch-ua",
         "value":"\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\""
      },
      {
         "name":"content-type",
         "value":"application/x-www-form-urlencoded; charset=UTF-8"
      },
      {
         "name":"Cache-Control",
         "value":"no-store, no-cache, must-revalidate"
      },
      {
         "name":"sec-ch-ua-mobile",
         "value":"?0"
      },
      {
         "name":"User-Agent",
         "value":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
      },
      {
         "name":"sec-ch-ua-platform",
         "value":"\"Linux\""
      },
      {
         "name":"Accept",
         "value":"*/*"
      }
   ],
   "requestId":"4580",
   "tabId":512694328,
   "timeStamp":1689122386134.9722,
   "type":"xmlhttprequest",
   "url":"https://buscacepinter.correios.com.br/app/endereco/carrega-cep-endereco.php"
}
'''

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaCep.cfm"

payload = {
    "relaxation": "78135420",
    "tipoCEP": "ALL",
    "semelhante": "N"
}

response = requests.post(url, data=payload)

with open('correios_2.html', 'w') as f:
    f.write(response.text)