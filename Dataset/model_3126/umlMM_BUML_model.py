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

# Enumerations
KIND: Enumeration = Enumeration(
    name="KIND",
    literals={
            EnumerationLiteral(name="OTHER"),
			EnumerationLiteral(name="PERSISTENT")
    }
)

# Classes
umlMM__Classifier = Class(name="umlMM::::Classifier", is_abstract=True)
umlMM__Association = Class(name="umlMM::::Association")
umlMM__dummy = Class(name="umlMM::::dummy")
umlMM__Class = Class(name="umlMM::::Class")
Classifier = Class(name="Classifier")
umlMM__Attribute = Class(name="umlMM::::Attribute")
umlMM__Package = Class(name="umlMM::::Package")
umlMM__PrimitiveDataType = Class(name="umlMM::::PrimitiveDataType")

# umlMM__Classifier class attributes and methods
umlMM__Classifier_name: Property = Property(name="name", type=StringType)
umlMM__Classifier.attributes={umlMM__Classifier_name}

# umlMM__Association class attributes and methods
umlMM__Association_name: Property = Property(name="name", type=StringType)
umlMM__Association.attributes={umlMM__Association_name}

# umlMM__dummy class attributes and methods

# umlMM__Class class attributes and methods
umlMM__Class_kind: Property = Property(name="kind", type=StringType)
umlMM__Class.attributes={umlMM__Class_kind}

# Classifier class attributes and methods

# umlMM__Attribute class attributes and methods
umlMM__Attribute_name: Property = Property(name="name", type=StringType)
umlMM__Attribute.attributes={umlMM__Attribute_name}

# umlMM__Package class attributes and methods
umlMM__Package_name: Property = Property(name="name", type=StringType)
umlMM__Package.attributes={umlMM__Package_name}

# umlMM__PrimitiveDataType class attributes and methods

# Relationships
classifier0: BinaryAssociation = BinaryAssociation(
    name="classifier0",
    ends={
        Property(name="Classifier", type=umlMM__Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=umlMM__Classifier, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Association", type=umlMM__Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace2", type=umlMM__Association, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dummy3: BinaryAssociation = BinaryAssociation(
    name="dummy3",
    ends={
        Property(name="dummy", type=umlMM__Package, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPackage", type=umlMM__dummy, multiplicity=Multiplicity(1, 1))
    }
)
attribute4: BinaryAssociation = BinaryAssociation(
    name="attribute4",
    ends={
        Property(name="Attribute", type=umlMM__Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=umlMM__Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subclass8: BinaryAssociation = BinaryAssociation(
    name="subclass8",
    ends={
        Property(name="Class9", type=umlMM__Class, multiplicity=Multiplicity(1, 1)),
        Property(name="general", type=umlMM__Class, multiplicity=Multiplicity(1, 9999))
    }
)
sourceOf10: BinaryAssociation = BinaryAssociation(
    name="sourceOf10",
    ends={
        Property(name="Association11", type=umlMM__Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=umlMM__Association, multiplicity=Multiplicity(1, 9999))
    }
)
destinationOf12: BinaryAssociation = BinaryAssociation(
    name="destinationOf12",
    ends={
        Property(name="Association13", type=umlMM__Class, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=umlMM__Association, multiplicity=Multiplicity(1, 9999))
    }
)
owner14: BinaryAssociation = BinaryAssociation(
    name="owner14",
    ends={
        Property(name="Class15", type=umlMM__Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=umlMM__Class, multiplicity=Multiplicity(1, 1))
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="Classifier17", type=umlMM__Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="typeOf", type=umlMM__Classifier, multiplicity=Multiplicity(1, 1))
    }
)
general6: BinaryAssociation = BinaryAssociation(
    name="general6",
    ends={
        Property(name="Class", type=umlMM__Class, multiplicity=Multiplicity(1, 1)),
        Property(name="subclass", type=umlMM__Class, multiplicity=Multiplicity(1, 1))
    }
)
namespace20: BinaryAssociation = BinaryAssociation(
    name="namespace20",
    ends={
        Property(name="Package", type=umlMM__Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifier", type=umlMM__Package, multiplicity=Multiplicity(1, 1))
    }
)
namespace21: BinaryAssociation = BinaryAssociation(
    name="namespace21",
    ends={
        Property(name="Package22", type=umlMM__Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=umlMM__Package, multiplicity=Multiplicity(1, 1))
    }
)
source23: BinaryAssociation = BinaryAssociation(
    name="source23",
    ends={
        Property(name="Class24", type=umlMM__Association, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceOf", type=umlMM__Class, multiplicity=Multiplicity(1, 1))
    }
)
destination25: BinaryAssociation = BinaryAssociation(
    name="destination25",
    ends={
        Property(name="Class26", type=umlMM__Association, multiplicity=Multiplicity(1, 1)),
        Property(name="destinationOf", type=umlMM__Class, multiplicity=Multiplicity(1, 1))
    }
)
typeOf18: BinaryAssociation = BinaryAssociation(
    name="typeOf18",
    ends={
        Property(name="Attribute19", type=umlMM__Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=umlMM__Attribute, multiplicity=Multiplicity(1, 9999))
    }
)
containsPackage27: BinaryAssociation = BinaryAssociation(
    name="containsPackage27",
    ends={
        Property(name="Package29", type=umlMM__dummy, multiplicity=Multiplicity(1, 1)),
        Property(name="dummy28", type=umlMM__Package, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_umlMM__Class_Classifier = Generalization(general=Classifier, specific=umlMM__Class)
gen_umlMM__PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=umlMM__PrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="umlMM_",
    types={umlMM__Classifier, umlMM__Association, umlMM__dummy, umlMM__Class, Classifier, umlMM__Attribute, umlMM__Package, umlMM__PrimitiveDataType, KIND},
    associations={classifier0, association1, dummy3, attribute4, subclass8, sourceOf10, destinationOf12, owner14, type16, general6, namespace20, namespace21, source23, destination25, typeOf18, containsPackage27},
    generalizations={gen_umlMM__Class_Classifier, gen_umlMM__PrimitiveDataType_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)