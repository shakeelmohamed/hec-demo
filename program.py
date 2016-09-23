from subprocess import Popen, PIPE
import os
import requests
import json

def main():
    proccess = Popen("imagesnap -q && jp2a --width=128 snapshot.jpg", stdout=PIPE, shell=True)
    proccess.wait()
    data =  proccess.stdout.read()

    uri = os.environ["HEC_URI"]
    token = os.environ["HEC_TOKEN"]

    req = requests.post(
        "%s/services/collector" % uri,
        headers= {
            "Authorization": "Splunk %s" % token
        },
        data=json.dumps({
            'event': data
        })
    )

    print req.text

if __name__ == '__main__':
    main()