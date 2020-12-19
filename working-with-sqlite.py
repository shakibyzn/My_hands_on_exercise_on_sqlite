import sqlite3

conn = sqlite3.connect('test.db')

cur = conn.cursor()

# CREATE A TABLE    
cur.execute(""" 
        CREATE TABLE Employee 
        (   EmployeeId integer primary key,
            FirstName text, 
            LastName text
        )
""")

# EXECUTE MULTIPLE QUERIES AT A TIME
cur.executescript("""
        INSERT INTO Employee (FirstName, LastName) VALUES ('ali','karimi');
        INSERT INTO Employee (FirstName, LastName) VALUES ('kamal','karimi');
        INSERT INTO Employee (FirstName, LastName) VALUES ('behdad','karimi');
        INSERT INTO Employee (FirstName, LastName) VALUES ('behrad','karimi');
        INSERT INTO Employee (FirstName, LastName) VALUES ('sanaz','karimi');

""")

# WHERE CLAUSE WITH LIKE & LENGTH
print(cur.execute("""
        SELECT * FROM Employee WHERE LastName='karimi';
""").fetchall())

print(cur.execute("""
        SELECT * FROM Employee WHERE FirstName like 'beh%';
""").fetchall())

print(cur.execute("""
        SELECT * FROM Employee WHERE length(FirstName) < 6;
""").fetchall())

# UPDATE ROWS IN A TABLE
cur.execute("""
    UPDATE Employee set LastName='poorhamidi' where FirstName='sanaz';
""")

# DELETE ROWS IN A TABLE
# cur.execute("""
#     DELETE Employee WHERE LastName='poorhamidi'
# """)

# ALTER A TABLE 
cur.executescript("""
        ALTER TABLE Employee ADD COLUMN Age integer;
        ALTER TABLE Employee ADD COLUMN City text;
""")

cur.executescript("""
        UPDATE Employee set Age=24, City='Isfahan' WHERE FirstName='ali' ;
        UPDATE Employee set Age=21, City='Isfahan' WHERE FirstName='kamal' ;
        UPDATE Employee set Age=32, City='Tehran' WHERE FirstName='behdad' ;
        UPDATE Employee set Age=91, City='Karaj' WHERE FirstName='behrad' ;

""")

cur.executescript("""
        CREATE TABLE Product (
            ProductId integer primary key,
            ProductName text,
            Price real
        );
        INSERT INTO Product (ProductName, Price) VALUES ('Bag', 453.25);
        INSERT INTO Product (Productname, Price) VALUES ('Cap', 68.9);
        INSERT INTO Product (Productname, Price) VALUES ('T-shirt', 55);
""")

# cur.execute(" DELETE FROM Product")
# cur.execute(" DROP TABLE Product")


cur.executescript("""
        CREATE TABLE Orders (
            OrderId integer primary key,
            EmployeeId REFERENCES Customer (EmployeeId),
            ProductId REFERENCES Product (ProductId),
            OrderDate text
        );
        INSERT INTO Orders (EmployeeId, ProductId, OrderDate) VALUES (3, 1, date('now'));
        INSERT INTO Orders (EmployeeId, ProductId, OrderDate) VALUES (5, 1, date('now'));
        INSERT INTO Orders (EmployeeId, ProductId, OrderDate) VALUES (3, 2, date('now'));
        INSERT INTO Orders (EmployeeId, ProductId, OrderDate) VALUES (2, 2, date('now'));
        INSERT INTO Orders (EmployeeId, ProductId, OrderDate) VALUES (1, 3, date('now'));
""")
# cur.execute(" DROP TABLE Orders")

print(cur.execute("""
    SELECT * FROM Orders;
""").fetchall())

# INNTER JOIN
query_inner_join_emp_order = cur.execute("""
    SELECT e.*, o.OrderDate, p.ProductName, p.Price  FROM Employee as e inner join Orders as o on o.EmployeeId=e.EmployeeId 
    inner join Product as p on p.ProductId=o.ProductId
""").fetchall()
for query in query_inner_join_emp_order:
    print(query)

# GROUPBY
query_inner_join_emp_order = cur.execute("""
    SELECT e.FirstName, sum(p.Price)  FROM Employee as e inner join Orders as o on o.EmployeeId=e.EmployeeId 
    inner join Product as p on p.ProductId=o.ProductId GROUP BY e.FirstName
""").fetchall()
for query in query_inner_join_emp_order:
    print(query)

conn.commit()
conn.close()
