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
y3fsm_Region = Class(name="y3fsm::Region")
AbstractState = Class(name="AbstractState")
y3fsm_AbstractState = Class(name="y3fsm::AbstractState", is_abstract=True)
y3fsm_Foo = Class(name="y3fsm::Foo")

# y3fsm_Region class attributes and methods
y3fsm_Region_name: Property = Property(name="name", type=StringType)
y3fsm_Region.attributes={y3fsm_Region_name}

# AbstractState class attributes and methods

# y3fsm_AbstractState class attributes and methods
y3fsm_AbstractState_id: Property = Property(name="id", type=StringType)
y3fsm_AbstractState.attributes={y3fsm_AbstractState_id}

# y3fsm_Foo class attributes and methods
y3fsm_Foo_zoo: Property = Property(name="zoo", type=StringType)
y3fsm_Foo.attributes={y3fsm_Foo_zoo}

# Relationships
subElements0: BinaryAssociation = BinaryAssociation(
    name="subElements0",
    ends={
        Property(name="y3fsm_AbstractState", type=y3fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="y3fsm_Region", type=y3fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
afooz3: BinaryAssociation = BinaryAssociation(
    name="afooz3",
    ends={
        Property(name="y3fsm_Foo5", type=y3fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="y3fsm_AbstractState4", type=y3fsm_Foo, multiplicity=Multiplicity(0, 9999))
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="y3fsm_Foo", type=y3fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="y3fsm_AbstractState2", type=y3fsm_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_y3fsm_Region_AbstractState = Generalization(general=AbstractState, specific=y3fsm_Region)

# Domain Model
domain_model = DomainModel(
    name="y3fsm",
    types={y3fsm_Region, AbstractState, y3fsm_AbstractState, y3fsm_Foo},
    associations={subElements0, afooz3, foos1},
    generalizations={gen_y3fsm_Region_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)