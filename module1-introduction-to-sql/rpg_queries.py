import sqlite3
sql_conn = sqlite3.connect('rpg_db.sqlite3')
sql_curs = sql_conn.cursor()
## - How many total Characters are there?
sql_curs.execute('SELECT COUNT(*) FROM charactercreator_character;')
# 302 characters are there.
sql_curs.fetchall()

## - How many of each specific subclass?

# for mage subclass
sql_curs.execute('SELECT COUNT(*) FROM charactercreator_mage;')
sql_curs.fetchall()
# 108 mage characters are there

# for thief subclass
sql_curs.execute('SELECT COUNT(*) FROM charactercreator_thief;').fetchall()
# 51 thief characters are there

# for cleric subclass
sql_curs.execute('SELECT COUNT(*) FROM charactercreator_cleric;').fetchall()
# 75 cleric characters are there

# for fighter subclass
sql_curs.execute('SELECT COUNT(*) FROM charactercreator_fighter;').fetchall()
# 68 fighter characters are there

## - How many total Items?
sql_curs.execute('SELECT COUNT(*) FROM armory_item;').fetchall()
# 174 items are there.

## - How many of the Items are weapons? How many are not?
sql_curs.execute('SELECT COUNT(*) FROM armory_item WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon);').fetchall()
# 37 of 174 items are weapons
sql_curs.execute('SELECT COUNT(*) FROM armory_item WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);').fetchall()
# 137 of 174 items are not weapons

## - How many Items does each character have? (Return first 20 rows)
sql_curs.execute('SELECT character_id,COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;').fetchall()

## - How many Weapons does each character have? (Return first 20 rows)
sql_curs.execute('SELECT character_id,COUNT(item_id) FROM charactercreator_character_inventory WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon) GROUP BY character_id LIMIT 20;').fetchall()

## - On average, how many Items does each Character have?
sql_curs.execute('SELECT AVG(avg_item) FROM ( SELECT COUNT(item_id) as avg_item FROM charactercreator_character_inventory GROUP BY character_id) as Items').fetchall()
# avg no of item per character is 2.97

## - On average, how many Weapons does each character have?
sql_curs.execute('SELECT AVG(avg_weapons) FROM (SELECT COUNT(item_id) as avg_weapons FROM charactercreator_character_inventory WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon) GROUP BY character_id) as Weapons').fetchall()
# avg no of weapon per character is 1.309 

sql_curs.close()
sql_conn.commit()
