all:

run: 
	python manage.py runserver

migrations:
	python manage.py makemigrations
	
migrate:
	python manage.py migrate

compose: 
	docker-compose up --build

compose-up:
	docker-compose up