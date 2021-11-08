import datetime
import os.path
from  common import login
import pytest

if __name__ == "__main__":
    case_list=[
        # "./test_case/test_upload_case.py"
        "./test_case"
    ]
    date = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')
    for case in case_list:
        # pytest.main([case])
        fath = os.path.join("./report/report_"+date+".html")
        pytest.main(["--html={}".format(fath), case])
