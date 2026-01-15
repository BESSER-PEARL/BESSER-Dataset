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
umlMM_Association = Class(name="umlMM::Association")
PackageElement = Class(name="PackageElement")
umlMM_PackageElement = Class(name="umlMM::PackageElement", is_abstract=True)
umlMM_PrimitiveDataType = Class(name="umlMM::PrimitiveDataType")
umlMM_UMLModelElement = Class(name="umlMM::UMLModelElement", is_abstract=True)
umlMM_Class = Class(name="umlMM::Class")
umlMM_Attribute = Class(name="umlMM::Attribute")
UMLModelElement = Class(name="UMLModelElement")
umlMM_Classifier = Class(name="umlMM::Classifier", is_abstract=True)
Classifier = Class(name="Classifier")
umlMM_Package = Class(name="umlMM::Package")

# umlMM_Association class attributes and methods

# PackageElement class attributes and methods

# umlMM_PackageElement class attributes and methods

# umlMM_PrimitiveDataType class attributes and methods

# umlMM_UMLModelElement class attributes and methods
umlMM_UMLModelElement_kind: Property = Property(name="kind", type=StringType)
umlMM_UMLModelElement_name: Property = Property(name="name", type=StringType)
umlMM_UMLModelElement.attributes={umlMM_UMLModelElement_kind, umlMM_UMLModelElement_name}

# umlMM_Class class attributes and methods

# umlMM_Attribute class attributes and methods

# UMLModelElement class attributes and methods

# umlMM_Classifier class attributes and methods

# Classifier class attributes and methods

# umlMM_Package class attributes and methods

# Relationships
elements12: BinaryAssociation = BinaryAssociation(
    name="elements12",
    ends={
        Property(name="PackageElement", type=umlMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=umlMM_PackageElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
namespace13: BinaryAssociation = BinaryAssociation(
    name="namespace13",
    ends={
        Property(name="Package", type=umlMM_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=umlMM_Package, multiplicity=Multiplicity(1, 1))
    }
)
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="Class", type=umlMM_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="reverse", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
destination1: BinaryAssociation = BinaryAssociation(
    name="destination1",
    ends={
        Property(name="Class2", type=umlMM_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="forward", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Class4", type=umlMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="umlMM_Classifier", type=umlMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="umlMM_Attribute", type=umlMM_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
attribute6: BinaryAssociation = BinaryAssociation(
    name="attribute6",
    ends={
        Property(name="Attribute", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=umlMM_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general8: BinaryAssociation = BinaryAssociation(
    name="general8",
    ends={
        Property(name="umlMM_Class", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="umlMM_Class7", type=umlMM_Class, multiplicity=Multiplicity(0, 9999))
    }
)
forward9: BinaryAssociation = BinaryAssociation(
    name="forward9",
    ends={
        Property(name="Association", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=umlMM_Association, multiplicity=Multiplicity(0, 9999))
    }
)
reverse10: BinaryAssociation = BinaryAssociation(
    name="reverse10",
    ends={
        Property(name="Association11", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=umlMM_Association, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_umlMM_Association_PackageElement = Generalization(general=PackageElement, specific=umlMM_Association)
gen_umlMM_PackageElement_UMLModelElement = Generalization(general=UMLModelElement, specific=umlMM_PackageElement)
gen_umlMM_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=umlMM_PrimitiveDataType)
gen_umlMM_Attribute_UMLModelElement = Generalization(general=UMLModelElement, specific=umlMM_Attribute)
gen_umlMM_Class_Classifier = Generalization(general=Classifier, specific=umlMM_Class)
gen_umlMM_Classifier_PackageElement = Generalization(general=PackageElement, specific=umlMM_Classifier)
gen_umlMM_Package_UMLModelElement = Generalization(general=UMLModelElement, specific=umlMM_Package)

# Domain Model
domain_model = DomainModel(
    name="umlMM",
    types={umlMM_Association, PackageElement, umlMM_PackageElement, umlMM_PrimitiveDataType, umlMM_UMLModelElement, umlMM_Class, umlMM_Attribute, UMLModelElement, umlMM_Classifier, Classifier, umlMM_Package},
    associations={elements12, namespace13, source0, destination1, owner3, type5, attribute6, general8, forward9, reverse10},
    generalizations={gen_umlMM_Association_PackageElement, gen_umlMM_PackageElement_UMLModelElement, gen_umlMM_PrimitiveDataType_Classifier, gen_umlMM_Attribute_UMLModelElement, gen_umlMM_Class_Classifier, gen_umlMM_Classifier_PackageElement, gen_umlMM_Package_UMLModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)