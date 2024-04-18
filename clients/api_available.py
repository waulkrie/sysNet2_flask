# this file is used to check if the API is available

import requests

def ping_api(hostname: str = "localhost"):
    try:
        response = requests.get(f"http://{hostname}:5000/api/history")
        print(response.status_code)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        print ("Exception in ping_api")
        return False
    
    
if __name__ == "__main__":
    isAvail = ping_api()
    if isAvail:
        print ("API is available")
    else:
        print ("API is not available")
