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

# Classes
Supplier = Class(name="Supplier")
Orders = Class(name="Orders")
Stock = Class(name="Stock")
Items = Class(name="Items")
Interface_Interface = Class(name="Interface_Interface")
Section = Class(name="Section")
Employee = Class(name="Employee")
Attendance = Class(name="Attendance")
Leave = Class(name="Leave")
Staff = Class(name="Staff")
Worker = Class(name="Worker")
Administrator = Class(name="Administrator")
Order_Sent = Class(name="Order_Sent")
Salary = Class(name="Salary")
Bonus = Class(name="Bonus")
ETF_EPF = Class(name="ETF_EPF")
Daily_production = Class(name="Daily_production")

# Supplier class attributes and methods
Supplier_Supplier_id: Property = Property(name="Supplier_id", type=StringType)
Supplier_name: Property = Property(name="name", type=StringType)
Supplier_address: Property = Property(name="address", type=StringType)
Supplier_contact_no: Property = Property(name="contact_no", type=IntegerType)
Supplier_email: Property = Property(name="email", type=StringType)
Supplier.attributes={Supplier_email, Supplier_Supplier_id, Supplier_address, Supplier_name, Supplier_contact_no}

# Orders class attributes and methods
Orders_order_id: Property = Property(name="order_id", type=StringType)
Orders_item_id: Property = Property(name="item_id", type=StringType)
Orders_Quantity: Property = Property(name="Quantity", type=StringType)
Orders_order_date: Property = Property(name="order_date", type=StringType)
Orders_status: Property = Property(name="status", type=StringType)
Orders_recieved_date: Property = Property(name="recieved_date", type=StringType)
Orders_price_per_unit: Property = Property(name="price_per_unit", type=StringType)
Orders_total_amount: Property = Property(name="total_amount", type=StringType)
Orders.attributes={Orders_item_id, Orders_Quantity, Orders_recieved_date, Orders_status, Orders_order_date, Orders_total_amount, Orders_price_per_unit, Orders_order_id}

# Stock class attributes and methods
Stock_stock_id: Property = Property(name="stock_id", type=StringType)
Stock_item_id: Property = Property(name="item_id", type=StringType)
Stock_quantity: Property = Property(name="quantity", type=StringType)
Stock_exp_date: Property = Property(name="exp_date", type=StringType)
Stock.attributes={Stock_stock_id, Stock_quantity, Stock_item_id, Stock_exp_date}

# Items class attributes and methods
Items_item_id: Property = Property(name="item_id", type=StringType)
Items_item_code: Property = Property(name="item_code", type=StringType)
Items_description: Property = Property(name="description", type=StringType)
Items_re_order_qty: Property = Property(name="re_order_qty", type=StringType)
Items_unit_of_measure: Property = Property(name="unit_of_measure", type=StringType)
Items_price_per_unit: Property = Property(name="price_per_unit", type=StringType)
Items.attributes={Items_unit_of_measure, Items_item_code, Items_re_order_qty, Items_price_per_unit, Items_description, Items_item_id}

# Interface_Interface class attributes and methods

# Section class attributes and methods
Section_section_id: Property = Property(name="section_id", type=StringType)
Section_name: Property = Property(name="name", type=StringType)
Section_description: Property = Property(name="description", type=StringType)
Section.attributes={Section_description, Section_section_id, Section_name}

# Employee class attributes and methods
Employee_fname: Property = Property(name="fname", type=StringType)
Employee_lname: Property = Property(name="lname", type=StringType)
Employee_address: Property = Property(name="address", type=StringType)
Employee_email: Property = Property(name="email", type=StringType)
Employee_phone: Property = Property(name="phone", type=IntegerType)
Employee_DOB: Property = Property(name="DOB", type=StringType)
Employee_attendance_count: Property = Property(name="attendance_count", type=IntegerType)
Employee_emp_id: Property = Property(name="emp_id", type=StringType)
Employee.attributes={Employee_address, Employee_lname, Employee_attendance_count, Employee_DOB, Employee_emp_id, Employee_phone, Employee_email, Employee_fname}

# Attendance class attributes and methods
Attendance_att_id: Property = Property(name="att_id", type=StringType)
Attendance_in_time: Property = Property(name="in_time", type=StringType)
Attendance_out_time: Property = Property(name="out_time", type=StringType)
Attendance_work_hours: Property = Property(name="work_hours", type=StringType)
Attendance_OT_hours: Property = Property(name="OT_hours", type=StringType)
Attendance_date: Property = Property(name="date", type=StringType)
Attendance.attributes={Attendance_att_id, Attendance_OT_hours, Attendance_date, Attendance_in_time, Attendance_work_hours, Attendance_out_time}

# Leave class attributes and methods
Leave_leave_id: Property = Property(name="leave_id", type=StringType)
Leave_date: Property = Property(name="date", type=StringType)
Leave_from: Property = Property(name="from", type=StringType)
Leave_to: Property = Property(name="to", type=StringType)
Leave_leave_type: Property = Property(name="leave_type", type=StringType)
Leave.attributes={Leave_from, Leave_leave_type, Leave_to, Leave_leave_id, Leave_date}

# Staff class attributes and methods
Staff_Position: Property = Property(name="Position", type=StringType)
Staff.attributes={Staff_Position}

# Worker class attributes and methods
Worker_section: Property = Property(name="section", type=StringType)
Worker_team: Property = Property(name="team", type=IntegerType)
Worker.attributes={Worker_team, Worker_section}

# Administrator class attributes and methods
Administrator_username: Property = Property(name="username", type=StringType)
Administrator_password: Property = Property(name="password", type=StringType)
Administrator.attributes={Administrator_password, Administrator_username}

# Order_Sent class attributes and methods
Order_Sent_sentOrder_id: Property = Property(name="sentOrder_id", type=StringType)
Order_Sent_Item_id: Property = Property(name="Item_id", type=StringType)
Order_Sent_quantity: Property = Property(name="quantity", type=StringType)
Order_Sent_order_status: Property = Property(name="order_status", type=StringType)
Order_Sent.attributes={Order_Sent_Item_id, Order_Sent_quantity, Order_Sent_sentOrder_id, Order_Sent_order_status}

# Salary class attributes and methods
Salary_id: Property = Property(name="id", type=IntegerType)
Salary_position: Property = Property(name="position", type=StringType)
Salary_Salary: Property = Property(name="Salary", type=StringType)
Salary.attributes={Salary_Salary, Salary_id, Salary_position}

# Bonus class attributes and methods
Bonus_id: Property = Property(name="id", type=IntegerType)
Bonus_type: Property = Property(name="type", type=StringType)
Bonus_amount: Property = Property(name="amount", type=StringType)
Bonus_IDnum: Property = Property(name="IDnum", type=IntegerType)
Bonus.attributes={Bonus_id, Bonus_amount, Bonus_IDnum, Bonus_type}

# ETF_EPF class attributes and methods
ETF_EPF_no: Property = Property(name="no", type=IntegerType)
ETF_EPF_rate: Property = Property(name="rate", type=StringType)
ETF_EPF_type: Property = Property(name="type", type=StringType)
ETF_EPF.attributes={ETF_EPF_rate, ETF_EPF_no, ETF_EPF_type}

# Daily_production class attributes and methods
Daily_production_date: Property = Property(name="date", type=StringType)
Daily_production_pro_number: Property = Property(name="pro_number", type=StringType)
Daily_production_item_code: Property = Property(name="item_code", type=StringType)
Daily_production_section: Property = Property(name="section", type=IntegerType)
Daily_production_curr_qty: Property = Property(name="curr_qty", type=IntegerType)
Daily_production_item_name: Property = Property(name="item_name", type=StringType)
Daily_production_future_Qty: Property = Property(name="future_Qty", type=IntegerType)
Daily_production.attributes={Daily_production_curr_qty, Daily_production_item_code, Daily_production_pro_number, Daily_production_item_name, Daily_production_date, Daily_production_section, Daily_production_future_Qty}

# Relationships
Supplier_Orders: BinaryAssociation = BinaryAssociation(
    name="Supplier_Orders",
    ends={
        Property(name="orders0", type=Orders, multiplicity=Multiplicity(1, 1)),
        Property(name="supplier1", type=Supplier, multiplicity=Multiplicity(1, 9999))
    }
)
Stock_Items: BinaryAssociation = BinaryAssociation(
    name="Stock_Items",
    ends={
        Property(name="items2", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="stock3", type=Stock, multiplicity=Multiplicity(1, 9999))
    }
)
Orders_Items: BinaryAssociation = BinaryAssociation(
    name="Orders_Items",
    ends={
        Property(name="items4", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="orders5", type=Orders, multiplicity=Multiplicity(1, 9999))
    }
)
Employee_Section: BinaryAssociation = BinaryAssociation(
    name="Employee_Section",
    ends={
        Property(name="section6", type=Section, multiplicity=Multiplicity(1, 9999)),
        Property(name="employee7", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance",
    ends={
        Property(name="attendance8", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="employee9", type=Employee, multiplicity=Multiplicity(1, 1))
    }
)
Leave_Employee: BinaryAssociation = BinaryAssociation(
    name="Leave_Employee",
    ends={
        Property(name="employee10", type=Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="leave11", type=Leave, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Orders: BinaryAssociation = BinaryAssociation(
    name="Administrator_Orders",
    ends={
        Property(name="orders12", type=Orders, multiplicity=Multiplicity(1, 9999)),
        Property(name="administrator13", type=Administrator, multiplicity=Multiplicity(1, 1))
    }
)
Order_Sent_Administrator: BinaryAssociation = BinaryAssociation(
    name="Order_Sent_Administrator",
    ends={
        Property(name="administrator14", type=Administrator, multiplicity=Multiplicity(1, 9999)),
        Property(name="order_Sent15", type=Order_Sent, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary16", type=Salary, multiplicity=Multiplicity(1, 1)),
        Property(name="employee17", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Salary_Bonus: BinaryAssociation = BinaryAssociation(
    name="Salary_Bonus",
    ends={
        Property(name="bonus18", type=Bonus, multiplicity=Multiplicity(0, 1)),
        Property(name="salary19", type=Salary, multiplicity=Multiplicity(0, 1))
    }
)
Salary_ETF_EPF: BinaryAssociation = BinaryAssociation(
    name="Salary_ETF_EPF",
    ends={
        Property(name="eTF_EPF20", type=ETF_EPF, multiplicity=Multiplicity(1, 1)),
        Property(name="salary21", type=Salary, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_SzT_0MqdEeeM1PgT03_3Vg",
    types={Supplier, Orders, Stock, Items, Interface_Interface, Section, Employee, Attendance, Leave, Staff, Worker, Administrator, Order_Sent, Salary, Bonus, ETF_EPF, Daily_production},
    associations={Supplier_Orders, Stock_Items, Orders_Items, Employee_Section, Employee_Attendance, Leave_Employee, Administrator_Orders, Order_Sent_Administrator, Employee_Salary, Salary_Bonus, Salary_ETF_EPF},
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