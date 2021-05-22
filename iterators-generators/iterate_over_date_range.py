from datetime import date, timedelta, datetime


def daterange(start_date : date, end_date : date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

if __name__ == '__main__':
    start_date = datetime.strptime('20210301', '%Y%m%d')
    end_date = datetime.strptime('20210322', '%Y%m%d')
    for current_date in daterange(start_date, end_date):
        print(current_date)


