import requests
from test_cases import Cases


test_data=Cases().test_cases
for case in test_data:
    c=test_data[case]
    result=requests.post("http://127.0.0.1:105/reservation",json=c).json()
    print(f"{case} : \n {result}")