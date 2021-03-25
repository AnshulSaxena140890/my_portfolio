Commands Run for the project:

sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx

Setting Postgres DB:

sudo -u postgres psql
CREATE DATABASE my_portfolio;
CREATE USER my_portfolio_user WITH PASSWORD 'my_portfolio_password';
GRANT ALL PRIVILEGES ON DATABASE my_portfolio TO my_portfolio_user;

pip install django gunicorn psycopg2

