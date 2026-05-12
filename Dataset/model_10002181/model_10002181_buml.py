####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

Enumeration1: Enumeration = Enumeration(
    name="Enumeration1",
    literals={
            
    }
)

# Classes
chef = Class(name="chef")
Employee = Class(name="Employee")
Storage = Class(name="Storage")
Plan = Class(name="Plan")
Customer = Class(name="Customer")
Menu = Class(name="Menu")
Order = Class(name="Order")
Payment = Class(name="Payment")
PrintRecipts = Class(name="PrintRecipts")
System = Class(name="System")
Catering = Class(name="Catering")
customer_Actor = Class(name="customer_Actor")
select_from_menu_UseCase = Class(name="select_from_menu_UseCase")
order_catering_service_UseCase = Class(name="order_catering_service_UseCase")
weekly_plan_of_each_cutomer_UseCase = Class(name="weekly_plan_of_each_cutomer_UseCase")
payorder_UseCase = Class(name="payorder_UseCase")
sign_up_login_logout_UseCase = Class(name="sign_up_login_logout_UseCase")
chef_Actor = Class(name="chef_Actor")
Employee_Actor = Class(name="Employee_Actor")
add_and_get_from_storage_check_storage_UseCase = Class(name="add_and_get_from_storage_check_storage_UseCase")
add_constraints_UseCase = Class(name="add_constraints_UseCase")
order_missing_components_UseCase = Class(name="order_missing_components_UseCase")
daily_weekly_monthly_plan_UseCase = Class(name="daily_weekly_monthly_plan_UseCase")
prepration_plan_dishes_UseCase = Class(name="prepration_plan_dishes_UseCase")
weekly_plan_dishes_UseCase = Class(name="weekly_plan_dishes_UseCase")
create_invoice_UseCase = Class(name="create_invoice_UseCase")
Generate_payment_cheque_employes_UseCase = Class(name="Generate_payment_cheque_employes_UseCase")
Shopping_cart = Class(name="Shopping_cart")
date2 = Class(name="date2")
Customer_Balance = Class(name="Customer_Balance")
Accounnt = Class(name="Accounnt")
Customer1 = Class(name="Customer1")
Menu1 = Class(name="Menu1")
Catering1 = Class(name="Catering1")
Customer_Balance1 = Class(name="Customer_Balance1")
chef1 = Class(name="chef1")
Accounnt1 = Class(name="Accounnt1")
Payment1 = Class(name="Payment1")
PrintRecipts1 = Class(name="PrintRecipts1")
Kitchen_worker = Class(name="Kitchen_worker")
Storage1 = Class(name="Storage1")
System1 = Class(name="System1")
Plan1 = Class(name="Plan1")
help = Class(name="help")
contact = Class(name="contact")
UseCase_UseCase = Class(name="UseCase_UseCase")
Order1 = Class(name="Order1")
Shopping_cart1 = Class(name="Shopping_cart1")
Web_master = Class(name="Web_master")
bank_account = Class(name="bank_account")
owner_System_Actor = Class(name="owner_System_Actor")
check_bank_account_for_payments_UseCase = Class(name="check_bank_account_for_payments_UseCase")
list_of_outdated_components_UseCase = Class(name="list_of_outdated_components_UseCase")
Dish = Class(name="Dish")
Employee1 = Class(name="Employee1")
Waiter = Class(name="Waiter")
Owner = Class(name="Owner")
Chef = Class(name="Chef")
Component = Class(name="Component", is_abstract=True)
menu = Class(name="menu")
food_dish = Class(name="food_dish")
order = Class(name="order")
dayplan = Class(name="dayplan")
kitchen_worker = Class(name="kitchen_worker")
chef2 = Class(name="chef2")
drink = Class(name="drink")
liquid = Class(name="liquid")
solid = Class(name="solid")
events = Class(name="events")
Csutomer = Class(name="Csutomer")
payment = Class(name="payment")
shopping_cart = Class(name="shopping_cart")
customer_account = Class(name="customer_account")
solid1 = Class(name="solid1")
Owner1 = Class(name="Owner1")
Owner2 = Class(name="Owner2")
Account = Class(name="Account")
Account1 = Class(name="Account1")
Account_for_employee = Class(name="Account_for_employee")
account_registration = Class(name="account_registration")
account_type = Class(name="account_type")
owner__system = Class(name="owner__system")
catering = Class(name="catering")

# chef class attributes and methods
chef_Name: Property = Property(name="Name", type=StringType)
chef_Employee_ID: Property = Property(name="Employee_ID", type=IntegerType)
chef_Email: Property = Property(name="Email", type=StringType)
chef_passowrd: Property = Property(name="passowrd", type=StringType)
chef_Room_no: Property = Property(name="Room_no", type=IntegerType)
chef.attributes={chef_Name, chef_Room_no, chef_Email, chef_passowrd, chef_Employee_ID}

# Employee class attributes and methods
Employee_Email: Property = Property(name="Email", type=StringType)
Employee_password: Property = Property(name="password", type=StringType)
Employee_attribute: Property = Property(name="attribute", type=StringType)
Employee_ID: Property = Property(name="ID", type=IntegerType)
Employee_Name: Property = Property(name="Name", type=StringType)
Employee.attributes={Employee_Name, Employee_ID, Employee_Email, Employee_password, Employee_attribute}

# Storage class attributes and methods
Storage_Component_id: Property = Property(name="Component_id", type=IntegerType)
Storage_Component_Name: Property = Property(name="Component_Name", type=StringType)
Storage.attributes={Storage_Component_Name, Storage_Component_id}

# Plan class attributes and methods
Plan_weekly_plan: Property = Property(name="weekly_plan", type=StringType)
Plan_Monthly_plan: Property = Property(name="Monthly_plan", type=StringType)
Plan_day_plan: Property = Property(name="day_plan", type=StringType)
Plan.attributes={Plan_Monthly_plan, Plan_day_plan, Plan_weekly_plan}

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_ID: Property = Property(name="ID", type=IntegerType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_Email: Property = Property(name="Email", type=StringType)
Customer_Password: Property = Property(name="Password", type=StringType)
Customer_Accontbalance: Property = Property(name="Accontbalance", type=StringType)
Customer_Phone: Property = Property(name="Phone", type=IntegerType)
Customer.attributes={Customer_Password, Customer_Phone, Customer_Name, Customer_Email, Customer_Accontbalance, Customer_Address, Customer_ID}

# Menu class attributes and methods
Menu_DishName: Property = Property(name="DishName", type=StringType)
Menu_Price: Property = Property(name="Price", type=StringType)
Menu_Quantity: Property = Property(name="Quantity", type=StringType)
Menu_Components: Property = Property(name="Components", type=StringType)
Menu.attributes={Menu_DishName, Menu_Price, Menu_Quantity, Menu_Components}

# Order class attributes and methods
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_Customerid: Property = Property(name="Customerid", type=IntegerType)
Order_Dishname: Property = Property(name="Dishname", type=StringType)
Order_attribute: Property = Property(name="attribute", type=StringType)
Order_date: Property = Property(name="date", type=StringType)
Order.attributes={Order_OrderID, Order_date, Order_Dishname, Order_attribute, Order_Customerid}

# Payment class attributes and methods
Payment_PaymentID: Property = Property(name="PaymentID", type=IntegerType)
Payment_Amount: Property = Property(name="Amount", type=StringType)
Payment_OrderID: Property = Property(name="OrderID", type=IntegerType)
Payment_CustomerID: Property = Property(name="CustomerID", type=IntegerType)
Payment_date: Property = Property(name="date", type=StringType)
Payment_time: Property = Property(name="time", type=StringType)
Payment.attributes={Payment_PaymentID, Payment_date, Payment_time, Payment_CustomerID, Payment_Amount, Payment_OrderID}

# PrintRecipts class attributes and methods
PrintRecipts_time: Property = Property(name="time", type=StringType)
PrintRecipts_date: Property = Property(name="date", type=StringType)
PrintRecipts_PaymentID: Property = Property(name="PaymentID", type=StringType)
PrintRecipts_CustomerID: Property = Property(name="CustomerID", type=IntegerType)
PrintRecipts_Amount: Property = Property(name="Amount", type=StringType)
PrintRecipts_Dishname: Property = Property(name="Dishname", type=StringType)
PrintRecipts_Quantity: Property = Property(name="Quantity", type=IntegerType)
PrintRecipts.attributes={PrintRecipts_Amount, PrintRecipts_Dishname, PrintRecipts_date, PrintRecipts_CustomerID, PrintRecipts_Quantity, PrintRecipts_time, PrintRecipts_PaymentID}

# System class attributes and methods

# Catering class attributes and methods
Catering_Menu: Property = Property(name="Menu", type=StringType)
Catering_attribute: Property = Property(name="attribute", type=StringType)
Catering.attributes={Catering_Menu, Catering_attribute}

# customer_Actor class attributes and methods

# select_from_menu_UseCase class attributes and methods

# order_catering_service_UseCase class attributes and methods

# weekly_plan_of_each_cutomer_UseCase class attributes and methods

# payorder_UseCase class attributes and methods

# sign_up_login_logout_UseCase class attributes and methods

# chef_Actor class attributes and methods

# Employee_Actor class attributes and methods

# add_and_get_from_storage_check_storage_UseCase class attributes and methods

# add_constraints_UseCase class attributes and methods

# order_missing_components_UseCase class attributes and methods

# daily_weekly_monthly_plan_UseCase class attributes and methods

# prepration_plan_dishes_UseCase class attributes and methods

# weekly_plan_dishes_UseCase class attributes and methods

# create_invoice_UseCase class attributes and methods

# Generate_payment_cheque_employes_UseCase class attributes and methods

# Shopping_cart class attributes and methods
Shopping_cart_Dishname: Property = Property(name="Dishname", type=StringType)
Shopping_cart_price: Property = Property(name="price", type=IntegerType)
Shopping_cart_Quantity: Property = Property(name="Quantity", type=IntegerType)
Shopping_cart_time: Property = Property(name="time", type=StringType)
Shopping_cart_attribute: Property = Property(name="attribute", type=StringType)
Shopping_cart.attributes={Shopping_cart_attribute, Shopping_cart_Dishname, Shopping_cart_time, Shopping_cart_price, Shopping_cart_Quantity}

# date2 class attributes and methods

# Customer_Balance class attributes and methods
Customer_Balance_CustomerID: Property = Property(name="CustomerID", type=IntegerType)
Customer_Balance_CustomerName: Property = Property(name="CustomerName", type=StringType)
Customer_Balance_Adress: Property = Property(name="Adress", type=StringType)
Customer_Balance_Date: Property = Property(name="Date", type=StringType)
Customer_Balance_Account_balance: Property = Property(name="Account_balance", type=StringType)
Customer_Balance.attributes={Customer_Balance_Date, Customer_Balance_Adress, Customer_Balance_CustomerID, Customer_Balance_Account_balance, Customer_Balance_CustomerName}

# Accounnt class attributes and methods
Accounnt_Email: Property = Property(name="Email", type=StringType)
Accounnt_password: Property = Property(name="password", type=StringType)
Accounnt_Accounttype: Property = Property(name="Accounttype", type=StringType)
Accounnt_Employee_ID: Property = Property(name="Employee_ID", type=StringType)
Accounnt.attributes={Accounnt_Email, Accounnt_Accounttype, Accounnt_password, Accounnt_Employee_ID}

# Customer1 class attributes and methods
Customer1_Name: Property = Property(name="Name", type=StringType)
Customer1_ID: Property = Property(name="ID", type=IntegerType)
Customer1_Address: Property = Property(name="Address", type=StringType)
Customer1_Email: Property = Property(name="Email", type=StringType)
Customer1_Password: Property = Property(name="Password", type=StringType)
Customer1_Accontbalance: Property = Property(name="Accontbalance", type=StringType)
Customer1_Phone: Property = Property(name="Phone", type=IntegerType)
Customer1_attribute: Property = Property(name="attribute", type=StringType)
Customer1__attr: Property = Property(name="_attr", type=StringType)
Customer1_Adress: Property = Property(name="Adress", type=StringType)
Customer1.attributes={Customer1_Password, Customer1_Address, Customer1_attribute, Customer1_Name, Customer1_ID, Customer1_Accontbalance, Customer1__attr, Customer1_Email, Customer1_Adress, Customer1_Phone}

# Menu1 class attributes and methods
Menu1_DishName: Property = Property(name="DishName", type=StringType)
Menu1_Price: Property = Property(name="Price", type=StringType)
Menu1_Quantity: Property = Property(name="Quantity", type=StringType)
Menu1_Components: Property = Property(name="Components", type=StringType)
Menu1.attributes={Menu1_Price, Menu1_Quantity, Menu1_DishName, Menu1_Components}

# Catering1 class attributes and methods
Catering1_Menu: Property = Property(name="Menu", type=StringType)
Catering1_attribute: Property = Property(name="attribute", type=StringType)
Catering1.attributes={Catering1_attribute, Catering1_Menu}

# Customer_Balance1 class attributes and methods
Customer_Balance1_Account_balance: Property = Property(name="Account_balance", type=StringType)
Customer_Balance1_CustomerID: Property = Property(name="CustomerID", type=IntegerType)
Customer_Balance1_CustomerName: Property = Property(name="CustomerName", type=StringType)
Customer_Balance1_Adress: Property = Property(name="Adress", type=StringType)
Customer_Balance1_Date: Property = Property(name="Date", type=StringType)
Customer_Balance1.attributes={Customer_Balance1_CustomerName, Customer_Balance1_CustomerID, Customer_Balance1_Account_balance, Customer_Balance1_Adress, Customer_Balance1_Date}

# chef1 class attributes and methods
chef1_Name: Property = Property(name="Name", type=StringType)
chef1_Employee_ID: Property = Property(name="Employee_ID", type=IntegerType)
chef1_Email: Property = Property(name="Email", type=StringType)
chef1_passowrd: Property = Property(name="passowrd", type=StringType)
chef1_Room_no: Property = Property(name="Room_no", type=IntegerType)
chef1.attributes={chef1_passowrd, chef1_Name, chef1_Email, chef1_Employee_ID, chef1_Room_no}

# Accounnt1 class attributes and methods
Accounnt1_Email: Property = Property(name="Email", type=StringType)
Accounnt1_password: Property = Property(name="password", type=StringType)
Accounnt1_Accounttype: Property = Property(name="Accounttype", type=StringType)
Accounnt1.attributes={Accounnt1_password, Accounnt1_Accounttype, Accounnt1_Email}

# Payment1 class attributes and methods
Payment1_PaymentID: Property = Property(name="PaymentID", type=IntegerType)
Payment1_Amount: Property = Property(name="Amount", type=StringType)
Payment1_OrderID: Property = Property(name="OrderID", type=IntegerType)
Payment1_CustomerID: Property = Property(name="CustomerID", type=IntegerType)
Payment1_date: Property = Property(name="date", type=StringType)
Payment1_time: Property = Property(name="time", type=StringType)
Payment1.attributes={Payment1_CustomerID, Payment1_OrderID, Payment1_Amount, Payment1_date, Payment1_PaymentID, Payment1_time}

# PrintRecipts1 class attributes and methods
PrintRecipts1_PaymentID: Property = Property(name="PaymentID", type=StringType)
PrintRecipts1_CustomerID: Property = Property(name="CustomerID", type=IntegerType)
PrintRecipts1_Amount: Property = Property(name="Amount", type=StringType)
PrintRecipts1_Dishname: Property = Property(name="Dishname", type=StringType)
PrintRecipts1_Quantity: Property = Property(name="Quantity", type=IntegerType)
PrintRecipts1_time: Property = Property(name="time", type=StringType)
PrintRecipts1_date: Property = Property(name="date", type=StringType)
PrintRecipts1.attributes={PrintRecipts1_time, PrintRecipts1_date, PrintRecipts1_PaymentID, PrintRecipts1_Quantity, PrintRecipts1_Dishname, PrintRecipts1_CustomerID, PrintRecipts1_Amount}

# Kitchen_worker class attributes and methods
Kitchen_worker_ID: Property = Property(name="ID", type=IntegerType)
Kitchen_worker_Name: Property = Property(name="Name", type=StringType)
Kitchen_worker_Email: Property = Property(name="Email", type=StringType)
Kitchen_worker_password: Property = Property(name="password", type=StringType)
Kitchen_worker_attribute: Property = Property(name="attribute", type=StringType)
Kitchen_worker.attributes={Kitchen_worker_ID, Kitchen_worker_Name, Kitchen_worker_password, Kitchen_worker_attribute, Kitchen_worker_Email}

# Storage1 class attributes and methods
Storage1_Component_id: Property = Property(name="Component_id", type=IntegerType)
Storage1_Component_Name: Property = Property(name="Component_Name", type=StringType)
Storage1.attributes={Storage1_Component_Name, Storage1_Component_id}

# System1 class attributes and methods
System1_WebAdmin_or_owner: Property = Property(name="WebAdmin_or_owner", type=StringType)
System1_Email: Property = Property(name="Email", type=StringType)
System1_Password: Property = Property(name="Password", type=StringType)
System1.attributes={System1_Password, System1_WebAdmin_or_owner, System1_Email}

# Plan1 class attributes and methods
Plan1_weekly_plan: Property = Property(name="weekly_plan", type=StringType)
Plan1_Monthly_plan: Property = Property(name="Monthly_plan", type=StringType)
Plan1_day_plan: Property = Property(name="day_plan", type=StringType)
Plan1.attributes={Plan1_day_plan, Plan1_Monthly_plan, Plan1_weekly_plan}

# help class attributes and methods

# contact class attributes and methods
contact_Name: Property = Property(name="Name", type=StringType)
contact_Adress: Property = Property(name="Adress", type=StringType)
contact_Email: Property = Property(name="Email", type=StringType)
contact_Tel: Property = Property(name="Tel", type=IntegerType)
contact_attribute: Property = Property(name="attribute", type=StringType)
contact.attributes={contact_attribute, contact_Name, contact_Tel, contact_Adress, contact_Email}

# UseCase_UseCase class attributes and methods

# Order1 class attributes and methods
Order1_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order1_Customerid: Property = Property(name="Customerid", type=IntegerType)
Order1_Dishname: Property = Property(name="Dishname", type=StringType)
Order1_attribute: Property = Property(name="attribute", type=StringType)
Order1_date: Property = Property(name="date", type=StringType)
Order1.attributes={Order1_attribute, Order1_Customerid, Order1_date, Order1_OrderID, Order1_Dishname}

# Shopping_cart1 class attributes and methods
Shopping_cart1_Dishname: Property = Property(name="Dishname", type=StringType)
Shopping_cart1_price: Property = Property(name="price", type=IntegerType)
Shopping_cart1_Quantity: Property = Property(name="Quantity", type=IntegerType)
Shopping_cart1_time: Property = Property(name="time", type=StringType)
Shopping_cart1_attribute: Property = Property(name="attribute", type=StringType)
Shopping_cart1.attributes={Shopping_cart1_attribute, Shopping_cart1_Quantity, Shopping_cart1_price, Shopping_cart1_Dishname, Shopping_cart1_time}

# Web_master class attributes and methods

# bank_account class attributes and methods

# owner_System_Actor class attributes and methods

# check_bank_account_for_payments_UseCase class attributes and methods

# list_of_outdated_components_UseCase class attributes and methods

# Dish class attributes and methods
Dish__attr: Property = Property(name="_attr", type=StringType)
Dish.attributes={Dish__attr}

# Employee1 class attributes and methods
Employee1_ID: Property = Property(name="ID", type=StringType)
Employee1_Name: Property = Property(name="Name", type=StringType)
Employee1_Email: Property = Property(name="Email", type=StringType)
Employee1_Password: Property = Property(name="Password", type=StringType)
Employee1_attribute: Property = Property(name="attribute", type=StringType)
Employee1.attributes={Employee1_attribute, Employee1_Name, Employee1_Email, Employee1_ID, Employee1_Password}

# Waiter class attributes and methods

# Owner class attributes and methods

# Chef class attributes and methods

# Component class attributes and methods
Component_ID: Property = Property(name="ID", type=StringType)
Component_Name: Property = Property(name="Name", type=StringType)
Component_Type: Property = Property(name="Type", type=StringType)
Component_Storage_or_sehlf: Property = Property(name="Storage_or_sehlf", type=StringType)
Component_Expiry_date: Property = Property(name="Expiry_date", type=StringType)
Component_attribute: Property = Property(name="attribute", type=StringType)
Component.attributes={Component_ID, Component_Type, Component_attribute, Component_Name, Component_Storage_or_sehlf, Component_Expiry_date}

# menu class attributes and methods
menu_dishname: Property = Property(name="dishname", type=StringType)
menu_price: Property = Property(name="price", type=StringType)
menu_dish_quantity: Property = Property(name="dish_quantity", type=StringType)
menu_attribute: Property = Property(name="attribute", type=StringType)
menu_drinkname: Property = Property(name="drinkname", type=StringType)
menu.attributes={menu_dishname, menu_dish_quantity, menu_price, menu_attribute, menu_drinkname}

# food_dish class attributes and methods
food_dish_type: Property = Property(name="type", type=StringType)
food_dish_attribute: Property = Property(name="attribute", type=StringType)
food_dish_attribute2: Property = Property(name="attribute2", type=StringType)
food_dish.attributes={food_dish_type, food_dish_attribute2, food_dish_attribute}

# order class attributes and methods
order_order_id: Property = Property(name="order_id", type=StringType)
order_ordered_item: Property = Property(name="ordered_item", type=StringType)
order_status: Property = Property(name="status", type=StringType)
order__attr: Property = Property(name="_attr", type=StringType)
order_date: Property = Property(name="date", type=StringType)
order.attributes={order_order_id, order_status, order_ordered_item, order__attr, order_date}

# dayplan class attributes and methods
dayplan_Monday: Property = Property(name="Monday", type=StringType)
dayplan_tuesday: Property = Property(name="tuesday", type=StringType)
dayplan_wenesday: Property = Property(name="wenesday", type=StringType)
dayplan_thursday: Property = Property(name="thursday", type=StringType)
dayplan_friday: Property = Property(name="friday", type=StringType)
dayplan_saturday: Property = Property(name="saturday", type=StringType)
dayplan_sunday: Property = Property(name="sunday", type=StringType)
dayplan_plan_per_date: Property = Property(name="plan_per_date", type=StringType)
dayplan.attributes={dayplan_thursday, dayplan_sunday, dayplan_saturday, dayplan_wenesday, dayplan_friday, dayplan_plan_per_date, dayplan_Monday, dayplan_tuesday}

# kitchen_worker class attributes and methods

# chef2 class attributes and methods

# drink class attributes and methods
drink_type: Property = Property(name="type", type=StringType)
drink.attributes={drink_type}

# liquid class attributes and methods
liquid_must_be_unit_in_ml: Property = Property(name="must_be_unit_in_ml", type=StringType)
liquid_name: Property = Property(name="name", type=StringType)
liquid_quantiy: Property = Property(name="quantiy", type=StringType)
liquid.attributes={liquid_name, liquid_must_be_unit_in_ml, liquid_quantiy}

# solid class attributes and methods
solid_must_be_unit_in_kg: Property = Property(name="must_be_unit_in_kg", type=StringType)
solid.attributes={solid_must_be_unit_in_kg}

# events class attributes and methods
events_get_employee_name: Property = Property(name="get_employee_name", type=StringType)
events_duration: Property = Property(name="duration", type=StringType)
events_attribute: Property = Property(name="attribute", type=StringType)
events_catering_location: Property = Property(name="catering_location", type=StringType)
events.attributes={events_get_employee_name, events_attribute, events_catering_location, events_duration}

# Csutomer class attributes and methods
Csutomer_id: Property = Property(name="id", type=StringType)
Csutomer_email: Property = Property(name="email", type=StringType)
Csutomer_password: Property = Property(name="password", type=StringType)
Csutomer_tel_no: Property = Property(name="tel_no", type=StringType)
Csutomer_register: Property = Property(name="register", type=StringType)
Csutomer_attribute: Property = Property(name="attribute", type=StringType)
Csutomer_Adress: Property = Property(name="Adress", type=StringType)
Csutomer_name: Property = Property(name="name", type=StringType)
Csutomer.attributes={Csutomer_tel_no, Csutomer_attribute, Csutomer_name, Csutomer_register, Csutomer_password, Csutomer_id, Csutomer_email, Csutomer_Adress}

# payment class attributes and methods
payment_amount: Property = Property(name="amount", type=StringType)
payment__attr: Property = Property(name="_attr", type=StringType)
payment_total_amount: Property = Property(name="total_amount", type=StringType)
payment.attributes={payment_total_amount, payment__attr, payment_amount}

# shopping_cart class attributes and methods

# customer_account class attributes and methods

# solid1 class attributes and methods
solid1_name: Property = Property(name="name", type=StringType)
solid1_weight__kg_: Property = Property(name="weight__kg_", type=StringType)
solid1_pieces: Property = Property(name="pieces", type=IntegerType)
solid1_state: Property = Property(name="state", type=StringType)
solid1.attributes={solid1_weight__kg_, solid1_pieces, solid1_name, solid1_state}

# Owner1 class attributes and methods

# Owner2 class attributes and methods

# Account class attributes and methods
Account_Name: Property = Property(name="Name", type=StringType)
Account_id: Property = Property(name="id", type=StringType)
Account_email: Property = Property(name="email", type=StringType)
Account_password: Property = Property(name="password", type=StringType)
Account__attr: Property = Property(name="_attr", type=StringType)
Account_attribute: Property = Property(name="attribute", type=StringType)
Account.attributes={Account_Name, Account_attribute, Account_password, Account_id, Account_email, Account__attr}

# Account1 class attributes and methods
Account1_Name: Property = Property(name="Name", type=StringType)
Account1_id: Property = Property(name="id", type=StringType)
Account1_email: Property = Property(name="email", type=StringType)
Account1_password: Property = Property(name="password", type=StringType)
Account1__attr: Property = Property(name="_attr", type=StringType)
Account1_attribute: Property = Property(name="attribute", type=StringType)
Account1.attributes={Account1_email, Account1_attribute, Account1_password, Account1__attr, Account1_Name, Account1_id}

# Account_for_employee class attributes and methods
Account_for_employee_name: Property = Property(name="name", type=StringType)
Account_for_employee_id: Property = Property(name="id", type=StringType)
Account_for_employee_email: Property = Property(name="email", type=StringType)
Account_for_employee_password: Property = Property(name="password", type=StringType)
Account_for_employee_getaccount: Property = Property(name="getaccount", type=StringType)
Account_for_employee_attribute: Property = Property(name="attribute", type=StringType)
Account_for_employee.attributes={Account_for_employee_id, Account_for_employee_name, Account_for_employee_getaccount, Account_for_employee_attribute, Account_for_employee_password, Account_for_employee_email}

# account_registration class attributes and methods

# account_type class attributes and methods
account_type_name: Property = Property(name="name", type=StringType)
account_type_id: Property = Property(name="id", type=StringType)
account_type_email: Property = Property(name="email", type=StringType)
account_type_password: Property = Property(name="password", type=StringType)
account_type__attr: Property = Property(name="_attr", type=StringType)
account_type.attributes={account_type_name, account_type_password, account_type_id, account_type_email, account_type__attr}

# owner__system class attributes and methods
owner__system_attribute: Property = Property(name="attribute", type=StringType)
owner__system.attributes={owner__system_attribute}

# catering class attributes and methods

# Relationships
Employee_Storage: BinaryAssociation = BinaryAssociation(
    name="Employee_Storage",
    ends={
        Property(name="storage0", type=Storage, multiplicity=Multiplicity(0, 9999)),
        Property(name="employee1", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_Plan: BinaryAssociation = BinaryAssociation(
    name="Employee_Plan",
    ends={
        Property(name="plan2", type=Plan, multiplicity=Multiplicity(0, 9999)),
        Property(name="employee3", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)
customer_select_from_menu: BinaryAssociation = BinaryAssociation(
    name="customer_select_from_menu",
    ends={
        Property(name="select_from_menu4", type=select_from_menu_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_order_catering_service: BinaryAssociation = BinaryAssociation(
    name="customer_order_catering_service",
    ends={
        Property(name="order_catering_service6", type=order_catering_service_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_weekly_plan_of_each_cutomer: BinaryAssociation = BinaryAssociation(
    name="customer_weekly_plan_of_each_cutomer",
    ends={
        Property(name="weekly_plan_of_each_cutomer8", type=weekly_plan_of_each_cutomer_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_payorder: BinaryAssociation = BinaryAssociation(
    name="customer_payorder",
    ends={
        Property(name="payorder10", type=payorder_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_login: BinaryAssociation = BinaryAssociation(
    name="customer_login",
    ends={
        Property(name="login12", type=sign_up_login_logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
chef_login: BinaryAssociation = BinaryAssociation(
    name="chef_login",
    ends={
        Property(name="login14", type=sign_up_login_logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="chef15", type=chef_Actor, multiplicity=Multiplicity(0, 1))
    }
)
worker_login: BinaryAssociation = BinaryAssociation(
    name="worker_login",
    ends={
        Property(name="login16", type=sign_up_login_logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="worker17", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
chef_Accounnt: BinaryAssociation = BinaryAssociation(
    name="chef_Accounnt",
    ends={
        Property(name="chef35", type=chef, multiplicity=Multiplicity(1, 1)),
        Property(name="accounnt34", type=Accounnt, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Accounnt: BinaryAssociation = BinaryAssociation(
    name="Customer_Accounnt",
    ends={
        Property(name="accounnt36", type=Accounnt1, multiplicity=Multiplicity(1, 1)),
        Property(name="customer37", type=Customer1, multiplicity=Multiplicity(1, 1))
    }
)
chef_Accounnt2: BinaryAssociation = BinaryAssociation(
    name="chef_Accounnt2",
    ends={
        Property(name="accounnt38", type=Accounnt1, multiplicity=Multiplicity(1, 1)),
        Property(name="chef39", type=chef1, multiplicity=Multiplicity(1, 1))
    }
)
Accounnt_Employee: BinaryAssociation = BinaryAssociation(
    name="Accounnt_Employee",
    ends={
        Property(name="employee40", type=Kitchen_worker, multiplicity=Multiplicity(1, 1)),
        Property(name="accounnt41", type=Accounnt1, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Customer_Balance: BinaryAssociation = BinaryAssociation(
    name="Customer_Customer_Balance",
    ends={
        Property(name="customer_Balance42", type=Customer_Balance1, multiplicity=Multiplicity(1, 1)),
        Property(name="customer43", type=Customer1, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Storage2: BinaryAssociation = BinaryAssociation(
    name="Employee_Storage2",
    ends={
        Property(name="storage44", type=Storage1, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee45", type=Kitchen_worker, multiplicity=Multiplicity(0, 9999))
    }
)
Plan_chef: BinaryAssociation = BinaryAssociation(
    name="Plan_chef",
    ends={
        Property(name="chef46", type=chef1, multiplicity=Multiplicity(1, 9999)),
        Property(name="plan47", type=Plan1, multiplicity=Multiplicity(1, 9999))
    }
)
Menu_Catering: BinaryAssociation = BinaryAssociation(
    name="Menu_Catering",
    ends={
        Property(name="catering48", type=Catering1, multiplicity=Multiplicity(1, 1)),
        Property(name="menu49", type=Menu1, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Catering: BinaryAssociation = BinaryAssociation(
    name="Customer_Catering",
    ends={
        Property(name="catering50", type=Catering1, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer51", type=Customer1, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Customer: BinaryAssociation = BinaryAssociation(
    name="Order_Customer",
    ends={
        Property(name="customer52", type=Customer1, multiplicity=Multiplicity(1, 1)),
        Property(name="order53", type=Order1, multiplicity=Multiplicity(0, 9999))
    }
)
Shopping_cart_Menu: BinaryAssociation = BinaryAssociation(
    name="Shopping_cart_Menu",
    ends={
        Property(name="menu54", type=Menu1, multiplicity=Multiplicity(1, 1)),
        Property(name="shopping_cart55", type=Shopping_cart1, multiplicity=Multiplicity(1, 1))
    }
)
Order_Payment: BinaryAssociation = BinaryAssociation(
    name="Order_Payment",
    ends={
        Property(name="payment56", type=Payment1, multiplicity=Multiplicity(1, 1)),
        Property(name="order57", type=Order1, multiplicity=Multiplicity(1, 1))
    }
)
Payment_PrintRecipts: BinaryAssociation = BinaryAssociation(
    name="Payment_PrintRecipts",
    ends={
        Property(name="printRecipts58", type=PrintRecipts1, multiplicity=Multiplicity(1, 1)),
        Property(name="payment59", type=Payment1, multiplicity=Multiplicity(1, 1))
    }
)
Web_master_help: BinaryAssociation = BinaryAssociation(
    name="Web_master_help",
    ends={
        Property(name="help60", type=help, multiplicity=Multiplicity(0, 1)),
        Property(name="web_master61", type=Web_master, multiplicity=Multiplicity(0, 1))
    }
)
Web_master_contact: BinaryAssociation = BinaryAssociation(
    name="Web_master_contact",
    ends={
        Property(name="contact62", type=contact, multiplicity=Multiplicity(0, 1)),
        Property(name="web_master63", type=Web_master, multiplicity=Multiplicity(0, 1))
    }
)
Storage_chef: BinaryAssociation = BinaryAssociation(
    name="Storage_chef",
    ends={
        Property(name="chef64", type=chef1, multiplicity=Multiplicity(0, 9999)),
        Property(name="storage65", type=Storage1, multiplicity=Multiplicity(0, 9999))
    }
)
Payment_bank_account: BinaryAssociation = BinaryAssociation(
    name="Payment_bank_account",
    ends={
        Property(name="bank_account66", type=bank_account, multiplicity=Multiplicity(1, 1)),
        Property(name="payment67", type=Payment1, multiplicity=Multiplicity(0, 9999))
    }
)
System_bank_account: BinaryAssociation = BinaryAssociation(
    name="System_bank_account",
    ends={
        Property(name="bank_account68", type=bank_account, multiplicity=Multiplicity(0, 1)),
        Property(name="system69", type=System1, multiplicity=Multiplicity(0, 1))
    }
)
System_bank_account2: BinaryAssociation = BinaryAssociation(
    name="System_bank_account2",
    ends={
        Property(name="bank_account70", type=bank_account, multiplicity=Multiplicity(0, 1)),
        Property(name="system71", type=System1, multiplicity=Multiplicity(0, 1))
    }
)
System_contact: BinaryAssociation = BinaryAssociation(
    name="System_contact",
    ends={
        Property(name="contact72", type=contact, multiplicity=Multiplicity(0, 1)),
        Property(name="system73", type=System1, multiplicity=Multiplicity(0, 1))
    }
)
System_help: BinaryAssociation = BinaryAssociation(
    name="System_help",
    ends={
        Property(name="help74", type=help, multiplicity=Multiplicity(1, 1)),
        Property(name="system75", type=System1, multiplicity=Multiplicity(1, 1))
    }
)
owner_webmaster_check_bank_account_for_payments: BinaryAssociation = BinaryAssociation(
    name="owner_webmaster_check_bank_account_for_payments",
    ends={
        Property(name="check_bank_account_for_payments76", type=check_bank_account_for_payments_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_webmaster77", type=owner_System_Actor, multiplicity=Multiplicity(0, 1))
    }
)
owner_webmaster_add_and_get_from_storage: BinaryAssociation = BinaryAssociation(
    name="owner_webmaster_add_and_get_from_storage",
    ends={
        Property(name="add_and_get_from_storage78", type=add_and_get_from_storage_check_storage_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_webmaster79", type=owner_System_Actor, multiplicity=Multiplicity(0, 1))
    }
)
owner_webmaster_order_missing_components: BinaryAssociation = BinaryAssociation(
    name="owner_webmaster_order_missing_components",
    ends={
        Property(name="order_missing_components80", type=order_missing_components_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_webmaster81", type=owner_System_Actor, multiplicity=Multiplicity(0, 1))
    }
)
add_and_get_from_storage_worker: BinaryAssociation = BinaryAssociation(
    name="add_and_get_from_storage_worker",
    ends={
        Property(name="worker18", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="add_and_get_from_storage19", type=add_and_get_from_storage_check_storage_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Employee_list_of_outdated_components: BinaryAssociation = BinaryAssociation(
    name="Employee_list_of_outdated_components",
    ends={
        Property(name="list_of_outdated_components82", type=list_of_outdated_components_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee83", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
worker_order_missing_components: BinaryAssociation = BinaryAssociation(
    name="worker_order_missing_components",
    ends={
        Property(name="order_missing_components20", type=order_missing_components_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="worker21", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
add_constraints_worker: BinaryAssociation = BinaryAssociation(
    name="add_constraints_worker",
    ends={
        Property(name="worker22", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="add_constraints23", type=add_constraints_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
worker_weekly_monthly_plan: BinaryAssociation = BinaryAssociation(
    name="worker_weekly_monthly_plan",
    ends={
        Property(name="weekly_monthly_plan24", type=daily_weekly_monthly_plan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="worker25", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
worker_prepration_plan_dishes: BinaryAssociation = BinaryAssociation(
    name="worker_prepration_plan_dishes",
    ends={
        Property(name="prepration_plan_dishes26", type=prepration_plan_dishes_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="worker27", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
weekly_plan_dishes_chef: BinaryAssociation = BinaryAssociation(
    name="weekly_plan_dishes_chef",
    ends={
        Property(name="chef28", type=chef_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="weekly_plan_dishes29", type=weekly_plan_dishes_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
create_invoice_chef: BinaryAssociation = BinaryAssociation(
    name="create_invoice_chef",
    ends={
        Property(name="chef30", type=chef_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="create_invoice31", type=create_invoice_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Generate_payment_cheque_employes_chef: BinaryAssociation = BinaryAssociation(
    name="Generate_payment_cheque_employes_chef",
    ends={
        Property(name="chef32", type=chef_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="generate_payment_cheque_employes33", type=Generate_payment_cheque_employes_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Accounnt_chef: BinaryAssociation = BinaryAssociation(
    name="Accounnt_chef",
    ends={
        Property(name="chef100", type=chef1, multiplicity=Multiplicity(0, 1)),
        Property(name="accounnt101", type=Accounnt1, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Accounnt2: BinaryAssociation = BinaryAssociation(
    name="Customer_Accounnt2",
    ends={
        Property(name="accounnt102", type=Accounnt1, multiplicity=Multiplicity(0, 1)),
        Property(name="customer103", type=Customer1, multiplicity=Multiplicity(0, 1))
    }
)
Dish_Menu: BinaryAssociation = BinaryAssociation(
    name="Dish_Menu",
    ends={
        Property(name="menu104", type=Menu1, multiplicity=Multiplicity(0, 1)),
        Property(name="dish105", type=Dish, multiplicity=Multiplicity(0, 1))
    }
)
Menu_Dish: BinaryAssociation = BinaryAssociation(
    name="Menu_Dish",
    ends={
        Property(name="dish106", type=Dish, multiplicity=Multiplicity(1, 9999)),
        Property(name="menu107", type=Menu1, multiplicity=Multiplicity(1, 9999))
    }
)
Component_solid: BinaryAssociation = BinaryAssociation(
    name="Component_solid",
    ends={
        Property(name="solid108", type=solid, multiplicity=Multiplicity(0, 1)),
        Property(name="component109", type=Component, multiplicity=Multiplicity(0, 1))
    }
)
Component_liquid: BinaryAssociation = BinaryAssociation(
    name="Component_liquid",
    ends={
        Property(name="liquid110", type=liquid, multiplicity=Multiplicity(0, 1)),
        Property(name="component111", type=Component, multiplicity=Multiplicity(0, 1))
    }
)
food_dish_Component: BinaryAssociation = BinaryAssociation(
    name="food_dish_Component",
    ends={
        Property(name="component112", type=Component, multiplicity=Multiplicity(0, 1)),
        Property(name="food_dish113", type=food_dish, multiplicity=Multiplicity(0, 1))
    }
)
food_dish_Component2: BinaryAssociation = BinaryAssociation(
    name="food_dish_Component2",
    ends={
        Property(name="component114", type=Component, multiplicity=Multiplicity(0, 1)),
        Property(name="food_dish115", type=food_dish, multiplicity=Multiplicity(0, 1))
    }
)
drink_Component: BinaryAssociation = BinaryAssociation(
    name="drink_Component",
    ends={
        Property(name="component116", type=Component, multiplicity=Multiplicity(0, 1)),
        Property(name="drink117", type=drink, multiplicity=Multiplicity(0, 1))
    }
)
menu_food_dish: BinaryAssociation = BinaryAssociation(
    name="menu_food_dish",
    ends={
        Property(name="food_dish118", type=food_dish, multiplicity=Multiplicity(0, 1)),
        Property(name="menu119", type=menu, multiplicity=Multiplicity(0, 1))
    }
)
menu_drink: BinaryAssociation = BinaryAssociation(
    name="menu_drink",
    ends={
        Property(name="drink120", type=drink, multiplicity=Multiplicity(0, 1)),
        Property(name="menu121", type=menu, multiplicity=Multiplicity(0, 1))
    }
)
menu_Csutomer: BinaryAssociation = BinaryAssociation(
    name="menu_Csutomer",
    ends={
        Property(name="csutomer122", type=Csutomer, multiplicity=Multiplicity(0, 1)),
        Property(name="menu123", type=menu, multiplicity=Multiplicity(0, 1))
    }
)
menu_order: BinaryAssociation = BinaryAssociation(
    name="menu_order",
    ends={
        Property(name="order124", type=order, multiplicity=Multiplicity(0, 1)),
        Property(name="menu125", type=menu, multiplicity=Multiplicity(0, 1))
    }
)
order_Csutomer: BinaryAssociation = BinaryAssociation(
    name="order_Csutomer",
    ends={
        Property(name="csutomer126", type=Csutomer, multiplicity=Multiplicity(1, 9999)),
        Property(name="order127", type=order, multiplicity=Multiplicity(1, 9999))
    }
)
Csutomer_shopping_cart: BinaryAssociation = BinaryAssociation(
    name="Csutomer_shopping_cart",
    ends={
        Property(name="shopping_cart128", type=shopping_cart, multiplicity=Multiplicity(0, 1)),
        Property(name="csutomer129", type=Csutomer, multiplicity=Multiplicity(0, 1))
    }
)
order_shopping_cart: BinaryAssociation = BinaryAssociation(
    name="order_shopping_cart",
    ends={
        Property(name="shopping_cart130", type=shopping_cart, multiplicity=Multiplicity(0, 1)),
        Property(name="order131", type=order, multiplicity=Multiplicity(0, 1))
    }
)
shopping_cart_payment: BinaryAssociation = BinaryAssociation(
    name="shopping_cart_payment",
    ends={
        Property(name="payment132", type=payment, multiplicity=Multiplicity(1, 9999)),
        Property(name="shopping_cart133", type=shopping_cart, multiplicity=Multiplicity(1, 9999))
    }
)
planning_weekly_planning_of_dishes__by_waiter: BinaryAssociation = BinaryAssociation(
    name="planning_weekly_planning_of_dishes__by_waiter",
    ends={
        Property(name="weekly_planning_of_dishes__by_waiter134", type=events, multiplicity=Multiplicity(1, 9999)),
        Property(name="planning135", type=dayplan, multiplicity=Multiplicity(1, 1))
    }
)
planning_chef: BinaryAssociation = BinaryAssociation(
    name="planning_chef",
    ends={
        Property(name="chef136", type=chef2, multiplicity=Multiplicity(0, 1)),
        Property(name="planning137", type=dayplan, multiplicity=Multiplicity(0, 1))
    }
)
Component_waiter: BinaryAssociation = BinaryAssociation(
    name="Component_waiter",
    ends={
        Property(name="waiter138", type=kitchen_worker, multiplicity=Multiplicity(1, 9999)),
        Property(name="component139", type=Component, multiplicity=Multiplicity(1, 9999))
    }
)
weekly_planning_of_dishes__by_waiter_Component: BinaryAssociation = BinaryAssociation(
    name="weekly_planning_of_dishes__by_waiter_Component",
    ends={
        Property(name="component140", type=Component, multiplicity=Multiplicity(0, 1)),
        Property(name="weekly_planning_of_dishes__by_waiter141", type=events, multiplicity=Multiplicity(0, 1))
    }
)
weekly_planning_of_dishes__by_waiter_weekly_planning_of_dishes__by_waiter: BinaryAssociation = BinaryAssociation(
    name="weekly_planning_of_dishes__by_waiter_weekly_planning_of_dishes__by_waiter",
    ends={
        Property(name="weekly_planning_of_dishes__by_waiter142", type=events, multiplicity=Multiplicity(0, 1)),
        Property(name="weekly_planning_of_dishes__by_waiter143", type=events, multiplicity=Multiplicity(0, 1))
    }
)
weekly_planning_of_dishes__by_waiter_waiter: BinaryAssociation = BinaryAssociation(
    name="weekly_planning_of_dishes__by_waiter_waiter",
    ends={
        Property(name="waiter144", type=kitchen_worker, multiplicity=Multiplicity(0, 1)),
        Property(name="weekly_planning_of_dishes__by_waiter145", type=events, multiplicity=Multiplicity(0, 1))
    }
)
owner_System_add_and_get_from_storage: BinaryAssociation = BinaryAssociation(
    name="owner_System_add_and_get_from_storage",
    ends={
        Property(name="add_and_get_from_storage84", type=add_and_get_from_storage_check_storage_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_System85", type=owner_System_Actor, multiplicity=Multiplicity(0, 1))
    }
)
System_Storage: BinaryAssociation = BinaryAssociation(
    name="System_Storage",
    ends={
        Property(name="storage86", type=Storage1, multiplicity=Multiplicity(1, 1)),
        Property(name="system87", type=System1, multiplicity=Multiplicity(1, 1))
    }
)
Plan_Customer: BinaryAssociation = BinaryAssociation(
    name="Plan_Customer",
    ends={
        Property(name="customer88", type=Customer1, multiplicity=Multiplicity(1, 1)),
        Property(name="plan89", type=Plan1, multiplicity=Multiplicity(0, 1))
    }
)
Plan_Kitchen_worker: BinaryAssociation = BinaryAssociation(
    name="Plan_Kitchen_worker",
    ends={
        Property(name="kitchen_worker90", type=Kitchen_worker, multiplicity=Multiplicity(0, 9999)),
        Property(name="plan91", type=Plan1, multiplicity=Multiplicity(0, 9999))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order92", type=Order1, multiplicity=Multiplicity(0, 1)),
        Property(name="customer93", type=Customer1, multiplicity=Multiplicity(0, 1))
    }
)
Menu_Shopping_cart: BinaryAssociation = BinaryAssociation(
    name="Menu_Shopping_cart",
    ends={
        Property(name="shopping_cart94", type=Shopping_cart1, multiplicity=Multiplicity(0, 1)),
        Property(name="menu95", type=Menu1, multiplicity=Multiplicity(0, 1))
    }
)
Storage_Kitchen_worker: BinaryAssociation = BinaryAssociation(
    name="Storage_Kitchen_worker",
    ends={
        Property(name="kitchen_worker96", type=Kitchen_worker, multiplicity=Multiplicity(1, 9999)),
        Property(name="storage97", type=Storage1, multiplicity=Multiplicity(1, 9999))
    }
)
order_shopping_cart2: BinaryAssociation = BinaryAssociation(
    name="order_shopping_cart2",
    ends={
        Property(name="shopping_cart158", type=shopping_cart, multiplicity=Multiplicity(1, 9999)),
        Property(name="order159", type=order, multiplicity=Multiplicity(1, 9999))
    }
)
Accounnt_Customer: BinaryAssociation = BinaryAssociation(
    name="Accounnt_Customer",
    ends={
        Property(name="customer98", type=Customer1, multiplicity=Multiplicity(1, 1)),
        Property(name="accounnt99", type=Accounnt1, multiplicity=Multiplicity(1, 1))
    }
)
weekly_planning_of_dishes__by_waiter_food_dish: BinaryAssociation = BinaryAssociation(
    name="weekly_planning_of_dishes__by_waiter_food_dish",
    ends={
        Property(name="food_dish160", type=food_dish, multiplicity=Multiplicity(0, 1)),
        Property(name="weekly_planning_of_dishes__by_waiter161", type=events, multiplicity=Multiplicity(0, 1))
    }
)
Component_owner__system2: BinaryAssociation = BinaryAssociation(
    name="Component_owner__system2",
    ends={
        Property(name="owner__system162", type=owner__system, multiplicity=Multiplicity(0, 1)),
        Property(name="component163", type=Component, multiplicity=Multiplicity(1, 1))
    }
)
weekly_planning_of_dishes__for__waiter_food_dish: BinaryAssociation = BinaryAssociation(
    name="weekly_planning_of_dishes__for__waiter_food_dish",
    ends={
        Property(name="food_dish164", type=food_dish, multiplicity=Multiplicity(1, 9999)),
        Property(name="weekly_planning_of_dishes__for__waiter165", type=events, multiplicity=Multiplicity(1, 9999))
    }
)
chef_kitchen_worker: BinaryAssociation = BinaryAssociation(
    name="chef_kitchen_worker",
    ends={
        Property(name="kitchen_worker166", type=kitchen_worker, multiplicity=Multiplicity(0, 1)),
        Property(name="chef167", type=chef2, multiplicity=Multiplicity(1, 9999))
    }
)
menu_order2: BinaryAssociation = BinaryAssociation(
    name="menu_order2",
    ends={
        Property(name="order168", type=order, multiplicity=Multiplicity(1, 9999)),
        Property(name="menu169", type=menu, multiplicity=Multiplicity(1, 9999))
    }
)
shopping_cart_payment2: BinaryAssociation = BinaryAssociation(
    name="shopping_cart_payment2",
    ends={
        Property(name="payment170", type=payment, multiplicity=Multiplicity(0, 1)),
        Property(name="shopping_cart171", type=shopping_cart, multiplicity=Multiplicity(0, 1))
    }
)
Component_owner__system3: BinaryAssociation = BinaryAssociation(
    name="Component_owner__system3",
    ends={
        Property(name="owner__system172", type=owner__system, multiplicity=Multiplicity(0, 1)),
        Property(name="component173", type=Component, multiplicity=Multiplicity(0, 1))
    }
)
Csutomer_catering: BinaryAssociation = BinaryAssociation(
    name="Csutomer_catering",
    ends={
        Property(name="catering174", type=catering, multiplicity=Multiplicity(0, 1)),
        Property(name="csutomer175", type=Csutomer, multiplicity=Multiplicity(0, 1))
    }
)
menu_catering: BinaryAssociation = BinaryAssociation(
    name="menu_catering",
    ends={
        Property(name="catering176", type=catering, multiplicity=Multiplicity(0, 1)),
        Property(name="menu177", type=menu, multiplicity=Multiplicity(0, 1))
    }
)
Component_weekly_planning_of_dishes__for__waiter: BinaryAssociation = BinaryAssociation(
    name="Component_weekly_planning_of_dishes__for__waiter",
    ends={
        Property(name="weekly_planning_of_dishes__for__waiter178", type=Component, multiplicity=Multiplicity(1, 9999)),
        Property(name="component179", type=events, multiplicity=Multiplicity(1, 1))
    }
)
food_dish_weekly_planning_of_dishes__for__waiter: BinaryAssociation = BinaryAssociation(
    name="food_dish_weekly_planning_of_dishes__for__waiter",
    ends={
        Property(name="weekly_planning_of_dishes__for__waiter180", type=food_dish, multiplicity=Multiplicity(1, 9999)),
        Property(name="food_dish181", type=events, multiplicity=Multiplicity(1, 1))
    }
)
events_order: BinaryAssociation = BinaryAssociation(
    name="events_order",
    ends={
        Property(name="order182", type=order, multiplicity=Multiplicity(0, 9999)),
        Property(name="events183", type=events, multiplicity=Multiplicity(1, 1))
    }
)
weekly_planning_of_dishes__by_waiter_waiter2: BinaryAssociation = BinaryAssociation(
    name="weekly_planning_of_dishes__by_waiter_waiter2",
    ends={
        Property(name="waiter146", type=kitchen_worker, multiplicity=Multiplicity(1, 9999)),
        Property(name="weekly_planning_of_dishes__by_waiter147", type=events, multiplicity=Multiplicity(1, 9999))
    }
)
Component_owner__system: BinaryAssociation = BinaryAssociation(
    name="Component_owner__system",
    ends={
        Property(name="owner__system148", type=owner__system, multiplicity=Multiplicity(0, 1)),
        Property(name="component149", type=Component, multiplicity=Multiplicity(0, 1))
    }
)
chef_planning: BinaryAssociation = BinaryAssociation(
    name="chef_planning",
    ends={
        Property(name="planning150", type=dayplan, multiplicity=Multiplicity(1, 9999)),
        Property(name="chef151", type=chef2, multiplicity=Multiplicity(0, 1))
    }
)
Component_food_dish: BinaryAssociation = BinaryAssociation(
    name="Component_food_dish",
    ends={
        Property(name="food_dish152", type=Component, multiplicity=Multiplicity(1, 9999)),
        Property(name="component153", type=food_dish, multiplicity=Multiplicity(1, 1))
    }
)
Component_drink: BinaryAssociation = BinaryAssociation(
    name="Component_drink",
    ends={
        Property(name="drink154", type=Component, multiplicity=Multiplicity(0, 1)),
        Property(name="component155", type=menu, multiplicity=Multiplicity(0, 1))
    }
)
food_dish_menu: BinaryAssociation = BinaryAssociation(
    name="food_dish_menu",
    ends={
        Property(name="menu156", type=food_dish, multiplicity=Multiplicity(1, 9999)),
        Property(name="food_dish157", type=menu, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_uj5zoENuEeqonN_RS9oRzw",
    types={chef, Employee, Storage, Plan, Customer, Menu, Order, Payment, PrintRecipts, System, Catering, customer_Actor, select_from_menu_UseCase, order_catering_service_UseCase, weekly_plan_of_each_cutomer_UseCase, payorder_UseCase, sign_up_login_logout_UseCase, chef_Actor, Employee_Actor, add_and_get_from_storage_check_storage_UseCase, add_constraints_UseCase, order_missing_components_UseCase, daily_weekly_monthly_plan_UseCase, prepration_plan_dishes_UseCase, weekly_plan_dishes_UseCase, create_invoice_UseCase, Generate_payment_cheque_employes_UseCase, Shopping_cart, date2, Customer_Balance, Accounnt, Customer1, Menu1, Catering1, Customer_Balance1, chef1, Accounnt1, Payment1, PrintRecipts1, Kitchen_worker, Storage1, System1, Plan1, help, contact, UseCase_UseCase, Order1, Shopping_cart1, Web_master, bank_account, owner_System_Actor, check_bank_account_for_payments_UseCase, list_of_outdated_components_UseCase, Dish, Employee1, Waiter, Owner, Chef, Component, menu, food_dish, order, dayplan, kitchen_worker, chef2, drink, liquid, solid, events, Csutomer, payment, shopping_cart, customer_account, solid1, Owner1, Owner2, Account, Account1, Account_for_employee, account_registration, account_type, owner__system, catering, Enumeration_, Enumeration1},
    associations={Employee_Storage, Employee_Plan, customer_select_from_menu, customer_order_catering_service, customer_weekly_plan_of_each_cutomer, customer_payorder, customer_login, chef_login, worker_login, chef_Accounnt, Customer_Accounnt, chef_Accounnt2, Accounnt_Employee, Customer_Customer_Balance, Employee_Storage2, Plan_chef, Menu_Catering, Customer_Catering, Order_Customer, Shopping_cart_Menu, Order_Payment, Payment_PrintRecipts, Web_master_help, Web_master_contact, Storage_chef, Payment_bank_account, System_bank_account, System_bank_account2, System_contact, System_help, owner_webmaster_check_bank_account_for_payments, owner_webmaster_add_and_get_from_storage, owner_webmaster_order_missing_components, add_and_get_from_storage_worker, Employee_list_of_outdated_components, worker_order_missing_components, add_constraints_worker, worker_weekly_monthly_plan, worker_prepration_plan_dishes, weekly_plan_dishes_chef, create_invoice_chef, Generate_payment_cheque_employes_chef, Accounnt_chef, Customer_Accounnt2, Dish_Menu, Menu_Dish, Component_solid, Component_liquid, food_dish_Component, food_dish_Component2, drink_Component, menu_food_dish, menu_drink, menu_Csutomer, menu_order, order_Csutomer, Csutomer_shopping_cart, order_shopping_cart, shopping_cart_payment, planning_weekly_planning_of_dishes__by_waiter, planning_chef, Component_waiter, weekly_planning_of_dishes__by_waiter_Component, weekly_planning_of_dishes__by_waiter_weekly_planning_of_dishes__by_waiter, weekly_planning_of_dishes__by_waiter_waiter, owner_System_add_and_get_from_storage, System_Storage, Plan_Customer, Plan_Kitchen_worker, Customer_Order, Menu_Shopping_cart, Storage_Kitchen_worker, order_shopping_cart2, Accounnt_Customer, weekly_planning_of_dishes__by_waiter_food_dish, Component_owner__system2, weekly_planning_of_dishes__for__waiter_food_dish, chef_kitchen_worker, menu_order2, shopping_cart_payment2, Component_owner__system3, Csutomer_catering, menu_catering, Component_weekly_planning_of_dishes__for__waiter, food_dish_weekly_planning_of_dishes__for__waiter, events_order, weekly_planning_of_dishes__by_waiter_waiter2, Component_owner__system, chef_planning, Component_food_dish, Component_drink, food_dish_menu},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)