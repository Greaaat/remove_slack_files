import requests
import json
import calendar
import sys
from datetime import datetime, timedelta

_token = sys.argv[1]

if __name__ == '__main__':
    files_list_url = 'https://slack.com/api/files.list'
    date = str(calendar.timegm((datetime.now() + timedelta(-30))
        .utctimetuple()))
    data = {"token": _token, "ts_to": date}
    response = requests.post(files_list_url, data = data)
    for f in response.json()["files"]:
        print "Deleting file " + f["name"] + "..."
        timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
        delete_url = "https://levatas.slack.com/api/files.delete?t=" + timestamp
        requests.post(delete_url, data = {
            "token": _token,
            "file": f["id"],
            "set_active": "true",
            "_attempts": "1"})
