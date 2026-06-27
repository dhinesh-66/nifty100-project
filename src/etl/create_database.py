import sqlite3

# Create/Open the database
conn = sqlite3.connect("db/nifty100.db")

# Enable foreign keys
conn.execute("PRAGMA foreign_keys = ON;")

# Read the schema.sql file
with open("db/schema.sql", "r") as f:
    schema = f.read()

# Execute all SQL commands
conn.executescript(schema)

print("Database and tables created successfully!")

# Close the connection
conn.close()