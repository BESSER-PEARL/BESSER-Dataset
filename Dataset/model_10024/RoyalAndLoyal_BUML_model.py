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
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

RandLColor: Enumeration = Enumeration(
    name="RandLColor",
    literals={
            EnumerationLiteral(name="silver"),
			EnumerationLiteral(name="gold")
    }
)

# Classes
RandL_Transaction = Class(name="RandL_Transaction", is_abstract=True)
RandL_Date = Class(name="RandL_Date")
RandL_LoyaltyAccount = Class(name="RandL_LoyaltyAccount")
RandL_ServiceLevel = Class(name="RandL_ServiceLevel")
RandL_LoyaltyProgram = Class(name="RandL_LoyaltyProgram")
RandL_Service = Class(name="RandL_Service")
RandL_Membership = Class(name="RandL_Membership")
RandL_CustomerCard = Class(name="RandL_CustomerCard")
RandL_Earning = Class(name="RandL_Earning")
Transaction = Class(name="Transaction")
RandL_ProgramPartner = Class(name="RandL_ProgramPartner")
RandL_TransactionReportLine = Class(name="RandL_TransactionReportLine")
RandL_Burning = Class(name="RandL_Burning")
RandL_TransactionReport = Class(name="RandL_TransactionReport")
RandL_Customer = Class(name="RandL_Customer")
RandL_Container_RandL = Class(name="RandL_Container_RandL")

# RandL_Transaction class attributes and methods
RandL_Transaction_amount: Property = Property(name="amount", type=StringType)
RandL_Transaction_points: Property = Property(name="points", type=StringType)
RandL_Transaction_m_program: Method = Method(name="program", parameters={}, type=StringType)
RandL_Transaction.attributes={RandL_Transaction_amount, RandL_Transaction_points}
RandL_Transaction.methods={RandL_Transaction_m_program}

# RandL_Date class attributes and methods
RandL_Date_year: Property = Property(name="year", type=StringType)
RandL_Date_month: Property = Property(name="month", type=StringType)
RandL_Date_day: Property = Property(name="day", type=StringType)
RandL_Date_m_isBefore: Method = Method(name="isBefore", parameters={Parameter(name='RandL_t', type=StringType)}, type=StringType)
RandL_Date_m_isEqual: Method = Method(name="isEqual", parameters={Parameter(name='RandL_t', type=StringType)}, type=StringType)
RandL_Date_m_isAfter: Method = Method(name="isAfter", parameters={Parameter(name='RandL_t', type=StringType)}, type=StringType)
RandL_Date_m_fromYMD: Method = Method(name="fromYMD", parameters={Parameter(name='RandL_m', type=StringType), Parameter(name='RandL_y', type=StringType), Parameter(name='RandL_k', type=StringType)}, type=StringType)
RandL_Date.attributes={RandL_Date_year, RandL_Date_month, RandL_Date_day}
RandL_Date.methods={RandL_Date_m_isAfter, RandL_Date_m_fromYMD, RandL_Date_m_isBefore, RandL_Date_m_isEqual}

# RandL_LoyaltyAccount class attributes and methods
RandL_LoyaltyAccount_points: Property = Property(name="points", type=StringType)
RandL_LoyaltyAccount_totalPointsEarned: Property = Property(name="totalPointsEarned", type=StringType)
RandL_LoyaltyAccount_number: Property = Property(name="number", type=StringType)
RandL_LoyaltyAccount_m_isEmpty: Method = Method(name="isEmpty", parameters={}, type=StringType)
RandL_LoyaltyAccount_m_earn: Method = Method(name="earn", parameters={Parameter(name='RandL_i', type=StringType)})
RandL_LoyaltyAccount_m_burn: Method = Method(name="burn", parameters={Parameter(name='RandL_i', type=StringType)})
RandL_LoyaltyAccount_m_getCustomerName: Method = Method(name="getCustomerName", parameters={}, type=StringType)
RandL_LoyaltyAccount.attributes={RandL_LoyaltyAccount_number, RandL_LoyaltyAccount_totalPointsEarned, RandL_LoyaltyAccount_points}
RandL_LoyaltyAccount.methods={RandL_LoyaltyAccount_m_burn, RandL_LoyaltyAccount_m_isEmpty, RandL_LoyaltyAccount_m_getCustomerName, RandL_LoyaltyAccount_m_earn}

# RandL_ServiceLevel class attributes and methods
RandL_ServiceLevel_name: Property = Property(name="name", type=StringType)
RandL_ServiceLevel.attributes={RandL_ServiceLevel_name}

# RandL_LoyaltyProgram class attributes and methods
RandL_LoyaltyProgram_name: Property = Property(name="name", type=StringType)
RandL_LoyaltyProgram_m_selectPopularPartners: Method = Method(name="selectPopularPartners", parameters={Parameter(name='RandL_d', type=StringType)}, type=StringType)
RandL_LoyaltyProgram_m_addService: Method = Method(name="addService", parameters={Parameter(name='RandL_p', type=StringType), Parameter(name='RandL_s', type=StringType), Parameter(name='RandL_l', type=StringType)})
RandL_LoyaltyProgram_m_getServices: Method = Method(name="getServices", parameters={Parameter(name='RandL_pp', type=StringType)}, type=StringType)
RandL_LoyaltyProgram_m_enrollAndCreateCustomer: Method = Method(name="enrollAndCreateCustomer", parameters={Parameter(name='RandL_d', type=StringType), Parameter(name='RandL_n', type=StringType)}, type=StringType)
RandL_LoyaltyProgram_m_addTransaction: Method = Method(name="addTransaction", parameters={Parameter(name='RandL_servId', type=StringType), Parameter(name='RandL_d', type=StringType), Parameter(name='RandL_accNr', type=StringType), Parameter(name='RandL_pName', type=StringType), Parameter(name='RandL_amnt', type=StringType)})
RandL_LoyaltyProgram_m_getServices: Method = Method(name="getServices", parameters={}, type=StringType)
RandL_LoyaltyProgram_m_enroll: Method = Method(name="enroll", parameters={Parameter(name='RandL_c', type=StringType)})
RandL_LoyaltyProgram.attributes={RandL_LoyaltyProgram_name}
RandL_LoyaltyProgram.methods={RandL_LoyaltyProgram_m_getServices, RandL_LoyaltyProgram_m_addTransaction, RandL_LoyaltyProgram_m_getServices, RandL_LoyaltyProgram_m_enrollAndCreateCustomer, RandL_LoyaltyProgram_m_addService, RandL_LoyaltyProgram_m_enroll, RandL_LoyaltyProgram_m_selectPopularPartners}

# RandL_Service class attributes and methods
RandL_Service_serviceNr: Property = Property(name="serviceNr", type=StringType)
RandL_Service_description: Property = Property(name="description", type=StringType)
RandL_Service_pointsEarned: Property = Property(name="pointsEarned", type=StringType)
RandL_Service_condition: Property = Property(name="condition", type=StringType)
RandL_Service_pointsBurned: Property = Property(name="pointsBurned", type=StringType)
RandL_Service_m_upgradePointsEarned: Method = Method(name="upgradePointsEarned", parameters={Parameter(name='RandL_amount', type=StringType)})
RandL_Service_m_calcPoints: Method = Method(name="calcPoints", parameters={}, type=StringType)
RandL_Service.attributes={RandL_Service_pointsBurned, RandL_Service_condition, RandL_Service_serviceNr, RandL_Service_description, RandL_Service_pointsEarned}
RandL_Service.methods={RandL_Service_m_upgradePointsEarned, RandL_Service_m_calcPoints}

# RandL_Membership class attributes and methods

# RandL_CustomerCard class attributes and methods
RandL_CustomerCard_valid: Property = Property(name="valid", type=StringType)
RandL_CustomerCard_color: Property = Property(name="color", type=StringType)
RandL_CustomerCard_printedName: Property = Property(name="printedName", type=StringType)
RandL_CustomerCard_m_getTransactions: Method = Method(name="getTransactions", parameters={Parameter(name='RandL_until', type=StringType), Parameter(name='RandL_from_', type=StringType)}, type=Transaction)
RandL_CustomerCard.attributes={RandL_CustomerCard_printedName, RandL_CustomerCard_valid, RandL_CustomerCard_color}
RandL_CustomerCard.methods={RandL_CustomerCard_m_getTransactions}

# RandL_Earning class attributes and methods

# Transaction class attributes and methods

# RandL_ProgramPartner class attributes and methods
RandL_ProgramPartner_name: Property = Property(name="name", type=StringType)
RandL_ProgramPartner_numberOfCustomers: Property = Property(name="numberOfCustomers", type=StringType)
RandL_ProgramPartner.attributes={RandL_ProgramPartner_name, RandL_ProgramPartner_numberOfCustomers}

# RandL_TransactionReportLine class attributes and methods
RandL_TransactionReportLine_partnerName: Property = Property(name="partnerName", type=StringType)
RandL_TransactionReportLine_serviceDesc: Property = Property(name="serviceDesc", type=StringType)
RandL_TransactionReportLine_points: Property = Property(name="points", type=StringType)
RandL_TransactionReportLine_amount: Property = Property(name="amount", type=StringType)
RandL_TransactionReportLine.attributes={RandL_TransactionReportLine_amount, RandL_TransactionReportLine_partnerName, RandL_TransactionReportLine_serviceDesc, RandL_TransactionReportLine_points}

# RandL_Burning class attributes and methods

# RandL_TransactionReport class attributes and methods
RandL_TransactionReport_balance: Property = Property(name="balance", type=StringType)
RandL_TransactionReport_totalEarned: Property = Property(name="totalEarned", type=StringType)
RandL_TransactionReport_totalBurned: Property = Property(name="totalBurned", type=StringType)
RandL_TransactionReport_number: Property = Property(name="number", type=StringType)
RandL_TransactionReport_name: Property = Property(name="name", type=StringType)
RandL_TransactionReport.attributes={RandL_TransactionReport_number, RandL_TransactionReport_totalBurned, RandL_TransactionReport_name, RandL_TransactionReport_balance, RandL_TransactionReport_totalEarned}

# RandL_Customer class attributes and methods
RandL_Customer_gender: Property = Property(name="gender", type=StringType)
RandL_Customer_isMale: Property = Property(name="isMale", type=StringType)
RandL_Customer_name: Property = Property(name="name", type=StringType)
RandL_Customer_title: Property = Property(name="title", type=StringType)
RandL_Customer_age: Property = Property(name="age", type=StringType)
RandL_Customer_m_birthdayHappens: Method = Method(name="birthdayHappens", parameters={})
RandL_Customer_m_age: Method = Method(name="age", parameters={}, type=StringType)
RandL_Customer.attributes={RandL_Customer_name, RandL_Customer_gender, RandL_Customer_title, RandL_Customer_isMale, RandL_Customer_age}
RandL_Customer.methods={RandL_Customer_m_birthdayHappens, RandL_Customer_m_age}

# RandL_Container_RandL class attributes and methods

# Relationships
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
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="LoyaltyProgram", type=RandL_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="levels", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(0, 1))
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
card8: BinaryAssociation = BinaryAssociation(
    name="card8",
    ends={
        Property(name="CustomerCard", type=RandL_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions9", type=RandL_CustomerCard, multiplicity=Multiplicity(0, 1))
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
until19: BinaryAssociation = BinaryAssociation(
    name="until19",
    ends={
        Property(name="RandL_Date20", type=RandL_TransactionReport, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_TransactionReport", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from_21: BinaryAssociation = BinaryAssociation(
    name="from_21",
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
programs49: BinaryAssociation = BinaryAssociation(
    name="programs49",
    ends={
        Property(name="RandL_LoyaltyProgram", type=RandL_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Membership", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 1))
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
ref_RandL_LoyaltyProgram66: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_LoyaltyProgram66",
    ends={
        Property(name="RandL_LoyaltyProgram68", type=RandL_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_Container_RandL67", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
date101: BinaryAssociation = BinaryAssociation(
    name="date101",
    ends={
        Property(name="RandL_Date103", type=RandL_TransactionReportLine, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_TransactionReportLine102", type=RandL_Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partners108: BinaryAssociation = BinaryAssociation(
    name="partners108",
    ends={
        Property(name="ProgramPartner109", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="programs", type=RandL_ProgramPartner, multiplicity=Multiplicity(1, 9999))
    }
)
memberships115: BinaryAssociation = BinaryAssociation(
    name="memberships115",
    ends={
        Property(name="RandL_Membership117", type=RandL_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="RandL_LoyaltyProgram116", type=RandL_Membership, multiplicity=Multiplicity(0, 9999))
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


# OCL Constraints
invariant_ServiceLevel19: Constraint = Constraint(
    name="invariant_ServiceLevel19",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (Sequence{'a', 'b', 'c', 'c', 'd', 'e'}->prepend('X')) = Sequence{'X', 'a', 'b', 'c', 'c', 'd', 'e'}",
    language="OCL"
)
invariant_ServiceLevel17: Constraint = Constraint(
    name="invariant_ServiceLevel17",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (OrderedSet{'a', 'b', 'c', 'd'}->subOrderedSet(2, 3)) = OrderedSet{'b', 'c'}",
    language="OCL"
)
invariant_ServiceLevel4: Constraint = Constraint(
    name="invariant_ServiceLevel4",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: Bag{Set{1, 2}, Set{1, 2}, Set{4, 5, 6}}->isEmpty()",
    language="OCL"
)
invariant_ServiceLevel12: Constraint = Constraint(
    name="invariant_ServiceLevel12",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (OrderedSet{'a', 'b', 'c', 'd'}->last()) = 'd'",
    language="OCL"
)
invariant_ServiceLevel18: Constraint = Constraint(
    name="invariant_ServiceLevel18",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (Sequence{'a', 'b', 'c', 'c', 'd', 'e'}->append('X')) = Sequence{'a', 'b', 'c', 'c', 'd', 'e', 'X'}",
    language="OCL"
)
invariant_ServiceLevel1: Constraint = Constraint(
    name="invariant_ServiceLevel1",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: self.program.partners->isEmpty()",
    language="OCL"
)
invariant_ServiceLevel10: Constraint = Constraint(
    name="invariant_ServiceLevel10",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (Set{1, 4, 7, 10}->symmetricDifference(Set{4, 5, 7})) = Set{1, 5, 10}",
    language="OCL"
)
invariant_ServiceLevel7: Constraint = Constraint(
    name="invariant_ServiceLevel7",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: Sequence{2, 1, 2, 3, 5, 6, 4}->isEmpty()",
    language="OCL"
)
invariant_ServiceLevel5: Constraint = Constraint(
    name="invariant_ServiceLevel5",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: Bag{1, 1, 2, 2, 4, 5, 6}->isEmpty()",
    language="OCL"
)
invariant_ServiceLevel16: Constraint = Constraint(
    name="invariant_ServiceLevel16",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (Sequence{'a', 'b', 'c', 'c', 'd', 'e'}->subSequence(3, 5)) = Sequence{'c', 'c', 'd'}",
    language="OCL"
)
invariant_ServiceLevel6: Constraint = Constraint(
    name="invariant_ServiceLevel6",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: Sequence{Set{1, 2}, Set{2, 3}, Set{4, 5, 6}}->isEmpty()",
    language="OCL"
)
invariant_ServiceLevel13: Constraint = Constraint(
    name="invariant_ServiceLevel13",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (Sequence{'a', 'b', 'c', 'c', 'd', 'e'}->at(3)) = 'c'",
    language="OCL"
)
invariant_ServiceLevel3: Constraint = Constraint(
    name="invariant_ServiceLevel3",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: Set{1, 2, 3, 4, 5, 6}->isEmpty()",
    language="OCL"
)
invariant_ServiceLevel11: Constraint = Constraint(
    name="invariant_ServiceLevel11",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (Sequence{'a', 'b', 'c', 'c', 'd', 'e'}->first()) = 'a'",
    language="OCL"
)
invariant_ServiceLevel8: Constraint = Constraint(
    name="invariant_ServiceLevel8",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: ((Set{1, 4, 7, 10}) - Set{4, 7}) = Set{1, 10}",
    language="OCL"
)
invariant_ServiceLevel2: Constraint = Constraint(
    name="invariant_ServiceLevel2",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: Set{Set{1, 2}, Set{2, 3}, Set{4, 5, 6}}->isEmpty()",
    language="OCL"
)
invariant_ServiceLevel9: Constraint = Constraint(
    name="invariant_ServiceLevel9",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: ((OrderedSet{12, 9, 6, 3}) - Set{1, 3, 2}) = OrderedSet{12, 9, 6}",
    language="OCL"
)
invariant_ServiceLevel14: Constraint = Constraint(
    name="invariant_ServiceLevel14",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (Sequence{'a', 'b', 'c', 'c', 'd', 'e'}->indexOf('c')) = 3",
    language="OCL"
)
invariant_ServiceLevel15: Constraint = Constraint(
    name="invariant_ServiceLevel15",
    context=RandL_ServiceLevel,
    expression="context ServiceLevel inv: (OrderedSet{'a', 'b', 'c', 'd'}->insertAt(3, 'X')) = OrderedSet{'a', 'b', 'X', 'c', 'd'}",
    language="OCL"
)
invariant_Transaction1: Constraint = Constraint(
    name="invariant_Transaction1",
    context=RandL_Transaction,
    expression="context Transaction inv: self.oclIsKindOf(Transaction) = true",
    language="OCL"
)
invariant_Transaction3: Constraint = Constraint(
    name="invariant_Transaction3",
    context=RandL_Transaction,
    expression="context Transaction inv: self.oclIsTypeOf(Burning) = false",
    language="OCL"
)
invariant_Transaction2: Constraint = Constraint(
    name="invariant_Transaction2",
    context=RandL_Transaction,
    expression="context Transaction inv: self.oclIsTypeOf(Transaction) = true",
    language="OCL"
)
invariant_Transaction4: Constraint = Constraint(
    name="invariant_Transaction4",
    context=RandL_Transaction,
    expression="context Transaction inv: self.oclIsKindOf(Burning) = false",
    language="OCL"
)
invariant_points: Constraint = Constraint(
    name="invariant_points",
    context=RandL_LoyaltyAccount,
    expression="context LoyaltyAccount inv: (self.points > 0) implies self.transactions->exists( t : Transaction | t.points > 0 )",
    language="OCL"
)
invariant_transactions: Constraint = Constraint(
    name="invariant_transactions",
    context=RandL_LoyaltyAccount,
    expression="context LoyaltyAccount inv: self.transactions->collect( i_Transaction : Transaction | i_Transaction.points )->exists( p : Integer | p = 500 )",
    language="OCL"
)
invariant_oneOwner: Constraint = Constraint(
    name="invariant_oneOwner",
    context=RandL_LoyaltyAccount,
    expression="context LoyaltyAccount inv: (self.transactions->collect( i_Transaction : Transaction | i_Transaction.card )->collect( i_CustomerCard : CustomerCard | i_CustomerCard.owner )->asSet()->size()) = 1",
    language="OCL"
)
invariant_totalPointsEarning2: Constraint = Constraint(
    name="invariant_totalPointsEarning2",
    context=RandL_ProgramPartner,
    expression="context ProgramPartner inv: (self.deliveredServices->collect( i_Service : Service | i_Service.transactions )->select( i_Transaction : Transaction | i_Transaction.oclIsTypeOf(Earning) )->collect( i_Transaction : Transaction | i_Transaction.points )->sum()) < 10000",
    language="OCL"
)
invariant_totalPointsEarning: Constraint = Constraint(
    name="invariant_totalPointsEarning",
    context=RandL_ProgramPartner,
    expression="context ProgramPartner inv: (self.deliveredServices->collect( i_Service : Service | i_Service.transactions )->select( i_Transaction : Transaction | i_Transaction.oclIsTypeOf(Earning) )->collect( i_Transaction : Transaction | i_Transaction.points )->sum()) < 10000",
    language="OCL"
)
invariant_nrOfParticipants: Constraint = Constraint(
    name="invariant_nrOfParticipants",
    context=RandL_ProgramPartner,
    expression="context ProgramPartner inv: self.numberOfCustomers = self.programs->collect( i_LoyaltyProgram : LoyaltyProgram | i_LoyaltyProgram.participants )->size()def  :getBurningTransactions() : Set(Transaction) = self.deliveredServices.transactions->iterate(t : Transaction; resultSet : Set( Transaction) = Set{ } | if t.oclIsTypeOf(Burning) then resultSet->including(t) else resultSet endif)",
    language="OCL"
)
invariant_totalPoints: Constraint = Constraint(
    name="invariant_totalPoints",
    context=RandL_ProgramPartner,
    expression="context ProgramPartner inv: (self.deliveredServices->collect( i_Service : Service | i_Service.transactions )->collect( i_Transaction : Transaction | i_Transaction.points )->sum()) < 10000",
    language="OCL"
)
invariant_ProgramPartner1: Constraint = Constraint(
    name="invariant_ProgramPartner1",
    context=RandL_ProgramPartner,
    expression="context ProgramPartner inv: self.programs->collect( i_LoyaltyProgram : LoyaltyProgram | i_LoyaltyProgram.partners )->select( p : ProgramPartner | p <> self )->isEmpty()",
    language="OCL"
)
invariant_nrOfParticipants2: Constraint = Constraint(
    name="invariant_nrOfParticipants2",
    context=RandL_ProgramPartner,
    expression="context ProgramPartner inv: self.numberOfCustomers = self.programs->collect( i_LoyaltyProgram : LoyaltyProgram | i_LoyaltyProgram.participants )->asSet()->size()",
    language="OCL"
)
invariant_Burning5: Constraint = Constraint(
    name="invariant_Burning5",
    context=RandL_Burning,
    expression="context Burning inv: self.oclIsTypeOf(Earning) = false",
    language="OCL"
)
invariant_Burning6: Constraint = Constraint(
    name="invariant_Burning6",
    context=RandL_Burning,
    expression="context Burning inv: self.oclIsKindOf(Earning) = false",
    language="OCL"
)
invariant_Burning4: Constraint = Constraint(
    name="invariant_Burning4",
    context=RandL_Burning,
    expression="context Burning inv: self.oclIsKindOf(Burning) = true",
    language="OCL"
)
invariant_Burning3: Constraint = Constraint(
    name="invariant_Burning3",
    context=RandL_Burning,
    expression="context Burning inv: self.oclIsTypeOf(Burning) = true",
    language="OCL"
)
invariant_Burning2: Constraint = Constraint(
    name="invariant_Burning2",
    context=RandL_Burning,
    expression="context Burning inv: self.oclIsTypeOf(Transaction) = false",
    language="OCL"
)
invariant_Burning1: Constraint = Constraint(
    name="invariant_Burning1",
    context=RandL_Burning,
    expression="context Burning inv: self.oclIsKindOf(Transaction) = true",
    language="OCL"
)
invariant_dates: Constraint = Constraint(
    name="invariant_dates",
    context=RandL_TransactionReport,
    expression="context TransactionReport inv: self.lines->collect( i_TransactionReportLine : TransactionReportLine | i_TransactionReportLine.date )->forAll( d : Date | d.isBefore(self.until) and d.isAfter(self.from) )",
    language="OCL"
)
invariant_cycle: Constraint = Constraint(
    name="invariant_cycle",
    context=RandL_TransactionReport,
    expression="context TransactionReport inv: self.card.transactions->includesAll(self.lines->collect( i_TransactionReportLine : TransactionReportLine | i_TransactionReportLine.transaction ))",
    language="OCL"
)
invariant_CustomerCard4: Constraint = Constraint(
    name="invariant_CustomerCard4",
    context=RandL_CustomerCard,
    expression="context CustomerCard inv: self.transactions->select( i_Transaction : Transaction | i_Transaction.points > 100 )->notEmpty()",
    language="OCL"
)
invariant_ofAge: Constraint = Constraint(
    name="invariant_ofAge",
    context=RandL_CustomerCard,
    expression="context CustomerCard inv: self.owner.age >= 18",
    language="OCL"
)
invariant_CustomerCard3: Constraint = Constraint(
    name="invariant_CustomerCard3",
    context=RandL_CustomerCard,
    expression="context CustomerCard inv: self.owner.programs->size() > 0",
    language="OCL"
)
invariant_checkDates: Constraint = Constraint(
    name="invariant_checkDates",
    context=RandL_CustomerCard,
    expression="context CustomerCard inv: self.validFrom.isBefore(self.goodThru)",
    language="OCL"
)
invariant_Membership1: Constraint = Constraint(
    name="invariant_Membership1",
    context=RandL_Membership,
    expression="context Membership inv: (self.account.points >= 0) or self.account->asSet()->isEmpty()",
    language="OCL"
)
invariant_Membership2: Constraint = Constraint(
    name="invariant_Membership2",
    context=RandL_Membership,
    expression="context Membership inv: self.participants.cards->collect( i_CustomerCard : CustomerCard | i_CustomerCard.Membership )->includes(self)",
    language="OCL"
)
invariant_noEarnings: Constraint = Constraint(
    name="invariant_noEarnings",
    context=RandL_Membership,
    expression="context Membership inv: programs.partners.deliveredServices->forAll(pointsEarned = 0) implies account->isEmpty()",
    language="OCL"
)
invariant_correctCard: Constraint = Constraint(
    name="invariant_correctCard",
    context=RandL_Membership,
    expression="context Membership inv: self.participants.cards->includes(self.card)",
    language="OCL"
)
invariant_Membership3: Constraint = Constraint(
    name="invariant_Membership3",
    context=RandL_Membership,
    expression="context Membership inv: self.programs.levels->includes(self.currentLevel)",
    language="OCL"
)
invariant_Membership4: Constraint = Constraint(
    name="invariant_Membership4",
    context=RandL_Membership,
    expression="context Membership inv: self.account->asSet()->isEmpty()",
    language="OCL"
)
invariant_levelAndColor: Constraint = Constraint(
    name="invariant_levelAndColor",
    context=RandL_Membership,
    expression="context Membership inv: ((self.currentLevel.name = 'Silver') implies (self.card.color = RandLColor_silver) and self.currentLevel.name = 'Gold') implies self.card.color = RandLColor_gold",
    language="OCL"
)
invariant_Membership5: Constraint = Constraint(
    name="invariant_Membership5",
    context=RandL_Membership,
    expression="context Membership inv: self.programs.levels->includes(self.currentLevel)",
    language="OCL"
)
invariant_Service5: Constraint = Constraint(
    name="invariant_Service5",
    context=RandL_ServiceLevel,
    expression="context Service inv: 'Anneke'.toUpperCase() = 'ANNEKE'",
    language="OCL"
)
invariant_Service6: Constraint = Constraint(
    name="invariant_Service6",
    context=RandL_ServiceLevel,
    expression="context Service inv: 'Anneke'.toLowerCase() = 'anneke'",
    language="OCL"
)
invariant_Service7: Constraint = Constraint(
    name="invariant_Service7",
    context=RandL_ServiceLevel,
    expression="context Service inv: ('Anneke and Jos'.substring(12, 14)) = 'Jos'",
    language="OCL"
)
invariant_Service4: Constraint = Constraint(
    name="invariant_Service4",
    context=RandL_ServiceLevel,
    expression="context Service inv: ('Anneke '.concat('and Jos')) = 'Anneke and Jos'",
    language="OCL"
)
invariant_Service1: Constraint = Constraint(
    name="invariant_Service1",
    context=RandL_ServiceLevel,
    expression="context Service inv: (self.pointsEarned > 0) implies not (self.pointsBurned = 0)",
    language="OCL"
)
invariant_Service3: Constraint = Constraint(
    name="invariant_Service3",
    context=RandL_ServiceLevel,
    expression="context Service inv: ('Anneke' = 'Jos') = false",
    language="OCL"
)
invariant_Service2: Constraint = Constraint(
    name="invariant_Service2",
    context=RandL_ServiceLevel,
    expression="context Service inv: 'Anneke'.size() = 6",
    language="OCL"
)
invariant_Customer4: Constraint = Constraint(
    name="invariant_Customer4",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.name = 'Edward'",
    language="OCL"
)
invariant_Customer5: Constraint = Constraint(
    name="invariant_Customer5",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.title = 'Mr.'",
    language="OCL"
)
invariant_Customer10: Constraint = Constraint(
    name="invariant_Customer10",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.programs->collect( i_LoyaltyProgram : LoyaltyProgram | i_LoyaltyProgram.partners )->collectNested( i_ProgramPartner : ProgramPartner | i_ProgramPartner.deliveredServices )->isEmpty()",
    language="OCL"
)
invariant_Customer2: Constraint = Constraint(
    name="invariant_Customer2",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.name = 'Edward'",
    language="OCL"
)
invariant_Customer9: Constraint = Constraint(
    name="invariant_Customer9",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.memberships->collect( i_Membership : Membership | i_Membership.account )->reject( i_LoyaltyAccount : LoyaltyAccount | not (i_LoyaltyAccount.points > 0) )->isEmpty()",
    language="OCL"
)
invariant_myInvariant23: Constraint = Constraint(
    name="invariant_myInvariant23",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.name = 'Edward'",
    language="OCL"
)
invariant_Customer1: Constraint = Constraint(
    name="invariant_Customer1",
    context=RandL_CustomerCard,
    expression="context Customer inv: (self.cards->select( i_CustomerCard : CustomerCard | i_CustomerCard.valid = true )->size()) > 1",
    language="OCL"
)
invariant_Customer7: Constraint = Constraint(
    name="invariant_Customer7",
    context=RandL_CustomerCard,
    expression="context Customer inv: (self.gender = Gender_male) implies self.title = 'Mr.'",
    language="OCL"
)
invariant_Customer11: Constraint = Constraint(
    name="invariant_Customer11",
    context=RandL_CustomerCard,
    expression="context Customer inv: Set{1, 2, 3 }->iterate(i : Integer; sum : Integer = 0 | sum + i) = 0",
    language="OCL"
)
invariant_ANY: Constraint = Constraint(
    name="invariant_ANY",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.memberships->collect( i_Membership : Membership | i_Membership.account )->any( i_LoyaltyAccount : LoyaltyAccount | i_LoyaltyAccount.number < 10000 )->asSet()->isEmpty()",
    language="OCL"
)
invariant_ofAge1: Constraint = Constraint(
    name="invariant_ofAge1",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.age >= 18",
    language="OCL"
)
invariant_sizesAgree: Constraint = Constraint(
    name="invariant_sizesAgree",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.programs->size()= self.cards->select( i_CustomerCard : CustomerCard| i_CustomerCard.valid = true)->size()",
    language="OCL"
)
invariant_Customer8: Constraint = Constraint(
    name="invariant_Customer8",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.memberships->collect( i_Membership : Membership | i_Membership.account )->select( i_LoyaltyAccount : LoyaltyAccount | i_LoyaltyAccount.points > 0 )->isEmpty()",
    language="OCL"
)
invariant_Customer6: Constraint = Constraint(
    name="invariant_Customer6",
    context=RandL_CustomerCard,
    expression="context Customer inv: (self.name = 'Edward') and self.title = 'Mr.'def  :wellUsedCards : Set(CustomerCard) = self.cards->select( i_CustomerCard : CustomerCard | (i_CustomerCard.transactions->collect( i_Transaction : Transaction | i_Transaction.points )->sum()) > 10000 )",
    language="OCL"
)
invariant_Customer3: Constraint = Constraint(
    name="invariant_Customer3",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.name = 'Edward'def  :initial : String = self.name.substring(1, 1)",
    language="OCL"
)
invariant_Customer12: Constraint = Constraint(
    name="invariant_Customer12",
    context=RandL_CustomerCard,
    expression="context Customer inv: self.programs->size() = self.cards->select( i_CustomerCard : CustomerCard | i_CustomerCard.valid = true )->size()def  :cardsForProgram(p : LoyaltyProgram) : Sequence(CustomerCard) = p.memberships->collect( i_Membership : Membership | i_Membership.card )def  :loyalToCompanies : Bag(ProgramPartner) = self.programs->collect( i_LoyaltyProgram : LoyaltyProgram | i_LoyaltyProgram.partners )",
    language="OCL"
)
invariant_LoyaltyProgram18: Constraint = Constraint(
    name="invariant_LoyaltyProgram18",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.participants->forAll( c1 : Customer | self.participants->forAll( c2 : Customer | (c1 <> c2) implies c1.name <> c2.name ) )",
    language="OCL"
)
invariant_LoyaltyProgram1: Constraint = Constraint(
    name="invariant_LoyaltyProgram1",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.levels->includesAll(self.memberships->collect( i_Membership : Membership | i_Membership.currentLevel ))",
    language="OCL"
)
invariant_LoyaltyProgram17: Constraint = Constraint(
    name="invariant_LoyaltyProgram17",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.participants->forAll( c1 : Customer, c2 : Customer | (c1 <> c2) implies c1.name <> c2.name )",
    language="OCL"
)
invariant_LoyaltyProgram14: Constraint = Constraint(
    name="invariant_LoyaltyProgram14",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.memberships->collect( i_Membership : Membership | i_Membership.account )->isUnique( acc : LoyaltyAccount | acc.number )def  :sortedAccounts : Sequence(LoyaltyAccount) = self.memberships->collect( i_Membership : Membership | i_Membership.account )->sortedBy( i_LoyaltyAccount : LoyaltyAccount | i_LoyaltyAccount.number )",
    language="OCL"
)
invariant_LoyaltyProgram10: Constraint = Constraint(
    name="invariant_LoyaltyProgram10",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: Sequence{1 .. 10}->isEmpty()",
    language="OCL"
)
invariant_firstLevel: Constraint = Constraint(
    name="invariant_firstLevel",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.levels->first().name = 'Silver'",
    language="OCL"
)
invariant_LoyaltyProgram8: Constraint = Constraint(
    name="invariant_LoyaltyProgram8",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: Bag{1, 3, 4, 3, 5}->isEmpty()",
    language="OCL"
)
invariant_knownServiceLevel: Constraint = Constraint(
    name="invariant_knownServiceLevel",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.levels->includesAll(self.memberships->collect( i_Membership : Membership | i_Membership.currentLevel ))def  :getServicesByLevel(levelName : String) : Set(Service) = self.levels->select( i_ServiceLevel : ServiceLevel | i_ServiceLevel.name = levelName )->collect( i_ServiceLevel : ServiceLevel | i_ServiceLevel.availableServices )->asSet()",
    language="OCL"
)
invariant_LoyaltyProgram13: Constraint = Constraint(
    name="invariant_LoyaltyProgram13",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.memberships->collect( i_Membership : Membership | i_Membership.account )->isUnique( acc : LoyaltyAccount | acc.number )",
    language="OCL"
)
invariant_minServices: Constraint = Constraint(
    name="invariant_minServices",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: (self.partners->collect( i_ProgramPartner : ProgramPartner | i_ProgramPartner.deliveredServices )->size()) >= 1",
    language="OCL"
)
invariant_LoyaltyProgram19: Constraint = Constraint(
    name="invariant_LoyaltyProgram19",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.memberships->collect( i_Membership : Membership | i_Membership.account )->one( i_LoyaltyAccount : LoyaltyAccount | i_LoyaltyAccount.number < 10000 )",
    language="OCL"
)
invariant_LoyaltyProgram12: Constraint = Constraint(
    name="invariant_LoyaltyProgram12",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.participants->size() < 10000",
    language="OCL"
)
invariant_LoyaltyProgram7: Constraint = Constraint(
    name="invariant_LoyaltyProgram7",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: Sequence{'ape', 'nut'}->isEmpty()",
    language="OCL"
)
invariant_LoyaltyProgram11: Constraint = Constraint(
    name="invariant_LoyaltyProgram11",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: Sequence{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}->isEmpty()def  :isSaving : Boolean = self.partners->collect( i_ProgramPartner : ProgramPartner | i_ProgramPartner.deliveredServices )->forAll( i_Service : Service | i_Service.pointsEarned = 0 )",
    language="OCL"
)
invariant_LoyaltyProgram3: Constraint = Constraint(
    name="invariant_LoyaltyProgram3",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: Set{1, 2, 5, 88}->isEmpty()",
    language="OCL"
)
invariant_LoyaltyProgram2: Constraint = Constraint(
    name="invariant_LoyaltyProgram2",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.levels->exists( i_ServiceLevel : ServiceLevel | i_ServiceLevel.name = 'basic' )",
    language="OCL"
)
invariant_noAccounts: Constraint = Constraint(
    name="invariant_noAccounts",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: (self.partners->collect( i_ProgramPartner : ProgramPartner | i_ProgramPartner.deliveredServices )->forAll( i_Service : Service | (i_Service.pointsEarned = 0) and i_Service.pointsBurned = 0 )) implies self.memberships->collect( i_Membership : Membership | i_Membership.account )->isEmpty()",
    language="OCL"
)
invariant_LoyaltyProgram15: Constraint = Constraint(
    name="invariant_LoyaltyProgram15",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.memberships->collect( i_Membership : Membership | i_Membership.account )->isUnique( i_LoyaltyAccount : LoyaltyAccount | i_LoyaltyAccount.number )",
    language="OCL"
)
invariant_LoyaltyProgram4: Constraint = Constraint(
    name="invariant_LoyaltyProgram4",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: Set{'apple', 'orange', 'strawberry'}->isEmpty()",
    language="OCL"
)
invariant_LoyaltyProgram6: Constraint = Constraint(
    name="invariant_LoyaltyProgram6",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: Sequence{1, 3, 45, 2, 3}->isEmpty()",
    language="OCL"
)
invariant_LoyaltyProgram9: Constraint = Constraint(
    name="invariant_LoyaltyProgram9",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: Sequence{1 .. 6 + 4}->isEmpty()",
    language="OCL"
)
invariant_LoyaltyProgram5: Constraint = Constraint(
    name="invariant_LoyaltyProgram5",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: OrderedSet{'apple', 'orange', 'strawberry', 'pear'}->isEmpty()",
    language="OCL"
)
invariant_LoyaltyProgram16: Constraint = Constraint(
    name="invariant_LoyaltyProgram16",
    context=RandL_LoyaltyProgram,
    expression="context LoyaltyProgram inv: self.participants->forAll( i_Customer : Customer | i_Customer.age() <= 70 )",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="RandL",
    types={RandL_Transaction, RandL_Date, RandL_LoyaltyAccount, RandL_ServiceLevel, RandL_LoyaltyProgram, RandL_Service, RandL_Membership, RandL_CustomerCard, RandL_Earning, Transaction, RandL_ProgramPartner, RandL_TransactionReportLine, RandL_Burning, RandL_TransactionReport, RandL_Customer, RandL_Container_RandL, Gender, RandLColor},
    associations={date3, account4, generatedBy5, program0, availableServices1, Membership2, card8, transactions13, deliveredServices15, programs17, usedServices10, Membership11, until19, from_21, lines24, card25, owner35, Membership36, transactions38, goodThru27, validFrom30, myLevel33, currentLevel41, card43, account46, participants50, ref_RandL_Customer52, ref_RandL_Date54, ref_RandL_CustomerCard57, ref_RandL_Membership60, ref_RandL_Service63, programs49, ref_RandL_Earning69, ref_RandL_LoyaltyAccount71, ref_RandL_ServiceLevel74, ref_RandL_TransactionReport77, ref_RandL_ProgramPartner80, ref_RandL_Burning82, ref_RandL_TransactionReportLine84, ref_RandL_LoyaltyProgram66, partner86, transactions87, level89, dateOfBirth91, programs94, cards96, memberships98, transaction104, report107, date101, partners108, memberships115, levels110, participants112},
    constraints={invariant_ServiceLevel19, invariant_ServiceLevel17, invariant_ServiceLevel4, invariant_ServiceLevel12, invariant_ServiceLevel18, invariant_ServiceLevel1, invariant_ServiceLevel10, invariant_ServiceLevel7, invariant_ServiceLevel5, invariant_ServiceLevel16, invariant_ServiceLevel6, invariant_ServiceLevel13, invariant_ServiceLevel3, invariant_ServiceLevel11, invariant_ServiceLevel8, invariant_ServiceLevel2, invariant_ServiceLevel9, invariant_ServiceLevel14, invariant_ServiceLevel15, invariant_Transaction1, invariant_Transaction3, invariant_Transaction2, invariant_Transaction4, invariant_points, invariant_transactions, invariant_oneOwner, invariant_totalPointsEarning2, invariant_totalPointsEarning, invariant_nrOfParticipants, invariant_totalPoints, invariant_ProgramPartner1, invariant_nrOfParticipants2, invariant_Burning5, invariant_Burning6, invariant_Burning4, invariant_Burning3, invariant_Burning2, invariant_Burning1, invariant_dates, invariant_cycle, invariant_CustomerCard4, invariant_ofAge, invariant_CustomerCard3, invariant_checkDates, invariant_Membership1, invariant_Membership2, invariant_noEarnings, invariant_correctCard, invariant_Membership3, invariant_Membership4, invariant_levelAndColor, invariant_Membership5, invariant_Service5, invariant_Service6, invariant_Service7, invariant_Service4, invariant_Service1, invariant_Service3, invariant_Service2, invariant_Customer4, invariant_Customer5, invariant_Customer10, invariant_Customer2, invariant_Customer9, invariant_myInvariant23, invariant_Customer1, invariant_Customer7, invariant_Customer11, invariant_ANY, invariant_ofAge1, invariant_sizesAgree, invariant_Customer8, invariant_Customer6, invariant_Customer3, invariant_Customer12, invariant_LoyaltyProgram18, invariant_LoyaltyProgram1, invariant_LoyaltyProgram17, invariant_LoyaltyProgram14, invariant_LoyaltyProgram10, invariant_firstLevel, invariant_LoyaltyProgram8, invariant_knownServiceLevel, invariant_LoyaltyProgram13, invariant_minServices, invariant_LoyaltyProgram19, invariant_LoyaltyProgram12, invariant_LoyaltyProgram7, invariant_LoyaltyProgram11, invariant_LoyaltyProgram3, invariant_LoyaltyProgram2, invariant_noAccounts, invariant_LoyaltyProgram15, invariant_LoyaltyProgram4, invariant_LoyaltyProgram6, invariant_LoyaltyProgram9, invariant_LoyaltyProgram5, invariant_LoyaltyProgram16},
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