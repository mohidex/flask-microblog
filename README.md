# Flask Microblog

A full featured blog application using :snake: Python Flask framework where an authenticated user can create a new post in markdown. A user can update and delete his/her post. An user can follow/unfollow other user and only see the post he/she follwing in his/her home page.

---

**Live Demo**: [Demo](http://awesome-blogging.herokuapp.com/)

**Some Screenshot**: [Screenshot](some-cool-features.md)

## Running the application

***Clone the repository***

```bash
git clone https://github.com/ifat-mohit/flask-microblog.git
```

***Install virual environment and all necessary dependencies***
```bash
pip install -r requirements.txt
```
***Configure environment variables***

Create a `.env` file in root directory
```sh
SECRET_KEY=<your-secret-key>
# Database Url
SQLALCHEMY_DATABASE_URI=<database-url>
# Server configuration
MAIL_SERVER=<your-mail-server>
MAIL_PORT=<mil-port>
MAIL_USE_TLS=<True/False>
MAIL_USERNAME=<your-mail-address>
MAIL_PASSWORD=<your-mail-password>
# Email list of admins
ADMINS=[list of admiin mail address]
# Elastic search url
ELASTICSEARCH_URL=<elastic-search-host:port>
```

***Migrate the database***

```bash
flask db upgrade
```
***Test***

```bash
python tests.py
```

***Run***
```bash
# Turn on elastic search server(Ubuntu/Debian)
sudo -i service elasticsearch start
export FLASK_DEBUG=1                  # Debug mode on
flask run 
```
Then visit `http://localhost:5000` :rocket: enjoy the app.
