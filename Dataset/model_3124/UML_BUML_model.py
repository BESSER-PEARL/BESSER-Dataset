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
UML_Package = Class(name="UML::Package")
UML_Classifier = Class(name="UML::Classifier", is_abstract=True)
UML_Association = Class(name="UML::Association")
UML_Class = Class(name="UML::Class")
Classifier = Class(name="Classifier")
UML_Attribute = Class(name="UML::Attribute")
UML_PrimitiveDataType = Class(name="UML::PrimitiveDataType")

# UML_Package class attributes and methods
UML_Package_name: Property = Property(name="name", type=StringType)
UML_Package.attributes={UML_Package_name}

# UML_Classifier class attributes and methods
UML_Classifier_name: Property = Property(name="name", type=StringType)
UML_Classifier.attributes={UML_Classifier_name}

# UML_Association class attributes and methods
UML_Association_name: Property = Property(name="name", type=StringType)
UML_Association.attributes={UML_Association_name}

# UML_Class class attributes and methods
UML_Class_kind: Property = Property(name="kind", type=StringType)
UML_Class.attributes={UML_Class_kind}

# Classifier class attributes and methods

# UML_Attribute class attributes and methods
UML_Attribute_name: Property = Property(name="name", type=StringType)
UML_Attribute.attributes={UML_Attribute_name}

# UML_PrimitiveDataType class attributes and methods

# Relationships
subclass7: BinaryAssociation = BinaryAssociation(
    name="subclass7",
    ends={
        Property(name="Class8", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="general", type=UML_Class, multiplicity=Multiplicity(0, 9999))
    }
)
sourceOf9: BinaryAssociation = BinaryAssociation(
    name="sourceOf9",
    ends={
        Property(name="Association10", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=UML_Association, multiplicity=Multiplicity(0, 9999))
    }
)
destinationOf11: BinaryAssociation = BinaryAssociation(
    name="destinationOf11",
    ends={
        Property(name="Association12", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=UML_Association, multiplicity=Multiplicity(0, 9999))
    }
)
classifier0: BinaryAssociation = BinaryAssociation(
    name="classifier0",
    ends={
        Property(name="Classifier", type=UML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=UML_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Association", type=UML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace2", type=UML_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute3: BinaryAssociation = BinaryAssociation(
    name="attribute3",
    ends={
        Property(name="Attribute", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=UML_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general5: BinaryAssociation = BinaryAssociation(
    name="general5",
    ends={
        Property(name="Class", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="subclass", type=UML_Class, multiplicity=Multiplicity(0, 1))
    }
)
namespace20: BinaryAssociation = BinaryAssociation(
    name="namespace20",
    ends={
        Property(name="Package21", type=UML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=UML_Package, multiplicity=Multiplicity(1, 1))
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="Class23", type=UML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceOf", type=UML_Class, multiplicity=Multiplicity(1, 1))
    }
)
destination24: BinaryAssociation = BinaryAssociation(
    name="destination24",
    ends={
        Property(name="Class25", type=UML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="destinationOf", type=UML_Class, multiplicity=Multiplicity(1, 1))
    }
)
owner13: BinaryAssociation = BinaryAssociation(
    name="owner13",
    ends={
        Property(name="Class14", type=UML_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=UML_Class, multiplicity=Multiplicity(1, 1))
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="Classifier16", type=UML_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="typeOf", type=UML_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
typeOf17: BinaryAssociation = BinaryAssociation(
    name="typeOf17",
    ends={
        Property(name="Attribute18", type=UML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=UML_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
namespace19: BinaryAssociation = BinaryAssociation(
    name="namespace19",
    ends={
        Property(name="Package", type=UML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifier", type=UML_Package, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_UML_Class_Classifier = Generalization(general=Classifier, specific=UML_Class)
gen_UML_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=UML_PrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="UML",
    types={UML_Package, UML_Classifier, UML_Association, UML_Class, Classifier, UML_Attribute, UML_PrimitiveDataType},
    associations={subclass7, sourceOf9, destinationOf11, classifier0, association1, attribute3, general5, namespace20, source22, destination24, owner13, type15, typeOf17, namespace19},
    generalizations={gen_UML_Class_Classifier, gen_UML_PrimitiveDataType_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)