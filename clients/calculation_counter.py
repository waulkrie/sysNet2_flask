# this file is to count the number of calculations

import requests

def cnt_calc(hostname: str = "localhost"):
    try:
        response = requests.get(f"http://{hostname}:5000/api/history")
        print(response.status_code)
        if response.status_code == 200:
            return response.json()
        else:
            return False
    except:
        print ("Exception in cnt_calc")
        return False
    
if __name__ == "__main__":
    cnt = cnt_calc()
    if cnt:
        print (f"Number of calculations: {len(cnt)}")
    else:
        print ("API is not available")