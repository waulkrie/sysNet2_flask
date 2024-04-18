# this file is used to measure the latency of the API

import requests
import time

def latency(hostname: str = "localhost"):
    try:
        start = time.time()
        response = requests.get(f"http://{hostname}:5000/api/history")
        end = time.time()
        print(response.status_code)
        if response.status_code == 200:
            return end - start
        else:
            return False
    except:
        print ("Exception in latency")
        return False
    
if __name__ == "__main__":
    lat = latency()
    if lat:
        print (f"Latency: {lat}")
    else:
        print ("API is not available")
