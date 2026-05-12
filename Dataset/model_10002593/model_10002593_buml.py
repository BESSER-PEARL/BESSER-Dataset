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
ClassC = Class(name="ClassC")
ElevatorController = Class(name="ElevatorController")
Elevator = Class(name="Elevator")
Door = Class(name="Door")
Button = Class(name="Button")
People = Class(name="People")
Data = Class(name="Data")
Floor_Button = Class(name="Floor_Button")
Elevator_Button = Class(name="Elevator_Button")
Building = Class(name="Building")

# BankAccount class attributes and methods
BankAccount_ownerName: Property = Property(name="ownerName", type=StringType)
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount.attributes={BankAccount_ownerName, BankAccount_balance}

# ClassC class attributes and methods
ClassC_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassC_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassC_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassC_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassC.attributes={ClassC_publicAttribute, ClassC_privateAttribute, ClassC_protectedAttribute, ClassC_packageAttribute}

# ElevatorController class attributes and methods

# Elevator class attributes and methods

# Door class attributes and methods

# Button class attributes and methods

# People class attributes and methods

# Data class attributes and methods

# Floor_Button class attributes and methods

# Elevator_Button class attributes and methods

# Building class attributes and methods

# Relationships
Elevator_Button_Button: BinaryAssociation = BinaryAssociation(
    name="Elevator_Button_Button",
    ends={
        Property(name="Elevator_Button_Button_00", type=Button, multiplicity=Multiplicity(0, 9999)),
        Property(name="elevator_Button1", type=Elevator_Button, multiplicity=Multiplicity(0, 1))
    }
)
Floor_Button_Button: BinaryAssociation = BinaryAssociation(
    name="Floor_Button_Button",
    ends={
        Property(name="button2", type=Button, multiplicity=Multiplicity(0, 1)),
        Property(name="floor_Button3", type=Floor_Button, multiplicity=Multiplicity(0, 1))
    }
)
Button_ElevatorController: BinaryAssociation = BinaryAssociation(
    name="Button_ElevatorController",
    ends={
        Property(name="elevatorController4", type=ElevatorController, multiplicity=Multiplicity(0, 1)),
        Property(name="button5", type=Button, multiplicity=Multiplicity(0, 1))
    }
)
Data_ElevatorController: BinaryAssociation = BinaryAssociation(
    name="Data_ElevatorController",
    ends={
        Property(name="elevatorController6", type=ElevatorController, multiplicity=Multiplicity(0, 1)),
        Property(name="data7", type=Data, multiplicity=Multiplicity(0, 1))
    }
)
Door_ElevatorController: BinaryAssociation = BinaryAssociation(
    name="Door_ElevatorController",
    ends={
        Property(name="elevatorController8", type=ElevatorController, multiplicity=Multiplicity(0, 1)),
        Property(name="door9", type=Door, multiplicity=Multiplicity(0, 1))
    }
)
Elevator_ElevatorController: BinaryAssociation = BinaryAssociation(
    name="Elevator_ElevatorController",
    ends={
        Property(name="elevatorController10", type=ElevatorController, multiplicity=Multiplicity(0, 1)),
        Property(name="elevator11", type=Elevator, multiplicity=Multiplicity(0, 1))
    }
)
People_ElevatorController: BinaryAssociation = BinaryAssociation(
    name="People_ElevatorController",
    ends={
        Property(name="elevatorController12", type=ElevatorController, multiplicity=Multiplicity(0, 1)),
        Property(name="people13", type=People, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c4d04420_5ff8_45da_a9e6_6b9806686e5d",
    types={BankAccount, ClassC, ElevatorController, Elevator, Door, Button, People, Data, Floor_Button, Elevator_Button, Building},
    associations={Elevator_Button_Button, Floor_Button_Button, Button_ElevatorController, Data_ElevatorController, Door_ElevatorController, Elevator_ElevatorController, People_ElevatorController},
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