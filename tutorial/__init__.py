from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import Session, Base

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    Session.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings,
                          root_factory='tutorial.models.Root')
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('adminPanel', '/adminPanel')

    #product routes
    config.add_route('productInsert','/productInsert')
    config.add_route('productList','/productList')
    config.add_route('productEdit', '/productList')
    config.add_route('productDel', '/productList')

    config.add_route('reg','/reg')
    config.add_route('login', '/login')
    # config.add_route('logout', '/logout')
    config.add_static_view(name='templates',path='tutorial:templates')
    config.scan('.views')
    return config.make_wsgi_app()