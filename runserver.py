import os
ip = input('ip:')
port = input('port:')
if ip:
    if port:
        os.system(f'python manage.py runserver {ip}:{port}')
    else:
        os.system(f'python manage.py runserver {ip}:8000')
else:
    os.system('python manage.py runserver 8080')