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
SimpleUML_Classifier = Class(name="SimpleUML::Classifier")
PackageElement = Class(name="PackageElement")
SimpleUML_Attribute = Class(name="SimpleUML::Attribute")
UMLModelElement = Class(name="UMLModelElement")
SimpleUML_Class = Class(name="SimpleUML::Class")
Classifier = Class(name="Classifier")
SimpleUML_Association = Class(name="SimpleUML::Association")
SimpleUML_PrimitiveDataType = Class(name="SimpleUML::PrimitiveDataType")
SimpleUML_UMLModelElement = Class(name="SimpleUML::UMLModelElement", is_abstract=True)
SimpleUML_Package = Class(name="SimpleUML::Package")
SimpleUML_PackageElement = Class(name="SimpleUML::PackageElement")

# SimpleUML_Classifier class attributes and methods

# PackageElement class attributes and methods

# SimpleUML_Attribute class attributes and methods

# UMLModelElement class attributes and methods

# SimpleUML_Class class attributes and methods

# Classifier class attributes and methods

# SimpleUML_Association class attributes and methods

# SimpleUML_PrimitiveDataType class attributes and methods

# SimpleUML_UMLModelElement class attributes and methods
SimpleUML_UMLModelElement_kind: Property = Property(name="kind", type=StringType)
SimpleUML_UMLModelElement_name: Property = Property(name="name", type=StringType)
SimpleUML_UMLModelElement.attributes={SimpleUML_UMLModelElement_name, SimpleUML_UMLModelElement_kind}

# SimpleUML_Package class attributes and methods

# SimpleUML_PackageElement class attributes and methods

# Relationships
namespace13: BinaryAssociation = BinaryAssociation(
    name="namespace13",
    ends={
        Property(name="Package", type=SimpleUML_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=SimpleUML_Package, multiplicity=Multiplicity(0, 1))
    }
)
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="SimpleUML_Classifier", type=SimpleUML_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUML_Attribute", type=SimpleUML_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
owner1: BinaryAssociation = BinaryAssociation(
    name="owner1",
    ends={
        Property(name="Class", type=SimpleUML_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=SimpleUML_Class, multiplicity=Multiplicity(0, 1))
    }
)
attribute2: BinaryAssociation = BinaryAssociation(
    name="attribute2",
    ends={
        Property(name="Attribute", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=SimpleUML_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general4: BinaryAssociation = BinaryAssociation(
    name="general4",
    ends={
        Property(name="SimpleUML_Class", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUML_Class3", type=SimpleUML_Class, multiplicity=Multiplicity(0, 9999))
    }
)
reverse5: BinaryAssociation = BinaryAssociation(
    name="reverse5",
    ends={
        Property(name="Association", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=SimpleUML_Association, multiplicity=Multiplicity(0, 9999))
    }
)
forward6: BinaryAssociation = BinaryAssociation(
    name="forward6",
    ends={
        Property(name="Association7", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=SimpleUML_Association, multiplicity=Multiplicity(0, 9999))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="Class9", type=SimpleUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="reverse", type=SimpleUML_Class, multiplicity=Multiplicity(0, 1))
    }
)
destination10: BinaryAssociation = BinaryAssociation(
    name="destination10",
    ends={
        Property(name="Class11", type=SimpleUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="forward", type=SimpleUML_Class, multiplicity=Multiplicity(0, 1))
    }
)
elements12: BinaryAssociation = BinaryAssociation(
    name="elements12",
    ends={
        Property(name="PackageElement", type=SimpleUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=SimpleUML_PackageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SimpleUML_Classifier_PackageElement = Generalization(general=PackageElement, specific=SimpleUML_Classifier)
gen_SimpleUML_Attribute_UMLModelElement = Generalization(general=UMLModelElement, specific=SimpleUML_Attribute)
gen_SimpleUML_PackageElement_UMLModelElement = Generalization(general=UMLModelElement, specific=SimpleUML_PackageElement)
gen_SimpleUML_Class_Classifier = Generalization(general=Classifier, specific=SimpleUML_Class)
gen_SimpleUML_Association_PackageElement = Generalization(general=PackageElement, specific=SimpleUML_Association)
gen_SimpleUML_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=SimpleUML_PrimitiveDataType)
gen_SimpleUML_Package_UMLModelElement = Generalization(general=UMLModelElement, specific=SimpleUML_Package)

# Domain Model
domain_model = DomainModel(
    name="SimpleUML",
    types={SimpleUML_Classifier, PackageElement, SimpleUML_Attribute, UMLModelElement, SimpleUML_Class, Classifier, SimpleUML_Association, SimpleUML_PrimitiveDataType, SimpleUML_UMLModelElement, SimpleUML_Package, SimpleUML_PackageElement},
    associations={namespace13, type0, owner1, attribute2, general4, reverse5, forward6, source8, destination10, elements12},
    generalizations={gen_SimpleUML_Classifier_PackageElement, gen_SimpleUML_Attribute_UMLModelElement, gen_SimpleUML_PackageElement_UMLModelElement, gen_SimpleUML_Class_Classifier, gen_SimpleUML_Association_PackageElement, gen_SimpleUML_PrimitiveDataType_Classifier, gen_SimpleUML_Package_UMLModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)