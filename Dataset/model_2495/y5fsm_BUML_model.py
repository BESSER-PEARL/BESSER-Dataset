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
y5fsm_Region = Class(name="y5fsm::Region")
y5fsm_State = Class(name="y5fsm::State")
y5fsm_Foo = Class(name="y5fsm::Foo")
y5fsm_Bar = Class(name="y5fsm::Bar")

# y5fsm_Region class attributes and methods

# y5fsm_State class attributes and methods
y5fsm_State_id: Property = Property(name="id", type=StringType)
y5fsm_State.attributes={y5fsm_State_id}

# y5fsm_Foo class attributes and methods
y5fsm_Foo_zoo: Property = Property(name="zoo", type=StringType)
y5fsm_Foo.attributes={y5fsm_Foo_zoo}

# y5fsm_Bar class attributes and methods
y5fsm_Bar_baz: Property = Property(name="baz", type=StringType)
y5fsm_Bar.attributes={y5fsm_Bar_baz}

# Relationships
subElements0: BinaryAssociation = BinaryAssociation(
    name="subElements0",
    ends={
        Property(name="y5fsm_State", type=y5fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="y5fsm_Region", type=y5fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="y5fsm_Foo", type=y5fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="y5fsm_State2", type=y5fsm_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars3: BinaryAssociation = BinaryAssociation(
    name="bars3",
    ends={
        Property(name="y5fsm_Bar", type=y5fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="y5fsm_State4", type=y5fsm_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="y5fsm",
    types={y5fsm_Region, y5fsm_State, y5fsm_Foo, y5fsm_Bar},
    associations={subElements0, foos1, bars3},
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