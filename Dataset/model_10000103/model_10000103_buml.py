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
UserBean = Class(name="UserBean")
ClassA = Class(name="ClassA")
ClassB = Class(name="ClassB")
ClassC = Class(name="ClassC")
ClassD = Class(name="ClassD")
ClassE = Class(name="ClassE")
ClassF = Class(name="ClassF")
ClassG = Class(name="ClassG")
ClassJ = Class(name="ClassJ")
ClassH = Class(name="ClassH")
ClassK = Class(name="ClassK")
ClassL = Class(name="ClassL")
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

# UserBean class attributes and methods
UserBean_username: Property = Property(name="username", type=StringType)
UserBean_pass: Property = Property(name="pass", type=StringType)
UserBean_email: Property = Property(name="email", type=StringType)
UserBean_company: Property = Property(name="company", type=StringType)
UserBean_registration_date: Property = Property(name="registration_date", type=StringType)
UserBean_valid: Property = Property(name="valid", type=BooleanType)
UserBean.attributes={UserBean_email, UserBean_registration_date, UserBean_valid, UserBean_username, UserBean_pass, UserBean_company}

# ClassA class attributes and methods
ClassA_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassA_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassA_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassA_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassA.attributes={ClassA_packageAttribute, ClassA_privateAttribute, ClassA_protectedAttribute, ClassA_publicAttribute}

# ClassB class attributes and methods

# ClassC class attributes and methods
ClassC_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassC_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassC_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassC_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassC.attributes={ClassC_publicAttribute, ClassC_privateAttribute, ClassC_protectedAttribute, ClassC_packageAttribute}

# ClassD class attributes and methods

# ClassE class attributes and methods

# ClassF class attributes and methods

# ClassG class attributes and methods

# ClassJ class attributes and methods

# ClassH class attributes and methods

# ClassK class attributes and methods

# ClassL class attributes and methods

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
ClassD_ClassECopyCopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopyCopy",
    ends={
        Property(name="classG4", type=ClassJ, multiplicity=Multiplicity(0, 1)),
        Property(name="classF5", type=ClassH, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0df155ef_8383_4fe2_9449_346ce7fa6dcf",
    types={UserBean, ClassA, ClassB, ClassC, ClassD, ClassE, ClassF, ClassG, ClassJ, ClassH, ClassK, ClassL, ClassM, ClassN, ClassP, InterfaceO_Interface, ClassQ, ClassR, ClassS, ClassT, ClassU, ClassV},
    associations={ClassD_ClassE, ClassD_ClassECopy, ClassD_ClassECopyCopy},
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