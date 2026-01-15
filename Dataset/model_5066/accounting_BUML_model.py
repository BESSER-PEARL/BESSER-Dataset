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
accounting_Account = Class(name="accounting::Account", is_abstract=True)
accounting_AccountGroup = Class(name="accounting::AccountGroup")
accounting_Accounting = Class(name="accounting::Accounting")
Serializable = Class(name="Serializable")
accounting_Vat = Class(name="accounting::Vat")
accounting_BalanceAccount = Class(name="accounting::BalanceAccount")
accounting_Report = Class(name="accounting::Report")
accounting_JournalGroup = Class(name="accounting::JournalGroup")
Account = Class(name="Account")
accounting_ReportGroup = Class(name="accounting::ReportGroup")
accounting_JournalStatement = Class(name="accounting::JournalStatement")
accounting_PLAccount = Class(name="accounting::PLAccount")
accounting_Serializable = Class(name="accounting::Serializable", is_abstract=True)

# accounting_Account class attributes and methods
accounting_Account_name: Property = Property(name="name", type=StringType)
accounting_Account.attributes={accounting_Account_name}

# accounting_AccountGroup class attributes and methods
accounting_AccountGroup_name: Property = Property(name="name", type=StringType)
accounting_AccountGroup.attributes={accounting_AccountGroup_name}

# accounting_Accounting class attributes and methods
accounting_Accounting_name: Property = Property(name="name", type=StringType)
accounting_Accounting.attributes={accounting_Accounting_name}

# Serializable class attributes and methods

# accounting_Vat class attributes and methods
accounting_Vat_name: Property = Property(name="name", type=StringType)
accounting_Vat_rate: Property = Property(name="rate", type=StringType)
accounting_Vat.attributes={accounting_Vat_rate, accounting_Vat_name}

# accounting_BalanceAccount class attributes and methods

# accounting_Report class attributes and methods
accounting_Report_name: Property = Property(name="name", type=StringType)
accounting_Report.attributes={accounting_Report_name}

# accounting_JournalGroup class attributes and methods
accounting_JournalGroup_name: Property = Property(name="name", type=StringType)
accounting_JournalGroup.attributes={accounting_JournalGroup_name}

# Account class attributes and methods

# accounting_ReportGroup class attributes and methods
accounting_ReportGroup_name: Property = Property(name="name", type=StringType)
accounting_ReportGroup.attributes={accounting_ReportGroup_name}

# accounting_JournalStatement class attributes and methods
accounting_JournalStatement_description: Property = Property(name="description", type=StringType)
accounting_JournalStatement_date: Property = Property(name="date", type=StringType)
accounting_JournalStatement_amount: Property = Property(name="amount", type=StringType)
accounting_JournalStatement.attributes={accounting_JournalStatement_amount, accounting_JournalStatement_description, accounting_JournalStatement_date}

# accounting_PLAccount class attributes and methods

# accounting_Serializable class attributes and methods

# Relationships
account0: BinaryAssociation = BinaryAssociation(
    name="account0",
    ends={
        Property(name="accounting_Account", type=accounting_AccountGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_AccountGroup", type=accounting_Account, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accountGroup1: BinaryAssociation = BinaryAssociation(
    name="accountGroup1",
    ends={
        Property(name="accounting_AccountGroup2", type=accounting_Accounting, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Accounting", type=accounting_AccountGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vat3: BinaryAssociation = BinaryAssociation(
    name="vat3",
    ends={
        Property(name="accounting_Vat", type=accounting_Accounting, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Accounting4", type=accounting_Vat, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vatAccount5: BinaryAssociation = BinaryAssociation(
    name="vatAccount5",
    ends={
        Property(name="accounting_BalanceAccount", type=accounting_Accounting, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Accounting6", type=accounting_BalanceAccount, multiplicity=Multiplicity(0, 1))
    }
)
report7: BinaryAssociation = BinaryAssociation(
    name="report7",
    ends={
        Property(name="accounting_Report", type=accounting_Accounting, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Accounting8", type=accounting_Report, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
journalGroup9: BinaryAssociation = BinaryAssociation(
    name="journalGroup9",
    ends={
        Property(name="accounting_JournalGroup", type=accounting_Accounting, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Accounting10", type=accounting_JournalGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
report11: BinaryAssociation = BinaryAssociation(
    name="report11",
    ends={
        Property(name="ReportGroup", type=accounting_BalanceAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="account", type=accounting_ReportGroup, multiplicity=Multiplicity(0, 9999))
    }
)
journalGroups13: BinaryAssociation = BinaryAssociation(
    name="journalGroups13",
    ends={
        Property(name="accounting_JournalGroup14", type=accounting_JournalGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_JournalGroup12", type=accounting_JournalGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
journalStatements15: BinaryAssociation = BinaryAssociation(
    name="journalStatements15",
    ends={
        Property(name="accounting_JournalStatement", type=accounting_JournalGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_JournalGroup16", type=accounting_JournalStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
debitAccount17: BinaryAssociation = BinaryAssociation(
    name="debitAccount17",
    ends={
        Property(name="accounting_Account19", type=accounting_JournalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_JournalStatement18", type=accounting_Account, multiplicity=Multiplicity(1, 1))
    }
)
creditAccount20: BinaryAssociation = BinaryAssociation(
    name="creditAccount20",
    ends={
        Property(name="accounting_Account22", type=accounting_JournalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_JournalStatement21", type=accounting_Account, multiplicity=Multiplicity(1, 1))
    }
)
vat23: BinaryAssociation = BinaryAssociation(
    name="vat23",
    ends={
        Property(name="accounting_Vat25", type=accounting_JournalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_JournalStatement24", type=accounting_Vat, multiplicity=Multiplicity(0, 1))
    }
)
debitReportGroup26: BinaryAssociation = BinaryAssociation(
    name="debitReportGroup26",
    ends={
        Property(name="accounting_ReportGroup", type=accounting_Report, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Report27", type=accounting_ReportGroup, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
creditReportGroup28: BinaryAssociation = BinaryAssociation(
    name="creditReportGroup28",
    ends={
        Property(name="accounting_ReportGroup30", type=accounting_Report, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Report29", type=accounting_ReportGroup, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reportGroup32: BinaryAssociation = BinaryAssociation(
    name="reportGroup32",
    ends={
        Property(name="accounting_ReportGroup33", type=accounting_ReportGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_ReportGroup31", type=accounting_ReportGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
account34: BinaryAssociation = BinaryAssociation(
    name="account34",
    ends={
        Property(name="BalanceAccount", type=accounting_ReportGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="report", type=accounting_BalanceAccount, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_accounting_Accounting_Serializable = Generalization(general=Serializable, specific=accounting_Accounting)
gen_accounting_BalanceAccount_Account = Generalization(general=Account, specific=accounting_BalanceAccount)
gen_accounting_PLAccount_Account = Generalization(general=Account, specific=accounting_PLAccount)

# Domain Model
domain_model = DomainModel(
    name="accounting",
    types={accounting_Account, accounting_AccountGroup, accounting_Accounting, Serializable, accounting_Vat, accounting_BalanceAccount, accounting_Report, accounting_JournalGroup, Account, accounting_ReportGroup, accounting_JournalStatement, accounting_PLAccount, accounting_Serializable},
    associations={account0, accountGroup1, vat3, vatAccount5, report7, journalGroup9, report11, journalGroups13, journalStatements15, debitAccount17, creditAccount20, vat23, debitReportGroup26, creditReportGroup28, reportGroup32, account34},
    generalizations={gen_accounting_Accounting_Serializable, gen_accounting_BalanceAccount_Account, gen_accounting_PLAccount_Account},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)