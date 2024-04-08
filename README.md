# SalonConnect

SalonConnect is an appointment booking app for beauty salons, spas, and wellness centers. Users can schedule appointments for haircuts, massages, facials, and other beauty treatments and view stylist profiles.
Key Features: Appointment booking for beauty services, stylist profiles, service menus, real-time availability, appointment reminders emails, customer reviews, and ratings.

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
Username: salonadmin
Password: Admin@123
```
# Demo & Screenshots

Demo URL
```python
http://x23180013mysalon-env.eba-4wzwbr6m.eu-west-1.elasticbeanstalk.com/
```
Demo video URL
```python
youtube
```
Pages Screenshots

Home

<img width="1425" alt="Screenshot 2024-04-04 at 11 25 15 PM" src="https://github.com/Annurag99/Salon/assets/157478528/9f4d608c-1cd4-4026-ba60-10493e7b5a27">
<img width="1397" alt="Screenshot 2024-04-04 at 5 14 29 PM" src="https://github.com/Annurag99/Salon/assets/157478528/21c46580-7a88-4baa-a9fa-16a6571e9b58">
<img width="1397" alt="Screenshot 2024-04-04 at 5 14 39 PM" src="https://github.com/Annurag99/Salon/assets/157478528/f6fbd854-d69f-410d-bce4-f8feda129b2f">
<img width="1397" alt="Screenshot 2024-04-04 at 5 15 00 PM" src="https://github.com/Annurag99/Salon/assets/157478528/1a248700-98ed-4344-869a-860dc5fe5a83">
<img width="1397" alt="Screenshot 2024-04-04 at 5 15 09 PM" src="https://github.com/Annurag99/Salon/assets/157478528/f6aeb2d9-a515-4a95-ac5a-0a4e211e828f">

Login

<img width="1397" alt="Screenshot 2024-04-04 at 5 29 28 PM" src="https://github.com/Annurag99/Salon/assets/157478528/af49d824-e543-4978-8868-33215cf69823">

Appointment Page

<img width="1397" alt="Screenshot 2024-04-04 at 5 28 17 PM" src="https://github.com/Annurag99/Salon/assets/157478528/281f45cb-679b-4adf-a7c4-3ba46c4a1db8">

Admin Page

<img width="1208" alt="image" src="https://github.com/Annurag99/Salon-Connect/assets/157478528/6f9b0c23-f221-49b7-8a47-0ab77a55e04f">








