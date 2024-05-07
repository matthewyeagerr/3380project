
USE stock;
/*create table portfolio(
	price	int,
    inv_ID int not null,
    ID	int	primary key,
    totalinvestments	varchar(20)
);
create table investor(
	ID	INT	primary key,
    Fname	varchar(20)	not null,
    Lname	varchar(20)	not null,
    Minit	char(1),
    viewportID	int
);
create table Address(
	Investor_ID	INT	Primary key,
    ZIP	varchar(10) not null,
    street varchar(255)	not null,
    city varchar(100) not null,
    Foreign key(investor_id) references investor(ID)
);

    
    create table stock(
    price varchar(6),
    symbol	varchar(4) primary key not null
);
create table Phone(
	InvID	int primary key,
    Pnum	varchar(10) not null,
    foreign key(InvID) references investor(ID)
);
create table transaction(
	quantity INT not null,
    InvID	INT not null,
    StockSymbol varchar(4) not null,
    trans_id	int	PRIMARY key,
    foreign key(InvID) references investor(ID),
    foreign key(StockSymbol) references stock(symbol)
);

create table stored_in(
	shares	int not null,
    symbol	varchar(4)not null,
    port_id	int	primary key not null,
    foreign key(symbol) references stock(symbol),
    foreign key(port_id) references portfolio(ID)
);
ALTER TABLE Investor
ADD COLUMN AddressID INT,
ADD CONSTRAINT fk_investor_address
FOREIGN KEY (AddressID) REFERENCES Address(Investor_ID);
*/
-- Insert data for the stocks
/*INSERT INTO stock (price, symbol)
VALUES
    ('150.25', 'AAPL'),
    ('230.50', 'NVDA'),
    ('720.80', 'TSLA'),
    ('310.40', 'MSFT'),
    ('50.75', 'META'),
    ('280.00', 'GOOG'),
    ('350.00', 'AMZN');



-- Insert data for the investors
INSERT INTO Investor (ID, Fname, Lname, Minit, viewportID)
VALUES
    (1, 'John', 'Doe', 'J', NULL),    -- John Doe
    (2, 'Jane', 'Smith', 'A', NULL),   -- Jane Smith
	(3,'Matthew','Yeager','P',NULL);

-- Insert data for their addresses
INSERT INTO Address (Investor_ID, ZIP, street, city)
VALUES
    (1, '12345', 'Main St', 'Anytown'),   -- John Doe's address
    (2, '54321', 'Oak Ave', 'Another City'),  -- Jane Smith's address
    (3,'12445','Main St', 'Anytown');

-- Insert data for investor phone numbers
INSERT INTO Phone (InvID, Pnum)
VALUES
    (1, '555-1234'),  -- John Doe's phone number
    (2, '555-5678'),  -- Jane Smith's phone number
    (3, '555-1234');

-- Insert data for investor transactions
INSERT INTO transaction (quantity, InvID, StockSymbol, trans_id)
VALUES
    (100, 1, 'AAPL', 1),   -- John Doe buys 100 shares of AAPL
    (50, 1, 'NVDA', 2),    -- John Doe buys 50 shares of NVDA
    (75, 2, 'TSLA', 3),    -- Jane Smith buys 75 shares of TSLA
    (150, 2, 'MSFT', 4);   -- Jane Smith buys 150 shares of MSFT*/




