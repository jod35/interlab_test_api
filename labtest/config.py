class DevConfig:

    #database connection string
                             #database+driver:username:password/database_name  
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://jon:nathanoj35@localhost/labtest'
    # SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    SECRET_KEY='@#$@#jn4j2n4ijio24234@$@3423423uy85823yu'
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=True #turn to False in Production
