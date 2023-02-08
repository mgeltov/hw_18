class Config(object):
    DEBUG = False
    SECRET_HERE = '1111'
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/movies.db"  # и здесь не нужно будет прописывать полный путь instance/
    SQLALCHEMY_TRACK_MODIFICATION = False
