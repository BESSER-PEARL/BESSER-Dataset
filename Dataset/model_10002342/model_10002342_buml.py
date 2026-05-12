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
ErrorCodeException = Class(name="ErrorCodeException")
ErrorCode = Class(name="ErrorCode")
ClassD = Class(name="ClassD")
ClassE = Class(name="ClassE")
ClassF = Class(name="ClassF")
ClassG = Class(name="ClassG")
ClassM = Class(name="ClassM")
ClassN = Class(name="ClassN")
ClassP = Class(name="ClassP")
InterfaceO_Interface = Class(name="InterfaceO_Interface")
ClassQ = Class(name="ClassQ")
ClassR = Class(name="ClassR")
ClassS = Class(name="ClassS")
ClassT = Class(name="ClassT")
ClassU = Class(name="ClassU")
ClassV = Class(name="ClassV")
Exception = Class(name="Exception")

# BankAccount class attributes and methods
BankAccount_ownerName: Property = Property(name="ownerName", type=StringType)
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount.attributes={BankAccount_balance, BankAccount_ownerName}

# ErrorCodeException class attributes and methods
ErrorCodeException_errorCode: Property = Property(name="errorCode", type=ErrorCode)
ErrorCodeException_errorCodeMessage: Property = Property(name="errorCodeMessage", type=StringType)
ErrorCodeException_throwable: Property = Property(name="throwable", type=StringType)
ErrorCodeException.attributes={ErrorCodeException_throwable, ErrorCodeException_errorCodeMessage, ErrorCodeException_errorCode}

# ErrorCode class attributes and methods
ErrorCode_tier: Property = Property(name="tier", type=IntegerType)
ErrorCode_domain: Property = Property(name="domain", type=IntegerType)
ErrorCode_subdomain: Property = Property(name="subdomain", type=IntegerType)
ErrorCode_reason: Property = Property(name="reason", type=IntegerType)
ErrorCode.attributes={ErrorCode_tier, ErrorCode_subdomain, ErrorCode_domain, ErrorCode_reason}

# ClassD class attributes and methods

# ClassE class attributes and methods

# ClassF class attributes and methods

# ClassG class attributes and methods

# ClassM class attributes and methods

# ClassN class attributes and methods

# ClassP class attributes and methods

# InterfaceO_Interface class attributes and methods

# ClassQ class attributes and methods

# ClassR class attributes and methods

# ClassS class attributes and methods

# ClassT class attributes and methods

# ClassU class attributes and methods

# ClassV class attributes and methods

# Exception class attributes and methods

# Relationships
ClassD_ClassE: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassE",
    ends={
        Property(name="classE0", type=ClassE, multiplicity=Multiplicity(0, 1)),
        Property(name="classD1", type=ClassD, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopy",
    ends={
        Property(name="classG2", type=ClassG, multiplicity=Multiplicity(0, 1)),
        Property(name="classF3", type=ClassF, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="aa1a269e_ddc2_4683_8626_740b43ab1721",
    types={BankAccount, ErrorCodeException, ErrorCode, ClassD, ClassE, ClassF, ClassG, ClassM, ClassN, ClassP, InterfaceO_Interface, ClassQ, ClassR, ClassS, ClassT, ClassU, ClassV, Exception},
    associations={ClassD_ClassE, ClassD_ClassECopy},
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