*** Settings ***
Resource  resource.robot
Resource    login.robot
Resource    home.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  miumiu
    Set Password  miumiu123
    Set Password Confirmation  miumiu123
    Submit Registeration Credentials
    Registeration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  i
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registeration Credentials
    Registeration Should Fail With Message  Username or password is too short


Register With Valid Username And Too Short Password
    Set Username  kisu
    Set Password  k12
    Set Password Confirmation  k12
    Submit Registeration Credentials
    Registeration Should Fail With Message  Username or password is too short  


Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kisu
    Set Password  kisukisukisu
    Set Password Confirmation  kisukisukisu
    Submit Registeration Credentials
    Registeration Should Fail With Message  Password should not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kisu
    Set Password  kisukisu123
    Set Password Confirmation  kisukisu145
    Submit Registeration Credentials
    Registeration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registeration Credentials
    Registeration Should Fail With Message  User with username kalle already exists

Login After Successful Registeration
    Set Username  miumiu
    Set Password  miumiu123
    Set Password Confirmation  miumiu123
    Submit Registeration Credentials
    Registeration Should Succeed
    Go To Main Page
    Submit Logout
    Title Should Be  Login
    Set Username  miumiu
    Set Password  miumiu123
    Submit Credentials
    Title Should Be  Ohtu Application main page

Login After Failed Registeration
    Set Username  kisu
    Set Password  kisukisu123
    Set Password Confirmation  kisukisu145
    Submit Registeration Credentials
    Registeration Should Fail With Message  Password and password confirmation do not match
    Submit Login
    Title Should Be  Login
    Set Username  kisu
    Set Password  kisukisu123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Register Page
  Reset Application
  Create User  kalle  kalle123
  Go To  ${REGISTER_URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Set Password Confirmation
    [arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Registeration Credentials
    Click Button  Register

Registeration Should Succeed
   Title Should Be  Welcome to Ohtu Application!

Registeration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Page Should Be Open
    Title Should Be    Register

Go To Main Page
    Go To  ${OHTU_URL}

Submit Logout
    Click Button  logout

Submit Login
    Click Link  Login

Submit Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


    