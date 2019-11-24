Installation Procedure

Create a virtual Enviiornment python3.7
	install pip
	for Linux user:
		In command line use following command:
			pip install virtualenv
			virtualenv -p python3 venv
		activate virtual env
			source venv/bin/activate
	        for windows user:
		    In command line use following commands:
			install pip
			virtualenv venv
		    activate virtual env
		   	venv\Scripts\activate
install packages using command 
	pip install -r requirement.txt
then run application using
	python manage.py runserver
now go to browser and open localhost:8000