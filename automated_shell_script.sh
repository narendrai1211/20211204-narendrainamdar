mkdir automated_deploy
cd automated_deploy
git clone https://github.com/narendrai1211/20211204-narendrainamdar.git
sudo apt-get update
sudo apt-get install python3
sudo apt install python3-pip
sudo apt install virtualenv
virtualenv --version
virtualenv 20211204_narendrainamdar_venv
virtualenv -p /usr/bin/python3 20211204_narendrainamdar_venv
source 20211204_narendrainamdar_venv/bin/activate
pwd
cd 20211204-narendrainamdar
pip3 install -r requirements.txt
python3 main.py
echo 'Showing the output file'
cat output_file.csv
echo 'We are done Thank you!'
