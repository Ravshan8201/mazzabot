import sqlite3
conn = sqlite3.connect('user_list.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Promo_list(
Promo STRING,
Name_uz STRING,
Name_ru STRING
)
''')
first_insetd = '''
INSERT INTO Promo_list VALUES ('{}',' ',' ')
'''

promo_id = '''
SELECT Promo 
FROM Promo_list
Where Promo = '{}'
'''
promo_upd = '''
UPDATE Promo_list  
SET Promo = '{}'
Where Promo = '{}'
'''
name_uz_id = '''
SELECT Name_uz 
FROM Promo_list
Where Promo = '{}'
'''
name_uz_upd = '''
UPDATE Promo_list  
SET Name_uz = '{}'
Where Promo = '{}'
'''
name_ru_id = '''
SELECT Name_ru 
FROM Promo_list
Where Promo = '{}'
'''
name_ru_upd = '''
UPDATE Promo_list  
SET Name_ru = '{}'
Where Promo = '{}'
'''
