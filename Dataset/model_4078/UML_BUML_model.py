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
umlMM_Class = Class(name="umlMM::Class")
Classifier = Class(name="Classifier")
umlMM_Package = Class(name="umlMM::Package")
umlMM_Associaton = Class(name="umlMM::Associaton")
umlMM_Classifier = Class(name="umlMM::Classifier")
umlMM_Attribute = Class(name="umlMM::Attribute")
umlMM_Datatype = Class(name="umlMM::Datatype")

# umlMM_Class class attributes and methods

# Classifier class attributes and methods

# umlMM_Package class attributes and methods
umlMM_Package_name: Property = Property(name="name", type=StringType)
umlMM_Package.attributes={umlMM_Package_name}

# umlMM_Associaton class attributes and methods
umlMM_Associaton_name: Property = Property(name="name", type=StringType)
umlMM_Associaton.attributes={umlMM_Associaton_name}

# umlMM_Classifier class attributes and methods
umlMM_Classifier_name: Property = Property(name="name", type=StringType)
umlMM_Classifier.attributes={umlMM_Classifier_name}

# umlMM_Attribute class attributes and methods
umlMM_Attribute_name: Property = Property(name="name", type=StringType)
umlMM_Attribute.attributes={umlMM_Attribute_name}

# umlMM_Datatype class attributes and methods

# Relationships
namespace3: BinaryAssociation = BinaryAssociation(
    name="namespace3",
    ends={
        Property(name="Package", type=umlMM_Associaton, multiplicity=Multiplicity(1, 1)),
        Property(name="Association", type=umlMM_Package, multiplicity=Multiplicity(1, 1))
    }
)
destination4: BinaryAssociation = BinaryAssociation(
    name="destination4",
    ends={
        Property(name="Class", type=umlMM_Associaton, multiplicity=Multiplicity(1, 1)),
        Property(name="destinationOf", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="Class6", type=umlMM_Associaton, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceOf", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
destinationOf7: BinaryAssociation = BinaryAssociation(
    name="destinationOf7",
    ends={
        Property(name="Associaton8", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=umlMM_Associaton, multiplicity=Multiplicity(0, 9999))
    }
)
Association0: BinaryAssociation = BinaryAssociation(
    name="Association0",
    ends={
        Property(name="Associaton", type=umlMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=umlMM_Associaton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier1: BinaryAssociation = BinaryAssociation(
    name="classifier1",
    ends={
        Property(name="Classifier", type=umlMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace2", type=umlMM_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceOf9: BinaryAssociation = BinaryAssociation(
    name="sourceOf9",
    ends={
        Property(name="Associaton10", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=umlMM_Associaton, multiplicity=Multiplicity(0, 9999))
    }
)
attribute11: BinaryAssociation = BinaryAssociation(
    name="attribute11",
    ends={
        Property(name="Attribute", type=umlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Owner", type=umlMM_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="Classifier13", type=umlMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="typeOf", type=umlMM_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
Owner14: BinaryAssociation = BinaryAssociation(
    name="Owner14",
    ends={
        Property(name="Class15", type=umlMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=umlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
typeOf16: BinaryAssociation = BinaryAssociation(
    name="typeOf16",
    ends={
        Property(name="Attribute17", type=umlMM_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=umlMM_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
namespace18: BinaryAssociation = BinaryAssociation(
    name="namespace18",
    ends={
        Property(name="Package19", type=umlMM_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifier", type=umlMM_Package, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_umlMM_Class_Classifier = Generalization(general=Classifier, specific=umlMM_Class)
gen_umlMM_Datatype_Classifier = Generalization(general=Classifier, specific=umlMM_Datatype)

# Domain Model
domain_model = DomainModel(
    name="umlMM",
    types={umlMM_Class, Classifier, umlMM_Package, umlMM_Associaton, umlMM_Classifier, umlMM_Attribute, umlMM_Datatype},
    associations={namespace3, destination4, source5, destinationOf7, Association0, classifier1, sourceOf9, attribute11, type12, Owner14, typeOf16, namespace18},
    generalizations={gen_umlMM_Class_Classifier, gen_umlMM_Datatype_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)