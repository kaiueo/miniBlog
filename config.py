import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MINIBLOG_MAIL_SUBJECT_PREFIX = '[miniBlog]'
    MINIBLOG_MAIL_SENDER = 'miniBlog Admin'
    MINIBLOG_ADMIN = os.environ.get('MINIBLOG_ADMIN')
    MINIBLOG_POST_PER_PAGE = os.environ.get('MINIBLOG_POST_PER_PAGE') or 10
    MINIBLOG_FOLLOWERS_PER_PAGE = os.environ.get('MINIBLOG_FOLLOWERS_PER_PAGE') or 10
    MINIBLOG_COMMENTS_PER_PAGE = os.environ.get('MINIBLOG_COMMENTS_PER_PAGE') or 10

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
