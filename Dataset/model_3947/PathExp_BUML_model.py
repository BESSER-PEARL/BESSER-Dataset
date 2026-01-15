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
PathExp_PathExp = Class(name="PathExp::PathExp")
Element = Class(name="Element")
State = Class(name="State")
Transition = Class(name="Transition")
PathExp_State = Class(name="PathExp::State", is_abstract=True)
PathExp = Class(name="PathExp")
PathExp_Element = Class(name="PathExp::Element", is_abstract=True)
PathExp_Transition = Class(name="PathExp::Transition")
PathExp_Initial = Class(name="PathExp::Initial")
PathExp_Final = Class(name="PathExp::Final")
PathExp_Internal = Class(name="PathExp::Internal")

# PathExp_PathExp class attributes and methods

# Element class attributes and methods

# State class attributes and methods

# Transition class attributes and methods

# PathExp_State class attributes and methods

# PathExp class attributes and methods

# PathExp_Element class attributes and methods
PathExp_Element_name: Property = Property(name="name", type=StringType)
PathExp_Element.attributes={PathExp_Element_name}

# PathExp_Transition class attributes and methods

# PathExp_Initial class attributes and methods
PathExp_Initial_bool_attr: Property = Property(name="bool_attr", type=BooleanType)
PathExp_Initial.attributes={PathExp_Initial_bool_attr}

# PathExp_Final class attributes and methods
PathExp_Final_bool_attr: Property = Property(name="bool_attr", type=BooleanType)
PathExp_Final.attributes={PathExp_Final_bool_attr}

# PathExp_Internal class attributes and methods
PathExp_Internal_attr: Property = Property(name="attr", type=IntegerType)
PathExp_Internal.attributes={PathExp_Internal_attr}

# Relationships
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
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="#7", type=PathExp_State, multiplicity=Multiplicity(1, 1)),
        Property(name="06", type=Transition, multiplicity=Multiplicity(0, 9999))
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
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="#16", type=PathExp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="015", type=State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PathExp_PathExp_Element = Generalization(general=Element, specific=PathExp_PathExp)
gen_PathExp_Transition_Element = Generalization(general=Element, specific=PathExp_Transition)
gen_PathExp_Initial_State = Generalization(general=State, specific=PathExp_Initial)
gen_PathExp_Final_State = Generalization(general=State, specific=PathExp_Final)
gen_PathExp_Internal_State = Generalization(general=State, specific=PathExp_Internal)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PathExp_PathExp, Element, State, Transition, PathExp_State, PathExp, PathExp_Element, PathExp_Transition, PathExp_Initial, PathExp_Final, PathExp_Internal},
    associations={states0, transitions1, incoming2, outgoing5, owner8, source11, target14},
    generalizations={gen_PathExp_PathExp_Element, gen_PathExp_Transition_Element, gen_PathExp_Initial_State, gen_PathExp_Final_State, gen_PathExp_Internal_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)