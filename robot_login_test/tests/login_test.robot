*** Settings ***
Library    SeleniumLibrary
Resource          ../resources/keywords.resource
Variables         ../variables/config_variables.py

*** Test Cases ***
Login Test
    Open Browser    ${LOGIN_URL}    Chrome   
    Input Text    id=id    id 
    Input Text    id=pw    password
    Click Button    id=log.login
    #Page Should Contain    Welcome, testuser
    #Close Browser