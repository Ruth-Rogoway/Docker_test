import requests
import time

url = "http://flask-todo:5000/add"
data = {"title": "Auto test item"}

print("Starting test... waiting for web service")

# ניסיון חיבור חוזר
for i in range(10):
    try:
        response = requests.post(url, data=data, timeout=5)
        if response.ok:
            print("✅ Test passed! POST /add succeeded")
            exit(0)
        else:
            print(f"❌ Bad response: {response.status_code}")
    except Exception as e:
        print("Web not ready yet, retrying...")
        time.sleep(3)

print("❌ Test failed - could not reach Flask app")
exit(1)
