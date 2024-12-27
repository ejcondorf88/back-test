# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres.tbkijdkppdrrgsyudtut:Mejia2523658!@aws-0-us-west-1.pooler.supabase.com:6543/postgres')  # Default: SQLite si no está definida la var
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
