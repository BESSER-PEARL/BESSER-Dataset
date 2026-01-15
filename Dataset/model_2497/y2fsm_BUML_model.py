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
y2fsm_AbstractState = Class(name="y2fsm::AbstractState", is_abstract=True)
y2fsm_Foo = Class(name="y2fsm::Foo")
y2fsm_Region = Class(name="y2fsm::Region")
AbstractState = Class(name="AbstractState")

# y2fsm_AbstractState class attributes and methods
y2fsm_AbstractState_id: Property = Property(name="id", type=StringType)
y2fsm_AbstractState.attributes={y2fsm_AbstractState_id}

# y2fsm_Foo class attributes and methods
y2fsm_Foo_id: Property = Property(name="id", type=StringType)
y2fsm_Foo.attributes={y2fsm_Foo_id}

# y2fsm_Region class attributes and methods
y2fsm_Region_name: Property = Property(name="name", type=StringType)
y2fsm_Region.attributes={y2fsm_Region_name}

# AbstractState class attributes and methods

# Relationships
subElements0: BinaryAssociation = BinaryAssociation(
    name="subElements0",
    ends={
        Property(name="y2fsm_AbstractState", type=y2fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="y2fsm_Region", type=y2fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="y2fsm_Foo", type=y2fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="y2fsm_Region2", type=y2fsm_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foo3: BinaryAssociation = BinaryAssociation(
    name="foo3",
    ends={
        Property(name="y2fsm_Foo5", type=y2fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="y2fsm_AbstractState4", type=y2fsm_Foo, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_y2fsm_Region_AbstractState = Generalization(general=AbstractState, specific=y2fsm_Region)

# Domain Model
domain_model = DomainModel(
    name="y2fsm",
    types={y2fsm_AbstractState, y2fsm_Foo, y2fsm_Region, AbstractState},
    associations={subElements0, foos1, foo3},
    generalizations={gen_y2fsm_Region_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)