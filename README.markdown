# Django-Heroku-BoilerPlate

## Rationale
This is all it takes to push to a heroku app repo.
This project is good for you if you:
- Like heroku(obviously)
- Like django
- Like sass
- Like shpaml

## How to use this
The flow goes like this

#### In some dir you have to have this folders
    bin include lib your_project Procfile requirements.txt

#### Those folders include the virtualenv folders generated with this line
    virtualenv --no-site-packages .

#### Install this packages, to run in heroku
    pip install Django pyscopg2

#### Freeze those packages in file needed by heroku
    pip freeze > requirements.txt

#### Create the Procfile that heroku executes to run actually your app
    web: example/manage.py runserver 0.0.0.0:$PORT --noreload

#### Create a nice git repo
    git init

#### Include in your .gitignore these lines, heroku generates its own version of them, i've done this for you already
    bin/
    include/
    lib/
    *.pyc

#### Add everything and commit
    git add .
    git commit -a -m 'first commit'

#### I use rvm to manage my Ruby rubies, because the heroku commands are rubies, but you can install the heroku-cli https://github.com/heroku/heroku
    rvm use ruby-1.9.2

#### The heroku-toolbelt allows you to create apps using your heroku account in the cedar stack, this stack handles non-ruby apps
    heroku create --stack cedar

Run locally your django_project and if it all went well...

#### Push to heroku!
    git push heroku master

Now heroku can use postgresql as db backend, right now it uses sqlite3 and works out of the box
but for some more serious use you might want to uncomment the postgresql lines and sync your db
    heroku run bin/python django_project/manage.py syncdb

