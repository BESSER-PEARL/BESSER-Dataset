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
PaymentType: Enumeration = Enumeration(
    name="PaymentType",
    literals={
            EnumerationLiteral(name="CASH"),
			EnumerationLiteral(name="CHEQUE"),
			EnumerationLiteral(name="ELECTRONIC")
    }
)

# Classes
shop_Shop = Class(name="shop::Shop")
shop_Customer = Class(name="shop::Customer")
shop_Sale = Class(name="shop::Sale")
shop_Employee = Class(name="shop::Employee")
shop_AccountBook = Class(name="shop::AccountBook")
Person = Class(name="Person")
Valuable = Class(name="Valuable")
shop_Payment = Class(name="shop::Payment", is_abstract=True)
shop_Person = Class(name="shop::Person", is_abstract=True)
shop_Valuable = Class(name="shop::Valuable", is_abstract=True)
shop_ChequePayment = Class(name="shop::ChequePayment")
Payment = Class(name="Payment")
shop_CashPayment = Class(name="shop::CashPayment")
shop_ElectronicPayment = Class(name="shop::ElectronicPayment")
shop_BankOperation = Class(name="shop::BankOperation")

# shop_Shop class attributes and methods

# shop_Customer class attributes and methods

# shop_Sale class attributes and methods
shop_Sale_description: Property = Property(name="description", type=StringType)
shop_Sale.attributes={shop_Sale_description}

# shop_Employee class attributes and methods

# shop_AccountBook class attributes and methods
shop_AccountBook_cashFlow: Property = Property(name="cashFlow", type=FloatType)
shop_AccountBook_m_depositCash: Method = Method(name="depositCash", parameters={Parameter(name='cashValue'), Parameter(name='date')})
shop_AccountBook_m_depositCheques: Method = Method(name="depositCheques", parameters={Parameter(name='date'), Parameter(name='cheques')})
shop_AccountBook.attributes={shop_AccountBook_cashFlow}
shop_AccountBook.methods={shop_AccountBook_m_depositCheques, shop_AccountBook_m_depositCash}

# Person class attributes and methods

# Valuable class attributes and methods

# shop_Payment class attributes and methods
shop_Payment_type: Property = Property(name="type", type=StringType)
shop_Payment.attributes={shop_Payment_type}

# shop_Person class attributes and methods
shop_Person_firstName: Property = Property(name="firstName", type=StringType)
shop_Person_lastName: Property = Property(name="lastName", type=StringType)
shop_Person_birthDate: Property = Property(name="birthDate", type=DateType)
shop_Person_emails: Property = Property(name="emails", type=StringType)
shop_Person_phoneNumbers: Property = Property(name="phoneNumbers", type=StringType)
shop_Person_address: Property = Property(name="address", type=StringType)
shop_Person_m_getDisplayName: Method = Method(name="getDisplayName", parameters={}, type=StringType)
shop_Person.attributes={shop_Person_emails, shop_Person_birthDate, shop_Person_firstName, shop_Person_address, shop_Person_lastName, shop_Person_phoneNumbers}
shop_Person.methods={shop_Person_m_getDisplayName}

# shop_Valuable class attributes and methods
shop_Valuable_date: Property = Property(name="date", type=DateType)
shop_Valuable_value: Property = Property(name="value", type=FloatType)
shop_Valuable.attributes={shop_Valuable_date, shop_Valuable_value}

# shop_ChequePayment class attributes and methods
shop_ChequePayment_deposited: Property = Property(name="deposited", type=BooleanType)
shop_ChequePayment_depositDate: Property = Property(name="depositDate", type=DateType)
shop_ChequePayment.attributes={shop_ChequePayment_depositDate, shop_ChequePayment_deposited}

# Payment class attributes and methods

# shop_CashPayment class attributes and methods

# shop_ElectronicPayment class attributes and methods

# shop_BankOperation class attributes and methods
shop_BankOperation_description: Property = Property(name="description", type=StringType)
shop_BankOperation.attributes={shop_BankOperation_description}

# Relationships
customers0: BinaryAssociation = BinaryAssociation(
    name="customers0",
    ends={
        Property(name="shop_Customer", type=shop_Shop, multiplicity=Multiplicity(1, 1)),
        Property(name="shop_Shop", type=shop_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sales1: BinaryAssociation = BinaryAssociation(
    name="sales1",
    ends={
        Property(name="shop_Sale", type=shop_Shop, multiplicity=Multiplicity(1, 1)),
        Property(name="shop_Shop2", type=shop_Sale, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees3: BinaryAssociation = BinaryAssociation(
    name="employees3",
    ends={
        Property(name="shop_Employee", type=shop_Shop, multiplicity=Multiplicity(1, 1)),
        Property(name="shop_Shop4", type=shop_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accountBook5: BinaryAssociation = BinaryAssociation(
    name="accountBook5",
    ends={
        Property(name="AccountBook", type=shop_Shop, multiplicity=Multiplicity(1, 1)),
        Property(name="shop", type=shop_AccountBook, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sales6: BinaryAssociation = BinaryAssociation(
    name="sales6",
    ends={
        Property(name="Sale", type=shop_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=shop_Sale, multiplicity=Multiplicity(0, 9999))
    }
)
employees8: BinaryAssociation = BinaryAssociation(
    name="employees8",
    ends={
        Property(name="Employee", type=shop_Sale, multiplicity=Multiplicity(1, 1)),
        Property(name="sales9", type=shop_Employee, multiplicity=Multiplicity(1, 9999))
    }
)
payments10: BinaryAssociation = BinaryAssociation(
    name="payments10",
    ends={
        Property(name="Payment", type=shop_Sale, multiplicity=Multiplicity(1, 1)),
        Property(name="sale", type=shop_Payment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sales11: BinaryAssociation = BinaryAssociation(
    name="sales11",
    ends={
        Property(name="Sale12", type=shop_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=shop_Sale, multiplicity=Multiplicity(0, 9999))
    }
)
customer7: BinaryAssociation = BinaryAssociation(
    name="customer7",
    ends={
        Property(name="Customer", type=shop_Sale, multiplicity=Multiplicity(1, 1)),
        Property(name="sales", type=shop_Customer, multiplicity=Multiplicity(1, 1))
    }
)
sale13: BinaryAssociation = BinaryAssociation(
    name="sale13",
    ends={
        Property(name="Sale14", type=shop_Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="payments", type=shop_Sale, multiplicity=Multiplicity(0, 1))
    }
)
bankOperations15: BinaryAssociation = BinaryAssociation(
    name="bankOperations15",
    ends={
        Property(name="shop_BankOperation", type=shop_AccountBook, multiplicity=Multiplicity(1, 1)),
        Property(name="shop_AccountBook", type=shop_BankOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shop16: BinaryAssociation = BinaryAssociation(
    name="shop16",
    ends={
        Property(name="Shop", type=shop_AccountBook, multiplicity=Multiplicity(1, 1)),
        Property(name="accountBook", type=shop_Shop, multiplicity=Multiplicity(1, 1))
    }
)
payments17: BinaryAssociation = BinaryAssociation(
    name="payments17",
    ends={
        Property(name="shop_Payment", type=shop_AccountBook, multiplicity=Multiplicity(1, 1)),
        Property(name="shop_AccountBook18", type=shop_Payment, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_shop_Customer_Person = Generalization(general=Person, specific=shop_Customer)
gen_shop_Sale_Valuable = Generalization(general=Valuable, specific=shop_Sale)
gen_shop_Employee_Person = Generalization(general=Person, specific=shop_Employee)
gen_shop_Payment_Valuable = Generalization(general=Valuable, specific=shop_Payment)
gen_shop_ChequePayment_Payment = Generalization(general=Payment, specific=shop_ChequePayment)
gen_shop_CashPayment_Payment = Generalization(general=Payment, specific=shop_CashPayment)
gen_shop_ElectronicPayment_Payment = Generalization(general=Payment, specific=shop_ElectronicPayment)
gen_shop_BankOperation_Valuable = Generalization(general=Valuable, specific=shop_BankOperation)

# Domain Model
domain_model = DomainModel(
    name="shop",
    types={shop_Shop, shop_Customer, shop_Sale, shop_Employee, shop_AccountBook, Person, Valuable, shop_Payment, shop_Person, shop_Valuable, shop_ChequePayment, Payment, shop_CashPayment, shop_ElectronicPayment, shop_BankOperation, PaymentType},
    associations={customers0, sales1, employees3, accountBook5, sales6, employees8, payments10, sales11, customer7, sale13, bankOperations15, shop16, payments17},
    generalizations={gen_shop_Customer_Person, gen_shop_Sale_Valuable, gen_shop_Employee_Person, gen_shop_Payment_Valuable, gen_shop_ChequePayment_Payment, gen_shop_CashPayment_Payment, gen_shop_ElectronicPayment_Payment, gen_shop_BankOperation_Valuable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)