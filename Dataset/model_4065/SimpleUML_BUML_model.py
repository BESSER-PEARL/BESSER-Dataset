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
simpleuml_Attribute = Class(name="simpleuml::Attribute")
UMLModelElement = Class(name="UMLModelElement")
simpleuml_Package = Class(name="simpleuml::Package")
simpleuml_PackageElement = Class(name="simpleuml::PackageElement", is_abstract=True)
simpleuml_PrimitiveDataType = Class(name="simpleuml::PrimitiveDataType")
simpleuml_UMLModelElement = Class(name="simpleuml::UMLModelElement", is_abstract=True)
simpleuml_Class = Class(name="simpleuml::Class")
simpleuml_Classifier = Class(name="simpleuml::Classifier", is_abstract=True)
simpleuml_Association = Class(name="simpleuml::Association")
PackageElement = Class(name="PackageElement")
Classifier = Class(name="Classifier")

# simpleuml_Attribute class attributes and methods

# UMLModelElement class attributes and methods

# simpleuml_Package class attributes and methods

# simpleuml_PackageElement class attributes and methods

# simpleuml_PrimitiveDataType class attributes and methods

# simpleuml_UMLModelElement class attributes and methods
simpleuml_UMLModelElement_kind: Property = Property(name="kind", type=StringType)
simpleuml_UMLModelElement_name: Property = Property(name="name", type=StringType)
simpleuml_UMLModelElement.attributes={simpleuml_UMLModelElement_name, simpleuml_UMLModelElement_kind}

# simpleuml_Class class attributes and methods

# simpleuml_Classifier class attributes and methods

# simpleuml_Association class attributes and methods

# PackageElement class attributes and methods

# Classifier class attributes and methods

# Relationships
general9: BinaryAssociation = BinaryAssociation(
    name="general9",
    ends={
        Property(name="generalOpposite", type=simpleuml_Class, multiplicity=Multiplicity(0, 9999)),
        Property(name="Class10", type=simpleuml_Class, multiplicity=Multiplicity(1, 1))
    }
)
generalOpposite12: BinaryAssociation = BinaryAssociation(
    name="generalOpposite12",
    ends={
        Property(name="Class13", type=simpleuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="general", type=simpleuml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
reverse14: BinaryAssociation = BinaryAssociation(
    name="reverse14",
    ends={
        Property(name="Association15", type=simpleuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=simpleuml_Association, multiplicity=Multiplicity(0, 9999))
    }
)
typeOpposite16: BinaryAssociation = BinaryAssociation(
    name="typeOpposite16",
    ends={
        Property(name="Attribute17", type=simpleuml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=simpleuml_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
elements18: BinaryAssociation = BinaryAssociation(
    name="elements18",
    ends={
        Property(name="PackageElement", type=simpleuml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=simpleuml_PackageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespace19: BinaryAssociation = BinaryAssociation(
    name="namespace19",
    ends={
        Property(name="Package", type=simpleuml_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=simpleuml_Package, multiplicity=Multiplicity(1, 1))
    }
)
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="Class", type=simpleuml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=simpleuml_Class, multiplicity=Multiplicity(1, 1))
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="Classifier", type=simpleuml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="typeOpposite", type=simpleuml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
destination2: BinaryAssociation = BinaryAssociation(
    name="destination2",
    ends={
        Property(name="Class3", type=simpleuml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="reverse", type=simpleuml_Class, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Class5", type=simpleuml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="forward", type=simpleuml_Class, multiplicity=Multiplicity(1, 1))
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="Attribute", type=simpleuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simpleuml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forward7: BinaryAssociation = BinaryAssociation(
    name="forward7",
    ends={
        Property(name="Association", type=simpleuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=simpleuml_Association, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_simpleuml_Attribute_UMLModelElement = Generalization(general=UMLModelElement, specific=simpleuml_Attribute)
gen_simpleuml_Classifier_PackageElement = Generalization(general=PackageElement, specific=simpleuml_Classifier)
gen_simpleuml_Package_UMLModelElement = Generalization(general=UMLModelElement, specific=simpleuml_Package)
gen_simpleuml_PackageElement_UMLModelElement = Generalization(general=UMLModelElement, specific=simpleuml_PackageElement)
gen_simpleuml_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=simpleuml_PrimitiveDataType)
gen_simpleuml_Association_PackageElement = Generalization(general=PackageElement, specific=simpleuml_Association)
gen_simpleuml_Class_Classifier = Generalization(general=Classifier, specific=simpleuml_Class)

# Domain Model
domain_model = DomainModel(
    name="simpleuml",
    types={simpleuml_Attribute, UMLModelElement, simpleuml_Package, simpleuml_PackageElement, simpleuml_PrimitiveDataType, simpleuml_UMLModelElement, simpleuml_Class, simpleuml_Classifier, simpleuml_Association, PackageElement, Classifier},
    associations={general9, generalOpposite12, reverse14, typeOpposite16, elements18, namespace19, owner0, type1, destination2, source4, attributes6, forward7},
    generalizations={gen_simpleuml_Attribute_UMLModelElement, gen_simpleuml_Classifier_PackageElement, gen_simpleuml_Package_UMLModelElement, gen_simpleuml_PackageElement_UMLModelElement, gen_simpleuml_PrimitiveDataType_Classifier, gen_simpleuml_Association_PackageElement, gen_simpleuml_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)