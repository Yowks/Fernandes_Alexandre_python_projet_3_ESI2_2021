create:
	python3 -m venv convertisseur

activate:
	cd bin source activate

run: 
	python3 main.py

requires:
	pip3 install -r requirements.txt