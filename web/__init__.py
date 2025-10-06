from flask import Flask, redirect, url_for, request





def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    


    from .view import view
    from .api import api
    from .projects import projects

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(projects, url_prefix='/projects')

    @app.context_processor
    def inject_template_scope():
        injections = dict()
        
        def cookies_check():
            value = request.cookies.get('cookie_consent')
            return value
        injections.update(cookies_check=cookies_check)

        return injections
    
    return app

