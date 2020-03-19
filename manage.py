#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask_script import Server, Manager, Shell, prompt_bool
from flask_migrate import Migrate, MigrateCommand
from flask import url_for
from sqlalchemy_utils.functions import create_database, database_exists
from chadevmonster import db
from chadevmonster import app
from chadevmonster.models.article import Article

migrate = Migrate(app, db)
manager = Manager(app)
db_manager = Manager(usage='Perform database operations')


def _make_context():
    return dict(app=app, db=db, Article=Article)


@manager.command
def create_db():
    '''Creates database if it doesn't exist.'''
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(db_uri):
        print('Creating database ...')
        create_database(db_uri)
        # db.create_all()
    else:
        print('Database already exists. Nothing to create.')


manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)


port = int(os.environ.get('PORT', 5000))
manager.add_command('runserver', Server(use_debugger=True, use_reloader=True, host='0.0.0.0', port=port))


@db_manager.command
def drop():
    '''Drops database tables'''
    if prompt_bool('Are you sure you want to lose all your data'):
        db.drop_all()
        print('Database tables dropped!')


@db_manager.command
def create(default_data=True, sample_data=False):
    '''Creates database tables from sqlalchemy models'''
    db.configure_mappers()
    db.create_all()
    print('Database tables created!')


@db_manager.command
def recreate(default_data=True, sample_data=False):
    '''Recreates database tables (same as issuing 'drop' and then 'create')'''
    drop()
    create(default_data, sample_data)


manager.add_command('database', db_manager)


@manager.command
def init_db():
    '''
    Drops and re-creates the SQL schema
    Ran by: python manage.py init_db
    '''
    db.drop_all()
    db.configure_mappers()
    db.create_all()
    db.session.commit()


@manager.command
def routes():
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = f'[{arg}]'
        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote(f'{rule.endpoint:25s} {methods:25s} {url}')
        output.append(line)

    for line in sorted(output):
        print(line)


@manager.command
def test():
    '''Run the unit tests
    Ran by: python manage.py test
    '''
    import unittest
    import sys

    tests = unittest.TestLoader().discover('tests')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    if results.failures or results.errors:
        sys.exit(1)


@manager.command
def cov():
    import coverage
    import unittest

    '''Runs the unit tests with coverage.
    Ran by: python manage.py cov
    '''
    cov = coverage.Coverage(branch=True, source=['./chadevmonster'])
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    try:
        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'coverage')
        cov.html_report(directory=covdir)
    except coverage.misc.CoverageException as e:
        print(e)
    cov.erase()


if __name__ == '__main__':
    manager.run()
