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
seller__Actor = Class(name="seller__Actor")
direct_sale_UseCase = Class(name="direct_sale_UseCase")
later_payment_sale__UseCase = Class(name="later_payment_sale__UseCase")
Online_customer_request_UseCase = Class(name="Online_customer_request_UseCase")
customer_name_UseCase = Class(name="customer_name_UseCase")
customer_address__UseCase = Class(name="customer_address__UseCase")
Card_id_registration_UseCase = Class(name="Card_id_registration_UseCase")
cashier_Actor = Class(name="cashier_Actor")
Add_sold_products_UseCase = Class(name="Add_sold_products_UseCase")
Calculating_the_check_UseCase = Class(name="Calculating_the_check_UseCase")
Make_comprehensive_reports_UseCase = Class(name="Make_comprehensive_reports_UseCase")
Entering_prices_UseCase = Class(name="Entering_prices_UseCase")
manager_Actor = Class(name="manager_Actor")
delete_customer__UseCase = Class(name="delete_customer__UseCase")
update_section_UseCase = Class(name="update_section_UseCase")
add_products_to_sections__UseCase = Class(name="add_products_to_sections__UseCase")
seller_registration_UseCase = Class(name="seller_registration_UseCase")
delete_seller_UseCase = Class(name="delete_seller_UseCase")
add_seller__UseCase = Class(name="add_seller__UseCase")
add_customer_UseCase = Class(name="add_customer_UseCase")
the_product = Class(name="the_product")
online_market = Class(name="online_market")
section = Class(name="section")
seller = Class(name="seller")
direct_sale = Class(name="direct_sale")
sale_by_instalment = Class(name="sale_by_instalment")
customer = Class(name="customer")

# seller__Actor class attributes and methods

# direct_sale_UseCase class attributes and methods

# later_payment_sale__UseCase class attributes and methods

# Online_customer_request_UseCase class attributes and methods

# customer_name_UseCase class attributes and methods

# customer_address__UseCase class attributes and methods

# Card_id_registration_UseCase class attributes and methods

# cashier_Actor class attributes and methods

# Add_sold_products_UseCase class attributes and methods

# Calculating_the_check_UseCase class attributes and methods

# Make_comprehensive_reports_UseCase class attributes and methods

# Entering_prices_UseCase class attributes and methods

# manager_Actor class attributes and methods

# delete_customer__UseCase class attributes and methods

# update_section_UseCase class attributes and methods

# add_products_to_sections__UseCase class attributes and methods

# seller_registration_UseCase class attributes and methods

# delete_seller_UseCase class attributes and methods

# add_seller__UseCase class attributes and methods

# add_customer_UseCase class attributes and methods

# the_product class attributes and methods
the_product_name: Property = Property(name="name", type=StringType)
the_product_type: Property = Property(name="type", type=StringType)
the_product_price: Property = Property(name="price", type=IntegerType)
the_product.attributes={the_product_name, the_product_price, the_product_type}

# online_market class attributes and methods
online_market_register_id_card: Property = Property(name="register_id_card", type=IntegerType)
online_market_customer_address: Property = Property(name="customer_address", type=StringType)
online_market_customer_name: Property = Property(name="customer_name", type=StringType)
online_market_product_type: Property = Property(name="product_type", type=StringType)
online_market_product_price: Property = Property(name="product_price", type=StringType)
online_market.attributes={online_market_register_id_card, online_market_customer_address, online_market_customer_name, online_market_product_type, online_market_product_price}

# section class attributes and methods
section_name: Property = Property(name="name", type=StringType)
section_number: Property = Property(name="number", type=IntegerType)
section.attributes={section_name, section_number}

# seller class attributes and methods
seller_name: Property = Property(name="name", type=StringType)
seller_section_name: Property = Property(name="section_name", type=StringType)
seller_salary: Property = Property(name="salary", type=IntegerType)
seller_number: Property = Property(name="number", type=IntegerType)
seller.attributes={seller_number, seller_salary, seller_name, seller_section_name}

# direct_sale class attributes and methods
direct_sale_username: Property = Property(name="username", type=StringType)
direct_sale_saled_products: Property = Property(name="saled_products", type=StringType)
direct_sale_attribute: Property = Property(name="attribute", type=StringType)
direct_sale.attributes={direct_sale_username, direct_sale_attribute, direct_sale_saled_products}

# sale_by_instalment class attributes and methods
sale_by_instalment_customer_name: Property = Property(name="customer_name", type=StringType)
sale_by_instalment_id_card: Property = Property(name="id_card", type=IntegerType)
sale_by_instalment_saled_product: Property = Property(name="saled_product", type=StringType)
sale_by_instalment.attributes={sale_by_instalment_customer_name, sale_by_instalment_id_card, sale_by_instalment_saled_product}

# customer class attributes and methods
customer_name: Property = Property(name="name", type=StringType)
customer_id_card: Property = Property(name="id_card", type=IntegerType)
customer_address: Property = Property(name="address", type=StringType)
customer.attributes={customer_address, customer_id_card, customer_name}

# Relationships
seller__later_payment_sale: BinaryAssociation = BinaryAssociation(
    name="seller__later_payment_sale",
    ends={
        Property(name="later_payment_sale2", type=later_payment_sale__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="seller3", type=seller__Actor, multiplicity=Multiplicity(0, 1))
    }
)
seller__Online_customer_request: BinaryAssociation = BinaryAssociation(
    name="seller__Online_customer_request",
    ends={
        Property(name="online_customer_request4", type=Online_customer_request_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="seller5", type=seller__Actor, multiplicity=Multiplicity(0, 1))
    }
)
cashier_Add_sold_products: BinaryAssociation = BinaryAssociation(
    name="cashier_Add_sold_products",
    ends={
        Property(name="add_sold_products6", type=Add_sold_products_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cashier7", type=cashier_Actor, multiplicity=Multiplicity(0, 1))
    }
)
cashier_Calculating_the_check: BinaryAssociation = BinaryAssociation(
    name="cashier_Calculating_the_check",
    ends={
        Property(name="calculating_the_check8", type=Calculating_the_check_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cashier9", type=cashier_Actor, multiplicity=Multiplicity(0, 1))
    }
)
cashier_Make_comprehensive_reports: BinaryAssociation = BinaryAssociation(
    name="cashier_Make_comprehensive_reports",
    ends={
        Property(name="make_comprehensive_reports10", type=Make_comprehensive_reports_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cashier11", type=cashier_Actor, multiplicity=Multiplicity(0, 1))
    }
)
cashier_UseCase: BinaryAssociation = BinaryAssociation(
    name="cashier_UseCase",
    ends={
        Property(name="useCase12", type=Entering_prices_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cashier13", type=cashier_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase6: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase6",
    ends={
        Property(name="useCase614", type=add_seller__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor15", type=manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase2",
    ends={
        Property(name="useCase216", type=update_section_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor17", type=manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase7: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase7",
    ends={
        Property(name="useCase718", type=add_customer_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor19", type=manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase4: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase4",
    ends={
        Property(name="useCase420", type=seller_registration_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor21", type=manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase5: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase5",
    ends={
        Property(name="useCase522", type=delete_seller_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor23", type=manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="useCase24", type=delete_customer__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor25", type=manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase3: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase3",
    ends={
        Property(name="useCase326", type=add_products_to_sections__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor27", type=manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
seller__direct_sale: BinaryAssociation = BinaryAssociation(
    name="seller__direct_sale",
    ends={
        Property(name="direct_sale0", type=direct_sale_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="seller1", type=seller__Actor, multiplicity=Multiplicity(0, 1))
    }
)
the_product_online_market: BinaryAssociation = BinaryAssociation(
    name="the_product_online_market",
    ends={
        Property(name="online_market28", type=online_market, multiplicity=Multiplicity(1, 1)),
        Property(name="the_product29", type=the_product, multiplicity=Multiplicity(0, 1))
    }
)
the_product_customer: BinaryAssociation = BinaryAssociation(
    name="the_product_customer",
    ends={
        Property(name="customer30", type=customer, multiplicity=Multiplicity(1, 1)),
        Property(name="the_product31", type=the_product, multiplicity=Multiplicity(0, 1))
    }
)
the_product_direct_sale: BinaryAssociation = BinaryAssociation(
    name="the_product_direct_sale",
    ends={
        Property(name="direct_sale32", type=direct_sale, multiplicity=Multiplicity(1, 1)),
        Property(name="the_product33", type=the_product, multiplicity=Multiplicity(0, 1))
    }
)
the_product_sale_by_instalment: BinaryAssociation = BinaryAssociation(
    name="the_product_sale_by_instalment",
    ends={
        Property(name="sale_by_instalment34", type=sale_by_instalment, multiplicity=Multiplicity(1, 1)),
        Property(name="the_product35", type=the_product, multiplicity=Multiplicity(0, 1))
    }
)
seller_section: BinaryAssociation = BinaryAssociation(
    name="seller_section",
    ends={
        Property(name="section36", type=section, multiplicity=Multiplicity(1, 1)),
        Property(name="seller37", type=seller, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_AB8kYInOEemopIBfncy06w",
    types={seller__Actor, direct_sale_UseCase, later_payment_sale__UseCase, Online_customer_request_UseCase, customer_name_UseCase, customer_address__UseCase, Card_id_registration_UseCase, cashier_Actor, Add_sold_products_UseCase, Calculating_the_check_UseCase, Make_comprehensive_reports_UseCase, Entering_prices_UseCase, manager_Actor, delete_customer__UseCase, update_section_UseCase, add_products_to_sections__UseCase, seller_registration_UseCase, delete_seller_UseCase, add_seller__UseCase, add_customer_UseCase, the_product, online_market, section, seller, direct_sale, sale_by_instalment, customer},
    associations={seller__later_payment_sale, seller__Online_customer_request, cashier_Add_sold_products, cashier_Calculating_the_check, cashier_Make_comprehensive_reports, cashier_UseCase, Actor_UseCase6, Actor_UseCase2, Actor_UseCase7, Actor_UseCase4, Actor_UseCase5, Actor_UseCase, Actor_UseCase3, seller__direct_sale, the_product_online_market, the_product_customer, the_product_direct_sale, the_product_sale_by_instalment, seller_section},
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