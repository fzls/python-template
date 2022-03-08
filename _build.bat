python -m venv .venv
call .venv\Scripts\activate

pip install -i https://pypi.doubanio.com/simple pyinstaller wheel
pip install -i https://pypi.doubanio.com/simple -r requirements.txt

pyinstaller --name main.exe -F main.py
