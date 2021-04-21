def includeme(config):
    config.add_route('user', '/user')
    config.add_route('user_with_id', '/user/{id:\d+}')
    config.add_route('report', '/report')
    config.add_route('report_with_id', '/report/{id:\d+}')
    config.add_route('delete_with_id', '/delete/report/{id:\d+}')