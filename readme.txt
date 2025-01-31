### Python API Automation Framework

Hybrid Custom API Automation Framework include the proper folder structure

![Screenshot 2024-08-05 at 08 18 38](https://github.com/user-attachments/assets/3c7d5fe5-207a-42e7-84fe-f4d53354d987)

Tech Stack
- Python 3.12
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure Report, PyTest HTML
- Test Data - CSV, Excel, JSON, Faker
- Advance API Testcase - jsonschema
- Parallel Execution - x distribute (xdist)

How to Install Packages
```
pip install requests pytest pytest-html faker allure-pytest jsonschema
```

How to run your Testcase Parallel
```pip install pytest-xdist ```


How to run the Basic Test with Allure report

```
 pytest tests/tests/crud/test_create_booking.py  --alluredir=allure_result -s
```
pip freeze > requirements.txt
python -m pip install python-dotenv
pip install pandas
@pytest.parameterize
use MySql connector in python get them as strimng and verify them with json response
