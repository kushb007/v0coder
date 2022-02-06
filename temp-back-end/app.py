import requests
import time
filename = "./b.wav"
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
headers = {'authorization': "d5086660044c456f8645a3a38e517c0b"} 
response = requests.post('https://api.assemblyai.com/v2/upload',
                        headers=headers,
                        data=read_file(filename))
print(response.json())
endpoint = "https://api.assemblyai.com/v2/transcript"
json = { "audio_url": response.json()['upload_url'] }
headers = {
    "authorization": "d5086660044c456f8645a3a38e517c0b",
    "content-type": "application/json"
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())
print("yo")
time.sleep(10)
endpoint = "https://api.assemblyai.com/v2/transcript/"+str(response.json()['id'])
headers = {
    "authorization": "d5086660044c456f8645a3a38e517c0b",
}
response = requests.get(endpoint, headers=headers)
print(response.json())
