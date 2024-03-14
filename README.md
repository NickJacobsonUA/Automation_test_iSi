# Automation_test_iSi

# To be able to use Allure reports you need:

1. Make sure Scoop is installed(Windows) / Homebrew for Mac/Linux
2. Make sure Java version 8 or above installed, and its directory is specified in the JAVA_HOME environment variable.
3. In a terminal, run this command
    
   "windows terminal" - scoop install allure
   
   "bash" - brew install allure 

4. Make sure allure is installed by using command in terminal

    allure version

# set the variable allure by running the command
    setx allure "C:\Users\iSi\scoop\apps\allure\current\bin"

# running tests + allure in the directory 
    pytest --alluredir=tests\allure_results .\tests\passengers_test.py

# Serving the completed tests from the dir into GUI report
    allure serve .\tests\allure_results\

# Adding all the requirements to the requirement file
    pip freeze > .\requirements.txt