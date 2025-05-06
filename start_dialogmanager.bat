@echo off

set OC_LICENSE=OTVB.uni_Magdeburg_IESK.lic

REM :: -e erase logfiles at startup
REM :: -s0 severity level of logged messages (0-6)
REM :: path to ccxml-file
REM ot_ccxml_interpreter -e Files/simple.ccxml

chdir Optimtalk
ot_vxml_interpreter.exe -e Files/hello.vxml
PAUSE 

