import os

class Config:
	SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	#SECRET_KEY = os.environ.get('SECRET_KEY')
	#SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'sanrast06@gmail.com'
	MAIL_PASSWORD = 'rastogi06'