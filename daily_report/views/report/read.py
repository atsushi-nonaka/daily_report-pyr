from pyramid.response import Response
from pyramid.request import Request
from pyramid.view import view_config

from daily_report.models.report import Report

@view_config(route_name='report', request_method='GET', renderer='json')
@view_config(route_name='report_with_id', request_method='GET', renderer='json')
def read(request: Request):
    report_id = request.matchdict.get('id')
    if(report_id):
        return _select_report_with_id(
            report_id,
            request.dbsession
        )
    else:
        return _select_report(request.dbsession)
        
def _select_report_with_id(report_id, dbsession):
    report = dbsession.query(Report) \
                      .filter(Report.id == report_id) \
                      .first()
    if report:
        return {'data': report.as_dict()}
    else:
        return {'data': {}}
    
def _select_report(dbsession):
    reports = dbsession.query(Report).all()
    return {'data': list(map(lambda report: report.as_dict(), reports))}

        