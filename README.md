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
- Source the virtual environment and run migrations.
```
source venv/bin/activate
python -m django migrate
python -m django migrate portfolios
```
- Create superuser
```
python -m django createsuperuser
```
- Run the development server
```
python -m django runserver
```
