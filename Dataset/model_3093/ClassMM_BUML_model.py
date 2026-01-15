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
ClassMM_Classifier = Class(name="ClassMM::Classifier", is_abstract=True)
ClassMM_PrimitiveDataType = Class(name="ClassMM::PrimitiveDataType")
ClassMM_ClassModel = Class(name="ClassMM::ClassModel")
ClassMM_Association = Class(name="ClassMM::Association")
ClassMM_Class = Class(name="ClassMM::Class")
ClassMM_Attribute = Class(name="ClassMM::Attribute")
Classifier = Class(name="Classifier")

# ClassMM_Classifier class attributes and methods
ClassMM_Classifier_name: Property = Property(name="name", type=StringType)
ClassMM_Classifier.attributes={ClassMM_Classifier_name}

# ClassMM_PrimitiveDataType class attributes and methods

# ClassMM_ClassModel class attributes and methods

# ClassMM_Association class attributes and methods
ClassMM_Association_name: Property = Property(name="name", type=StringType)
ClassMM_Association.attributes={ClassMM_Association_name}

# ClassMM_Class class attributes and methods
ClassMM_Class_is_persistent: Property = Property(name="is_persistent", type=StringType)
ClassMM_Class.attributes={ClassMM_Class_is_persistent}

# ClassMM_Attribute class attributes and methods
ClassMM_Attribute_name: Property = Property(name="name", type=StringType)
ClassMM_Attribute_is_primary: Property = Property(name="is_primary", type=StringType)
ClassMM_Attribute.attributes={ClassMM_Attribute_is_primary, ClassMM_Attribute_name}

# Classifier class attributes and methods

# Relationships
classifier11: BinaryAssociation = BinaryAssociation(
    name="classifier11",
    ends={
        Property(name="ClassMM_Classifier12", type=ClassMM_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassMM_ClassModel", type=ClassMM_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association13: BinaryAssociation = BinaryAssociation(
    name="association13",
    ends={
        Property(name="ClassMM_Association15", type=ClassMM_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassMM_ClassModel14", type=ClassMM_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src0: BinaryAssociation = BinaryAssociation(
    name="src0",
    ends={
        Property(name="ClassMM_Class", type=ClassMM_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassMM_Association", type=ClassMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
dest1: BinaryAssociation = BinaryAssociation(
    name="dest1",
    ends={
        Property(name="ClassMM_Class3", type=ClassMM_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassMM_Association2", type=ClassMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="ClassMM_Classifier", type=ClassMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassMM_Attribute", type=ClassMM_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
attrs5: BinaryAssociation = BinaryAssociation(
    name="attrs5",
    ends={
        Property(name="ClassMM_Attribute7", type=ClassMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassMM_Class6", type=ClassMM_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent9: BinaryAssociation = BinaryAssociation(
    name="parent9",
    ends={
        Property(name="ClassMM_Class10", type=ClassMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassMM_Class8", type=ClassMM_Class, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ClassMM_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=ClassMM_PrimitiveDataType)
gen_ClassMM_Class_Classifier = Generalization(general=Classifier, specific=ClassMM_Class)

# Domain Model
domain_model = DomainModel(
    name="ClassMM",
    types={ClassMM_Classifier, ClassMM_PrimitiveDataType, ClassMM_ClassModel, ClassMM_Association, ClassMM_Class, ClassMM_Attribute, Classifier},
    associations={classifier11, association13, src0, dest1, type4, attrs5, parent9},
    generalizations={gen_ClassMM_PrimitiveDataType_Classifier, gen_ClassMM_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)