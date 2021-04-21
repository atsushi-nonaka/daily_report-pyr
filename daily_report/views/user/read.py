from pyramid.response import Response
from pyramid.request import Request
from pyramid.view import view_config

from daily_report.models.user import User

import logging

@view_config(route_name='user', request_method='GET', renderer='json')
@view_config(route_name='user_with_id', request_method='GET', renderer='json')
def read(request: Request):
    logging.info('user')
    user_id = request.matchdict.get('id')
    if(user_id):
        return _select_user_with_id(
            user_id,
            request.dbsession
        )
    else:
        return _select_user(request.dbsession)
        
def _select_user_with_id(user_id, dbsession):
    user = dbsession.query(User).filter(User.id == user_id).first()
    if user:
        return {'data': user.as_dict()}
    else:
        return {'data': {}}

def _select_user(dbsession):
    users = dbsession.query(User).all()
    return {'data': list(map(lambda user: user.as_dict(), users))}

        