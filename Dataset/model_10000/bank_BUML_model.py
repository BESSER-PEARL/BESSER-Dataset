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
CardType: Enumeration = Enumeration(
    name="CardType",
    literals={
            
    }
)

# Classes
bank_Account = Class(name="bank_Account")
bank_Client = Class(name="bank_Client")
bank_Card = Class(name="bank_Card")
bank_Bank = Class(name="bank_Bank")
bank_Manager = Class(name="bank_Manager")

# bank_Account class attributes and methods
bank_Account_credit: Property = Property(name="credit", type=FloatType)
bank_Account_overdraft: Property = Property(name="overdraft", type=FloatType)
bank_Account.attributes={bank_Account_overdraft, bank_Account_credit}

# bank_Client class attributes and methods
bank_Client_name: Property = Property(name="name", type=StringType)
bank_Client_capacity: Property = Property(name="capacity", type=IntegerType)
bank_Client.attributes={bank_Client_name, bank_Client_capacity}

# bank_Card class attributes and methods
bank_Card_number: Property = Property(name="number", type=StringType)
bank_Card_type: Property = Property(name="type", type=StringType)
bank_Card.attributes={bank_Card_type, bank_Card_number}

# bank_Bank class attributes and methods

# bank_Manager class attributes and methods
bank_Manager_name: Property = Property(name="name", type=StringType)
bank_Manager.attributes={bank_Manager_name}

# Relationships
managers0: BinaryAssociation = BinaryAssociation(
    name="managers0",
    ends={
        Property(name="bank_Bank", type=bank_Manager, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="bank_Manager", type=bank_Bank, multiplicity=Multiplicity(1, 1))
    }
)
accounts1: BinaryAssociation = BinaryAssociation(
    name="accounts1",
    ends={
        Property(name="bank_Account", type=bank_Bank, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Bank2", type=bank_Account, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clients3: BinaryAssociation = BinaryAssociation(
    name="clients3",
    ends={
        Property(name="bank_Client", type=bank_Bank, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Bank4", type=bank_Client, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manager5: BinaryAssociation = BinaryAssociation(
    name="manager5",
    ends={
        Property(name="Manager", type=bank_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="clients", type=bank_Manager, multiplicity=Multiplicity(0, 9999))
    }
)
accounts6: BinaryAssociation = BinaryAssociation(
    name="accounts6",
    ends={
        Property(name="Account", type=bank_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="owners", type=bank_Account, multiplicity=Multiplicity(0, 9999))
    }
)
sponsorships8: BinaryAssociation = BinaryAssociation(
    name="sponsorships8",
    ends={
        Property(name="bank_Client9", type=bank_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Client7", type=bank_Client, multiplicity=Multiplicity(0, 9999))
    }
)
clients10: BinaryAssociation = BinaryAssociation(
    name="clients10",
    ends={
        Property(name="Client", type=bank_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=bank_Client, multiplicity=Multiplicity(0, 9999))
    }
)
owners11: BinaryAssociation = BinaryAssociation(
    name="owners11",
    ends={
        Property(name="Client12", type=bank_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="accounts", type=bank_Client, multiplicity=Multiplicity(0, 9999))
    }
)
cards13: BinaryAssociation = BinaryAssociation(
    name="cards13",
    ends={
        Property(name="bank_Card", type=bank_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="bank_Account14", type=bank_Card, multiplicity=Multiplicity(0, 9999))
    }
)


# OCL Constraints
minAccounts: Constraint = Constraint(
    name="minAccounts",
    context=bank_Client,
    expression="context Client inv: self.accounts->size()> 0",
    language="OCL"
)
minManagers: Constraint = Constraint(
    name="minManagers",
    context=bank_Client,
    expression="context Client inv: self.manager->size()>0",
    language="OCL"
)
maxAccounts: Constraint = Constraint(
    name="maxAccounts",
    context=bank_Client,
    expression="context Client inv: Client_allInstances()->forAll(var | var.accounts->size() <= var.capacity)",
    language="OCL"
)
minCredit: Constraint = Constraint(
    name="minCredit",
    context=bank_Account,
    expression="context Account inv: Account_allInstances()->select(var| var.credit < 0)->isEmpty()",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="bank",
    types={bank_Account, bank_Client, bank_Card, bank_Bank, bank_Manager, CardType},
    associations={managers0, accounts1, clients3, manager5, accounts6, sponsorships8, clients10, owners11, cards13},
    constraints={minAccounts, minManagers, maxAccounts, minCredit},
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