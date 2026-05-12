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
Car = Class(name="Car", is_abstract=True)
Tennis = Class(name="Tennis")
Engine = Class(name="Engine")
M6 = Class(name="M6")
TestStand = Class(name="TestStand")
Test = Class(name="Test")

# Car class attributes and methods

# Tennis class attributes and methods
Tennis_manufacturer: Property = Property(name="manufacturer", type=StringType)
Tennis_color: Property = Property(name="color", type=StringType)
Tennis_engine: Property = Property(name="engine", type=Engine)
Tennis.attributes={Tennis_engine, Tennis_color, Tennis_manufacturer}

# Engine class attributes and methods
Engine_type: Property = Property(name="type", type=StringType)
Engine_efficiencyCoefficient: Property = Property(name="efficiencyCoefficient", type=IntegerType)
Engine_engineSpeed: Property = Property(name="engineSpeed", type=IntegerType)
Engine.attributes={Engine_efficiencyCoefficient, Engine_engineSpeed, Engine_type}

# M6 class attributes and methods
M6_manufacturer: Property = Property(name="manufacturer", type=StringType)
M6_color: Property = Property(name="color", type=StringType)
M6_engine: Property = Property(name="engine", type=Engine)
M6.attributes={M6_manufacturer, M6_engine, M6_color}

# TestStand class attributes and methods
TestStand_carToBeTested: Property = Property(name="carToBeTested", type=Car)
TestStand.attributes={TestStand_carToBeTested}

# Test class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_bB4QkBdGEemVbcpIjcQyug",
    types={Car, Tennis, Engine, M6, TestStand, Test},
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