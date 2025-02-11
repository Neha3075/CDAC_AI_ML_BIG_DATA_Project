

from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017')
db=client['dbda']
def getallempinfo():
    emp = db['emp']
    emps = emp.find()
    for e in emps:
        print(e['_id'], '-', e['ename'], '-', e['job'], '-', e['sal'])
getallempinfo()
