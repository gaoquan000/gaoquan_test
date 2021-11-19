import datetime
import os.path
import pytest
import schedule
import time


def run_case():
    case_list = [
        "./test_case"
    ]
    for case in case_list:
        date = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')
        # pytest.main([case])
        fath = os.path.join("./report/report_" + date + ".html")
        pytest.main(["--html={}".format(fath), case])


schedule.every().day.at("10:00").do(run_case)
schedule.every().day.at("20:00").do(run_case)

while True:
    schedule.run_pending()
    time.sleep(1)
