@echo off

set NLM=^


set NL=^^^%NLM%%NLM%^%NLM%%NLM%


echo Select an action :%NL%1) Start Application %NL%2) Stop Application %NL%3) Build Application
set /P selection="Type your selection :"
CALL :CASE_%selection%
EXIT /B 0



:start
    echo "Application is starting. If image is not built already it will be build."
    docker compose up -d
    EXIT /B 0

:build
    docker build -t infinity .
    EXIT /B 0




:CASE_1
  CALL :start
  EXIT /B 0
:CASE_2
  docker-compose down
  EXIT /B 0
:CASE_3
  CALL :build
  EXIT /B 0

