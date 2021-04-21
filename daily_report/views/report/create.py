import json

from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import text
from sqlalchemy.dialects.mysql import insert 
from zope.sqlalchemy import mark_changed

from daily_report.models.report import Report

@view_config(route_name='report', request_method='POST')
def create(request):
    request.copy_body()
    try:
        body = json.loads(request.body_file.read())
    except json.JSONDecodeError as e:
        return Response("Failed")
    
    return _insert_report(
        request.dbsession,
        body
    )
    
def _insert_report(dbsession, body: dict):
    daily_report = Report(
        title=body.get('title'),
        content=body.get('content'),
        report_date=body.get('report_date'),
        user_id=body.get('user_id')
    )
    dbsession.add(daily_report)
    dbsession.flush()
    
    return Response("SUCCESS!")
