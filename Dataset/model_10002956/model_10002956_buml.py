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
CoordinateController = Class(name="CoordinateController")
InstrumentController = Class(name="InstrumentController")
MeasurementController = Class(name="MeasurementController")
StatisticsController = Class(name="StatisticsController")
TeamController = Class(name="TeamController")
UserController = Class(name="UserController")
Task_InstrumentUser_ = Class(name="Task_InstrumentUser_")
Task_IEnumerable_User__ = Class(name="Task_IEnumerable_User__")
Task_IEnumerable_Team__ = Class(name="Task_IEnumerable_Team__")
IAccess_T__Interface = Class(name="IAccess_T__Interface")
CoordinateAccess = Class(name="CoordinateAccess")
MeasurementAccess = Class(name="MeasurementAccess")
InstrumentAccess = Class(name="InstrumentAccess")
StatisticsAccess = Class(name="StatisticsAccess")
UserAcces = Class(name="UserAcces")
TeamAccess = Class(name="TeamAccess")
BaseAccess = Class(name="BaseAccess")

# ClassB class attributes and methods

# ClassC class attributes and methods
ClassC_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassC_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassC_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassC_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassC.attributes={ClassC_publicAttribute, ClassC_protectedAttribute, ClassC_packageAttribute, ClassC_privateAttribute}

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

# CoordinateController class attributes and methods

# InstrumentController class attributes and methods

# MeasurementController class attributes and methods

# StatisticsController class attributes and methods

# TeamController class attributes and methods

# UserController class attributes and methods

# Task_InstrumentUser_ class attributes and methods

# Task_IEnumerable_User__ class attributes and methods

# Task_IEnumerable_Team__ class attributes and methods

# IAccess_T__Interface class attributes and methods

# CoordinateAccess class attributes and methods

# MeasurementAccess class attributes and methods

# InstrumentAccess class attributes and methods

# StatisticsAccess class attributes and methods

# UserAcces class attributes and methods

# TeamAccess class attributes and methods

# BaseAccess class attributes and methods

# Relationships
InstrumentController_InstrumentAccess: BinaryAssociation = BinaryAssociation(
    name="InstrumentController_InstrumentAccess",
    ends={
        Property(name="instrumentAccess12", type=InstrumentAccess, multiplicity=Multiplicity(0, 1)),
        Property(name="instrumentController13", type=InstrumentController, multiplicity=Multiplicity(0, 1))
    }
)
CoordinateController_CoordinateAccess: BinaryAssociation = BinaryAssociation(
    name="CoordinateController_CoordinateAccess",
    ends={
        Property(name="coordinateAccess14", type=CoordinateAccess, multiplicity=Multiplicity(0, 1)),
        Property(name="coordinateController15", type=CoordinateController, multiplicity=Multiplicity(0, 1))
    }
)
MeasurementController_MeasurementAccess: BinaryAssociation = BinaryAssociation(
    name="MeasurementController_MeasurementAccess",
    ends={
        Property(name="measurementAccess16", type=MeasurementAccess, multiplicity=Multiplicity(0, 1)),
        Property(name="measurementController17", type=MeasurementController, multiplicity=Multiplicity(0, 1))
    }
)
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
UserController_UserAcces: BinaryAssociation = BinaryAssociation(
    name="UserController_UserAcces",
    ends={
        Property(name="userAcces6", type=UserAcces, multiplicity=Multiplicity(0, 1)),
        Property(name="userController7", type=UserController, multiplicity=Multiplicity(0, 1))
    }
)
TeamController_TeamAccess: BinaryAssociation = BinaryAssociation(
    name="TeamController_TeamAccess",
    ends={
        Property(name="teamAccess8", type=TeamAccess, multiplicity=Multiplicity(0, 1)),
        Property(name="teamController9", type=TeamController, multiplicity=Multiplicity(0, 1))
    }
)
StatisticsController_StatisticsAccess: BinaryAssociation = BinaryAssociation(
    name="StatisticsController_StatisticsAccess",
    ends={
        Property(name="statisticsAccess10", type=StatisticsAccess, multiplicity=Multiplicity(0, 1)),
        Property(name="statisticsController11", type=StatisticsController, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ef45d883_6ce2_4e55_b5c7_a64f245f14a3",
    types={ClassB, ClassC, ClassD, ClassE, ClassF, ClassG, ClassJ, ClassH, ClassK, ClassL, ClassM, ClassN, ClassP, InterfaceO_Interface, ClassQ, ClassR, ClassS, ClassT, ClassU, ClassV, CoordinateController, InstrumentController, MeasurementController, StatisticsController, TeamController, UserController, Task_InstrumentUser_, Task_IEnumerable_User__, Task_IEnumerable_Team__, IAccess_T__Interface, CoordinateAccess, MeasurementAccess, InstrumentAccess, StatisticsAccess, UserAcces, TeamAccess, BaseAccess},
    associations={InstrumentController_InstrumentAccess, CoordinateController_CoordinateAccess, MeasurementController_MeasurementAccess, ClassD_ClassE, ClassD_ClassECopy, ClassD_ClassECopyCopy, UserController_UserAcces, TeamController_TeamAccess, StatisticsController_StatisticsAccess},
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