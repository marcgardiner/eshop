# shop based on Django

Here is some more detailed information about the scripts I have written.
If you would like to make any comments then please feel free to email me at servicemanager@easy.com.

- Shop based on Django 1.8.6
- Pillow library
- Asynchronous and distributed task queue: Celery 3.1.18
- Monitoring Celery Flower
    as a note:  in terminal
                pip install flower
                celery -A <appname> flower
                browsing http://ipaddress:5555/dashboard
                For more information about flower, please navigate to http://flower.readthedocs.io/en/latest/config.html.
- Message broker: RabbitMQ 3.6.9
    as a note: enable rabbitmq plugins for GUI management
                rabbitmq-plugins enable rabbitmq_management
                browsing http://ipaddr:15672/
                    credential info: guest/guest


