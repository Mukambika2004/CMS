import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')

    # Azure Blob Storage Configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT', 'kewudacityproject1')
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY',
        'K1n0rJ7oNhaafo9+XyghbD8BqI7aq6J/ZX55cYF1fSyvDYYyIXdVV1rhGfHPXYdPsziN3pmMYoJiAzoQtnmSUw=='
    )
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER', 'images')

    # Azure SQL Information
    SQL_SERVER = os.environ.get('SQL_SERVER', 'kew-udacity-project1.database.windows.net')
    SQL_DATABASE = os.environ.get('SQL_DATABASE', 'udacity-project1')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME', 'udacityadmin')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD', '**put your own here****')

    # Correct SQLAlchemy connection string
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/"
        f"{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_SECRET = ".9dzHDnmAt2.yAPk15x8dS2S~JY9y.3.p4"
    AUTHORITY = "https://login.microsoftonline.com/common"
    CLIENT_ID = "59b7e302-a779-4c5a-b1b6-efb3d1bf2934"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"  # Token cache storage
