docker_run = docker-compose run --rm api sh -c
test:
	echo "run django test"
	$(docker_run) "python manage.py test && flake8"

create_app:
	$(docker_run) "python manage.py startapp $(app)"

makemigrations:
	$(docker_run) "python manage.py makemigrations $(app)"
