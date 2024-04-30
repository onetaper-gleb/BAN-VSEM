import sqlite3


def sort_length_up(number):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT Name, Description FROM maps
    WHERE (Length > {number})""").fetchall()
    if len(result) == 0:
        pass
    con.close()
    return result


def sort_length_down(number):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT Name, Description FROM maps
    WHERE (Length < {number})""").fetchall()
    if len(result) == 0:
        pass
    con.close()
    return result


def sort_type(type):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT Name, Description FROM maps
        WHERE (Type like "%{type}%")""").fetchall()
    if len(result) == 0:
        pass
    con.close()
    return result


def sort_duration_up(number):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT Name, Description FROM maps
    WHERE (Duration > {number})""").fetchall()
    if len(result) == 0:
        pass
    con.close()
    return result


def sort_duration_down(number):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT Name, Description FROM maps
    WHERE (Duration < {number})""").fetchall()
    if len(result) == 0:
        pass
    con.close()
    return result

def sort_age(age):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT Name, Description FROM maps
        WHERE (Age <= {age})""").fetchall()
    if len(result) == 0:
        pass
    con.close()
    return result


def sort_season(season):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT Name, Description FROM maps
            WHERE (Seasons like "%{season}%")""").fetchall()
    if len(result) == 0:
        pass
    con.close()
    return result


def get_values():
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT Name, Description, Link_2, Link_3 FROM maps""").fetchall()
    if len(result) == 0:
        pass
    con.close()
    return result


def subscribe_him(name, chng):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT type FROM subscribers
            WHERE (name = "{name}")""").fetchall()
    if len(result) == 0 and chng:
        cur.execute(f"""INSERT INTO subscribers 
VALUES ("{name}", "subscribed");""")
    elif result == [('subscribed',)] and chng:
        cur.execute(f"""UPDATE subscribers SET type = "unsubscribed" WHERE (name = "{name}")""")
    elif chng:
        cur.execute(f"""UPDATE subscribers SET type = "subscribed" WHERE (name = "{name}")""")
    con.commit()
    con.close()
    if result == [('subscribed',)]:
        return True
    else:
        return False


def subscribers():
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT name FROM subscribers
            WHERE (type = "subscribed")""").fetchall()
    print(result)
    return result


def roots_new(name, chng):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT roots, hosts FROM News""").fetchall()
    if chng:
        cur.execute(f"""INSERT INTO News 
VALUES ("{len(result) + 1}", "{name}", "@{name.from_user.username}");""")
    con.commit()
    con.close()
    return result


def deller():
    con = sqlite3.connect("data")
    cur = con.cursor()
    cur.execute(f"""DELETE FROM News WHERE id == 1""")
    con.commit()
    con.close()