The `FunctionalTestAutomation` is a Python-based test automation framework designed to perform functional testing of OrangeHRM demo application. 
It uses Selenium for browser automation and Pytest for test execution and reporting. Below are the key components and features of the project:

### Key Features:
1. **Test Execution**:
   - Tests are executed using Pytest, which provides flexibility for parameterization, fixtures, and hooks.
   - Command-line options allow customization, such as specifying user roles (`--user_role=admin`) or generating HTML reports.

2. **Browser Automation**:
   - Selenium WebDriver is used for automating browser interactions.
   - The framework includes methods for logging in, navigating pages, and validating functionality.

3. **Parameterized Testing**:
   - The `conftest.py` file includes a `pytest_addoption` method to add custom command-line options for user roles.
   - Fixtures like `setup` handle browser initialization and login based on the specified user role.

4. **Error Handling and Reporting**:
   - Screenshots are captured automatically when a test fails, providing visual evidence of the failure.
   - HTML reports are generated using Pytest plugins, summarizing test results.


5. **Directory Structure**:
   - Screenshots are saved under the `functionalTestAutomation->screenshot` directory.
   - Reports are generated in the `tests/report.html` file.
   - Test files are organized under the `tests` directory
   - uitlity functions are placed in the `functionalTestAutomation/test/utils.py` file.
   - Page classes are organized in the `functionalTestAutomation/Pages` directory.
   - Configuration files are located in the `functionalTestAutomation/config` directory.
   - The main test file is `test_functionality.py`, which contains the actual test cases.
   - The `conftest.py` file is used for defining fixtures and hooks that are shared across multiple test files.
   - The `requirements.txt` file lists all the dependencies required for the project, making it easy to set up the environment.
   - The `README.md` file provides an overview of the project, including its purpose, features, and how to run tests.
   - Log files are stored in the `functionalTestAutomation/logs` directory, which helps in debugging and tracking test execution.

### Workflow:
1. **Setup**:
   - The `setup` fixture initializes the browser and logs in based on the user role.
   - The `web_url` configuration specifies the application URL.

2. **Test Execution**:
   - Tests are run using commands like:
     ```bash
     pytest test_functionality.py -s -v
     ```
   - For admin-specific tests:
     ```bash
     pytest --user_role=admin -s -v --html=report.html
     ```

3. **Reporting**:
   - HTML reports are generated using the `--html` option.
   - Reports include test results, sorted and filtered using JavaScript modules.

4. **Failure Handling**:
   - Screenshots are captured and saved in the `screenshot` folder when tests fail.

### Technologies Used:
- **Python**: Core language for test scripts and framework logic.
- **Selenium**: Browser automation.
- **Pytest**: Test execution and reporting.
- **HTML**: Report generation.
- **Faker**: Data generation for tests.

### Commands:
- Run tests: `pytest test_functionality.py -s -v`
- Generate report: `pytest test_functionality.py -s -v --html=report.html`
- Run tests with admin role: `pytest --user_role=admin -s -v --html=report.html`

This project is designed to streamline functional testing, providing robust reporting and debugging capabilities.


to run the test file text_transactions.py use below command

cd tests
pytest test_functionality.py -s -v

To generate report run with
pytest text_test_functionality.py -s -v --html=report.html
it will generate a report folder under tests package.

To run the test with user_role as admin use below command

pytest --user_role=admin -s -v --html=report.html

