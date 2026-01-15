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
SimpleUML_UmlAssociation = Class(name="SimpleUML::UmlAssociation")
UmlPackageElement = Class(name="UmlPackageElement")
SimpleUML_UmlClass = Class(name="SimpleUML::UmlClass")
SimpleUML_UmlAttribute = Class(name="SimpleUML::UmlAttribute")
UmlModelElement = Class(name="UmlModelElement")
SimpleUML_UmlClassifier = Class(name="SimpleUML::UmlClassifier")
UmlClassifier = Class(name="UmlClassifier")
SimpleUML_UmlModelElement = Class(name="SimpleUML::UmlModelElement")
SimpleUML_UmlPackage = Class(name="SimpleUML::UmlPackage")
SimpleUML_UmlPackageElement = Class(name="SimpleUML::UmlPackageElement")
SimpleUML_UmlPrimitiveDataType = Class(name="SimpleUML::UmlPrimitiveDataType")

# SimpleUML_UmlAssociation class attributes and methods

# UmlPackageElement class attributes and methods

# SimpleUML_UmlClass class attributes and methods

# SimpleUML_UmlAttribute class attributes and methods

# UmlModelElement class attributes and methods

# SimpleUML_UmlClassifier class attributes and methods

# UmlClassifier class attributes and methods

# SimpleUML_UmlModelElement class attributes and methods
SimpleUML_UmlModelElement_umlName: Property = Property(name="umlName", type=StringType)
SimpleUML_UmlModelElement_umlKind: Property = Property(name="umlKind", type=StringType)
SimpleUML_UmlModelElement_id: Property = Property(name="id", type=StringType)
SimpleUML_UmlModelElement.attributes={SimpleUML_UmlModelElement_umlKind, SimpleUML_UmlModelElement_umlName, SimpleUML_UmlModelElement_id}

# SimpleUML_UmlPackage class attributes and methods

# SimpleUML_UmlPackageElement class attributes and methods

# SimpleUML_UmlPrimitiveDataType class attributes and methods

# Relationships
umlReverse7: BinaryAssociation = BinaryAssociation(
    name="umlReverse7",
    ends={
        Property(name="UmlAssociation8", type=SimpleUML_UmlClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlSource", type=SimpleUML_UmlAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
umlAttribute9: BinaryAssociation = BinaryAssociation(
    name="umlAttribute9",
    ends={
        Property(name="UmlAttribute", type=SimpleUML_UmlClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlOwner", type=SimpleUML_UmlAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
umlDestination0: BinaryAssociation = BinaryAssociation(
    name="umlDestination0",
    ends={
        Property(name="UmlClass", type=SimpleUML_UmlAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlForward", type=SimpleUML_UmlClass, multiplicity=Multiplicity(1, 1))
    }
)
umlSource1: BinaryAssociation = BinaryAssociation(
    name="umlSource1",
    ends={
        Property(name="UmlClass2", type=SimpleUML_UmlAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlReverse", type=SimpleUML_UmlClass, multiplicity=Multiplicity(1, 1))
    }
)
umlOwner3: BinaryAssociation = BinaryAssociation(
    name="umlOwner3",
    ends={
        Property(name="UmlClass4", type=SimpleUML_UmlAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="umlAttribute", type=SimpleUML_UmlClass, multiplicity=Multiplicity(0, 1))
    }
)
umlType5: BinaryAssociation = BinaryAssociation(
    name="umlType5",
    ends={
        Property(name="UmlClassifier", type=SimpleUML_UmlAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="umlAttribute1", type=SimpleUML_UmlClassifier, multiplicity=Multiplicity(0, 1))
    }
)
umlForward6: BinaryAssociation = BinaryAssociation(
    name="umlForward6",
    ends={
        Property(name="UmlAssociation", type=SimpleUML_UmlClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlDestination", type=SimpleUML_UmlAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
umlGeneral11: BinaryAssociation = BinaryAssociation(
    name="umlGeneral11",
    ends={
        Property(name="UmlClass12", type=SimpleUML_UmlClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlSpecific", type=SimpleUML_UmlClass, multiplicity=Multiplicity(0, 9999))
    }
)
umlSpecific14: BinaryAssociation = BinaryAssociation(
    name="umlSpecific14",
    ends={
        Property(name="UmlClass15", type=SimpleUML_UmlClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlGeneral", type=SimpleUML_UmlClass, multiplicity=Multiplicity(0, 9999))
    }
)
umlAttribute116: BinaryAssociation = BinaryAssociation(
    name="umlAttribute116",
    ends={
        Property(name="UmlAttribute17", type=SimpleUML_UmlClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlType", type=SimpleUML_UmlAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
umlOwnedElement18: BinaryAssociation = BinaryAssociation(
    name="umlOwnedElement18",
    ends={
        Property(name="UmlPackageElement", type=SimpleUML_UmlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlNamespace", type=SimpleUML_UmlPackageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
umlNamespace19: BinaryAssociation = BinaryAssociation(
    name="umlNamespace19",
    ends={
        Property(name="UmlPackage", type=SimpleUML_UmlPackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlOwnedElement", type=SimpleUML_UmlPackage, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_SimpleUML_UmlAssociation_UmlPackageElement = Generalization(general=UmlPackageElement, specific=SimpleUML_UmlAssociation)
gen_SimpleUML_UmlAttribute_UmlModelElement = Generalization(general=UmlModelElement, specific=SimpleUML_UmlAttribute)
gen_SimpleUML_UmlClass_UmlClassifier = Generalization(general=UmlClassifier, specific=SimpleUML_UmlClass)
gen_SimpleUML_UmlClassifier_UmlPackageElement = Generalization(general=UmlPackageElement, specific=SimpleUML_UmlClassifier)
gen_SimpleUML_UmlPackage_UmlModelElement = Generalization(general=UmlModelElement, specific=SimpleUML_UmlPackage)
gen_SimpleUML_UmlPackageElement_UmlModelElement = Generalization(general=UmlModelElement, specific=SimpleUML_UmlPackageElement)
gen_SimpleUML_UmlPrimitiveDataType_UmlClassifier = Generalization(general=UmlClassifier, specific=SimpleUML_UmlPrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="SimpleUML",
    types={SimpleUML_UmlAssociation, UmlPackageElement, SimpleUML_UmlClass, SimpleUML_UmlAttribute, UmlModelElement, SimpleUML_UmlClassifier, UmlClassifier, SimpleUML_UmlModelElement, SimpleUML_UmlPackage, SimpleUML_UmlPackageElement, SimpleUML_UmlPrimitiveDataType},
    associations={umlReverse7, umlAttribute9, umlDestination0, umlSource1, umlOwner3, umlType5, umlForward6, umlGeneral11, umlSpecific14, umlAttribute116, umlOwnedElement18, umlNamespace19},
    generalizations={gen_SimpleUML_UmlAssociation_UmlPackageElement, gen_SimpleUML_UmlAttribute_UmlModelElement, gen_SimpleUML_UmlClass_UmlClassifier, gen_SimpleUML_UmlClassifier_UmlPackageElement, gen_SimpleUML_UmlPackage_UmlModelElement, gen_SimpleUML_UmlPackageElement_UmlModelElement, gen_SimpleUML_UmlPrimitiveDataType_UmlClassifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)