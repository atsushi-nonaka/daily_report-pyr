import json

from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import text
from sqlalchemy.dialects.mysql import insert 
from zope.sqlalchemy import mark_changed

from daily_report.models.user import User

@view_config(route_name='user', renderer='json', request_method='POST')
def create(request):
    request.copy_body()
    try:
        body = json.loads(request.body_file.read())
    except json.JSONDecodeError as e:
        return Response("Failed")
    
    return _insert_user(
        request.dbsession,
        body
    )
    
def _insert_user(dbsession, body: dict):
    
    user = User(
        name=body.get('name'),
        mail_address=body.get('mail_address'),
        password=body.get('password'),
        deleted=body.get('deleted')
    )
    dbsession.add(user)
    dbsession.flush()
    
    return Response("Success!")
