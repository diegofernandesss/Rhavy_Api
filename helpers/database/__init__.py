from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#create the extension
db = SQLAlchemy()
migrate = Migrate()