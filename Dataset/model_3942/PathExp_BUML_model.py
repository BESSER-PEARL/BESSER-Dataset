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
PathExp_Element = Class(name="PathExp::Element", is_abstract=True)
PathExp_PathExp = Class(name="PathExp::PathExp")
Element = Class(name="Element")
State = Class(name="State")
Transition = Class(name="Transition")
PathExp_State = Class(name="PathExp::State")
PathExp_Transition = Class(name="PathExp::Transition")

# PathExp_Element class attributes and methods
PathExp_Element_name: Property = Property(name="name", type=StringType)
PathExp_Element.attributes={PathExp_Element_name}

# PathExp_PathExp class attributes and methods

# Element class attributes and methods

# State class attributes and methods

# Transition class attributes and methods

# PathExp_State class attributes and methods

# PathExp_Transition class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=PathExp_PathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PathExp_PathExp", type=State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=PathExp_PathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PathExp_PathExp2", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="", type=PathExp_State, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="6", type=PathExp_State, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="9", type=PathExp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=State, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="12", type=PathExp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PathExp_PathExp_Element = Generalization(general=Element, specific=PathExp_PathExp)
gen_PathExp_Transition_Element = Generalization(general=Element, specific=PathExp_Transition)

# Domain Model
domain_model = DomainModel(
    name="PathExp",
    types={PathExp_Element, PathExp_PathExp, Element, State, Transition, PathExp_State, PathExp_Transition},
    associations={states0, transitions1, incoming3, outgoing4, source7, target10},
    generalizations={gen_PathExp_PathExp_Element, gen_PathExp_Transition_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)