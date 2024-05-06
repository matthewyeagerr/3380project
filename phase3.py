import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="stock"
)
cursor = db_connection.cursor()



def generate_unique_trans_id():
    try:
        cursor.execute("SELECT MAX(trans_id) FROM transaction")
        max_trans_id = cursor.fetchone()[0]
        if max_trans_id is None:
            return 1  # If no existing transactions, start with ID 1
        else:
            return max_trans_id + 1
    except mysql.connector.Error as err:
        print(f"Error generating unique transaction ID: {err}")
        return None
    
def view_stock_shares(portfolio_id, investor_id):
    try:
        cursor = db_connection.cursor()
        query = "SELECT StockSymbol, quantity FROM transaction WHERE InvID = %s"
        values = (investor_id,)
        cursor.execute(query, values)
        stocks = cursor.fetchall()
        print(f"Portfolio {portfolio_id} for investor {investor_id}:")
        for stock in stocks:
            print(f"- {stock[0]}: {stock[1]} shares")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()

def buy_stock(investor_id, stock_symbol, quantity):
    try:
        # Generate a unique transaction ID
        trans_id = generate_unique_trans_id()  # You need to implement this function
        
        # Add transaction record
        query = "INSERT INTO transaction (trans_id, quantity, InvID, StockSymbol) VALUES (%s, %s, %s, %s)"
        values = (trans_id, quantity, investor_id, stock_symbol)
        
        cursor.execute(query, values)
        db_connection.commit()
        print(f"{quantity} shares of {stock_symbol} bought successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def store_stock_in_portfolio(inv_id, port_id, symbol, shares, price):
    try:
        cursor = db_connection.cursor()

        # Calculate the total investment
        total_investment = shares * price

        # Check if the stock already exists in the portfolio
        query = "SELECT * FROM portfolio WHERE inv_ID = %s AND ID = %s AND stock_symbol = %s"
        cursor.execute(query, (inv_id, port_id, symbol))
        result = cursor.fetchone()

        if result:
            # Update the existing record
            update_query = "UPDATE portfolio SET shares = shares + %s, totalinvestments = totalinvestments + %s WHERE inv_ID = %s AND ID = %s AND stock_symbol = %s"
            cursor.execute(update_query, (shares, total_investment, inv_id, port_id, symbol))
            print("Stock successfully added to portfolio.")
        else:
            # Insert a new record
            insert_query = "INSERT INTO portfolio (inv_ID, ID, stock_symbol, shares, totalinvestments) VALUES (%s, %s, %s, %s, %s)"
            insert_values = (inv_id, port_id, symbol, shares, total_investment)
            cursor.execute(insert_query, insert_values)
            print("Stock successfully added to portfolio.")

        db_connection.commit()
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()



buy_stock(3, 'META', 193)
view_stock_shares(1, 3)
store_stock_in_portfolio(3,5,'META',10,150)