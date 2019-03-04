
from sqlalchemy import create_engine, DateTime, Date
from sqlalchemy.orm import sessionmaker

connection_string = 'postgresql://{user}:{pswd}@{host}:{port}/{db}'.format(
    user='postgres',
    pswd='123',
    host='localhost',
    port='5432',
    db='mydb',
)


def json_dumps_default(val):
    if False: pass
    elif isinstance(val, DateTime):
        return val.strftime("%Y-%m-%d %H:%M:%S %z") #convert datetime with timezone to string ref. https://stackoverflow.com/a/43414711/248616
    elif isinstance(val, Date):
        return val.strftime("%Y-%m-%d")
    else:
        return str(val)


def json_dumps(d):
    import json
    return json.dumps(d, default=json_dumps_default)


engine = create_engine(connection_string, json_serializer=json_dumps) #config engine to decode jsonb value as datetime ref. https://stackoverflow.com/a/36438671/248616
Session = sessionmaker(bind=engine)


#util
class DbUtil:
    from contextlib import contextmanager

    @classmethod
    @contextmanager #this helps to get around the error 'AttributeError: __exit__' #TODO why is that?
    def get_session(cls):
        """
        IMPORTANT NOTE
        we are creating a python generator ref. https://stackoverflow.com/a/231855/248616, NOT a normal method
        *yield* is used in place of *return* #TODO master this point, what the h*** is this ^^?
        """
        session = Session(expire_on_commit=False)
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


    @classmethod
    def insert(cls, model_instance):
        with cls.get_session() as session:
            session.add(model_instance)
            session.commit()
            session.refresh(model_instance)
            return model_instance


    @classmethod
    def update(cls, model_instance):
        """
        In sqlalchemy, update+insert are same when saving to db
        """
        with cls.get_session() as session:
            session.add(model_instance)
            session.commit()
            session.refresh(model_instance)
            return model_instance

