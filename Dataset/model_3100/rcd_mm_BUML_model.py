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
rcd_Attribute = Class(name="rcd::Attribute")
rcd_Classifier = Class(name="rcd::Classifier", is_abstract=True)
rcd_Association = Class(name="rcd::Association")
rcd_Class = Class(name="rcd::Class")
Classifier = Class(name="Classifier")
rcd_PrimitiveDataType = Class(name="rcd::PrimitiveDataType")
rcd_ClassModel = Class(name="rcd::ClassModel")

# rcd_Attribute class attributes and methods
rcd_Attribute_name: Property = Property(name="name", type=StringType)
rcd_Attribute_is_primary: Property = Property(name="is_primary", type=BooleanType)
rcd_Attribute_upper: Property = Property(name="upper", type=StringType)
rcd_Attribute_lower: Property = Property(name="lower", type=StringType)
rcd_Attribute.attributes={rcd_Attribute_is_primary, rcd_Attribute_upper, rcd_Attribute_name, rcd_Attribute_lower}

# rcd_Classifier class attributes and methods
rcd_Classifier_name: Property = Property(name="name", type=StringType)
rcd_Classifier.attributes={rcd_Classifier_name}

# rcd_Association class attributes and methods
rcd_Association_upper: Property = Property(name="upper", type=StringType)
rcd_Association_lower: Property = Property(name="lower", type=StringType)
rcd_Association_name: Property = Property(name="name", type=StringType)
rcd_Association.attributes={rcd_Association_name, rcd_Association_lower, rcd_Association_upper}

# rcd_Class class attributes and methods
rcd_Class_is_persistent: Property = Property(name="is_persistent", type=BooleanType)
rcd_Class.attributes={rcd_Class_is_persistent}

# Classifier class attributes and methods

# rcd_PrimitiveDataType class attributes and methods

# rcd_ClassModel class attributes and methods
rcd_ClassModel_name: Property = Property(name="name", type=StringType)
rcd_ClassModel.attributes={rcd_ClassModel_name}

# Relationships
dest1: BinaryAssociation = BinaryAssociation(
    name="dest1",
    ends={
        Property(name="rcd_Association2", type=rcd_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="rcd_Class3", type=rcd_Association, multiplicity=Multiplicity(1, 1))
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="rcd_Classifier", type=rcd_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="rcd_Attribute", type=rcd_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
src0: BinaryAssociation = BinaryAssociation(
    name="src0",
    ends={
        Property(name="rcd_Class", type=rcd_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="rcd_Association", type=rcd_Class, multiplicity=Multiplicity(1, 1))
    }
)
association13: BinaryAssociation = BinaryAssociation(
    name="association13",
    ends={
        Property(name="rcd_Association15", type=rcd_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rcd_ClassModel14", type=rcd_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrs5: BinaryAssociation = BinaryAssociation(
    name="attrs5",
    ends={
        Property(name="rcd_Attribute7", type=rcd_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="rcd_Class6", type=rcd_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent9: BinaryAssociation = BinaryAssociation(
    name="parent9",
    ends={
        Property(name="rcd_Class10", type=rcd_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="rcd_Class8", type=rcd_Class, multiplicity=Multiplicity(0, 1))
    }
)
classifier11: BinaryAssociation = BinaryAssociation(
    name="classifier11",
    ends={
        Property(name="rcd_Classifier12", type=rcd_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rcd_ClassModel", type=rcd_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_rcd_Class_Classifier = Generalization(general=Classifier, specific=rcd_Class)
gen_rcd_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=rcd_PrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="rcd",
    types={rcd_Attribute, rcd_Classifier, rcd_Association, rcd_Class, Classifier, rcd_PrimitiveDataType, rcd_ClassModel},
    associations={dest1, type4, src0, association13, attrs5, parent9, classifier11},
    generalizations={gen_rcd_Class_Classifier, gen_rcd_PrimitiveDataType_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)