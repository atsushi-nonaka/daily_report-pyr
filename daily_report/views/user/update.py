import json

from pyramid.view import view_config
from pyramid.response import Response
from daily_report.models.user import User

@view_config(route_name='user_with_id', request_method='PUT', renderer='json')
def update(request):
    request.copy_body()
    try:
        body = json.loads(request.body_file.read())
    except json.JSONDecodeError as e:
        return Response("Error")
    return _update_user(
        request.dbsession, 
        request.matchdict['id'],
        body)
    
def _update_user(dbsession, id, body: dict):
    user = dbsession.query(User) \
        .filter(User.id == id) \
        .with_for_update() \
        .first()
        
    if 'name' in body:
        user.name = body.get('name')
    if 'mail_address' in body:
        user.main_address = body.get('mail_address')
    if 'password' in body:
        user.password = body.get('password')
    if 'deleted' in body:
        user.deleted = body.get('deleted')
        
    return {"data": user.as_dict()}

