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
PathExp = Class(name="PathExp")
PathExp_Transition = Class(name="PathExp::Transition")
PathExp_Element = Class(name="PathExp::Element", is_abstract=True)
PathExp_PathExp = Class(name="PathExp::PathExp")
Element = Class(name="Element")
State = Class(name="State")
Transition = Class(name="Transition")
PathExp_State = Class(name="PathExp::State")
PathExp_NonReferencedClass = Class(name="PathExp::NonReferencedClass")

# PathExp class attributes and methods

# PathExp_Transition class attributes and methods

# PathExp_Element class attributes and methods
PathExp_Element_name: Property = Property(name="name", type=StringType)
PathExp_Element.attributes={PathExp_Element_name}

# PathExp_PathExp class attributes and methods

# Element class attributes and methods

# State class attributes and methods

# Transition class attributes and methods

# PathExp_State class attributes and methods

# PathExp_NonReferencedClass class attributes and methods

# Relationships
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="06", type=Transition, multiplicity=Multiplicity(0, 9999)),
        Property(name="#7", type=PathExp_State, multiplicity=Multiplicity(1, 1))
    }
)
owner8: BinaryAssociation = BinaryAssociation(
    name="owner8",
    ends={
        Property(name="#10", type=PathExp_State, multiplicity=Multiplicity(1, 1)),
        Property(name="09", type=PathExp, multiplicity=Multiplicity(1, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="#13", type=PathExp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="012", type=State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="#", type=PathExp_PathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=PathExp_PathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PathExp_PathExp", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="#4", type=PathExp_State, multiplicity=Multiplicity(1, 1)),
        Property(name="03", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="#16", type=PathExp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="015", type=State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PathExp_Transition_Element = Generalization(general=Element, specific=PathExp_Transition)
gen_PathExp_PathExp_Element = Generalization(general=Element, specific=PathExp_PathExp)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PathExp, PathExp_Transition, PathExp_Element, PathExp_PathExp, Element, State, Transition, PathExp_State, PathExp_NonReferencedClass},
    associations={outgoing5, owner8, source11, states0, transitions1, incoming2, target14},
    generalizations={gen_PathExp_Transition_Element, gen_PathExp_PathExp_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)