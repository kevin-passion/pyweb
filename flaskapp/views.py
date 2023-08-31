from collections import namedtuple
from flaskapp import app, request, render_template, datetime, relativedelta, timedelta, date
from flaskapp.models import User
from flaskapp.init_db import db_session, SQLAlchemyError, text


@app.route('/table')
def tb():
    try:
        u = User('abc@efg.com', 'hong')
        db_session.add(u)    
        db_session.commit()

        # ret = User.query.filter(User.id>0).first()
        ret = User.query.all()
        print(ret)
        add_res = ""
        for row in ret:
            if row:
                # result = f"User: Email - {row.email}, Nickname - {row.nickname} \n"
                result = f"{row} "
                print('row:',result)
            if result:
                add_res += result 
        print("result>> \n" , add_res)

        # if add_res:
        #     return "<p>%add_res</p>"%add_res 
        # else:
        #     return "No users found"
    except SQLAlchemyError as sqlerr: 
        db_session.rollback()
        print("Sqlerror>>", sqlerr)
        return "An error occurred while processing the request."

    except:
        print("Error!!")    
        return "An unexpected error occurred."
    
    finally:
        db_session.close()

    return render_template('main.html', userlist=ret)

@app.route("/sel")
def sel():
    ss = db_session()
    query = text('select id, email, nickname from user where id > :id')
    ret = ss.execute(query, {'id':30})
    print("result.keys >>", ret.keys())
    Record = namedtuple("user", ret.keys())
    print('Recode >>', Record)
    records = [Record(*r) for r in ret.fetchall()]
    print('records>>', records)
    for r in records:
        print(r, r.nickname, type(r))
    ss.close()
    return render_template('main.html', userlist=records)








@app.route('/calendar')
def calendar():
    today = '2023-08-01'
    print('calendar.today:',today)
    d = datetime.strptime(today, '%Y-%m-%d')
    print('calendar.d:',d)
    nextMonth = d + relativedelta(months=1)
    print('calendar.nextMonth:', nextMonth)

    edt = (nextMonth - timedelta(1)).day
    print('calendar.edt:', edt)
    mm = d.month
    print('calendar.mm:', mm)
    sdt = d.weekday() * -1
    print('calendar.sdt:', sdt)
    # print('year:', d.year)
    thisYear = request.args.get("year", date.today().year, int)
    return render_template('calendar.html', year=thisYear, sdt=sdt,edt=edt,  mm=mm)


