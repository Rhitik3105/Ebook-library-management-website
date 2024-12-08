import pymysql as p 
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='book')

def addlibrary(t):
    db=getConnection()
    sql='insert into library values(%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()



def selectAlllibrary():
    db=getConnection()
    sql='select * from library'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deletelibrary(Id):
    db=getConnection()
    sql='delete from library where Id=%s'
    cr=db.cursor()
    cr.execute(sql,Id)
    db.commit()
    db.close()

def selectlibraryById(Id):
    db=getConnection()
    sql='select * from library where Id=%s'
    cr=db.cursor()
    cr.execute(sql,Id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updatelibrary(t):
    db=getConnection()
    sql='update library set Name=%s,Bname=%s,Phone=%s,Email=%s ,Password=%s where Id=%s'
    cr=db.cursor()
    cr.execute(sql, t)
    db.commit()
    db.close()
