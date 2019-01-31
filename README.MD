install :

git clone https://github.com/yayassktas/mac1.git

cd mac1

pip install virtualenv

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

python3 main.py
