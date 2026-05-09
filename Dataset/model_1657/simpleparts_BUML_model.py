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
simpleparts_Part = Class(name="simpleparts_Part")
simpleparts_Element = Class(name="simpleparts_Element")
simpleparts_Item = Class(name="simpleparts_Item")
simpleparts_Piece = Class(name="simpleparts_Piece")
simpleparts_NamedElement = Class(name="simpleparts_NamedElement", is_abstract=True)
simpleparts_World = Class(name="simpleparts_World")
simpleparts_Thing = Class(name="simpleparts_Thing")
NamedElement = Class(name="NamedElement")
simpleparts_RelatedTo = Class(name="simpleparts_RelatedTo")

# simpleparts_Part class attributes and methods

# simpleparts_Element class attributes and methods

# simpleparts_Item class attributes and methods

# simpleparts_Piece class attributes and methods

# simpleparts_NamedElement class attributes and methods
simpleparts_NamedElement_name: Property = Property(name="name", type=StringType)
simpleparts_NamedElement.attributes={simpleparts_NamedElement_name}

# simpleparts_World class attributes and methods

# simpleparts_Thing class attributes and methods
simpleparts_Thing_id: Property = Property(name="id", type=IntegerType)
simpleparts_Thing.attributes={simpleparts_Thing_id}

# NamedElement class attributes and methods

# simpleparts_RelatedTo class attributes and methods
simpleparts_RelatedTo_since: Property = Property(name="since", type=StringType)
simpleparts_RelatedTo.attributes={simpleparts_RelatedTo_since}

# Relationships
parts2: BinaryAssociation = BinaryAssociation(
    name="parts2",
    ends={
        Property(name="simpleparts_Part", type=simpleparts_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleparts_Thing3", type=simpleparts_Part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="simpleparts_Element", type=simpleparts_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleparts_Thing5", type=simpleparts_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items6: BinaryAssociation = BinaryAssociation(
    name="items6",
    ends={
        Property(name="simpleparts_Item", type=simpleparts_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleparts_Thing7", type=simpleparts_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pieces8: BinaryAssociation = BinaryAssociation(
    name="pieces8",
    ends={
        Property(name="simpleparts_Piece", type=simpleparts_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleparts_Thing9", type=simpleparts_Piece, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing10: BinaryAssociation = BinaryAssociation(
    name="fromThing10",
    ends={
        Property(name="Thing", type=simpleparts_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=simpleparts_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing11: BinaryAssociation = BinaryAssociation(
    name="toThing11",
    ends={
        Property(name="simpleparts_Thing12", type=simpleparts_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleparts_RelatedTo", type=simpleparts_Thing, multiplicity=Multiplicity(0, 1))
    }
)
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="simpleparts_Thing", type=simpleparts_World, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleparts_World", type=simpleparts_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=simpleparts_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=simpleparts_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part13: BinaryAssociation = BinaryAssociation(
    name="part13",
    ends={
        Property(name="simpleparts_Part15", type=simpleparts_Piece, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleparts_Piece14", type=simpleparts_Part, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simpleparts_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=simpleparts_RelatedTo)
gen_simpleparts_Part_NamedElement = Generalization(general=NamedElement, specific=simpleparts_Part)
gen_simpleparts_Element_NamedElement = Generalization(general=NamedElement, specific=simpleparts_Element)
gen_simpleparts_Item_NamedElement = Generalization(general=NamedElement, specific=simpleparts_Item)
gen_simpleparts_Piece_NamedElement = Generalization(general=NamedElement, specific=simpleparts_Piece)
gen_simpleparts_Thing_NamedElement = Generalization(general=NamedElement, specific=simpleparts_Thing)

# Domain Model
domain_model = DomainModel(
    name="simpleparts",
    types={simpleparts_Part, simpleparts_Element, simpleparts_Item, simpleparts_Piece, simpleparts_NamedElement, simpleparts_World, simpleparts_Thing, NamedElement, simpleparts_RelatedTo},
    associations={parts2, elements4, items6, pieces8, fromThing10, toThing11, things0, relations1, part13},
    generalizations={gen_simpleparts_RelatedTo_NamedElement, gen_simpleparts_Part_NamedElement, gen_simpleparts_Element_NamedElement, gen_simpleparts_Item_NamedElement, gen_simpleparts_Piece_NamedElement, gen_simpleparts_Thing_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)