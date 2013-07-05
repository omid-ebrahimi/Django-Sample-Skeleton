@echo off
set VIRTUAL_ENV=H:\Web-Programming\Python\Practices\Books\Virtual-Environment

if not defined PROMPT (
    set PROMPT=$P$G
)

if defined _OLD_VIRTUAL_PROMPT (
    set PROMPT=%_OLD_VIRTUAL_PROMPT%
)

if defined _OLD_VIRTUAL_PYTHONHOME (
     set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%
)

set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(Virtual-Environment) %PROMPT%

if defined PYTHONHOME (
     set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
     set PYTHONHOME=
)

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%; goto SKIPPATH

set _OLD_VIRTUAL_PATH=%PATH%

:SKIPPATH
set PATH=%VIRTUAL_ENV%\Scripts;%PATH%

:END
