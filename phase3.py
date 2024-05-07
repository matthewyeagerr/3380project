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


def get_transaction_info(transaction_id):
    try:
        # Create a cursor
        cursor = db_connection.cursor()

        # Query to retrieve transaction information
        query = "SELECT trans_id, quantity, InvID, StockSymbol FROM transaction WHERE trans_id = %s"
        cursor.execute(query, (transaction_id,))
        
        # Fetch the transaction information
        transaction_info = cursor.fetchone()

        if transaction_info:
            # Process the transaction information (e.g., print or return)
            print("Transaction ID:", transaction_info[0])
            print("Quantity:", transaction_info[1])
            print("Investor ID:", transaction_info[2])
            print("Stock Symbol:", transaction_info[3])

        else:
            print("Transaction not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor (assuming db_connection is defined globally)
        cursor.close()

# Example usage
get_transaction_info(33)
buy_stock(3, 'META', 193)
view_stock_shares(1, 3)

