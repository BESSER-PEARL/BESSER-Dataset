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
uml_Attribute = Class(name="uml::Attribute")
UMLModelElement = Class(name="UMLModelElement")
uml_PackageElement = Class(name="uml::PackageElement", is_abstract=True)
uml_PrimitiveDataType = Class(name="uml::PrimitiveDataType")
uml_UMLModelElement = Class(name="uml::UMLModelElement", is_abstract=True)
uml_Class = Class(name="uml::Class")
uml_Classifier = Class(name="uml::Classifier", is_abstract=True)
uml_Association = Class(name="uml::Association")
PackageElement = Class(name="PackageElement")
Classifier = Class(name="Classifier")
uml_Package = Class(name="uml::Package")

# uml_Attribute class attributes and methods

# UMLModelElement class attributes and methods

# uml_PackageElement class attributes and methods

# uml_PrimitiveDataType class attributes and methods

# uml_UMLModelElement class attributes and methods
uml_UMLModelElement_kind: Property = Property(name="kind", type=StringType)
uml_UMLModelElement_name: Property = Property(name="name", type=StringType)
uml_UMLModelElement.attributes={uml_UMLModelElement_kind, uml_UMLModelElement_name}

# uml_Class class attributes and methods

# uml_Classifier class attributes and methods

# uml_Association class attributes and methods

# PackageElement class attributes and methods

# Classifier class attributes and methods

# uml_Package class attributes and methods

# Relationships
elements18: BinaryAssociation = BinaryAssociation(
    name="elements18",
    ends={
        Property(name="PackageElement", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=uml_PackageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespace19: BinaryAssociation = BinaryAssociation(
    name="namespace19",
    ends={
        Property(name="Package", type=uml_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=uml_Package, multiplicity=Multiplicity(1, 1))
    }
)
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="Class", type=uml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=uml_Class, multiplicity=Multiplicity(1, 1))
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="Classifier", type=uml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="typeOpposite", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
destination2: BinaryAssociation = BinaryAssociation(
    name="destination2",
    ends={
        Property(name="Class3", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="reverse", type=uml_Class, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Class5", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="forward", type=uml_Class, multiplicity=Multiplicity(1, 1))
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="Attribute", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=uml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forward7: BinaryAssociation = BinaryAssociation(
    name="forward7",
    ends={
        Property(name="Association", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=uml_Association, multiplicity=Multiplicity(0, 9999))
    }
)
general9: BinaryAssociation = BinaryAssociation(
    name="general9",
    ends={
        Property(name="Class10", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="generalOpposite", type=uml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
generalOpposite12: BinaryAssociation = BinaryAssociation(
    name="generalOpposite12",
    ends={
        Property(name="Class13", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="general", type=uml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
reverse14: BinaryAssociation = BinaryAssociation(
    name="reverse14",
    ends={
        Property(name="Association15", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=uml_Association, multiplicity=Multiplicity(0, 9999))
    }
)
typeOpposite16: BinaryAssociation = BinaryAssociation(
    name="typeOpposite16",
    ends={
        Property(name="Attribute17", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=uml_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_uml_Package_UMLModelElement = Generalization(general=UMLModelElement, specific=uml_Package)
gen_uml_PackageElement_UMLModelElement = Generalization(general=UMLModelElement, specific=uml_PackageElement)
gen_uml_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=uml_PrimitiveDataType)
gen_uml_Attribute_UMLModelElement = Generalization(general=UMLModelElement, specific=uml_Attribute)
gen_uml_Association_PackageElement = Generalization(general=PackageElement, specific=uml_Association)
gen_uml_Class_Classifier = Generalization(general=Classifier, specific=uml_Class)
gen_uml_Classifier_PackageElement = Generalization(general=PackageElement, specific=uml_Classifier)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_Attribute, UMLModelElement, uml_PackageElement, uml_PrimitiveDataType, uml_UMLModelElement, uml_Class, uml_Classifier, uml_Association, PackageElement, Classifier, uml_Package},
    associations={elements18, namespace19, owner0, type1, destination2, source4, attributes6, forward7, general9, generalOpposite12, reverse14, typeOpposite16},
    generalizations={gen_uml_Package_UMLModelElement, gen_uml_PackageElement_UMLModelElement, gen_uml_PrimitiveDataType_Classifier, gen_uml_Attribute_UMLModelElement, gen_uml_Association_PackageElement, gen_uml_Class_Classifier, gen_uml_Classifier_PackageElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)