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
BankAccount = Class(name="BankAccount")
ClassA = Class(name="ClassA")
ClassB = Class(name="ClassB")
ClassC = Class(name="ClassC")
Class_ = Class(name="Class")

# BankAccount class attributes and methods
BankAccount_ownerName: Property = Property(name="ownerName", type=StringType)
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount.attributes={BankAccount_ownerName, BankAccount_balance}

# ClassA class attributes and methods
ClassA_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassA_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassA_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassA_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassA.attributes={ClassA_protectedAttribute, ClassA_privateAttribute, ClassA_publicAttribute, ClassA_packageAttribute}

# ClassB class attributes and methods

# ClassC class attributes and methods
ClassC_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassC_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassC_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassC_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassC.attributes={ClassC_publicAttribute, ClassC_privateAttribute, ClassC_packageAttribute, ClassC_protectedAttribute}

# Class class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_St2EoN8GEemZHaiox11UDg",
    types={BankAccount, ClassA, ClassB, ClassC, Class_},
    associations={},
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