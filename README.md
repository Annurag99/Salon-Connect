# Salon-Connect

Description: BeautySalonConnect is an appointment booking app for beauty salons, spas, and wellness centers. Users can schedule appointments for haircuts, massages, facials, and other beauty treatments, view stylist profiles, and receive notifications for upcoming appointments.
Key Features: Appointment booking for beauty services, stylist profiles, service menus, real-time availability, appointment reminders, customer reviews, and ratings.

# Tech Stack
```python
asgiref==3.4.1
Django==3.2.5
python-decouple==3.4
pytz==2021.1
sqlparse==0.4.1
Python
HTML
CSS
```

# Instructions for installation

```python
git clone https://github.com/Annurag99/Salon-Connect.git
```

```python
cd SalonConnect
```

```python
pip install virtualenv
```

```python
virtualenv env
```
or
```python
python3 -m venv env
```

# Mac/Linux
```python
source env/bin/activate
```

```python
pip install -r requirements.txt
```

```python
python3 manage.py makemigrations
```

If the above command throws an error update Pip and Setuptools
```python
pip install --upgrade pip setuptools
```

```python
python3 manage.py migrate
```

```python
python3 manage.py runserver 8080
```

To resolve the Invalid HTTP_HOST header error. You may need to add a host header 
example - 'd003a56484c942d88af2e1fc366a3f01.vfs.cloud9.eu-west-1.amazonaws.com'
to ALLOWED_HOSTS and CSRP_TRUSTED_ORIGINS inside the demo folder in the settings.py file.

# Admin Login

```python
python3 manage.py createsuperuser
Username: anuragsingh
Password: Admin@123
```
# Demo & Screenshots

