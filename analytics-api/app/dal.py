from connection import get_db_connection

def get_top_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = ("SELECT c.customerName, COUNT(o.orderNumber) as total_orders "
             "FROM customers c JOIN orders o ON c.customerNumber = o.customerNumber "
             "GROUP BY c.customerNumber, c.customerName "
             "ORDER BY total_orders DESC "
             "LIMIT 10")
    cursor.execute(query)
    res = cursor.fetchall()
    conn.close()
    return res


def get_customers_without_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = ("SELECT c.customerName, c.customerNumber "
             "FROM customers c LEFT JOIN orders o ON c.customerNumber = o.customerNumber "
             "WHERE o.orderNumber IS NULL")
    cursor.execute(query)
    res = cursor.fetchall()
    conn.close()
    return res


def get_zero_credit_active_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = ("SELECT DISTINCT c.customerName, c.customerNumber, c.creditsLimit "
             "FROM customers c JOIN orders o ON c.customerNumber = o.customerNumber "
             "WHERE c.creditsLimit = 0")
    cursor.execute(query)
    res = cursor.fetchall()
    conn.close()
    return res
