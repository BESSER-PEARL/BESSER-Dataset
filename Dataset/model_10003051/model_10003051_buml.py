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
Bill = Class(name="Bill")
Payment = Class(name="Payment")
Table = Class(name="Table")
Order = Class(name="Order")
Menu = Class(name="Menu")
Drinks = Class(name="Drinks")
Discount = Class(name="Discount")
Input_Order_UseCase = Class(name="Input_Order_UseCase")
Order_food_UseCase = Class(name="Order_food_UseCase")
Alerted_to_Prepare_food_UseCase = Class(name="Alerted_to_Prepare_food_UseCase")
Alerted_to_Serve_drinks_UseCase = Class(name="Alerted_to_Serve_drinks_UseCase")
Alerted_to_Serve_Food_UseCase = Class(name="Alerted_to_Serve_Food_UseCase")
Input_Order_external = Class(name="Input_Order_external")
Alerted_to_Serve_drinks_external = Class(name="Alerted_to_Serve_drinks_external")
Alerted_to_Serve_Food_external = Class(name="Alerted_to_Serve_Food_external")
Print_bill_external = Class(name="Print_bill_external")
Input_payment_details_external = Class(name="Input_payment_details_external")
Alerted_to_Prepare_food_external = Class(name="Alerted_to_Prepare_food_external")
Alerted_to_Prepare_drinks_external = Class(name="Alerted_to_Prepare_drinks_external")
Print_bill_UseCase = Class(name="Print_bill_UseCase")
Alerted_to_Prepare_drinks_UseCase = Class(name="Alerted_to_Prepare_drinks_UseCase")
Pay_for_food_UseCase = Class(name="Pay_for_food_UseCase")
Grant_discount_UseCase = Class(name="Grant_discount_UseCase")
Input_payment_details_UseCase = Class(name="Input_payment_details_UseCase")
Change_Order_UseCase = Class(name="Change_Order_UseCase")
View_statistics_UseCase = Class(name="View_statistics_UseCase")
Diner_Actor = Class(name="Diner_Actor")
Waiter_Actor = Class(name="Waiter_Actor")
Kitchen_Staff_Actor = Class(name="Kitchen_Staff_Actor")
Bar_Staff_Actor = Class(name="Bar_Staff_Actor")
Management_Actor = Class(name="Management_Actor")
_Component = Class(name="_Component")
Order_food_UseCase1 = Class(name="Order_food_UseCase1")
Pay_for_food_UseCase1 = Class(name="Pay_for_food_UseCase1")
Grant_discount_external = Class(name="Grant_discount_external")
View_statistics_external = Class(name="View_statistics_external")

# Bill class attributes and methods

# Payment class attributes and methods
Payment_paymentType: Property = Property(name="paymentType", type=StringType)
Payment.attributes={Payment_paymentType}

# Table class attributes and methods
Table_tableID: Property = Property(name="tableID", type=IntegerType)
Table.attributes={Table_tableID}

# Order class attributes and methods

# Menu class attributes and methods
Menu_starter: Property = Property(name="starter", type=StringType)
Menu_mainCourse: Property = Property(name="mainCourse", type=StringType)
Menu_desert: Property = Property(name="desert", type=StringType)
Menu_specialCourse: Property = Property(name="specialCourse", type=StringType)
Menu.attributes={Menu_starter, Menu_desert, Menu_specialCourse, Menu_mainCourse}

# Drinks class attributes and methods
Drinks_softDrink: Property = Property(name="softDrink", type=StringType)
Drinks_beer: Property = Property(name="beer", type=StringType)
Drinks_wine: Property = Property(name="wine", type=StringType)
Drinks_spirits: Property = Property(name="spirits", type=StringType)
Drinks_cocktail: Property = Property(name="cocktail", type=StringType)
Drinks.attributes={Drinks_softDrink, Drinks_cocktail, Drinks_wine, Drinks_beer, Drinks_spirits}

# Discount class attributes and methods
Discount_discountAmount: Property = Property(name="discountAmount", type=IntegerType)
Discount.attributes={Discount_discountAmount}

# Input_Order_UseCase class attributes and methods

# Order_food_UseCase class attributes and methods

# Alerted_to_Prepare_food_UseCase class attributes and methods

# Alerted_to_Serve_drinks_UseCase class attributes and methods

# Alerted_to_Serve_Food_UseCase class attributes and methods

# Input_Order_external class attributes and methods

# Alerted_to_Serve_drinks_external class attributes and methods

# Alerted_to_Serve_Food_external class attributes and methods

# Print_bill_external class attributes and methods

# Input_payment_details_external class attributes and methods

# Alerted_to_Prepare_food_external class attributes and methods

# Alerted_to_Prepare_drinks_external class attributes and methods

# Print_bill_UseCase class attributes and methods

# Alerted_to_Prepare_drinks_UseCase class attributes and methods

# Pay_for_food_UseCase class attributes and methods

# Grant_discount_UseCase class attributes and methods

# Input_payment_details_UseCase class attributes and methods

# Change_Order_UseCase class attributes and methods

# View_statistics_UseCase class attributes and methods

# Diner_Actor class attributes and methods

# Waiter_Actor class attributes and methods

# Kitchen_Staff_Actor class attributes and methods

# Bar_Staff_Actor class attributes and methods

# Management_Actor class attributes and methods

# _Component class attributes and methods

# Order_food_UseCase1 class attributes and methods

# Pay_for_food_UseCase1 class attributes and methods

# Grant_discount_external class attributes and methods

# View_statistics_external class attributes and methods

# Relationships
Bill_Payment: BinaryAssociation = BinaryAssociation(
    name="Bill_Payment",
    ends={
        Property(name="payment0", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="bill1", type=Bill, multiplicity=Multiplicity(0, 9999))
    }
)
Bill_Table: BinaryAssociation = BinaryAssociation(
    name="Bill_Table",
    ends={
        Property(name="Bill_Table_02", type=Table, multiplicity=Multiplicity(0, 1)),
        Property(name="Bill_Table_13", type=Bill, multiplicity=Multiplicity(1, 1))
    }
)
Bill_Order: BinaryAssociation = BinaryAssociation(
    name="Bill_Order",
    ends={
        Property(name="Bill_Order_04", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="Bill_Order_15", type=Bill, multiplicity=Multiplicity(1, 1))
    }
)
Order_Menu: BinaryAssociation = BinaryAssociation(
    name="Order_Menu",
    ends={
        Property(name="Order_Menu_06", type=Menu, multiplicity=Multiplicity(0, 9999)),
        Property(name="Order_Menu_17", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_Drinks: BinaryAssociation = BinaryAssociation(
    name="Order_Drinks",
    ends={
        Property(name="Order_Drinks_08", type=Drinks, multiplicity=Multiplicity(0, 9999)),
        Property(name="Order_Drinks_19", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Bill_Discount: BinaryAssociation = BinaryAssociation(
    name="Bill_Discount",
    ends={
        Property(name="discount10", type=Discount, multiplicity=Multiplicity(0, 9999)),
        Property(name="bill11", type=Bill, multiplicity=Multiplicity(0, 1))
    }
)
Diner_Order_food: BinaryAssociation = BinaryAssociation(
    name="Diner_Order_food",
    ends={
        Property(name="order_food12", type=Order_food_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="diner13", type=Diner_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Diner_Pay_for_food: BinaryAssociation = BinaryAssociation(
    name="Diner_Pay_for_food",
    ends={
        Property(name="pay_for_food14", type=Pay_for_food_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="diner15", type=Diner_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Input_Order: BinaryAssociation = BinaryAssociation(
    name="Waiter_Input_Order",
    ends={
        Property(name="input_Order16", type=Input_Order_external, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter17", type=Waiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Alerted_to_Serve_drinks: BinaryAssociation = BinaryAssociation(
    name="Waiter_Alerted_to_Serve_drinks",
    ends={
        Property(name="alerted_to_Serve_drinks18", type=Alerted_to_Serve_drinks_external, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter19", type=Waiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Alerted_to_Serve_Food: BinaryAssociation = BinaryAssociation(
    name="Waiter_Alerted_to_Serve_Food",
    ends={
        Property(name="alerted_to_Serve_Food20", type=Alerted_to_Serve_Food_external, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter21", type=Waiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Print_bill: BinaryAssociation = BinaryAssociation(
    name="Waiter_Print_bill",
    ends={
        Property(name="print_bill22", type=Print_bill_external, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter23", type=Waiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Input_payment_details: BinaryAssociation = BinaryAssociation(
    name="Waiter_Input_payment_details",
    ends={
        Property(name="input_payment_details24", type=Input_payment_details_external, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter25", type=Waiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Kitchen_Staff_Alerted_to_Prepare_food: BinaryAssociation = BinaryAssociation(
    name="Kitchen_Staff_Alerted_to_Prepare_food",
    ends={
        Property(name="alerted_to_Prepare_food26", type=Alerted_to_Prepare_food_external, multiplicity=Multiplicity(0, 1)),
        Property(name="kitchen_Staff27", type=Kitchen_Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bar_Staff_Alerted_to_Prepare_drinks: BinaryAssociation = BinaryAssociation(
    name="Bar_Staff_Alerted_to_Prepare_drinks",
    ends={
        Property(name="alerted_to_Prepare_drinks28", type=Alerted_to_Prepare_drinks_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bar_Staff29", type=Bar_Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Management_Grant_discount: BinaryAssociation = BinaryAssociation(
    name="Management_Grant_discount",
    ends={
        Property(name="grant_discount30", type=Grant_discount_external, multiplicity=Multiplicity(0, 1)),
        Property(name="management31", type=Management_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Management_View_statistics: BinaryAssociation = BinaryAssociation(
    name="Management_View_statistics",
    ends={
        Property(name="view_statistics32", type=View_statistics_external, multiplicity=Multiplicity(0, 1)),
        Property(name="management33", type=Management_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Input_Order2: BinaryAssociation = BinaryAssociation(
    name="Waiter_Input_Order2",
    ends={
        Property(name="input_Order34", type=Input_Order_external, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter35", type=Waiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f91bdd51_4f2b_4e58_a95d_482ffca6bbad",
    types={Bill, Payment, Table, Order, Menu, Drinks, Discount, Input_Order_UseCase, Order_food_UseCase, Alerted_to_Prepare_food_UseCase, Alerted_to_Serve_drinks_UseCase, Alerted_to_Serve_Food_UseCase, Input_Order_external, Alerted_to_Serve_drinks_external, Alerted_to_Serve_Food_external, Print_bill_external, Input_payment_details_external, Alerted_to_Prepare_food_external, Alerted_to_Prepare_drinks_external, Print_bill_UseCase, Alerted_to_Prepare_drinks_UseCase, Pay_for_food_UseCase, Grant_discount_UseCase, Input_payment_details_UseCase, Change_Order_UseCase, View_statistics_UseCase, Diner_Actor, Waiter_Actor, Kitchen_Staff_Actor, Bar_Staff_Actor, Management_Actor, _Component, Order_food_UseCase1, Pay_for_food_UseCase1, Grant_discount_external, View_statistics_external},
    associations={Bill_Payment, Bill_Table, Bill_Order, Order_Menu, Order_Drinks, Bill_Discount, Diner_Order_food, Diner_Pay_for_food, Waiter_Input_Order, Waiter_Alerted_to_Serve_drinks, Waiter_Alerted_to_Serve_Food, Waiter_Print_bill, Waiter_Input_payment_details, Kitchen_Staff_Alerted_to_Prepare_food, Bar_Staff_Alerted_to_Prepare_drinks, Management_Grant_discount, Management_View_statistics, Waiter_Input_Order2},
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