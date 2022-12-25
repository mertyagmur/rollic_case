class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "\xe3\xa7R\x8b&m\xafd+l+\xb1\xe4<\xcex.\x9ec\x01\xc5v\xd0Y"

    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = f"postgresql://rollic:rollic123@pgsql:5432/rollic_case"

class TestingConfig(Config):

    SQLALCHEMY_DATABASE_URI = f"postgresql://rollic:rollic123@pgsql:5432/rollic_case"


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = f"postgresql://rollic:rollic123@pgsql:5432/rollic_case"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}