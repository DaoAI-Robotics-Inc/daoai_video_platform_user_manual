@echo off
cd /d "%~dp0"

rem 2) 构建
call make latex

@REM rem 3) 进入输出目录
cd _build\latex

@REM rem 4) 编译两次
lualatex --interaction=nonstopmode --shell-escape daoai.tex
lualatex --interaction=nonstopmode --shell-escape daoai.tex

for /f %%i in ('wmic os get LocalDateTime ^| find "."') do set "LDT=%%i"
set "TODAY=%LDT:~0,4%-%LDT:~4,2%-%LDT:~6,2%"

rem 6) 重命名（如已存在同名先删）
if exist "DaoAI_Video_Platform_User_Manual_%TODAY%.pdf" del /f /q "DaoAI_Video_Platform_User_Manual_%TODAY%.pdf"
ren "daoai.pdf" "DaoAI_Video_Platform_User_Manual_%TODAY%.pdf"

rem 7) 回到原目录（可选）
cd ..\..