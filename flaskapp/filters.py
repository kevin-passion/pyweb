from flaskapp import app, date, datetime,  relativedelta, timedelta
from flaskapp.utils import make_date
@app.template_filter('ymd')
def datetime_ymd(dt, fmt='%m-%d'):
    print('datetime_ymd:', dt)
    if isinstance(dt, date):
        return dt.strftime(fmt)    
    else:
        return dt

@app.template_filter('simpledate')
def simpledate(dt):
    print('simpledate:', dt)
    if not isinstance(dt, date):   #date 타입이 아니면 date 타입으로 바꾼다. 
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')
    
    if(datetime.now() - dt).days < 1:
        fmt = "%H:%M"
    else:
        fmt = "%m/%d"
    return "<strong>%s</strong>" % dt.strftime(fmt)

@app.template_filter('sdt')
def sdt(dt, fmt='%Y-%m-%d'):
    print('template_filter.sdt.dt:', dt)
    d = make_date(dt, fmt)
    print('template_filter.sdt.weekday:', d.weekday())
    wd = d.weekday() * -1
    # if (wd == -6):
    #     wd = 1
    return 1 if wd == -6 else wd

@app.template_filter('month')
def month(dt, fmt='%Y-%m-%d'):
    print('template_filter.month.dt:', dt)
    d = make_date(dt, fmt)
    return d.month

@app.template_filter('edt')
def edt(dt, fmt='%Y-%m-%d'):
    print('template_filter.edt.dt:', dt)
    d = make_date(dt, fmt)
    nextMonth = d + relativedelta(months=1)
    print('template_filter.nextMonth:',nextMonth)
    print('template_filter.nextMonth.day+1:',(nextMonth-timedelta(1)).day + 1)
    return (nextMonth - timedelta(1)).day + 1