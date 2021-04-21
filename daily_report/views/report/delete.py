import json

from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config
from zope.sqlalchemy import mark_changed

from daily_report.models.report import Report

@view_config(route_name='delete_with_id', request_method='DELETE', renderer='json')
def delete(request: Request):
    report_id = request.matchdict.get('id')
    if(report_id):
        return _delete_report(
            report_id,
            request.dbsession
        )
    else:
        return {"failed": "Specified report isn't found"}
        
def _delete_report(report_id, dbsession):
    report = dbsession.query(Report) \
            .filter(Report.id == report_id) \
            .first()
            
    if report:
        dbsession.query(Report) \
                 .filter(Report.id == report_id) \
                 .delete()
                 
        return {'id': report_id}
    else:
        return {"failed": "Specified report isn't found"}
    

        