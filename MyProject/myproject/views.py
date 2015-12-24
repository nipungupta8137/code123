from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy import *

from .models import (
    DBSession,
    #MyModel,
    )

engine = create_engine('postgresql://tatomai:tatomai@10.29.55.54:5432/test1')

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        #one = DBSession.query(MyModel).filter(MyModel.username == 'one').first()
	connection = engine.connect()
        #result = connection.execute("select username from login")
        result = connection.execute("select name from employee")

        for row in result:
            print "username:", row['name']
        connection.close()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    #return {'one': one, 'project': 'MyProject'}
    return {'one': '1', 'project': 'MyProject'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_MyProject_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.


DROP TABLE employee;
CREATE TABLE employee (
     ID         int,
     name       varchar(10),
     salary     real,
     start_date date,
     city       varchar(10),
     region     char(1)
);



insert into employee (ID, name,    salary, start_date, city,       region)
values (1,  'Jason', 40420,  '02/01/94', 'New York', 'W');

insert into employee (ID, name,    salary, start_date, city,       region)
values (2,  'Robert',14420,  '01/02/95', 'Vancouver','N');

insert into employee (ID, name,    salary, start_date, city,       region)
values (3,  'Celia', 24020,  '12/03/96', 'Toronto',  'W');

insert into employee (ID, name,    salary, start_date, city,       region)
values (4,  'Linda', 40620,  '11/04/97', 'New York', 'N');

insert into employee (ID, name,    salary, start_date, city,       region)
values (5,  'David', 80026,  '10/05/98', 'Vancouver','W');

insert into employee (ID, name,    salary, start_date, city,       region)
values (6,  'James', 70060,  '09/06/99', 'Toronto',  'N');

insert into employee (ID, name,    salary, start_date, city,       region)
values (7,  'Alison',90620,  '08/07/00', 'New York', 'W');

insert into employee (ID, name,    salary, start_date, city,       region)
values (8,  'Chris', 26020,  '07/08/01', 'Vancouver','N');

insert into employee (ID, name,    salary, start_date, city,       region)
values (9,  'Mary',  60020,  '06/09/02', 'Toronto',  'W');

"""
