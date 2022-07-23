# financial-advisor-python
Financial-advisor implementation in Python/Django.

## Development
- Create a virtual environment
```
python3 -m venv venv
```
- (Optional) Change database password in `docker/postgres/init.sql` and `financialadvisor/settings.py`
- Create and init dev environmente containers
```
docker compose up -d
```
- Source the virtual environment, install dependencies, and run migrations.
```
source venv/bin/activate
pip install -r requirements.txt
export DJANGO_SETTINGS_MODULE=financialadvisor.settings
python -m django migrate
```
- Create superuser
```
python -m django createsuperuser
```
- Run the development server
```
python -m django runserver
```
