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
RandL_ServiceLevel = Class(name="RandL::ServiceLevel")
RandL_LoyaltyProgram = Class(name="RandL::LoyaltyProgram")
RandL_Earning = Class(name="RandL::Earning")
Transaction = Class(name="Transaction")
RandL_ProgramPartner = Class(name="RandL::ProgramPartner")
RandL_Burning = Class(name="RandL::Burning")
RandL_Service = Class(name="RandL::Service")
RandL_Membership = Class(name="RandL::Membership")
RandL_Transaction = Class(name="RandL::Transaction", is_abstract=True)
RandL_Date = Class(name="RandL::Date")
RandL_LoyaltyAccount = Class(name="RandL::LoyaltyAccount")
RandL_CustomerCard = Class(name="RandL::CustomerCard")
RandL_Customer = Class(name="RandL::Customer")
RandL_TransactionReport = Class(name="RandL::TransactionReport")
RandL_TransactionReportLine = Class(name="RandL::TransactionReportLine")
RandL_Container_RandL = Class(name="RandL::Container::RandL")

# RandL_ServiceLevel class attributes and methods
RandL_ServiceLevel_name: Property = Property(name="name", type=StringType)
RandL_ServiceLevel.attributes={RandL_ServiceLevel_name}

# RandL_LoyaltyProgram class attributes and methods
RandL_LoyaltyProgram_name: Property = Property(name="name", type=StringType)
RandL_LoyaltyProgram_m_selectPopularPartners: Method = Method(name="selectPopularPartners", parameters={Parameter(name='d')}, type=StringType)
RandL_LoyaltyProgram_m_addService: Method = Method(name="addService", parameters={Parameter(name='s'), Parameter(name='l'), Parameter(name='p')})
RandL_LoyaltyProgram_m_getServices: Method = Method(name="getServices", parameters={Parameter(name='pp')}, type=StringType)
RandL_LoyaltyProgram_m_enrollAndCreateCustomer: Method = Method(name="enrollAndCreateCustomer", parameters={Parameter(name='n'), Parameter(name='d')}, type=StringType)
RandL_LoyaltyProgram_m_enroll: Method = Method(name="enroll", parameters={Parameter(name='c')})
RandL_LoyaltyProgram_m_addTransaction: Method = Method(name="addTransaction", parameters={Parameter(name='accNr'), Parameter(name='servId'), Parameter(name='amnt'), Parameter(name='pName'), Parameter(name='d')})
RandL_LoyaltyProgram_m_getServices: Method = Method(name="getServices", parameters={}, type=StringType)
RandL_LoyaltyProgram.attributes={RandL_LoyaltyProgram_name}
RandL_LoyaltyProgram.methods={RandL_LoyaltyProgram_m_selectPopularPartners, RandL_LoyaltyProgram_m_getServices, RandL_LoyaltyProgram_m_getServices, RandL_LoyaltyProgram_m_addTransaction, RandL_LoyaltyProgram_m_enroll, RandL_LoyaltyProgram_m_enrollAndCreateCustomer, RandL_LoyaltyProgram_m_addService}

# RandL_Earning class attributes and methods

# Transaction class attributes and methods

# RandL_ProgramPartner class attributes and methods
RandL_ProgramPartner_name: Property = Property(name="name", type=StringType)
RandL_ProgramPartner_numberOfCustomers: Property = Property(name="numberOfCustomers", type=StringType)
RandL_ProgramPartner.attributes={RandL_ProgramPartner_name, RandL_ProgramPartner_numberOfCustomers}

# RandL_Burning class attributes and methods

# RandL_Service class attributes and methods
RandL_Service_serviceNr: Property = Property(name="serviceNr", type=StringType)
RandL_Service_description: Property = Property(name="description", type=StringType)
RandL_Service_pointsEarned: Property = Property(name="pointsEarned", type=StringType)
RandL_Service_condition: Property = Property(name="condition", type=StringType)
RandL_Service_pointsBurned: Property = Property(name="pointsBurned", type=StringType)
RandL_Service_m_calcPoints: Method = Method(name="calcPoints", parameters={}, type=StringType)
RandL_Service_m_upgradePointsEarned: Method = Method(name="upgradePointsEarned", parameters={Parameter(name='amount')})
RandL_Service.attributes={RandL_Service_pointsEarned, RandL_Service_pointsBurned, RandL_Service_description, RandL_Service_condition, RandL_Service_serviceNr}
RandL_Service.methods={RandL_Service_m_upgradePointsEarned, RandL_Service_m_calcPoints}

# RandL_Membership class attributes and methods

# RandL_Transaction class attributes and methods
RandL_Transaction_amount: Property = Property(name="amount", type=StringType)
RandL_Transaction_points: Property = Property(name="points", type=StringType)
RandL_Transaction_m_program: Method = Method(name="program", parameters={}, type=StringType)
RandL_Transaction.attributes={RandL_Transaction_points, RandL_Transaction_amount}
RandL_Transaction.methods={RandL_Transaction_m_program}

# RandL_Date class attributes and methods
RandL_Date_year: Property = Property(name="year", type=StringType)
RandL_Date_month: Property = Property(name="month", type=StringType)
RandL_Date_day: Property = Property(name="day", type=StringType)
RandL_Date_m_isBefore: Method = Method(name="isBefore", parameters={Parameter(name='t')}, type=StringType)
RandL_Date_m_isEqual: Method = Method(name="isEqual", parameters={Parameter(name='t')}, type=StringType)
RandL_Date_m_fromYMD: Method = Method(name="fromYMD", parameters={Parameter(name='k'), Parameter(name='y'), Parameter(name='m')}, type=StringType)
RandL_Date_m_isAfter: Method = Method(name="isAfter", parameters={Parameter(name='t')}, type=StringType)
RandL_Date.attributes={RandL_Date_day, RandL_Date_year, RandL_Date_month}
RandL_Date.methods={RandL_Date_m_isEqual, RandL_Date_m_fromYMD, RandL_Date_m_isAfter, RandL_Date_m_isBefore}

# RandL_LoyaltyAccount class attributes and methods
RandL_LoyaltyAccount_points: Property = Property(name="points", type=StringType)
RandL_LoyaltyAccount_totalPointsEarned: Property = Property(name="totalPointsEarned", type=StringType)
RandL_LoyaltyAccount_number: Property = Property(name="number", type=StringType)
RandL_LoyaltyAccount_m_earn: Method = Method(name="earn", parameters={Parameter(name='i')})
RandL_LoyaltyAccount_m_burn: Method = Method(name="burn", parameters={Parameter(name='i')})
RandL_LoyaltyAccount_m_getCustomerName: Method = Method(name="getCustomerName", parameters={}, type=StringType)
RandL_LoyaltyAccount_m_isEmpty: Method = Method(name="isEmpty", parameters={}, type=StringType)
RandL_LoyaltyAccount.attributes={RandL_LoyaltyAccount_number, RandL_LoyaltyAccount_totalPointsEarned, RandL_LoyaltyAccount_points}
RandL_LoyaltyAccount.methods={RandL_LoyaltyAccount_m_getCustomerName, RandL_LoyaltyAccount_m_isEmpty, RandL_LoyaltyAccount_m_earn, RandL_LoyaltyAccount_m_burn}

# RandL_CustomerCard class attributes and methods
RandL_CustomerCard_valid: Property = Property(name="valid", type=StringType)
RandL_CustomerCard_color: Property = Property(name="color", type=StringType)
RandL_CustomerCard_printedName: Property = Property(name="printedName", type=StringType)
RandL_CustomerCard_m_getTransactions: Method = Method(name="getTransactions", parameters={Parameter(name='from'), Parameter(name='until')}, type=Transaction)
RandL_CustomerCard.attributes={RandL_CustomerCard_color, RandL_CustomerCard_valid, RandL_CustomerCard_printedName}
RandL_CustomerCard.methods={RandL_CustomerCard_m_getTransactions}

# RandL_Customer class attributes and methods
RandL_Customer_gender: Property = Property(name="gender", type=StringType)
RandL_Customer_isMale: Property = Property(name="isMale", type=StringType)
RandL_Customer_name: Property = Property(name="name", type=StringType)
RandL_Customer_title: Property = Property(name="title", type=StringType)
RandL_Customer_age: Property = Property(name="age", type=StringType)
RandL_Customer_m_birthdayHappens: Method = Method(name="birthdayHappens", parameters={})
RandL_Customer_m_age: Method = Method(name="age", parameters={}, type=StringType)
RandL_Customer.attributes={RandL_Customer_isMale, RandL_Customer_gender, RandL_Customer_age, RandL_Customer_title, RandL_Customer_name}
RandL_Customer.methods={RandL_Customer_m_birthdayHappens, RandL_Customer_m_age}

# RandL_TransactionReport class attributes and methods
RandL_TransactionReport_balance: Property = Property(name="balance", type=StringType)
RandL_TransactionReport_totalEarned: Property = Property(name="totalEarned", type=StringType)
RandL_TransactionReport_totalBurned: Property = Property(name="totalBurned", type=StringType)
RandL_TransactionReport_number: Property = Property(name="number", type=StringType)
RandL_TransactionReport_name: Property = Property(name="name", type=StringType)
RandL_TransactionReport.attributes={RandL_TransactionReport_number, RandL_TransactionReport_name, RandL_TransactionReport_totalBurned, RandL_TransactionReport_balance, RandL_TransactionReport_totalEarned}

# RandL_TransactionReportLine class attributes and methods
RandL_TransactionReportLine_partnerName: Property = Property(name="partnerName", type=StringType)
RandL_TransactionReportLine_serviceDesc: Property = Property(name="serviceDesc", type=StringType)
RandL_TransactionReportLine_points: Property = Property(name="points", type=StringType)
RandL_TransactionReportLine_amount: Property = Property(name="amount", type=StringType)
RandL_TransactionReportLine.attributes={RandL_TransactionReportLine_amount, RandL_TransactionReportLine_serviceDesc, RandL_TransactionReportLine_partnerName, RandL_TransactionReportLine_points}

# RandL_Container_RandL class attributes and methods

# Relationships
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="LoyaltyProgram", type=RandL_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="levels", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(0, 1))
    }
)
usedServices10: BinaryAssociation = BinaryAssociation(
    name="usedServices10",
    ends={
        Property(name="RandL_Service", type=RandL_LoyaltyAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_LoyaltyAccount", type=RandL_Service, multiplicity=Multiplicity(0, 9999))
    }
)
Membership11: BinaryAssociation = BinaryAssociation(
    name="Membership11",
    ends={
        Property(name="Membership12", type=RandL_LoyaltyAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="account", type=RandL_Membership, multiplicity=Multiplicity(0, 1))
    }
)
transactions13: BinaryAssociation = BinaryAssociation(
    name="transactions13",
    ends={
        Property(name="Transaction", type=RandL_LoyaltyAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="account14", type=RandL_Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
deliveredServices15: BinaryAssociation = BinaryAssociation(
    name="deliveredServices15",
    ends={
        Property(name="Service16", type=RandL_ProgramPartner, multiplicity=Multiplicity(1, 1)),
        Property(name="partner", type=RandL_Service, multiplicity=Multiplicity(0, 9999))
    }
)
programs17: BinaryAssociation = BinaryAssociation(
    name="programs17",
    ends={
        Property(name="LoyaltyProgram18", type=RandL_ProgramPartner, multiplicity=Multiplicity(1, 1)),
        Property(name="partners", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 9999))
    }
)
availableServices1: BinaryAssociation = BinaryAssociation(
    name="availableServices1",
    ends={
        Property(name="Service", type=RandL_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="level", type=RandL_Service, multiplicity=Multiplicity(0, 9999))
    }
)
Membership2: BinaryAssociation = BinaryAssociation(
    name="Membership2",
    ends={
        Property(name="Membership", type=RandL_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="currentLevel", type=RandL_Membership, multiplicity=Multiplicity(0, 9999))
    }
)
date3: BinaryAssociation = BinaryAssociation(
    name="date3",
    ends={
        Property(name="RandL_Date", type=RandL_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Transaction", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
account4: BinaryAssociation = BinaryAssociation(
    name="account4",
    ends={
        Property(name="LoyaltyAccount", type=RandL_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions", type=RandL_LoyaltyAccount, multiplicity=Multiplicity(0, 1))
    }
)
generatedBy5: BinaryAssociation = BinaryAssociation(
    name="generatedBy5",
    ends={
        Property(name="Service7", type=RandL_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions6", type=RandL_Service, multiplicity=Multiplicity(0, 1))
    }
)
card8: BinaryAssociation = BinaryAssociation(
    name="card8",
    ends={
        Property(name="CustomerCard", type=RandL_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions9", type=RandL_CustomerCard, multiplicity=Multiplicity(0, 1))
    }
)
goodThru27: BinaryAssociation = BinaryAssociation(
    name="goodThru27",
    ends={
        Property(name="RandL_Date29", type=RandL_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_CustomerCard28", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validFrom30: BinaryAssociation = BinaryAssociation(
    name="validFrom30",
    ends={
        Property(name="RandL_Date32", type=RandL_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_CustomerCard31", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
myLevel33: BinaryAssociation = BinaryAssociation(
    name="myLevel33",
    ends={
        Property(name="RandL_ServiceLevel", type=RandL_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_CustomerCard34", type=RandL_ServiceLevel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner35: BinaryAssociation = BinaryAssociation(
    name="owner35",
    ends={
        Property(name="Customer", type=RandL_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="cards", type=RandL_Customer, multiplicity=Multiplicity(0, 1))
    }
)
Membership36: BinaryAssociation = BinaryAssociation(
    name="Membership36",
    ends={
        Property(name="Membership37", type=RandL_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="card", type=RandL_Membership, multiplicity=Multiplicity(0, 1))
    }
)
transactions38: BinaryAssociation = BinaryAssociation(
    name="transactions38",
    ends={
        Property(name="Transaction40", type=RandL_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="card39", type=RandL_Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
until19: BinaryAssociation = BinaryAssociation(
    name="until19",
    ends={
        Property(name="RandL_Date20", type=RandL_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_TransactionReport", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from21: BinaryAssociation = BinaryAssociation(
    name="from21",
    ends={
        Property(name="RandL_Date23", type=RandL_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_TransactionReport22", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lines24: BinaryAssociation = BinaryAssociation(
    name="lines24",
    ends={
        Property(name="TransactionReportLine", type=RandL_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="report", type=RandL_TransactionReportLine, multiplicity=Multiplicity(0, 9999))
    }
)
card25: BinaryAssociation = BinaryAssociation(
    name="card25",
    ends={
        Property(name="RandL_CustomerCard", type=RandL_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_TransactionReport26", type=RandL_CustomerCard, multiplicity=Multiplicity(0, 1))
    }
)
ref_RandL_Date54: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Date54",
    ends={
        Property(name="RandL_Date56", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL55", type=RandL_Date, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_CustomerCard57: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_CustomerCard57",
    ends={
        Property(name="RandL_CustomerCard59", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL58", type=RandL_CustomerCard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Membership60: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Membership60",
    ends={
        Property(name="RandL_Membership62", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL61", type=RandL_Membership, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Service63: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Service63",
    ends={
        Property(name="RandL_Service65", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL64", type=RandL_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_LoyaltyProgram66: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_LoyaltyProgram66",
    ends={
        Property(name="RandL_LoyaltyProgram68", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL67", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Earning69: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Earning69",
    ends={
        Property(name="RandL_Earning", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL70", type=RandL_Earning, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_LoyaltyAccount71: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_LoyaltyAccount71",
    ends={
        Property(name="RandL_LoyaltyAccount73", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL72", type=RandL_LoyaltyAccount, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_ServiceLevel74: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_ServiceLevel74",
    ends={
        Property(name="RandL_ServiceLevel76", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL75", type=RandL_ServiceLevel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_TransactionReport77: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_TransactionReport77",
    ends={
        Property(name="RandL_TransactionReport79", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL78", type=RandL_TransactionReport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_ProgramPartner80: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_ProgramPartner80",
    ends={
        Property(name="RandL_ProgramPartner", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL81", type=RandL_ProgramPartner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Burning82: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Burning82",
    ends={
        Property(name="RandL_Burning", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL83", type=RandL_Burning, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_TransactionReportLine84: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_TransactionReportLine84",
    ends={
        Property(name="RandL_TransactionReportLine", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL85", type=RandL_TransactionReportLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentLevel41: BinaryAssociation = BinaryAssociation(
    name="currentLevel41",
    ends={
        Property(name="ServiceLevel", type=RandL_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="Membership42", type=RandL_ServiceLevel, multiplicity=Multiplicity(0, 1))
    }
)
card43: BinaryAssociation = BinaryAssociation(
    name="card43",
    ends={
        Property(name="CustomerCard45", type=RandL_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="Membership44", type=RandL_CustomerCard, multiplicity=Multiplicity(0, 1))
    }
)
account46: BinaryAssociation = BinaryAssociation(
    name="account46",
    ends={
        Property(name="LoyaltyAccount48", type=RandL_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="Membership47", type=RandL_LoyaltyAccount, multiplicity=Multiplicity(0, 1))
    }
)
programs49: BinaryAssociation = BinaryAssociation(
    name="programs49",
    ends={
        Property(name="RandL_LoyaltyProgram", type=RandL_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Membership", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 1))
    }
)
participants50: BinaryAssociation = BinaryAssociation(
    name="participants50",
    ends={
        Property(name="RandL_Customer", type=RandL_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Membership51", type=RandL_Customer, multiplicity=Multiplicity(1, 1))
    }
)
ref_RandL_Customer52: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Customer52",
    ends={
        Property(name="RandL_Customer53", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL", type=RandL_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dateOfBirth91: BinaryAssociation = BinaryAssociation(
    name="dateOfBirth91",
    ends={
        Property(name="RandL_Date93", type=RandL_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Customer92", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
programs94: BinaryAssociation = BinaryAssociation(
    name="programs94",
    ends={
        Property(name="LoyaltyProgram95", type=RandL_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="participants", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(0, 9999))
    }
)
cards96: BinaryAssociation = BinaryAssociation(
    name="cards96",
    ends={
        Property(name="CustomerCard97", type=RandL_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=RandL_CustomerCard, multiplicity=Multiplicity(0, 9999))
    }
)
memberships98: BinaryAssociation = BinaryAssociation(
    name="memberships98",
    ends={
        Property(name="RandL_Membership100", type=RandL_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Customer99", type=RandL_Membership, multiplicity=Multiplicity(0, 9999))
    }
)
date101: BinaryAssociation = BinaryAssociation(
    name="date101",
    ends={
        Property(name="RandL_Date103", type=RandL_TransactionReportLine, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_TransactionReportLine102", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transaction104: BinaryAssociation = BinaryAssociation(
    name="transaction104",
    ends={
        Property(name="RandL_Transaction106", type=RandL_TransactionReportLine, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_TransactionReportLine105", type=RandL_Transaction, multiplicity=Multiplicity(0, 1))
    }
)
report107: BinaryAssociation = BinaryAssociation(
    name="report107",
    ends={
        Property(name="TransactionReport", type=RandL_TransactionReportLine, multiplicity=Multiplicity(1, 1)),
        Property(name="lines", type=RandL_TransactionReport, multiplicity=Multiplicity(0, 1))
    }
)
partner86: BinaryAssociation = BinaryAssociation(
    name="partner86",
    ends={
        Property(name="ProgramPartner", type=RandL_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="deliveredServices", type=RandL_ProgramPartner, multiplicity=Multiplicity(0, 1))
    }
)
transactions87: BinaryAssociation = BinaryAssociation(
    name="transactions87",
    ends={
        Property(name="Transaction88", type=RandL_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedBy", type=RandL_Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
level89: BinaryAssociation = BinaryAssociation(
    name="level89",
    ends={
        Property(name="ServiceLevel90", type=RandL_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="availableServices", type=RandL_ServiceLevel, multiplicity=Multiplicity(0, 1))
    }
)
memberships115: BinaryAssociation = BinaryAssociation(
    name="memberships115",
    ends={
        Property(name="RandL_Membership117", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_LoyaltyProgram116", type=RandL_Membership, multiplicity=Multiplicity(0, 9999))
    }
)
partners108: BinaryAssociation = BinaryAssociation(
    name="partners108",
    ends={
        Property(name="ProgramPartner109", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="programs", type=RandL_ProgramPartner, multiplicity=Multiplicity(1, 9999))
    }
)
levels110: BinaryAssociation = BinaryAssociation(
    name="levels110",
    ends={
        Property(name="ServiceLevel111", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="program", type=RandL_ServiceLevel, multiplicity=Multiplicity(1, 9999))
    }
)
participants112: BinaryAssociation = BinaryAssociation(
    name="participants112",
    ends={
        Property(name="Customer114", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="programs113", type=RandL_Customer, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_RandL_Earning_Transaction = Generalization(general=Transaction, specific=RandL_Earning)
gen_RandL_Burning_Transaction = Generalization(general=Transaction, specific=RandL_Burning)

# Domain Model
domain_model = DomainModel(
    name="RandL",
    types={RandL_ServiceLevel, RandL_LoyaltyProgram, RandL_Earning, Transaction, RandL_ProgramPartner, RandL_Burning, RandL_Service, RandL_Membership, RandL_Transaction, RandL_Date, RandL_LoyaltyAccount, RandL_CustomerCard, RandL_Customer, RandL_TransactionReport, RandL_TransactionReportLine, RandL_Container_RandL, RandLColor, Gender},
    associations={program0, usedServices10, Membership11, transactions13, deliveredServices15, programs17, availableServices1, Membership2, date3, account4, generatedBy5, card8, goodThru27, validFrom30, myLevel33, owner35, Membership36, transactions38, until19, from21, lines24, card25, ref_RandL_Date54, ref_RandL_CustomerCard57, ref_RandL_Membership60, ref_RandL_Service63, ref_RandL_LoyaltyProgram66, ref_RandL_Earning69, ref_RandL_LoyaltyAccount71, ref_RandL_ServiceLevel74, ref_RandL_TransactionReport77, ref_RandL_ProgramPartner80, ref_RandL_Burning82, ref_RandL_TransactionReportLine84, currentLevel41, card43, account46, programs49, participants50, ref_RandL_Customer52, dateOfBirth91, programs94, cards96, memberships98, date101, transaction104, report107, partner86, transactions87, level89, memberships115, partners108, levels110, participants112},
    generalizations={gen_RandL_Earning_Transaction, gen_RandL_Burning_Transaction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)