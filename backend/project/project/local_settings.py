SECRET_KEY = 'aSerTUrFdEwQwEQjuW#%!6``6(*)*34r%xzbohm(u#9i@=0et2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'health_tracker_database',
        'HOST' : 'localhost',
        'PORT' : '3306',
        'USER' : 'root',
        'PASSWORD' : 'root',
        
    }
}

# # # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-5lbu#t^k8iotdksrqm15&$@8)@qrmtd$0d^cgla3ox+q9pf(%u'