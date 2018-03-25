@ECHO Off 
REM windows install dependencies with command prompt
ECHO Installing Dependencies for you
python -m pip install --upgrade pip
pip install django==1.11
pip install djangorestframework
pip install coreapi