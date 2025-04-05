# settings.py

# Email configuration for development (print the email to the console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# In prouduction, you would typically use a real email backend like SMTP or a third-party service.
# Email_BACCKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.example.com'
# EMAIL_PORT = 587
# Email_USE_TLS = True
# Email_HOST_USER = 'your_username'
# Email_HOST_PASSWORD = 'your_password'