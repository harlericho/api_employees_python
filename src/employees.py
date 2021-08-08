from config import get_connection


def getList():
    try:
        db = get_connection()
        cur = db.cursor()
        sql = "SELECT * FROM employees"
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()


def getListId(id):
    try:
        db = get_connection()
        cur = db.cursor()
        sql = "SELECT * FROM employees WHERE id =?"
        cur.execute(sql, [id])
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()


def postData(names, email, age):
    try:
        db = get_connection()
        cur = db.cursor()
        sql = "INSERT INTO employees (names,email,age) VALUES(?,?,?)"
        cur.execute(sql, [names, email, age])
        db.commit()
        return True
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def putData(names, email, age, id):
    try:
        db = get_connection()
        cur = db.cursor()
        sql = "UPDATE employees SET names=?, email =?, age =? WHERE id = ?"
        cur.execute(sql, [names, email, age, id])
        db.commit()
        return True
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()


def deleteData(id):
    try:
        db = get_connection()
        cur = db.cursor()
        sql ="DELETE FROM employees WHERE id =?"
        cur.execute(sql, [id])
        data =db.commit()
        return True
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()
