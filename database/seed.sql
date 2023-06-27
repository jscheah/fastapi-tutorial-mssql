Use testdb
GO

CREATE TABLE Sales (
    Region varchar(255),
    Country varchar(255),
    Item_Type varchar(255),
    Sales_Channel varchar(255),
	Order_Priority varchar(255),
	Order_Date varchar(255),
	Order_ID int,
	Ship_Date varchar(255),
	Units_Sold int,
	Unit_Price float,
	Unit_Cost float,
	Total_Revenue float,
	Total_Cost float,
	Total_Profit float,
);

GO