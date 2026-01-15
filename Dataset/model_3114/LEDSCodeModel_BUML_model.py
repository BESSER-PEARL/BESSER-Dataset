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
StereotypeClass: Enumeration = Enumeration(
    name="StereotypeClass",
    literals={
            EnumerationLiteral(name="View"),
			EnumerationLiteral(name="Security"),
			EnumerationLiteral(name="Entity")
    }
)

PrimitiveData: Enumeration = Enumeration(
    name="PrimitiveData",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="byte"),
			EnumerationLiteral(name="short"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="char"),
			EnumerationLiteral(name="boolean")
    }
)

StereotypeAttribute: Enumeration = Enumeration(
    name="StereotypeAttribute",
    literals={
            EnumerationLiteral(name="Password"),
			EnumerationLiteral(name="User")
    }
)

# Classes
LedsCodeModel_AbstractClass = Class(name="LedsCodeModel::AbstractClass", is_abstract=True)
LedsCodeModel_Class = Class(name="LedsCodeModel::Class")
AbstractClass = Class(name="AbstractClass")
LedsCodeModel_Attribute = Class(name="LedsCodeModel::Attribute")
LedsCodeModel_Specification = Class(name="LedsCodeModel::Specification")
LedsCodeModel_Model = Class(name="LedsCodeModel::Model", is_abstract=True)
LedsCodeModel_Feature = Class(name="LedsCodeModel::Feature")
LedsCodeModel_ClassDiagram = Class(name="LedsCodeModel::ClassDiagram")
Model = Class(name="Model")
LedsCodeModel_ENUM = Class(name="LedsCodeModel::ENUM")
LedsCodeModel_Classifier = Class(name="LedsCodeModel::Classifier", is_abstract=True)
LedsCodeModel_PrimitiveDataType = Class(name="LedsCodeModel::PrimitiveDataType")
Classifier = Class(name="Classifier")
LedsCodeModel_Association = Class(name="LedsCodeModel::Association")

# LedsCodeModel_AbstractClass class attributes and methods

# LedsCodeModel_Class class attributes and methods
LedsCodeModel_Class_abstract: Property = Property(name="abstract", type=BooleanType)
LedsCodeModel_Class_stereotypeClass: Property = Property(name="stereotypeClass", type=StringType)
LedsCodeModel_Class.attributes={LedsCodeModel_Class_stereotypeClass, LedsCodeModel_Class_abstract}

# AbstractClass class attributes and methods

# LedsCodeModel_Attribute class attributes and methods
LedsCodeModel_Attribute_name: Property = Property(name="name", type=StringType)
LedsCodeModel_Attribute.attributes={LedsCodeModel_Attribute_name}

# LedsCodeModel_Specification class attributes and methods
LedsCodeModel_Specification_name: Property = Property(name="name", type=StringType)
LedsCodeModel_Specification_createdDate: Property = Property(name="createdDate", type=DateType)
LedsCodeModel_Specification.attributes={LedsCodeModel_Specification_name, LedsCodeModel_Specification_createdDate}

# LedsCodeModel_Model class attributes and methods

# LedsCodeModel_Feature class attributes and methods
LedsCodeModel_Feature_language: Property = Property(name="language", type=StringType)
LedsCodeModel_Feature_dataBaseName: Property = Property(name="dataBaseName", type=StringType)
LedsCodeModel_Feature_engine: Property = Property(name="engine", type=StringType)
LedsCodeModel_Feature_orm: Property = Property(name="orm", type=StringType)
LedsCodeModel_Feature_applicationType: Property = Property(name="applicationType", type=StringType)
LedsCodeModel_Feature.attributes={LedsCodeModel_Feature_engine, LedsCodeModel_Feature_dataBaseName, LedsCodeModel_Feature_orm, LedsCodeModel_Feature_language, LedsCodeModel_Feature_applicationType}

# LedsCodeModel_ClassDiagram class attributes and methods
LedsCodeModel_ClassDiagram_name: Property = Property(name="name", type=StringType)
LedsCodeModel_ClassDiagram.attributes={LedsCodeModel_ClassDiagram_name}

# Model class attributes and methods

# LedsCodeModel_ENUM class attributes and methods
LedsCodeModel_ENUM_values: Property = Property(name="values", type=StringType)
LedsCodeModel_ENUM.attributes={LedsCodeModel_ENUM_values}

# LedsCodeModel_Classifier class attributes and methods
LedsCodeModel_Classifier_name: Property = Property(name="name", type=StringType)
LedsCodeModel_Classifier.attributes={LedsCodeModel_Classifier_name}

# LedsCodeModel_PrimitiveDataType class attributes and methods
LedsCodeModel_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
LedsCodeModel_PrimitiveDataType.attributes={LedsCodeModel_PrimitiveDataType_type}

# Classifier class attributes and methods

# LedsCodeModel_Association class attributes and methods
LedsCodeModel_Association_name: Property = Property(name="name", type=StringType)
LedsCodeModel_Association.attributes={LedsCodeModel_Association_name}

# Relationships
composed3: BinaryAssociation = BinaryAssociation(
    name="composed3",
    ends={
        Property(name="LedsCodeModel_AbstractClass", type=LedsCodeModel_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="LedsCodeModel_ClassDiagram", type=LedsCodeModel_AbstractClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="LedsCodeModel_Attribute", type=LedsCodeModel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="LedsCodeModel_Class", type=LedsCodeModel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent6: BinaryAssociation = BinaryAssociation(
    name="parent6",
    ends={
        Property(name="LedsCodeModel_Class7", type=LedsCodeModel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="LedsCodeModel_Class5", type=LedsCodeModel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
has0: BinaryAssociation = BinaryAssociation(
    name="has0",
    ends={
        Property(name="LedsCodeModel_Model", type=LedsCodeModel_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="LedsCodeModel_Specification", type=LedsCodeModel_Model, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
described1: BinaryAssociation = BinaryAssociation(
    name="described1",
    ends={
        Property(name="LedsCodeModel_Feature", type=LedsCodeModel_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="LedsCodeModel_Specification2", type=LedsCodeModel_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="LedsCodeModel_Classifier", type=LedsCodeModel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="LedsCodeModel_Attribute9", type=LedsCodeModel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="LedsCodeModel_Class11", type=LedsCodeModel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="LedsCodeModel_Association", type=LedsCodeModel_Class, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="LedsCodeModel_Class14", type=LedsCodeModel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="LedsCodeModel_Association13", type=LedsCodeModel_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_LedsCodeModel_Class_AbstractClass = Generalization(general=AbstractClass, specific=LedsCodeModel_Class)
gen_LedsCodeModel_ClassDiagram_Model = Generalization(general=Model, specific=LedsCodeModel_ClassDiagram)
gen_LedsCodeModel_AbstractClass_Classifier = Generalization(general=Classifier, specific=LedsCodeModel_AbstractClass)
gen_LedsCodeModel_ENUM_AbstractClass = Generalization(general=AbstractClass, specific=LedsCodeModel_ENUM)
gen_LedsCodeModel_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=LedsCodeModel_PrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="LedsCodeModel",
    types={LedsCodeModel_AbstractClass, LedsCodeModel_Class, AbstractClass, LedsCodeModel_Attribute, LedsCodeModel_Specification, LedsCodeModel_Model, LedsCodeModel_Feature, LedsCodeModel_ClassDiagram, Model, LedsCodeModel_ENUM, LedsCodeModel_Classifier, LedsCodeModel_PrimitiveDataType, Classifier, LedsCodeModel_Association, StereotypeClass, PrimitiveData, StereotypeAttribute},
    associations={composed3, attributes4, parent6, has0, described1, type8, target10, source12},
    generalizations={gen_LedsCodeModel_Class_AbstractClass, gen_LedsCodeModel_ClassDiagram_Model, gen_LedsCodeModel_AbstractClass_Classifier, gen_LedsCodeModel_ENUM_AbstractClass, gen_LedsCodeModel_PrimitiveDataType_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)