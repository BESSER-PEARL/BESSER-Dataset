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
bank_Party = Class(name="bank::Party", is_abstract=True)
bank_ContactMethod = Class(name="bank::ContactMethod", is_abstract=True)
bank_EMail = Class(name="bank::EMail")
ContactMethod = Class(name="ContactMethod")
bank_WebAddress = Class(name="bank::WebAddress")
bank_Bank = Class(name="bank::Bank")
Party = Class(name="Party")
bank_Merchant = Class(name="bank::Merchant")
bank_Product = Class(name="bank::Product")
bank_Account = Class(name="bank::Account", is_abstract=True)
bank_Customer = Class(name="bank::Customer")
bank_Banker = Class(name="bank::Banker")
bank_CustomerAccount = Class(name="bank::CustomerAccount")
bank_Phone = Class(name="bank::Phone")
bank_PostalAddress = Class(name="bank::PostalAddress")
bank_Transaction = Class(name="bank::Transaction", is_abstract=True)
bank_TransactionInitiator = Class(name="bank::TransactionInitiator", is_abstract=True)
bank_OnlineSession = Class(name="bank::OnlineSession")
bank_Statement = Class(name="bank::Statement")
bank_PointOfSale = Class(name="bank::PointOfSale")
bank_Device = Class(name="bank::Device", is_abstract=True)
TransactionInitiator = Class(name="TransactionInitiator")
bank_Token = Class(name="bank::Token")
bank_MobilePhone = Class(name="bank::MobilePhone")
Device = Class(name="Device")
bank_Card = Class(name="bank::Card")
bank_DeviceTransaction = Class(name="bank::DeviceTransaction")
Account = Class(name="Account")
bank_InternalAccount = Class(name="bank::InternalAccount")
bank_BankerTransaction = Class(name="bank::BankerTransaction")
bank_TokenTransaction = Class(name="bank::TokenTransaction")
bank_OnlineTransaction = Class(name="bank::OnlineTransaction")

# bank_Party class attributes and methods
bank_Party_name: Property = Property(name="name", type=StringType)
bank_Party.attributes={bank_Party_name}

# bank_ContactMethod class attributes and methods
bank_ContactMethod_name: Property = Property(name="name", type=StringType)
bank_ContactMethod_description: Property = Property(name="description", type=StringType)
bank_ContactMethod.attributes={bank_ContactMethod_name, bank_ContactMethod_description}

# bank_EMail class attributes and methods
bank_EMail_eMailAddress: Property = Property(name="eMailAddress", type=StringType)
bank_EMail.attributes={bank_EMail_eMailAddress}

# ContactMethod class attributes and methods

# bank_WebAddress class attributes and methods
bank_WebAddress_url: Property = Property(name="url", type=StringType)
bank_WebAddress.attributes={bank_WebAddress_url}

# bank_Bank class attributes and methods

# Party class attributes and methods

# bank_Merchant class attributes and methods

# bank_Product class attributes and methods
bank_Product_name: Property = Property(name="name", type=StringType)
bank_Product_description: Property = Property(name="description", type=StringType)
bank_Product.attributes={bank_Product_description, bank_Product_name}

# bank_Account class attributes and methods
bank_Account_number: Property = Property(name="number", type=StringType)
bank_Account_balance: Property = Property(name="balance", type=StringType)
bank_Account_description: Property = Property(name="description", type=StringType)
bank_Account_periodStart: Property = Property(name="periodStart", type=IntegerType)
bank_Account.attributes={bank_Account_periodStart, bank_Account_description, bank_Account_balance, bank_Account_number}

# bank_Customer class attributes and methods

# bank_Banker class attributes and methods

# bank_CustomerAccount class attributes and methods

# bank_Phone class attributes and methods
bank_Phone_countryCode: Property = Property(name="countryCode", type=IntegerType)
bank_Phone_areaCode: Property = Property(name="areaCode", type=IntegerType)
bank_Phone_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
bank_Phone_extension: Property = Property(name="extension", type=IntegerType)
bank_Phone.attributes={bank_Phone_countryCode, bank_Phone_areaCode, bank_Phone_extension, bank_Phone_phoneNumber}

# bank_PostalAddress class attributes and methods
bank_PostalAddress_country: Property = Property(name="country", type=StringType)
bank_PostalAddress_stateProvince: Property = Property(name="stateProvince", type=StringType)
bank_PostalAddress_city: Property = Property(name="city", type=StringType)
bank_PostalAddress_postalCode: Property = Property(name="postalCode", type=StringType)
bank_PostalAddress_line1: Property = Property(name="line1", type=StringType)
bank_PostalAddress_line2: Property = Property(name="line2", type=StringType)
bank_PostalAddress.attributes={bank_PostalAddress_postalCode, bank_PostalAddress_country, bank_PostalAddress_line2, bank_PostalAddress_stateProvince, bank_PostalAddress_city, bank_PostalAddress_line1}

# bank_Transaction class attributes and methods
bank_Transaction_amount: Property = Property(name="amount", type=StringType)
bank_Transaction_date: Property = Property(name="date", type=DateType)
bank_Transaction_comment: Property = Property(name="comment", type=StringType)
bank_Transaction_id: Property = Property(name="id", type=StringType)
bank_Transaction.attributes={bank_Transaction_comment, bank_Transaction_amount, bank_Transaction_date, bank_Transaction_id}

# bank_TransactionInitiator class attributes and methods

# bank_OnlineSession class attributes and methods
bank_OnlineSession_internetAddress: Property = Property(name="internetAddress", type=StringType)
bank_OnlineSession_start: Property = Property(name="start", type=DateType)
bank_OnlineSession_end: Property = Property(name="end", type=DateType)
bank_OnlineSession.attributes={bank_OnlineSession_start, bank_OnlineSession_internetAddress, bank_OnlineSession_end}

# bank_Statement class attributes and methods
bank_Statement_openingBalance: Property = Property(name="openingBalance", type=StringType)
bank_Statement_openingDate: Property = Property(name="openingDate", type=DateType)
bank_Statement_closingBalance: Property = Property(name="closingBalance", type=StringType)
bank_Statement_closingDate: Property = Property(name="closingDate", type=DateType)
bank_Statement.attributes={bank_Statement_closingBalance, bank_Statement_openingBalance, bank_Statement_openingDate, bank_Statement_closingDate}

# bank_PointOfSale class attributes and methods
bank_PointOfSale_id: Property = Property(name="id", type=StringType)
bank_PointOfSale.attributes={bank_PointOfSale_id}

# bank_Device class attributes and methods

# TransactionInitiator class attributes and methods

# bank_Token class attributes and methods
bank_Token_value: Property = Property(name="value", type=StringType)
bank_Token.attributes={bank_Token_value}

# bank_MobilePhone class attributes and methods
bank_MobilePhone_number: Property = Property(name="number", type=StringType)
bank_MobilePhone_key: Property = Property(name="key", type=StringType)
bank_MobilePhone.attributes={bank_MobilePhone_number, bank_MobilePhone_key}

# Device class attributes and methods

# bank_Card class attributes and methods
bank_Card_virtual: Property = Property(name="virtual", type=BooleanType)
bank_Card_id: Property = Property(name="id", type=StringType)
bank_Card_issued: Property = Property(name="issued", type=DateType)
bank_Card_activated: Property = Property(name="activated", type=DateType)
bank_Card_deactivated: Property = Property(name="deactivated", type=DateType)
bank_Card_expires: Property = Property(name="expires", type=DateType)
bank_Card.attributes={bank_Card_id, bank_Card_expires, bank_Card_activated, bank_Card_deactivated, bank_Card_virtual, bank_Card_issued}

# bank_DeviceTransaction class attributes and methods

# Account class attributes and methods

# bank_InternalAccount class attributes and methods

# bank_BankerTransaction class attributes and methods

# bank_TokenTransaction class attributes and methods

# bank_OnlineTransaction class attributes and methods

# Relationships
contactMethods0: BinaryAssociation = BinaryAssociation(
    name="contactMethods0",
    ends={
        Property(name="bank_ContactMethod", type=bank_Party, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Party", type=bank_ContactMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
merchants1: BinaryAssociation = BinaryAssociation(
    name="merchants1",
    ends={
        Property(name="bank_Merchant", type=bank_Bank, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Bank", type=bank_Merchant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products2: BinaryAssociation = BinaryAssociation(
    name="products2",
    ends={
        Property(name="bank_Product", type=bank_Bank, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Bank3", type=bank_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accounts4: BinaryAssociation = BinaryAssociation(
    name="accounts4",
    ends={
        Property(name="bank_Account", type=bank_Bank, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Bank5", type=bank_Account, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers6: BinaryAssociation = BinaryAssociation(
    name="customers6",
    ends={
        Property(name="bank_Customer", type=bank_Bank, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Bank7", type=bank_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bankers8: BinaryAssociation = BinaryAssociation(
    name="bankers8",
    ends={
        Property(name="bank_Banker", type=bank_Bank, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Bank9", type=bank_Banker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accounts10: BinaryAssociation = BinaryAssociation(
    name="accounts10",
    ends={
        Property(name="CustomerAccount", type=bank_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="owners", type=bank_CustomerAccount, multiplicity=Multiplicity(0, 9999))
    }
)
statements13: BinaryAssociation = BinaryAssociation(
    name="statements13",
    ends={
        Property(name="bank_Statement", type=bank_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Account14", type=bank_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
debit15: BinaryAssociation = BinaryAssociation(
    name="debit15",
    ends={
        Property(name="Statement", type=bank_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="debits", type=bank_Statement, multiplicity=Multiplicity(1, 1))
    }
)
credit16: BinaryAssociation = BinaryAssociation(
    name="credit16",
    ends={
        Property(name="Statement17", type=bank_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="credits", type=bank_Statement, multiplicity=Multiplicity(1, 1))
    }
)
initiator18: BinaryAssociation = BinaryAssociation(
    name="initiator18",
    ends={
        Property(name="bank_TransactionInitiator", type=bank_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Transaction", type=bank_TransactionInitiator, multiplicity=Multiplicity(0, 1))
    }
)
onlineSessions11: BinaryAssociation = BinaryAssociation(
    name="onlineSessions11",
    ends={
        Property(name="bank_OnlineSession", type=bank_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Customer12", type=bank_OnlineSession, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pointsOfSale19: BinaryAssociation = BinaryAssociation(
    name="pointsOfSale19",
    ends={
        Property(name="bank_PointOfSale", type=bank_Merchant, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Merchant20", type=bank_PointOfSale, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location21: BinaryAssociation = BinaryAssociation(
    name="location21",
    ends={
        Property(name="bank_PostalAddress", type=bank_PointOfSale, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_PointOfSale22", type=bank_PostalAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tokens23: BinaryAssociation = BinaryAssociation(
    name="tokens23",
    ends={
        Property(name="bank_Token", type=bank_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Device", type=bank_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pointOfSale29: BinaryAssociation = BinaryAssociation(
    name="pointOfSale29",
    ends={
        Property(name="bank_PointOfSale30", type=bank_DeviceTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_DeviceTransaction", type=bank_PointOfSale, multiplicity=Multiplicity(0, 1))
    }
)
devices31: BinaryAssociation = BinaryAssociation(
    name="devices31",
    ends={
        Property(name="bank_Device32", type=bank_CustomerAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_CustomerAccount", type=bank_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
product33: BinaryAssociation = BinaryAssociation(
    name="product33",
    ends={
        Property(name="bank_Product35", type=bank_CustomerAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_CustomerAccount34", type=bank_Product, multiplicity=Multiplicity(1, 1))
    }
)
owners36: BinaryAssociation = BinaryAssociation(
    name="owners36",
    ends={
        Property(name="Customer", type=bank_CustomerAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="accounts", type=bank_Customer, multiplicity=Multiplicity(0, 9999))
    }
)
merchant37: BinaryAssociation = BinaryAssociation(
    name="merchant37",
    ends={
        Property(name="bank_Merchant39", type=bank_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Token38", type=bank_Merchant, multiplicity=Multiplicity(1, 1))
    }
)
lockedTo24: BinaryAssociation = BinaryAssociation(
    name="lockedTo24",
    ends={
        Property(name="bank_Merchant25", type=bank_Card, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Card", type=bank_Merchant, multiplicity=Multiplicity(0, 1))
    }
)
replaces27: BinaryAssociation = BinaryAssociation(
    name="replaces27",
    ends={
        Property(name="bank_Card28", type=bank_Card, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Card26", type=bank_Card, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_bank_EMail_ContactMethod = Generalization(general=ContactMethod, specific=bank_EMail)
gen_bank_WebAddress_ContactMethod = Generalization(general=ContactMethod, specific=bank_WebAddress)
gen_bank_Bank_Party = Generalization(general=Party, specific=bank_Bank)
gen_bank_Customer_Party = Generalization(general=Party, specific=bank_Customer)
gen_bank_Phone_ContactMethod = Generalization(general=ContactMethod, specific=bank_Phone)
gen_bank_PostalAddress_ContactMethod = Generalization(general=ContactMethod, specific=bank_PostalAddress)
gen_bank_Merchant_Party = Generalization(general=Party, specific=bank_Merchant)
gen_bank_Device_TransactionInitiator = Generalization(general=TransactionInitiator, specific=bank_Device)
gen_bank_MobilePhone_Device = Generalization(general=Device, specific=bank_MobilePhone)
gen_bank_Card_Device = Generalization(general=Device, specific=bank_Card)
gen_bank_CustomerAccount_Account = Generalization(general=Account, specific=bank_CustomerAccount)
gen_bank_InternalAccount_Account = Generalization(general=Account, specific=bank_InternalAccount)
gen_bank_Banker_Party = Generalization(general=Party, specific=bank_Banker)
gen_bank_Banker_TransactionInitiator = Generalization(general=TransactionInitiator, specific=bank_Banker)
gen_bank_Token_TransactionInitiator = Generalization(general=TransactionInitiator, specific=bank_Token)
gen_bank_OnlineSession_TransactionInitiator = Generalization(general=TransactionInitiator, specific=bank_OnlineSession)

# Domain Model
domain_model = DomainModel(
    name="bank",
    types={bank_Party, bank_ContactMethod, bank_EMail, ContactMethod, bank_WebAddress, bank_Bank, Party, bank_Merchant, bank_Product, bank_Account, bank_Customer, bank_Banker, bank_CustomerAccount, bank_Phone, bank_PostalAddress, bank_Transaction, bank_TransactionInitiator, bank_OnlineSession, bank_Statement, bank_PointOfSale, bank_Device, TransactionInitiator, bank_Token, bank_MobilePhone, Device, bank_Card, bank_DeviceTransaction, Account, bank_InternalAccount, bank_BankerTransaction, bank_TokenTransaction, bank_OnlineTransaction},
    associations={contactMethods0, merchants1, products2, accounts4, customers6, bankers8, accounts10, statements13, debit15, credit16, initiator18, onlineSessions11, pointsOfSale19, location21, tokens23, pointOfSale29, devices31, product33, owners36, merchant37, lockedTo24, replaces27},
    generalizations={gen_bank_EMail_ContactMethod, gen_bank_WebAddress_ContactMethod, gen_bank_Bank_Party, gen_bank_Customer_Party, gen_bank_Phone_ContactMethod, gen_bank_PostalAddress_ContactMethod, gen_bank_Merchant_Party, gen_bank_Device_TransactionInitiator, gen_bank_MobilePhone_Device, gen_bank_Card_Device, gen_bank_CustomerAccount_Account, gen_bank_InternalAccount_Account, gen_bank_Banker_Party, gen_bank_Banker_TransactionInitiator, gen_bank_Token_TransactionInitiator, gen_bank_OnlineSession_TransactionInitiator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)