
from flask import Flask

from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy

from flask_mail import Mail

from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
# from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_login import LoginManager

#Registering our login functions
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



db = SQLAlchemy() # an instance
mail= Mail()


# photos = UploadSet('photos',IMAGES)
def create_app(config_name):

    app = Flask(__name__)
    mail.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    # app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ahutdjtnbfddfq:cd782ccfb813ee005fb002b65c80cbfcf358ca887ece323e9971f2e92aa4eb51@ec2-44-196-223-128.compute-1.amazonaws.com:5432/d7m7331srjqb1m'
    


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # # configure UploadSet
    # configure_uploads(app,photos)
    
    # Registering the blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authentication')
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    
      # setting config
    from .requests import configure_request
    configure_request(app)
  
  
    return app
