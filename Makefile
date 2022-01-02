docker_run = docker-compose run --rm api sh -c
runserver:
	docker-compose up
test:
	echo "run django test"
	$(docker_run) "python manage.py test && flake8"

create_app:
	$(docker_run) "python manage.py startapp $(apps)"

makemigrations:
	$(docker_run) "python manage.py makemigrations $(apps)"

migrate:
	$(docker_run) "python manage.py migrate $(apps)"

create_superuser:
	$(docker_run) "python manage.py createsuperuser"