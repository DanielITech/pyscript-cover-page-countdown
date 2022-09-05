from datetime import datetime

def get_time():
    dt = datetime(2022, 10, 1, 0, 0, 0)
    rem = dt - datetime.now()
    nd = str(rem).replace(' days, ', ':')
    stmt = nd.split('.')[0]
    return stmt
