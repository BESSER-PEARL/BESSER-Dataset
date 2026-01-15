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
classdiagram_Package = Class(name="classdiagram::Package")
classdiagram_Classifier = Class(name="classdiagram::Classifier", is_abstract=True)
classdiagram_Association = Class(name="classdiagram::Association")
classdiagram_PrimitiveDataType = Class(name="classdiagram::PrimitiveDataType")
Classifier = Class(name="Classifier")
classdiagram_Class = Class(name="classdiagram::Class")
classdiagram_Attribute = Class(name="classdiagram::Attribute")

# classdiagram_Package class attributes and methods
classdiagram_Package_name: Property = Property(name="name", type=StringType)
classdiagram_Package.attributes={classdiagram_Package_name}

# classdiagram_Classifier class attributes and methods
classdiagram_Classifier_name: Property = Property(name="name", type=StringType)
classdiagram_Classifier.attributes={classdiagram_Classifier_name}

# classdiagram_Association class attributes and methods
classdiagram_Association_name: Property = Property(name="name", type=StringType)
classdiagram_Association.attributes={classdiagram_Association_name}

# classdiagram_PrimitiveDataType class attributes and methods

# Classifier class attributes and methods

# classdiagram_Class class attributes and methods
classdiagram_Class_is_persistent: Property = Property(name="is_persistent", type=BooleanType)
classdiagram_Class.attributes={classdiagram_Class_is_persistent}

# classdiagram_Attribute class attributes and methods
classdiagram_Attribute_name: Property = Property(name="name", type=StringType)
classdiagram_Attribute_is_primary: Property = Property(name="is_primary", type=BooleanType)
classdiagram_Attribute.attributes={classdiagram_Attribute_name, classdiagram_Attribute_is_primary}

# Relationships
classifiers0: BinaryAssociation = BinaryAssociation(
    name="classifiers0",
    ends={
        Property(name="classdiagram_Classifier", type=classdiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Package", type=classdiagram_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="classdiagram_Association", type=classdiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Package2", type=classdiagram_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrs3: BinaryAssociation = BinaryAssociation(
    name="attrs3",
    ends={
        Property(name="classdiagram_Attribute", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Class", type=classdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="classdiagram_Class6", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Class4", type=classdiagram_Class, multiplicity=Multiplicity(0, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="classdiagram_Classifier9", type=classdiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Attribute8", type=classdiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
src10: BinaryAssociation = BinaryAssociation(
    name="src10",
    ends={
        Property(name="classdiagram_Class12", type=classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Association11", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
dest13: BinaryAssociation = BinaryAssociation(
    name="dest13",
    ends={
        Property(name="classdiagram_Class15", type=classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Association14", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_classdiagram_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=classdiagram_PrimitiveDataType)
gen_classdiagram_Class_Classifier = Generalization(general=Classifier, specific=classdiagram_Class)

# Domain Model
domain_model = DomainModel(
    name="classdiagram",
    types={classdiagram_Package, classdiagram_Classifier, classdiagram_Association, classdiagram_PrimitiveDataType, Classifier, classdiagram_Class, classdiagram_Attribute},
    associations={classifiers0, associations1, attrs3, parent5, type7, src10, dest13},
    generalizations={gen_classdiagram_PrimitiveDataType_Classifier, gen_classdiagram_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)