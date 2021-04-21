import json

from pyramid.view import view_config
from pyramid.response import Response
from daily_report.models.report import Report

@view_config(route_name='report_with_id', request_method='PUT', renderer='json')
def update(request):
    request.copy_body()
    try:
        body = json.loads(request.body_file.read())
    except json.JSONDecodeError as e:
        return Response("Error")
    return _update_report(
        request.dbsession, 
        request.matchdict['id'],
        body)
    
def _update_report(dbsession, id, body: dict):
    report = dbsession.query(Report) \
        .filter(Report.id == id) \
        .with_for_update() \
        .first()
        
    if not report:
        return {"Can't find data"}
    
    if 'title' in body:
        report.title = body.get('title')
    if 'content' in body:
        report.content = body.get('content')
    if 'report_data' in body:
        report.report_date = body.get('report_date')
        
    return {"data": report.as_dict()}

