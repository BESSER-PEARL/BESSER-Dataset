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
y4fsm_Region = Class(name="y4fsm::Region")
State = Class(name="State")
y4fsm_Foo = Class(name="y4fsm::Foo")
y4fsm_Bar = Class(name="y4fsm::Bar")
y4fsm_State = Class(name="y4fsm::State", is_abstract=True)

# y4fsm_Region class attributes and methods
y4fsm_Region_name: Property = Property(name="name", type=StringType)
y4fsm_Region.attributes={y4fsm_Region_name}

# State class attributes and methods

# y4fsm_Foo class attributes and methods
y4fsm_Foo_zoo: Property = Property(name="zoo", type=StringType)
y4fsm_Foo.attributes={y4fsm_Foo_zoo}

# y4fsm_Bar class attributes and methods
y4fsm_Bar_baz: Property = Property(name="baz", type=StringType)
y4fsm_Bar.attributes={y4fsm_Bar_baz}

# y4fsm_State class attributes and methods
y4fsm_State_id: Property = Property(name="id", type=StringType)
y4fsm_State.attributes={y4fsm_State_id}

# Relationships
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="y4fsm_Foo", type=y4fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="y4fsm_State2", type=y4fsm_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars3: BinaryAssociation = BinaryAssociation(
    name="bars3",
    ends={
        Property(name="y4fsm_Bar", type=y4fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="y4fsm_State4", type=y4fsm_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subElements0: BinaryAssociation = BinaryAssociation(
    name="subElements0",
    ends={
        Property(name="y4fsm_State", type=y4fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="y4fsm_Region", type=y4fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_y4fsm_Region_State = Generalization(general=State, specific=y4fsm_Region)

# Domain Model
domain_model = DomainModel(
    name="y4fsm",
    types={y4fsm_Region, State, y4fsm_Foo, y4fsm_Bar, y4fsm_State},
    associations={foos1, bars3, subElements0},
    generalizations={gen_y4fsm_Region_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)