@echo off

set OC_LICENSE=OTVB.uni_Magdeburg_IESK.lic

REM :: -e erase logfiles at startup
REM :: -s0 severity level of logged messages (0-6)
REM :: path to ccxml-file
REM ot_ccxml_interpreter -e Files/simple.ccxml

@REM chdir Optimtalk
@REM ot_vxml_interpreter.exe -e Files/menu.vxml
@REM ot_vxml_interpreter.exe -e ../../Weihnachtsmarkt.vxml 
pushd ..\Dialogmanager\Optimtalk
ot_vxml_interpreter.exe -e ../../test_vxml/Files/dungeon.vxml
popd
PAUSE 

