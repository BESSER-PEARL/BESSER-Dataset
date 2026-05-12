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
Print_Receipt: Enumeration = Enumeration(
    name="Print_Receipt",
    literals={
            
    }
)

# Classes
restaurant = Class(name="restaurant")
customer = Class(name="customer")
staff = Class(name="staff")
menu = Class(name="menu")
chef = Class(name="chef")
waiter = Class(name="waiter")
order = Class(name="order")
payment = Class(name="payment")
bill = Class(name="bill")

# restaurant class attributes and methods
restaurant_tableid: Property = Property(name="tableid", type=IntegerType)
restaurant_Menuid: Property = Property(name="Menuid", type=StringType)
restaurant.attributes={restaurant_Menuid, restaurant_tableid}

# customer class attributes and methods
customer_Tableno: Property = Property(name="Tableno", type=IntegerType)
customer_Name: Property = Property(name="Name", type=StringType)
customer_Order: Property = Property(name="Order", type=StringType)
customer.attributes={customer_Name, customer_Tableno, customer_Order}

# staff class attributes and methods
staff_staffID: Property = Property(name="staffID", type=IntegerType)
staff_name: Property = Property(name="name", type=StringType)
staff_jobtype: Property = Property(name="jobtype", type=StringType)
staff.attributes={staff_name, staff_jobtype, staff_staffID}

# menu class attributes and methods
menu_Menuid: Property = Property(name="Menuid", type=StringType)
menu_Menuname: Property = Property(name="Menuname", type=StringType)
menu_Price: Property = Property(name="Price", type=IntegerType)
menu.attributes={menu_Menuid, menu_Price, menu_Menuname}

# chef class attributes and methods
chef_Staffid: Property = Property(name="Staffid", type=IntegerType)
chef_Name: Property = Property(name="Name", type=StringType)
chef.attributes={chef_Staffid, chef_Name}

# waiter class attributes and methods
waiter_Staffid: Property = Property(name="Staffid", type=IntegerType)
waiter_name: Property = Property(name="name", type=StringType)
waiter.attributes={waiter_Staffid, waiter_name}

# order class attributes and methods
order_orderid: Property = Property(name="orderid", type=IntegerType)
order_price: Property = Property(name="price", type=IntegerType)
order_orderdate: Property = Property(name="orderdate", type=StringType)
order.attributes={order_price, order_orderid, order_orderdate}

# payment class attributes and methods
payment_tableno: Property = Property(name="tableno", type=IntegerType)
payment_name: Property = Property(name="name", type=StringType)
payment.attributes={payment_tableno, payment_name}

# bill class attributes and methods
bill_tableno: Property = Property(name="tableno", type=IntegerType)
bill_orderid: Property = Property(name="orderid", type=IntegerType)
bill_menuid: Property = Property(name="menuid", type=StringType)
bill.attributes={bill_orderid, bill_menuid, bill_tableno}

# Relationships
customer__menu: BinaryAssociation = BinaryAssociation(
    name="customer__menu",
    ends={
        Property(name="menu2", type=menu, multiplicity=Multiplicity(0, 1)),
        Property(name="browse_menu3", type=customer, multiplicity=Multiplicity(0, 1))
    }
)
menu_order: BinaryAssociation = BinaryAssociation(
    name="menu_order",
    ends={
        Property(name="order4", type=order, multiplicity=Multiplicity(0, 1)),
        Property(name="menu5", type=menu, multiplicity=Multiplicity(0, 1))
    }
)
order_payment: BinaryAssociation = BinaryAssociation(
    name="order_payment",
    ends={
        Property(name="payment0", type=payment, multiplicity=Multiplicity(0, 1)),
        Property(name="order1", type=order, multiplicity=Multiplicity(0, 1))
    }
)
waiter_menu: BinaryAssociation = BinaryAssociation(
    name="waiter_menu",
    ends={
        Property(name="menu6", type=menu, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter7", type=waiter, multiplicity=Multiplicity(0, 1))
    }
)
waiter_chef: BinaryAssociation = BinaryAssociation(
    name="waiter_chef",
    ends={
        Property(name="chef8", type=chef, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter9", type=waiter, multiplicity=Multiplicity(0, 1))
    }
)
payment_customer: BinaryAssociation = BinaryAssociation(
    name="payment_customer",
    ends={
        Property(name="customer10", type=customer, multiplicity=Multiplicity(0, 1)),
        Property(name="payment_customer_111", type=payment, multiplicity=Multiplicity(0, 1))
    }
)
menu_staff: BinaryAssociation = BinaryAssociation(
    name="menu_staff",
    ends={
        Property(name="staff12", type=staff, multiplicity=Multiplicity(0, 1)),
        Property(name="menu13", type=menu, multiplicity=Multiplicity(0, 1))
    }
)
waiter_staff: BinaryAssociation = BinaryAssociation(
    name="waiter_staff",
    ends={
        Property(name="staff14", type=staff, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter15", type=waiter, multiplicity=Multiplicity(0, 1))
    }
)
restaurant_customer: BinaryAssociation = BinaryAssociation(
    name="restaurant_customer",
    ends={
        Property(name="customer16", type=customer, multiplicity=Multiplicity(0, 1)),
        Property(name="restaurant17", type=restaurant, multiplicity=Multiplicity(0, 1))
    }
)
restaurant_staff2: BinaryAssociation = BinaryAssociation(
    name="restaurant_staff2",
    ends={
        Property(name="staff18", type=staff, multiplicity=Multiplicity(0, 1)),
        Property(name="restaurant19", type=restaurant, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6_P0ACN5EeisAYMSV00L2Q",
    types={restaurant, customer, staff, menu, chef, waiter, order, payment, bill, Print_Receipt},
    associations={customer__menu, menu_order, order_payment, waiter_menu, waiter_chef, payment_customer, menu_staff, waiter_staff, restaurant_customer, restaurant_staff2},
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