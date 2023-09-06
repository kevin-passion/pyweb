from flaskapp import app, date, datetime, os, url_for
import sys
def make_date(dt, fmt):
    print('make_date.dt:', dt)
    if not isinstance(dt, date):
        return datetime.strptime(dt, fmt)
    else:
        return dt


@app.context_processor
def override_url_for():
    print("context_processor.override_url_for")
    return dict(url_for=dated_url_for)

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['ver'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
    