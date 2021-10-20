planetplanet
============

What's this
:::::::::::

This is so called 'PlanetPlanet' RSS aggregation site powerd by Django.

License
:::::::

This product distributed under MIT License.

How to use
:::::::::::

::

   $ git clone git@github.com:nakagami/planetplanet.git
   $ cd planetplanet
   $ python3 -mvenv venv
   $ source venv/bin/activate
   (venv) $ pip install -r requirements.txt
   (venv) $ python manage.py migrate
   (venv) $ python manage.py collectstatic
   (venv) $ python manage.py reatesuperuser
   (venv) $ python manage.py runserver

   ... Logged in Django admin & Add Rss feed URL

   (venv) $ python manage.py syncrss
