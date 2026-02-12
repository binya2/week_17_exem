import mysql.connector
from mysql.connector import Error

from congif import mysql_config


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=mysql_config.MYSQL_HOST,
            user=mysql_config.MYSQL_USER,
            password=mysql_config.MYSQL_ROOT_PASSWORD,
            database="dev_db"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise


def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    customers_table_query = """
                            CREATE TABLE IF NOT EXISTS customers
                            (
                                customerNumber         INT PRIMARY KEY,
                                customerName           VARCHAR(255)    ,
                                contactLastName        VARCHAR(45)    ,
                                contactFirstName       VARCHAR(45)    ,
                                phone                  VARCHAR(45)    ,
                                addressLine1           VARCHAR(45)    ,
                                addressLine2           VARCHAR(45)    ,
                                city                   VARCHAR(45)    ,
                                state                  VARCHAR(45)    ,
                                postalCode             VARCHAR(45)    ,
                                country                VARCHAR(45)    ,
                                salesRepEmployeeNumber INT            ,
                                creditsLimit           DECIMAL(19, 2) ,
                                UNIQUE (customerNumber)
                            ) \
                            """
    order_table_query = """
                        CREATE TABLE IF NOT EXISTS orders
                        (
                            orderNumber    INT PRIMARY KEY,
                            orderDate      DATE,
                            requiredDate   DATE,
                            shippedDate    DATE,
                            status         VARCHAR(15),
                            comments       VARCHAR(4000),
                            customerNumber INT,
                            FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
                        )
                        """
    cursor.execute(customers_table_query)
    print("Table customers created successfully")
    cursor.execute(order_table_query)
    print("Table orders created successfully")
    connection.commit()
    cursor.close()
    connection.close()

def insert_order(order):
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = """INSERT INTO orders (orderNumber, 
                                          orderDate, 
                                          requiredDate, 
                                          shippedDate, 
                                          status, 
                                          comments, 
                                          customerNumber) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s)
                   """
    values =(
        order['orderNumber'],
        order['orderDate'],
        order['requiredDate'],
        order['shippedDate'],
        order['status'],
        order['comments'],
        order['customerNumber']
    )
    try:
        cursor.execute(insert_query, values)
        connection.commit()
    except Error as e:
        print(f"Error inserting order: {e}")

def insert_customer(customer):
    connection = get_db_connection()
    cursor = connection.cursor()
    if get_customer_by_customer_number(customer['customerNumber']):
        return print(
            f"Customer with customerNumber {customer['customerNumber']} already exists"
        )
    insert_query = """INSERT INTO customers (customerNumber, 
                                             customerName, 
                                             contactLastName, 
                                             contactFirstName, 
                                             phone, 
                                             addressLine1, 
                                             addressLine2, 
                                             city, 
                                             state, 
                                             postalCode, 
                                             country, 
                                             salesRepEmployeeNumber, 
                                             creditsLimit) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (customer['customerNumber'],
              customer['customerName'],
              customer['contactLastName'],
              customer['contactFirstName'],
              customer['phone'],
              customer['addressLine1'],
              customer['addressLine2'],
              customer['city'],
              customer['state'],
              customer['postalCode'],
              customer['country'],
              customer['salesRepEmployeeNumber'],
              customer['creditLimit']
              )
    try:
        cursor.execute(insert_query, values)
        connection.commit()
    except Error as e:
        print(f"Error inserting customer: {e}")

def get_customer_by_customer_number(customer_number):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM customers WHERE customerNumber = %s"
    cursor.execute(query, (customer_number,))
    customer = cursor.fetchone()
    return customer

def get_orders_by_order_number(order_number):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM orders WHERE orderNumber = %s"
    cursor.execute(query, (order_number,))
    orders = cursor.fetchall()
    return orders