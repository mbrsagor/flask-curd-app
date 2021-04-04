# Flask-curd-app
> The project in a flask curd app with restful API.

##### Prerequisites
- At lest Python clear concept.
- Frontend like HTML5, CSS3, Bootstrap.
- Basic Database

#### Install project on your local development server.
1st make sure in your system install python3.8 and virtualenv. Then open your terminal and please follow the instructions.

```base
git clone https://github.com/mbrsagor/flask-curd-app.git
cd flask-crud-app
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Migarte `sqlite.db` 
Active your virtualenv then open shell after that, follow the commands

```python
from models import db
db.create_all()
```

### Others requirements
> If you set globally add to command line options flask automatifally run and reset server.
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Install SQL db
```base
pip install Flask-SQLAchemy 
```