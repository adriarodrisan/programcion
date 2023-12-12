@ echo off

:inicio
	echo 1 Hora
	echo 2 versio
	echo 3 ip
	echo 4 procesos
	echo 5 salir
	
	SET /p var= ^> Seleccione una opcion [1-5]:
	
	if "%var%"=="0" got inicio
	if "%var%"=="1" got hora
	if "%var%"=="2" got version
	if "%var%"=="3" got ip
	if "%var%"=="4" got procesos
	if "%var%"=="5" got salir
	
:hora
	hora.bat
	goto inicio
:version
	version.bat
	goto inicio
:ip
	ip.bat
	goto inicio
:procesos
	procesos.bat
	goto inicio
:salir
	@cls
echo on
