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
classDiagram_UMLAssoc = Class(name="classDiagram::UMLAssoc")
UMLDiagramItem = Class(name="UMLDiagramItem")
classDiagram_UMLRole = Class(name="classDiagram::UMLRole")
classDiagram_UMLCardinality = Class(name="classDiagram::UMLCardinality")
UMLIncrement = Class(name="UMLIncrement")
classDiagram_UMLClassDiagram = Class(name="classDiagram::UMLClassDiagram")
UMLElement = Class(name="UMLElement")
classDiagram_UMLElement = Class(name="classDiagram::UMLElement", is_abstract=True)
classDiagram_UMLClass = Class(name="classDiagram::UMLClass")
classDiagram_UMLDiagramItem = Class(name="classDiagram::UMLDiagramItem", is_abstract=True)
classDiagram_UMLIncrement = Class(name="classDiagram::UMLIncrement", is_abstract=True)
classDiagram_UMLStereotype = Class(name="classDiagram::UMLStereotype")

# classDiagram_UMLAssoc class attributes and methods

# UMLDiagramItem class attributes and methods

# classDiagram_UMLRole class attributes and methods
classDiagram_UMLRole_adornment: Property = Property(name="adornment", type=StringType)
classDiagram_UMLRole.attributes={classDiagram_UMLRole_adornment}

# classDiagram_UMLCardinality class attributes and methods
classDiagram_UMLCardinality_cardString: Property = Property(name="cardString", type=StringType)
classDiagram_UMLCardinality.attributes={classDiagram_UMLCardinality_cardString}

# UMLIncrement class attributes and methods

# classDiagram_UMLClassDiagram class attributes and methods

# UMLElement class attributes and methods

# classDiagram_UMLElement class attributes and methods
classDiagram_UMLElement_name: Property = Property(name="name", type=StringType)
classDiagram_UMLElement.attributes={classDiagram_UMLElement_name}

# classDiagram_UMLClass class attributes and methods

# classDiagram_UMLDiagramItem class attributes and methods

# classDiagram_UMLIncrement class attributes and methods

# classDiagram_UMLStereotype class attributes and methods
classDiagram_UMLStereotype_text: Property = Property(name="text", type=StringType)
classDiagram_UMLStereotype.attributes={classDiagram_UMLStereotype_text}

# Relationships
leftRole0: BinaryAssociation = BinaryAssociation(
    name="leftRole0",
    ends={
        Property(name="UMLRole", type=classDiagram_UMLAssoc, multiplicity=Multiplicity(1, 1)),
        Property(name="revLeftRole", type=classDiagram_UMLRole, multiplicity=Multiplicity(0, 1))
    }
)
rightRole1: BinaryAssociation = BinaryAssociation(
    name="rightRole1",
    ends={
        Property(name="UMLRole2", type=classDiagram_UMLAssoc, multiplicity=Multiplicity(1, 1)),
        Property(name="revRightRole", type=classDiagram_UMLRole, multiplicity=Multiplicity(0, 1))
    }
)
revCard3: BinaryAssociation = BinaryAssociation(
    name="revCard3",
    ends={
        Property(name="UMLRole4", type=classDiagram_UMLCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="card", type=classDiagram_UMLRole, multiplicity=Multiplicity(0, 1))
    }
)
elements5: BinaryAssociation = BinaryAssociation(
    name="elements5",
    ends={
        Property(name="UMLElement", type=classDiagram_UMLClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=classDiagram_UMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles6: BinaryAssociation = BinaryAssociation(
    name="roles6",
    ends={
        Property(name="UMLRole7", type=classDiagram_UMLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=classDiagram_UMLRole, multiplicity=Multiplicity(0, 9999))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="UMLClass", type=classDiagram_UMLRole, multiplicity=Multiplicity(1, 1)),
        Property(name="roles", type=classDiagram_UMLClass, multiplicity=Multiplicity(0, 1))
    }
)
increment15: BinaryAssociation = BinaryAssociation(
    name="increment15",
    ends={
        Property(name="UMLIncrement", type=classDiagram_UMLStereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypes", type=classDiagram_UMLIncrement, multiplicity=Multiplicity(0, 1))
    }
)
diagram8: BinaryAssociation = BinaryAssociation(
    name="diagram8",
    ends={
        Property(name="UMLClassDiagram", type=classDiagram_UMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=classDiagram_UMLClassDiagram, multiplicity=Multiplicity(0, 1))
    }
)
stereotypes9: BinaryAssociation = BinaryAssociation(
    name="stereotypes9",
    ends={
        Property(name="UMLStereotype", type=classDiagram_UMLIncrement, multiplicity=Multiplicity(1, 1)),
        Property(name="increment", type=classDiagram_UMLStereotype, multiplicity=Multiplicity(0, 9999))
    }
)
card10: BinaryAssociation = BinaryAssociation(
    name="card10",
    ends={
        Property(name="UMLCardinality", type=classDiagram_UMLRole, multiplicity=Multiplicity(1, 1)),
        Property(name="revCard", type=classDiagram_UMLCardinality, multiplicity=Multiplicity(0, 1))
    }
)
revLeftRole11: BinaryAssociation = BinaryAssociation(
    name="revLeftRole11",
    ends={
        Property(name="UMLAssoc", type=classDiagram_UMLRole, multiplicity=Multiplicity(1, 1)),
        Property(name="leftRole", type=classDiagram_UMLAssoc, multiplicity=Multiplicity(0, 1))
    }
)
revRightRole12: BinaryAssociation = BinaryAssociation(
    name="revRightRole12",
    ends={
        Property(name="UMLAssoc13", type=classDiagram_UMLRole, multiplicity=Multiplicity(1, 1)),
        Property(name="rightRole", type=classDiagram_UMLAssoc, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classDiagram_UMLAssoc_UMLDiagramItem = Generalization(general=UMLDiagramItem, specific=classDiagram_UMLAssoc)
gen_classDiagram_UMLCardinality_UMLIncrement = Generalization(general=UMLIncrement, specific=classDiagram_UMLCardinality)
gen_classDiagram_UMLClassDiagram_UMLElement = Generalization(general=UMLElement, specific=classDiagram_UMLClassDiagram)
gen_classDiagram_UMLClass_UMLDiagramItem = Generalization(general=UMLDiagramItem, specific=classDiagram_UMLClass)
gen_classDiagram_UMLDiagramItem_UMLIncrement = Generalization(general=UMLIncrement, specific=classDiagram_UMLDiagramItem)
gen_classDiagram_UMLStereotype_UMLIncrement = Generalization(general=UMLIncrement, specific=classDiagram_UMLStereotype)
gen_classDiagram_UMLIncrement_UMLElement = Generalization(general=UMLElement, specific=classDiagram_UMLIncrement)
gen_classDiagram_UMLRole_UMLIncrement = Generalization(general=UMLIncrement, specific=classDiagram_UMLRole)

# Domain Model
domain_model = DomainModel(
    name="classDiagram",
    types={classDiagram_UMLAssoc, UMLDiagramItem, classDiagram_UMLRole, classDiagram_UMLCardinality, UMLIncrement, classDiagram_UMLClassDiagram, UMLElement, classDiagram_UMLElement, classDiagram_UMLClass, classDiagram_UMLDiagramItem, classDiagram_UMLIncrement, classDiagram_UMLStereotype},
    associations={leftRole0, rightRole1, revCard3, elements5, roles6, target14, increment15, diagram8, stereotypes9, card10, revLeftRole11, revRightRole12},
    generalizations={gen_classDiagram_UMLAssoc_UMLDiagramItem, gen_classDiagram_UMLCardinality_UMLIncrement, gen_classDiagram_UMLClassDiagram_UMLElement, gen_classDiagram_UMLClass_UMLDiagramItem, gen_classDiagram_UMLDiagramItem_UMLIncrement, gen_classDiagram_UMLStereotype_UMLIncrement, gen_classDiagram_UMLIncrement_UMLElement, gen_classDiagram_UMLRole_UMLIncrement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)