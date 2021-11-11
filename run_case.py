import datetime
import os.path
import pytest


if __name__ == "__main__":
    case_list = [
        "./test_case"
    ]
    for case in case_list:
        date = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')
        # pytest.main([case])
        fath = os.path.join("./report/report_" + date + ".html")
        pytest.main(["--html={}".format(fath), case])
