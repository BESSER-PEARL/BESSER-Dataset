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
umlMM_Package = Class(name="umlMM::Package")
umlMM_Classifier = Class(name="umlMM::Classifier", is_abstract=True)
umlMM_Association = Class(name="umlMM::Association")
umlMM_Class = Class(name="umlMM::Class")
Classifier = Class(name="Classifier")
umlMM_Attribute = Class(name="umlMM::Attribute")
umlMM_dummy = Class(name="umlMM::dummy")
umlMM_PrimitiveDataType = Class(name="umlMM::PrimitiveDataType")

# umlMM_Package class attributes and methods
umlMM_Package_name: Property = Property(name="name", type=StringType)
umlMM_Package.attributes={umlMM_Package_name}

# umlMM_Classifier class attributes and methods
umlMM_Classifier_name: Property = Property(name="name", type=StringType)
umlMM_Classifier.attributes={umlMM_Classifier_name}

# umlMM_Association class attributes and methods
umlMM_Association_name: Property = Property(name="name", type=StringType)
umlMM_Association.attributes={umlMM_Association_name}

# umlMM_Class class attributes and methods
umlMM_Class_kind: Property = Property(name="kind", type=StringType)
umlMM_Class.attributes={umlMM_Class_kind}

# Classifier class attributes and methods

# umlMM_Attribute class attributes and methods
umlMM_Attribute_name: Property = Property(name="name", type=StringType)
umlMM_Attribute.attributes={umlMM_Attribute_name}

# umlMM_dummy class attributes and methods

# umlMM_PrimitiveDataType class attributes and methods

# Relationships
classifier0: BinaryAssociation = BinaryAssociation(
    name="classifier0",
    ends={
        Property(name="Classifier", type=umlMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=umlMM_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Association", type=umlMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace2", type=umlMM_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceOf9: BinaryAssociation = BinaryAssociation(
    name="sourceOf9",
    ends={
        Property(name="Association10", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=umlMM_Association, multiplicity=Multiplicity(0, 9999))
    }
)
destinationOf11: BinaryAssociation = BinaryAssociation(
    name="destinationOf11",
    ends={
        Property(name="Association12", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=umlMM_Association, multiplicity=Multiplicity(0, 9999))
    }
)
owner13: BinaryAssociation = BinaryAssociation(
    name="owner13",
    ends={
        Property(name="Class14", type=umlMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="Classifier16", type=umlMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="typeOf", type=umlMM_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
attribute3: BinaryAssociation = BinaryAssociation(
    name="attribute3",
    ends={
        Property(name="Attribute", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=umlMM_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general5: BinaryAssociation = BinaryAssociation(
    name="general5",
    ends={
        Property(name="Class", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="subclass", type=umlMM_Class, multiplicity=Multiplicity(0, 1))
    }
)
subclass7: BinaryAssociation = BinaryAssociation(
    name="subclass7",
    ends={
        Property(name="Class8", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="general", type=umlMM_Class, multiplicity=Multiplicity(0, 9999))
    }
)
namespace20: BinaryAssociation = BinaryAssociation(
    name="namespace20",
    ends={
        Property(name="association", type=umlMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package21", type=umlMM_Association, multiplicity=Multiplicity(1, 1))
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="Class23", type=umlMM_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceOf", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
destination24: BinaryAssociation = BinaryAssociation(
    name="destination24",
    ends={
        Property(name="Class25", type=umlMM_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="destinationOf", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
containsPackage26: BinaryAssociation = BinaryAssociation(
    name="containsPackage26",
    ends={
        Property(name="umlMM_Package", type=umlMM_dummy, multiplicity=Multiplicity(1, 1)),
        Property(name="umlMM_dummy", type=umlMM_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeOf17: BinaryAssociation = BinaryAssociation(
    name="typeOf17",
    ends={
        Property(name="Attribute18", type=umlMM_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=umlMM_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
namespace19: BinaryAssociation = BinaryAssociation(
    name="namespace19",
    ends={
        Property(name="Package", type=umlMM_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifier", type=umlMM_Package, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_umlMM_Class_Classifier = Generalization(general=Classifier, specific=umlMM_Class)
gen_umlMM_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=umlMM_PrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="umlMM",
    types={umlMM_Package, umlMM_Classifier, umlMM_Association, umlMM_Class, Classifier, umlMM_Attribute, umlMM_dummy, umlMM_PrimitiveDataType},
    associations={classifier0, association1, sourceOf9, destinationOf11, owner13, type15, attribute3, general5, subclass7, namespace20, source22, destination24, containsPackage26, typeOf17, namespace19},
    generalizations={gen_umlMM_Class_Classifier, gen_umlMM_PrimitiveDataType_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)