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
Right_Shoulder = Class(name="Right_Shoulder", is_abstract=True)
Membership_Function = Class(name="Membership_Function", is_abstract=True)
Left_Shoulder = Class(name="Left_Shoulder")
Linear = Class(name="Linear")
Triangular = Class(name="Triangular")
Trapezoidal = Class(name="Trapezoidal")

# Right_Shoulder class attributes and methods

# Membership_Function class attributes and methods
Membership_Function_HasUID: Property = Property(name="HasUID", type=FloatType)
Membership_Function_HasName: Property = Property(name="HasName", type=StringType)
Membership_Function_A: Property = Property(name="A", type=FloatType)
Membership_Function_B: Property = Property(name="B", type=FloatType)
Membership_Function.attributes={Membership_Function_HasUID, Membership_Function_A, Membership_Function_HasName, Membership_Function_B}

# Left_Shoulder class attributes and methods

# Linear class attributes and methods

# Triangular class attributes and methods
Triangular_C: Property = Property(name="C", type=FloatType)
Triangular.attributes={Triangular_C}

# Trapezoidal class attributes and methods
Trapezoidal_D: Property = Property(name="D", type=FloatType)
Trapezoidal_E: Property = Property(name="E", type=FloatType)
Trapezoidal.attributes={Trapezoidal_E, Trapezoidal_D}

# Domain Model
domain_model = DomainModel(
    name="_30159c20_aa76_4dc5_9114_0da0a4008018",
    types={Right_Shoulder, Membership_Function, Left_Shoulder, Linear, Triangular, Trapezoidal},
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