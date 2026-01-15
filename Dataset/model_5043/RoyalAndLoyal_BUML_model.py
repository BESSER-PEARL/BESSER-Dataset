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
RandLColor: Enumeration = Enumeration(
    name="RandLColor",
    literals={
            EnumerationLiteral(name="silver"),
			EnumerationLiteral(name="gold")
    }
)

Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

# Classes
RoyalAndLoyal_ServiceLevel = Class(name="RoyalAndLoyal::ServiceLevel")
RoyalAndLoyal_Earning = Class(name="RoyalAndLoyal::Earning")
Transaction = Class(name="Transaction")
RoyalAndLoyal_ProgramPartner = Class(name="RoyalAndLoyal::ProgramPartner")
RoyalAndLoyal_LoyaltyProgram = Class(name="RoyalAndLoyal::LoyaltyProgram")
RoyalAndLoyal_Service = Class(name="RoyalAndLoyal::Service")
RoyalAndLoyal_Membership = Class(name="RoyalAndLoyal::Membership")
RoyalAndLoyal_Transaction = Class(name="RoyalAndLoyal::Transaction", is_abstract=True)
RoyalAndLoyal_Date = Class(name="RoyalAndLoyal::Date")
RoyalAndLoyal_LoyaltyAccount = Class(name="RoyalAndLoyal::LoyaltyAccount")
RoyalAndLoyal_CustomerCard = Class(name="RoyalAndLoyal::CustomerCard")
RoyalAndLoyal_Customer = Class(name="RoyalAndLoyal::Customer")
RoyalAndLoyal_Burning = Class(name="RoyalAndLoyal::Burning")
RoyalAndLoyal_TransactionReport = Class(name="RoyalAndLoyal::TransactionReport")
RoyalAndLoyal_TransactionReportLine = Class(name="RoyalAndLoyal::TransactionReportLine")
RoyalAndLoyal_Container_RandL = Class(name="RoyalAndLoyal::Container::RandL")

# RoyalAndLoyal_ServiceLevel class attributes and methods
RoyalAndLoyal_ServiceLevel_name: Property = Property(name="name", type=StringType)
RoyalAndLoyal_ServiceLevel.attributes={RoyalAndLoyal_ServiceLevel_name}

# RoyalAndLoyal_Earning class attributes and methods

# Transaction class attributes and methods

# RoyalAndLoyal_ProgramPartner class attributes and methods
RoyalAndLoyal_ProgramPartner_name: Property = Property(name="name", type=StringType)
RoyalAndLoyal_ProgramPartner_numberOfCustomers: Property = Property(name="numberOfCustomers", type=IntegerType)
RoyalAndLoyal_ProgramPartner.attributes={RoyalAndLoyal_ProgramPartner_numberOfCustomers, RoyalAndLoyal_ProgramPartner_name}

# RoyalAndLoyal_LoyaltyProgram class attributes and methods
RoyalAndLoyal_LoyaltyProgram_name: Property = Property(name="name", type=StringType)
RoyalAndLoyal_LoyaltyProgram_m_enroll: Method = Method(name="enroll", parameters={Parameter(name='c')})
RoyalAndLoyal_LoyaltyProgram_m_addTransaction: Method = Method(name="addTransaction", parameters={Parameter(name='amnt'), Parameter(name='accNr'), Parameter(name='servId'), Parameter(name='pName'), Parameter(name='d')})
RoyalAndLoyal_LoyaltyProgram_m_selectPopularPartners: Method = Method(name="selectPopularPartners", parameters={Parameter(name='d')}, type=StringType)
RoyalAndLoyal_LoyaltyProgram_m_addService: Method = Method(name="addService", parameters={Parameter(name='s'), Parameter(name='l'), Parameter(name='p')})
RoyalAndLoyal_LoyaltyProgram_m_getServices: Method = Method(name="getServices", parameters={Parameter(name='pp')}, type=StringType)
RoyalAndLoyal_LoyaltyProgram_m_enrollAndCreateCustomer: Method = Method(name="enrollAndCreateCustomer", parameters={Parameter(name='n'), Parameter(name='d')}, type=StringType)
RoyalAndLoyal_LoyaltyProgram.attributes={RoyalAndLoyal_LoyaltyProgram_name}
RoyalAndLoyal_LoyaltyProgram.methods={RoyalAndLoyal_LoyaltyProgram_m_enrollAndCreateCustomer, RoyalAndLoyal_LoyaltyProgram_m_enroll, RoyalAndLoyal_LoyaltyProgram_m_addService, RoyalAndLoyal_LoyaltyProgram_m_selectPopularPartners, RoyalAndLoyal_LoyaltyProgram_m_addTransaction, RoyalAndLoyal_LoyaltyProgram_m_getServices}

# RoyalAndLoyal_Service class attributes and methods
RoyalAndLoyal_Service_serviceNr: Property = Property(name="serviceNr", type=IntegerType)
RoyalAndLoyal_Service_description: Property = Property(name="description", type=StringType)
RoyalAndLoyal_Service_pointsEarned: Property = Property(name="pointsEarned", type=IntegerType)
RoyalAndLoyal_Service_condition: Property = Property(name="condition", type=BooleanType)
RoyalAndLoyal_Service_pointsBurned: Property = Property(name="pointsBurned", type=IntegerType)
RoyalAndLoyal_Service_m_calcPoints: Method = Method(name="calcPoints", parameters={}, type=IntegerType)
RoyalAndLoyal_Service_m_upgradePointsEarned: Method = Method(name="upgradePointsEarned", parameters={Parameter(name='amount')})
RoyalAndLoyal_Service.attributes={RoyalAndLoyal_Service_description, RoyalAndLoyal_Service_pointsBurned, RoyalAndLoyal_Service_serviceNr, RoyalAndLoyal_Service_pointsEarned, RoyalAndLoyal_Service_condition}
RoyalAndLoyal_Service.methods={RoyalAndLoyal_Service_m_upgradePointsEarned, RoyalAndLoyal_Service_m_calcPoints}

# RoyalAndLoyal_Membership class attributes and methods

# RoyalAndLoyal_Transaction class attributes and methods
RoyalAndLoyal_Transaction_amount: Property = Property(name="amount", type=FloatType)
RoyalAndLoyal_Transaction_points: Property = Property(name="points", type=IntegerType)
RoyalAndLoyal_Transaction_m_program: Method = Method(name="program", parameters={}, type=StringType)
RoyalAndLoyal_Transaction.attributes={RoyalAndLoyal_Transaction_amount, RoyalAndLoyal_Transaction_points}
RoyalAndLoyal_Transaction.methods={RoyalAndLoyal_Transaction_m_program}

# RoyalAndLoyal_Date class attributes and methods
RoyalAndLoyal_Date_year: Property = Property(name="year", type=IntegerType)
RoyalAndLoyal_Date_month: Property = Property(name="month", type=IntegerType)
RoyalAndLoyal_Date_day: Property = Property(name="day", type=IntegerType)
RoyalAndLoyal_Date_m_isBefore: Method = Method(name="isBefore", parameters={Parameter(name='t')}, type=BooleanType)
RoyalAndLoyal_Date_m_isEqual: Method = Method(name="isEqual", parameters={Parameter(name='t')}, type=BooleanType)
RoyalAndLoyal_Date_m_fromYMD: Method = Method(name="fromYMD", parameters={Parameter(name='y'), Parameter(name='m'), Parameter(name='k')}, type=StringType)
RoyalAndLoyal_Date_m_isAfter: Method = Method(name="isAfter", parameters={Parameter(name='t')}, type=BooleanType)
RoyalAndLoyal_Date.attributes={RoyalAndLoyal_Date_year, RoyalAndLoyal_Date_day, RoyalAndLoyal_Date_month}
RoyalAndLoyal_Date.methods={RoyalAndLoyal_Date_m_fromYMD, RoyalAndLoyal_Date_m_isEqual, RoyalAndLoyal_Date_m_isBefore, RoyalAndLoyal_Date_m_isAfter}

# RoyalAndLoyal_LoyaltyAccount class attributes and methods
RoyalAndLoyal_LoyaltyAccount_points: Property = Property(name="points", type=IntegerType)
RoyalAndLoyal_LoyaltyAccount_totalPointsEarned: Property = Property(name="totalPointsEarned", type=IntegerType)
RoyalAndLoyal_LoyaltyAccount_number: Property = Property(name="number", type=IntegerType)
RoyalAndLoyal_LoyaltyAccount_m_burn: Method = Method(name="burn", parameters={Parameter(name='i')})
RoyalAndLoyal_LoyaltyAccount_m_getCustomerName: Method = Method(name="getCustomerName", parameters={}, type=StringType)
RoyalAndLoyal_LoyaltyAccount_m_isEmpty: Method = Method(name="isEmpty", parameters={}, type=BooleanType)
RoyalAndLoyal_LoyaltyAccount_m_earn: Method = Method(name="earn", parameters={Parameter(name='i')})
RoyalAndLoyal_LoyaltyAccount.attributes={RoyalAndLoyal_LoyaltyAccount_number, RoyalAndLoyal_LoyaltyAccount_totalPointsEarned, RoyalAndLoyal_LoyaltyAccount_points}
RoyalAndLoyal_LoyaltyAccount.methods={RoyalAndLoyal_LoyaltyAccount_m_earn, RoyalAndLoyal_LoyaltyAccount_m_getCustomerName, RoyalAndLoyal_LoyaltyAccount_m_burn, RoyalAndLoyal_LoyaltyAccount_m_isEmpty}

# RoyalAndLoyal_CustomerCard class attributes and methods
RoyalAndLoyal_CustomerCard_valid: Property = Property(name="valid", type=BooleanType)
RoyalAndLoyal_CustomerCard_color: Property = Property(name="color", type=StringType)
RoyalAndLoyal_CustomerCard_printedName: Property = Property(name="printedName", type=StringType)
RoyalAndLoyal_CustomerCard_m_getTransactions: Method = Method(name="getTransactions", parameters={Parameter(name='until'), Parameter(name='from')}, type=Transaction)
RoyalAndLoyal_CustomerCard.attributes={RoyalAndLoyal_CustomerCard_color, RoyalAndLoyal_CustomerCard_valid, RoyalAndLoyal_CustomerCard_printedName}
RoyalAndLoyal_CustomerCard.methods={RoyalAndLoyal_CustomerCard_m_getTransactions}

# RoyalAndLoyal_Customer class attributes and methods
RoyalAndLoyal_Customer_gender: Property = Property(name="gender", type=StringType)
RoyalAndLoyal_Customer_isMale: Property = Property(name="isMale", type=BooleanType)
RoyalAndLoyal_Customer_name: Property = Property(name="name", type=StringType)
RoyalAndLoyal_Customer_title: Property = Property(name="title", type=StringType)
RoyalAndLoyal_Customer_age: Property = Property(name="age", type=IntegerType)
RoyalAndLoyal_Customer_m_birthdayHappens: Method = Method(name="birthdayHappens", parameters={})
RoyalAndLoyal_Customer_m_age: Method = Method(name="age", parameters={}, type=IntegerType)
RoyalAndLoyal_Customer_m_updateName: Method = Method(name="updateName", parameters={Parameter(name='name')})
RoyalAndLoyal_Customer.attributes={RoyalAndLoyal_Customer_gender, RoyalAndLoyal_Customer_isMale, RoyalAndLoyal_Customer_age, RoyalAndLoyal_Customer_name, RoyalAndLoyal_Customer_title}
RoyalAndLoyal_Customer.methods={RoyalAndLoyal_Customer_m_age, RoyalAndLoyal_Customer_m_birthdayHappens, RoyalAndLoyal_Customer_m_updateName}

# RoyalAndLoyal_Burning class attributes and methods

# RoyalAndLoyal_TransactionReport class attributes and methods
RoyalAndLoyal_TransactionReport_balance: Property = Property(name="balance", type=IntegerType)
RoyalAndLoyal_TransactionReport_totalEarned: Property = Property(name="totalEarned", type=IntegerType)
RoyalAndLoyal_TransactionReport_totalBurned: Property = Property(name="totalBurned", type=IntegerType)
RoyalAndLoyal_TransactionReport_number: Property = Property(name="number", type=IntegerType)
RoyalAndLoyal_TransactionReport_name: Property = Property(name="name", type=StringType)
RoyalAndLoyal_TransactionReport.attributes={RoyalAndLoyal_TransactionReport_totalEarned, RoyalAndLoyal_TransactionReport_balance, RoyalAndLoyal_TransactionReport_name, RoyalAndLoyal_TransactionReport_totalBurned, RoyalAndLoyal_TransactionReport_number}

# RoyalAndLoyal_TransactionReportLine class attributes and methods
RoyalAndLoyal_TransactionReportLine_partnerName: Property = Property(name="partnerName", type=StringType)
RoyalAndLoyal_TransactionReportLine_serviceDesc: Property = Property(name="serviceDesc", type=StringType)
RoyalAndLoyal_TransactionReportLine_points: Property = Property(name="points", type=IntegerType)
RoyalAndLoyal_TransactionReportLine_amount: Property = Property(name="amount", type=FloatType)
RoyalAndLoyal_TransactionReportLine.attributes={RoyalAndLoyal_TransactionReportLine_amount, RoyalAndLoyal_TransactionReportLine_partnerName, RoyalAndLoyal_TransactionReportLine_serviceDesc, RoyalAndLoyal_TransactionReportLine_points}

# RoyalAndLoyal_Container_RandL class attributes and methods

# Relationships
usedServices10: BinaryAssociation = BinaryAssociation(
    name="usedServices10",
    ends={
        Property(name="RoyalAndLoyal_Service", type=RoyalAndLoyal_LoyaltyAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_LoyaltyAccount", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(0, 9999))
    }
)
Membership11: BinaryAssociation = BinaryAssociation(
    name="Membership11",
    ends={
        Property(name="Membership12", type=RoyalAndLoyal_LoyaltyAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="account", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(0, 1))
    }
)
transactions13: BinaryAssociation = BinaryAssociation(
    name="transactions13",
    ends={
        Property(name="Transaction", type=RoyalAndLoyal_LoyaltyAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="account14", type=RoyalAndLoyal_Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="LoyaltyProgram", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="levels", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(0, 1))
    }
)
availableServices1: BinaryAssociation = BinaryAssociation(
    name="availableServices1",
    ends={
        Property(name="Service", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="level", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(0, 9999))
    }
)
Membership2: BinaryAssociation = BinaryAssociation(
    name="Membership2",
    ends={
        Property(name="Membership", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="currentLevel", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(0, 9999))
    }
)
tDate3: BinaryAssociation = BinaryAssociation(
    name="tDate3",
    ends={
        Property(name="RoyalAndLoyal_Date", type=RoyalAndLoyal_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Transaction", type=RoyalAndLoyal_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
account4: BinaryAssociation = BinaryAssociation(
    name="account4",
    ends={
        Property(name="LoyaltyAccount", type=RoyalAndLoyal_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions", type=RoyalAndLoyal_LoyaltyAccount, multiplicity=Multiplicity(0, 1))
    }
)
generatedBy5: BinaryAssociation = BinaryAssociation(
    name="generatedBy5",
    ends={
        Property(name="Service7", type=RoyalAndLoyal_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions6", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(0, 1))
    }
)
card8: BinaryAssociation = BinaryAssociation(
    name="card8",
    ends={
        Property(name="CustomerCard", type=RoyalAndLoyal_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions9", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(0, 1))
    }
)
goodThru27: BinaryAssociation = BinaryAssociation(
    name="goodThru27",
    ends={
        Property(name="RoyalAndLoyal_Date29", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_CustomerCard28", type=RoyalAndLoyal_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validFrom30: BinaryAssociation = BinaryAssociation(
    name="validFrom30",
    ends={
        Property(name="RoyalAndLoyal_Date32", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_CustomerCard31", type=RoyalAndLoyal_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
myLevel33: BinaryAssociation = BinaryAssociation(
    name="myLevel33",
    ends={
        Property(name="RoyalAndLoyal_ServiceLevel", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_CustomerCard34", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner35: BinaryAssociation = BinaryAssociation(
    name="owner35",
    ends={
        Property(name="Customer", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="cards", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(0, 1))
    }
)
deliveredServices15: BinaryAssociation = BinaryAssociation(
    name="deliveredServices15",
    ends={
        Property(name="Service16", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(1, 1)),
        Property(name="partner", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(0, 9999))
    }
)
programs17: BinaryAssociation = BinaryAssociation(
    name="programs17",
    ends={
        Property(name="LoyaltyProgram18", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(1, 1)),
        Property(name="partners", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 9999))
    }
)
until19: BinaryAssociation = BinaryAssociation(
    name="until19",
    ends={
        Property(name="RoyalAndLoyal_Date20", type=RoyalAndLoyal_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_TransactionReport", type=RoyalAndLoyal_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from21: BinaryAssociation = BinaryAssociation(
    name="from21",
    ends={
        Property(name="RoyalAndLoyal_Date23", type=RoyalAndLoyal_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_TransactionReport22", type=RoyalAndLoyal_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lines24: BinaryAssociation = BinaryAssociation(
    name="lines24",
    ends={
        Property(name="TransactionReportLine", type=RoyalAndLoyal_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="report", type=RoyalAndLoyal_TransactionReportLine, multiplicity=Multiplicity(0, 9999))
    }
)
card25: BinaryAssociation = BinaryAssociation(
    name="card25",
    ends={
        Property(name="RoyalAndLoyal_CustomerCard", type=RoyalAndLoyal_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_TransactionReport26", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(0, 1))
    }
)
ref_RandL_Customer52: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Customer52",
    ends={
        Property(name="RoyalAndLoyal_Customer53", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Date54: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Date54",
    ends={
        Property(name="RoyalAndLoyal_Date56", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL55", type=RoyalAndLoyal_Date, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_CustomerCard57: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_CustomerCard57",
    ends={
        Property(name="RoyalAndLoyal_CustomerCard59", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL58", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Membership60: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Membership60",
    ends={
        Property(name="RoyalAndLoyal_Membership62", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL61", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Service63: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Service63",
    ends={
        Property(name="RoyalAndLoyal_Service65", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL64", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_LoyaltyProgram66: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_LoyaltyProgram66",
    ends={
        Property(name="RoyalAndLoyal_LoyaltyProgram68", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL67", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Earning69: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Earning69",
    ends={
        Property(name="RoyalAndLoyal_Earning", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL70", type=RoyalAndLoyal_Earning, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Membership36: BinaryAssociation = BinaryAssociation(
    name="Membership36",
    ends={
        Property(name="Membership37", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="card", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(0, 1))
    }
)
transactions38: BinaryAssociation = BinaryAssociation(
    name="transactions38",
    ends={
        Property(name="Transaction40", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="card39", type=RoyalAndLoyal_Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
currentLevel41: BinaryAssociation = BinaryAssociation(
    name="currentLevel41",
    ends={
        Property(name="ServiceLevel", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="Membership42", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(0, 1))
    }
)
card43: BinaryAssociation = BinaryAssociation(
    name="card43",
    ends={
        Property(name="CustomerCard45", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="Membership44", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(0, 1))
    }
)
account46: BinaryAssociation = BinaryAssociation(
    name="account46",
    ends={
        Property(name="LoyaltyAccount48", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="Membership47", type=RoyalAndLoyal_LoyaltyAccount, multiplicity=Multiplicity(0, 1))
    }
)
programs49: BinaryAssociation = BinaryAssociation(
    name="programs49",
    ends={
        Property(name="RoyalAndLoyal_LoyaltyProgram", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Membership", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 1))
    }
)
participants50: BinaryAssociation = BinaryAssociation(
    name="participants50",
    ends={
        Property(name="RoyalAndLoyal_Customer", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Membership51", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(1, 1))
    }
)
level89: BinaryAssociation = BinaryAssociation(
    name="level89",
    ends={
        Property(name="ServiceLevel90", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="availableServices", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(0, 1))
    }
)
dateOfBirth91: BinaryAssociation = BinaryAssociation(
    name="dateOfBirth91",
    ends={
        Property(name="RoyalAndLoyal_Date93", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Customer92", type=RoyalAndLoyal_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
programs94: BinaryAssociation = BinaryAssociation(
    name="programs94",
    ends={
        Property(name="LoyaltyProgram95", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="participants", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(0, 9999))
    }
)
cards96: BinaryAssociation = BinaryAssociation(
    name="cards96",
    ends={
        Property(name="CustomerCard97", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(0, 9999))
    }
)
ref_RandL_LoyaltyAccount71: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_LoyaltyAccount71",
    ends={
        Property(name="RoyalAndLoyal_LoyaltyAccount73", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL72", type=RoyalAndLoyal_LoyaltyAccount, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_ServiceLevel74: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_ServiceLevel74",
    ends={
        Property(name="RoyalAndLoyal_ServiceLevel76", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL75", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_TransactionReport77: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_TransactionReport77",
    ends={
        Property(name="RoyalAndLoyal_TransactionReport79", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL78", type=RoyalAndLoyal_TransactionReport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_ProgramPartner80: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_ProgramPartner80",
    ends={
        Property(name="RoyalAndLoyal_ProgramPartner", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL81", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Burning82: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Burning82",
    ends={
        Property(name="RoyalAndLoyal_Burning", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL83", type=RoyalAndLoyal_Burning, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_TransactionReportLine84: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_TransactionReportLine84",
    ends={
        Property(name="RoyalAndLoyal_TransactionReportLine", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL85", type=RoyalAndLoyal_TransactionReportLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partner86: BinaryAssociation = BinaryAssociation(
    name="partner86",
    ends={
        Property(name="ProgramPartner", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="deliveredServices", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(0, 1))
    }
)
transactions87: BinaryAssociation = BinaryAssociation(
    name="transactions87",
    ends={
        Property(name="Transaction88", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedBy", type=RoyalAndLoyal_Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
partners108: BinaryAssociation = BinaryAssociation(
    name="partners108",
    ends={
        Property(name="ProgramPartner109", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="programs", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(1, 9999))
    }
)
levels110: BinaryAssociation = BinaryAssociation(
    name="levels110",
    ends={
        Property(name="ServiceLevel111", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="program", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(1, 9999))
    }
)
participants112: BinaryAssociation = BinaryAssociation(
    name="participants112",
    ends={
        Property(name="Customer114", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="programs113", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(0, 9999))
    }
)
loymemberships115: BinaryAssociation = BinaryAssociation(
    name="loymemberships115",
    ends={
        Property(name="RoyalAndLoyal_Membership117", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_LoyaltyProgram116", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(0, 9999))
    }
)
custmemberships98: BinaryAssociation = BinaryAssociation(
    name="custmemberships98",
    ends={
        Property(name="RoyalAndLoyal_Membership100", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Customer99", type=RoyalAndLoyal_Membership, multiplicity=Multiplicity(0, 9999))
    }
)
trlDate101: BinaryAssociation = BinaryAssociation(
    name="trlDate101",
    ends={
        Property(name="RoyalAndLoyal_Date103", type=RoyalAndLoyal_TransactionReportLine, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_TransactionReportLine102", type=RoyalAndLoyal_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transaction104: BinaryAssociation = BinaryAssociation(
    name="transaction104",
    ends={
        Property(name="RoyalAndLoyal_Transaction106", type=RoyalAndLoyal_TransactionReportLine, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_TransactionReportLine105", type=RoyalAndLoyal_Transaction, multiplicity=Multiplicity(0, 1))
    }
)
report107: BinaryAssociation = BinaryAssociation(
    name="report107",
    ends={
        Property(name="TransactionReport", type=RoyalAndLoyal_TransactionReportLine, multiplicity=Multiplicity(1, 1)),
        Property(name="lines", type=RoyalAndLoyal_TransactionReport, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_RoyalAndLoyal_Earning_Transaction = Generalization(general=Transaction, specific=RoyalAndLoyal_Earning)
gen_RoyalAndLoyal_Burning_Transaction = Generalization(general=Transaction, specific=RoyalAndLoyal_Burning)

# Domain Model
domain_model = DomainModel(
    name="RoyalAndLoyal",
    types={RoyalAndLoyal_ServiceLevel, RoyalAndLoyal_Earning, Transaction, RoyalAndLoyal_ProgramPartner, RoyalAndLoyal_LoyaltyProgram, RoyalAndLoyal_Service, RoyalAndLoyal_Membership, RoyalAndLoyal_Transaction, RoyalAndLoyal_Date, RoyalAndLoyal_LoyaltyAccount, RoyalAndLoyal_CustomerCard, RoyalAndLoyal_Customer, RoyalAndLoyal_Burning, RoyalAndLoyal_TransactionReport, RoyalAndLoyal_TransactionReportLine, RoyalAndLoyal_Container_RandL, RandLColor, Gender},
    associations={usedServices10, Membership11, transactions13, program0, availableServices1, Membership2, tDate3, account4, generatedBy5, card8, goodThru27, validFrom30, myLevel33, owner35, deliveredServices15, programs17, until19, from21, lines24, card25, ref_RandL_Customer52, ref_RandL_Date54, ref_RandL_CustomerCard57, ref_RandL_Membership60, ref_RandL_Service63, ref_RandL_LoyaltyProgram66, ref_RandL_Earning69, Membership36, transactions38, currentLevel41, card43, account46, programs49, participants50, level89, dateOfBirth91, programs94, cards96, ref_RandL_LoyaltyAccount71, ref_RandL_ServiceLevel74, ref_RandL_TransactionReport77, ref_RandL_ProgramPartner80, ref_RandL_Burning82, ref_RandL_TransactionReportLine84, partner86, transactions87, partners108, levels110, participants112, loymemberships115, custmemberships98, trlDate101, transaction104, report107},
    generalizations={gen_RoyalAndLoyal_Earning_Transaction, gen_RoyalAndLoyal_Burning_Transaction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)