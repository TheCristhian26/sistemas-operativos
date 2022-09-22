@echo off
set /p letra=letra_unidad
set /p formato=formato_unidad
set /p label=Nombre_De_La_unidad
format %letra%: /FS:%formato% /V:%label% /q
pause