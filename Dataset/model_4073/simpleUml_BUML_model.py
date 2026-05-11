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
simpleUml_Package = Class(name="simpleUml_Package")
UMLModelElement = Class(name="UMLModelElement")
simpleUml_PackageElement = Class(name="simpleUml_PackageElement", is_abstract=True)
simpleUml_Class = Class(name="simpleUml_Class")
Classifier = Class(name="Classifier")
simpleUml_Attribute = Class(name="simpleUml_Attribute")
simpleUml_Association = Class(name="simpleUml_Association")
simpleUml_UMLModelElement = Class(name="simpleUml_UMLModelElement")
simpleUml_Classifier = Class(name="simpleUml_Classifier", is_abstract=True)
PackageElement = Class(name="PackageElement")

# simpleUml_Package class attributes and methods

# UMLModelElement class attributes and methods

# simpleUml_PackageElement class attributes and methods

# simpleUml_Class class attributes and methods

# Classifier class attributes and methods

# simpleUml_Attribute class attributes and methods

# simpleUml_Association class attributes and methods

# simpleUml_UMLModelElement class attributes and methods
simpleUml_UMLModelElement_kind: Property = Property(name="kind", type=StringType)
simpleUml_UMLModelElement_name: Property = Property(name="name", type=StringType)
simpleUml_UMLModelElement.attributes={simpleUml_UMLModelElement_name, simpleUml_UMLModelElement_kind}

# simpleUml_Classifier class attributes and methods

# PackageElement class attributes and methods

# Relationships
namespace2: BinaryAssociation = BinaryAssociation(
    name="namespace2",
    ends={
        Property(name="Package", type=simpleUml_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=simpleUml_Package, multiplicity=Multiplicity(0, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="PackageElement", type=simpleUml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=simpleUml_PackageElement, multiplicity=Multiplicity(0, 9999))
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="simpleUml_Attribute", type=simpleUml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUml_Class", type=simpleUml_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_simpleUml_Package_UMLModelElement = Generalization(general=UMLModelElement, specific=simpleUml_Package)
gen_simpleUml_Class_Classifier = Generalization(general=Classifier, specific=simpleUml_Class)
gen_simpleUml_Classifier_PackageElement = Generalization(general=PackageElement, specific=simpleUml_Classifier)
gen_simpleUml_PackageElement_UMLModelElement = Generalization(general=UMLModelElement, specific=simpleUml_PackageElement)

# Domain Model
domain_model = DomainModel(
    name="simpleUml",
    types={simpleUml_Package, UMLModelElement, simpleUml_PackageElement, simpleUml_Class, Classifier, simpleUml_Attribute, simpleUml_Association, simpleUml_UMLModelElement, simpleUml_Classifier, PackageElement},
    associations={namespace2, elements0, attribute1},
    generalizations={gen_simpleUml_Package_UMLModelElement, gen_simpleUml_Class_Classifier, gen_simpleUml_Classifier_PackageElement, gen_simpleUml_PackageElement_UMLModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)