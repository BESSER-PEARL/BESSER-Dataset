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
PathExp_Element = Class(name="PathExp_Element", is_abstract=True)
PathExp_PathExp = Class(name="PathExp_PathExp")
Element = Class(name="Element")
State = Class(name="State")
Transition = Class(name="Transition")
PathExp_State = Class(name="PathExp_State", is_abstract=True)
PathExp = Class(name="PathExp")
PathExp_Transition = Class(name="PathExp_Transition")
PathExp_Bool_attrElement = Class(name="PathExp_Bool_attrElement", is_abstract=True)
PathExp_Initial = Class(name="PathExp_Initial")
Bool_attrElement = Class(name="Bool_attrElement")
PathExp_Final = Class(name="PathExp_Final")
PathExp_Internal = Class(name="PathExp_Internal")

# PathExp_Element class attributes and methods
PathExp_Element_name: Property = Property(name="name", type=StringType)
PathExp_Element.attributes={PathExp_Element_name}

# PathExp_PathExp class attributes and methods

# Element class attributes and methods

# State class attributes and methods

# Transition class attributes and methods

# PathExp_State class attributes and methods

# PathExp class attributes and methods

# PathExp_Transition class attributes and methods

# PathExp_Bool_attrElement class attributes and methods
PathExp_Bool_attrElement_bool_attr: Property = Property(name="bool_attr", type=BooleanType)
PathExp_Bool_attrElement.attributes={PathExp_Bool_attrElement_bool_attr}

# PathExp_Initial class attributes and methods

# Bool_attrElement class attributes and methods

# PathExp_Final class attributes and methods

# PathExp_Internal class attributes and methods
PathExp_Internal_attr: Property = Property(name="attr", type=IntegerType)
PathExp_Internal.attributes={PathExp_Internal_attr}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=PathExp_PathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=State, multiplicity=Multiplicity(1, 9999), is_composite=True)
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
        Property(name="Transition3", type=PathExp_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=PathExp_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
owner6: BinaryAssociation = BinaryAssociation(
    name="owner6",
    ends={
        Property(name="PathExp", type=PathExp_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=PathExp, multiplicity=Multiplicity(1, 1))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="State8", type=PathExp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=State, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="State10", type=PathExp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PathExp_PathExp_Element = Generalization(general=Element, specific=PathExp_PathExp)
gen_PathExp_Transition_Element = Generalization(general=Element, specific=PathExp_Transition)
gen_PathExp_Initial_State = Generalization(general=State, specific=PathExp_Initial)
gen_PathExp_Initial_Bool_attrElement = Generalization(general=Bool_attrElement, specific=PathExp_Initial)
gen_PathExp_Final_State = Generalization(general=State, specific=PathExp_Final)
gen_PathExp_Final_Bool_attrElement = Generalization(general=Bool_attrElement, specific=PathExp_Final)
gen_PathExp_Internal_State = Generalization(general=State, specific=PathExp_Internal)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PathExp_Element, PathExp_PathExp, Element, State, Transition, PathExp_State, PathExp, PathExp_Transition, PathExp_Bool_attrElement, PathExp_Initial, Bool_attrElement, PathExp_Final, PathExp_Internal},
    associations={states0, transitions1, incoming2, outgoing4, owner6, source7, target9},
    generalizations={gen_PathExp_PathExp_Element, gen_PathExp_Transition_Element, gen_PathExp_Initial_State, gen_PathExp_Initial_Bool_attrElement, gen_PathExp_Final_State, gen_PathExp_Final_Bool_attrElement, gen_PathExp_Internal_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)