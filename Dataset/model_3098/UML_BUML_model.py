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
UML_PrimitiveDataType = Class(name="UML::PrimitiveDataType")
Classifier = Class(name="Classifier")
UML_Class = Class(name="UML::Class")
UML_Attribute = Class(name="UML::Attribute")
UML_Package = Class(name="UML::Package")
UML_Classifier = Class(name="UML::Classifier", is_abstract=True)
UML_Association = Class(name="UML::Association")

# UML_PrimitiveDataType class attributes and methods

# Classifier class attributes and methods

# UML_Class class attributes and methods
UML_Class_is_persistent: Property = Property(name="is_persistent", type=BooleanType)
UML_Class.attributes={UML_Class_is_persistent}

# UML_Attribute class attributes and methods
UML_Attribute_name: Property = Property(name="name", type=StringType)
UML_Attribute_is_primary: Property = Property(name="is_primary", type=BooleanType)
UML_Attribute.attributes={UML_Attribute_is_primary, UML_Attribute_name}

# UML_Package class attributes and methods
UML_Package_name: Property = Property(name="name", type=StringType)
UML_Package.attributes={UML_Package_name}

# UML_Classifier class attributes and methods
UML_Classifier_name: Property = Property(name="name", type=StringType)
UML_Classifier.attributes={UML_Classifier_name}

# UML_Association class attributes and methods
UML_Association_name: Property = Property(name="name", type=StringType)
UML_Association.attributes={UML_Association_name}

# Relationships
classifiers0: BinaryAssociation = BinaryAssociation(
    name="classifiers0",
    ends={
        Property(name="UML_Classifier", type=UML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Package", type=UML_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="UML_Association", type=UML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Package2", type=UML_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrs3: BinaryAssociation = BinaryAssociation(
    name="attrs3",
    ends={
        Property(name="UML_Attribute", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Class", type=UML_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="UML_Class6", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Class4", type=UML_Class, multiplicity=Multiplicity(0, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="UML_Classifier9", type=UML_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Attribute8", type=UML_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
src10: BinaryAssociation = BinaryAssociation(
    name="src10",
    ends={
        Property(name="UML_Class12", type=UML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Association11", type=UML_Class, multiplicity=Multiplicity(1, 1))
    }
)
dest13: BinaryAssociation = BinaryAssociation(
    name="dest13",
    ends={
        Property(name="UML_Class15", type=UML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Association14", type=UML_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_UML_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=UML_PrimitiveDataType)
gen_UML_Class_Classifier = Generalization(general=Classifier, specific=UML_Class)

# Domain Model
domain_model = DomainModel(
    name="UML",
    types={UML_PrimitiveDataType, Classifier, UML_Class, UML_Attribute, UML_Package, UML_Classifier, UML_Association},
    associations={classifiers0, associations1, attrs3, parent5, type7, src10, dest13},
    generalizations={gen_UML_PrimitiveDataType_Classifier, gen_UML_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)