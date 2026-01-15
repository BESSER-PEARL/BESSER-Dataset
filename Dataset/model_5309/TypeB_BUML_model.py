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
TypeB_SubElement = Class(name="TypeB::SubElement")
TypeB_AnotherElement = Class(name="TypeB::AnotherElement")
TypeB_ListElement = Class(name="TypeB::ListElement")
Element = Class(name="Element")
ElementX = Class(name="ElementX")
ElementR = Class(name="ElementR")
TypeB_Element = Class(name="TypeB::Element")
TypeB_ElementX = Class(name="TypeB::ElementX")
TypeB_ElementY = Class(name="TypeB::ElementY")
TypeB_ElementR = Class(name="TypeB::ElementR")
TypeB_ElementS = Class(name="TypeB::ElementS")

# TypeB_SubElement class attributes and methods
TypeB_SubElement_additionalField: Property = Property(name="additionalField", type=StringType)
TypeB_SubElement.attributes={TypeB_SubElement_additionalField}

# TypeB_AnotherElement class attributes and methods
TypeB_AnotherElement_abstractBaseName: Property = Property(name="abstractBaseName", type=StringType)
TypeB_AnotherElement_nameElement: Property = Property(name="nameElement", type=StringType)
TypeB_AnotherElement_type: Property = Property(name="type", type=StringType)
TypeB_AnotherElement_additionalField: Property = Property(name="additionalField", type=StringType)
TypeB_AnotherElement.attributes={TypeB_AnotherElement_type, TypeB_AnotherElement_additionalField, TypeB_AnotherElement_abstractBaseName, TypeB_AnotherElement_nameElement}

# TypeB_ListElement class attributes and methods
TypeB_ListElement_nameListElement: Property = Property(name="nameListElement", type=StringType)
TypeB_ListElement.attributes={TypeB_ListElement_nameListElement}

# Element class attributes and methods

# ElementX class attributes and methods

# ElementR class attributes and methods

# TypeB_Element class attributes and methods
TypeB_Element_nameElement: Property = Property(name="nameElement", type=StringType)
TypeB_Element_type: Property = Property(name="type", type=StringType)
TypeB_Element_abstractBaseName: Property = Property(name="abstractBaseName", type=StringType)
TypeB_Element.attributes={TypeB_Element_abstractBaseName, TypeB_Element_nameElement, TypeB_Element_type}

# TypeB_ElementX class attributes and methods
TypeB_ElementX_nameX: Property = Property(name="nameX", type=StringType)
TypeB_ElementX.attributes={TypeB_ElementX_nameX}

# TypeB_ElementY class attributes and methods
TypeB_ElementY_nameY: Property = Property(name="nameY", type=StringType)
TypeB_ElementY.attributes={TypeB_ElementY_nameY}

# TypeB_ElementR class attributes and methods
TypeB_ElementR_nameR: Property = Property(name="nameR", type=StringType)
TypeB_ElementR.attributes={TypeB_ElementR_nameR}

# TypeB_ElementS class attributes and methods
TypeB_ElementS_nameS: Property = Property(name="nameS", type=StringType)
TypeB_ElementS.attributes={TypeB_ElementS_nameS}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Element", type=TypeB_ListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_ListElement", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xyElements1: BinaryAssociation = BinaryAssociation(
    name="xyElements1",
    ends={
        Property(name="ElementX", type=TypeB_ListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_ListElement2", type=ElementX, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rsElements3: BinaryAssociation = BinaryAssociation(
    name="rsElements3",
    ends={
        Property(name="ElementR", type=TypeB_ListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_ListElement4", type=ElementR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_TypeB_SubElement_Element = Generalization(general=Element, specific=TypeB_SubElement)
gen_TypeB_ElementY_ElementX = Generalization(general=ElementX, specific=TypeB_ElementY)
gen_TypeB_ElementS_ElementR = Generalization(general=ElementR, specific=TypeB_ElementS)

# Domain Model
domain_model = DomainModel(
    name="TypeB",
    types={TypeB_SubElement, TypeB_AnotherElement, TypeB_ListElement, Element, ElementX, ElementR, TypeB_Element, TypeB_ElementX, TypeB_ElementY, TypeB_ElementR, TypeB_ElementS},
    associations={elements0, xyElements1, rsElements3},
    generalizations={gen_TypeB_SubElement_Element, gen_TypeB_ElementY_ElementX, gen_TypeB_ElementS_ElementR},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)