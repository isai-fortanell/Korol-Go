import sqlite3

sqliteConnection = sqlite3.connect('C:\\Users\\Nieto\\Documents\\Isai\\Desarrollo Web\\Django\\korol-go\\db.sqlite3')
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")

sqlite_select_Query = "select sqlite_version();"
cursor.execute(sqlite_select_Query)
record = cursor.fetchall()
print("SQLite Database Version is: ", record)
# cursor.execute("create table myapp_client (id integer primary key, data)")
cursor.execute("""CREATE TABLE "myapp_client" (
    "id" integer NOT NULL,
	"is_worker"	bool NOT NULL,
    "client_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
""")
	# FOREIGN KEY("client_id") REFERENCES "myapp_order"("name") 

sqliteConnection.commit()
cursor.close()


if sqliteConnection:
    sqliteConnection.close()
    print("The SQLite connection is closed")    