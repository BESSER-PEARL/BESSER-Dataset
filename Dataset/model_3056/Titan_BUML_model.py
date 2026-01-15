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
InternalDSLType: Enumeration = Enumeration(
    name="InternalDSLType",
    literals={
            EnumerationLiteral(name="NestedFunctions")
    }
)

DataTypes: Enumeration = Enumeration(
    name="DataTypes",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Long"),
			EnumerationLiteral(name="Double")
    }
)

# Classes
titan_Module = Class(name="titan::Module")
titan_Package = Class(name="titan::Package")
titan_Feature = Class(name="titan::Feature")
titan_Reference = Class(name="titan::Reference")
Feature = Class(name="Feature")
titan_MultiReference = Class(name="titan::MultiReference")
titan_SingleReference = Class(name="titan::SingleReference")
Reference = Class(name="Reference")
titan_DataType = Class(name="titan::DataType")
titan_MultiDataType = Class(name="titan::MultiDataType")
titan_SingleDataType = Class(name="titan::SingleDataType")
DataType = Class(name="DataType")
titan_Entity = Class(name="titan::Entity")

# titan_Module class attributes and methods
titan_Module_name: Property = Property(name="name", type=StringType)
titan_Module_type: Property = Property(name="type", type=StringType)
titan_Module.attributes={titan_Module_name, titan_Module_type}

# titan_Package class attributes and methods
titan_Package_name: Property = Property(name="name", type=StringType)
titan_Package.attributes={titan_Package_name}

# titan_Feature class attributes and methods
titan_Feature_name: Property = Property(name="name", type=StringType)
titan_Feature.attributes={titan_Feature_name}

# titan_Reference class attributes and methods
titan_Reference_unique: Property = Property(name="unique", type=BooleanType)
titan_Reference.attributes={titan_Reference_unique}

# Feature class attributes and methods

# titan_MultiReference class attributes and methods

# titan_SingleReference class attributes and methods

# Reference class attributes and methods

# titan_DataType class attributes and methods
titan_DataType_type: Property = Property(name="type", type=StringType)
titan_DataType.attributes={titan_DataType_type}

# titan_MultiDataType class attributes and methods
titan_MultiDataType_unique: Property = Property(name="unique", type=BooleanType)
titan_MultiDataType.attributes={titan_MultiDataType_unique}

# titan_SingleDataType class attributes and methods

# DataType class attributes and methods

# titan_Entity class attributes and methods
titan_Entity_name: Property = Property(name="name", type=StringType)
titan_Entity.attributes={titan_Entity_name}

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="titan_Package", type=titan_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="titan_Module", type=titan_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features6: BinaryAssociation = BinaryAssociation(
    name="features6",
    ends={
        Property(name="titan_Feature", type=titan_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="titan_Entity7", type=titan_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference8: BinaryAssociation = BinaryAssociation(
    name="reference8",
    ends={
        Property(name="titan_Entity9", type=titan_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="titan_Reference", type=titan_Entity, multiplicity=Multiplicity(0, 1))
    }
)
opposite10: BinaryAssociation = BinaryAssociation(
    name="opposite10",
    ends={
        Property(name="titan_MultiReference", type=titan_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="titan_Reference11", type=titan_MultiReference, multiplicity=Multiplicity(0, 1))
    }
)
opposite12: BinaryAssociation = BinaryAssociation(
    name="opposite12",
    ends={
        Property(name="titan_MultiDataType", type=titan_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="titan_DataType", type=titan_MultiDataType, multiplicity=Multiplicity(0, 1))
    }
)
entities1: BinaryAssociation = BinaryAssociation(
    name="entities1",
    ends={
        Property(name="titan_Entity", type=titan_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="titan_Package2", type=titan_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superEntity4: BinaryAssociation = BinaryAssociation(
    name="superEntity4",
    ends={
        Property(name="titan_Entity5", type=titan_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="titan_Entity3", type=titan_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_titan_Reference_Feature = Generalization(general=Feature, specific=titan_Reference)
gen_titan_SingleReference_Reference = Generalization(general=Reference, specific=titan_SingleReference)
gen_titan_MultiReference_Reference = Generalization(general=Reference, specific=titan_MultiReference)
gen_titan_DataType_Feature = Generalization(general=Feature, specific=titan_DataType)
gen_titan_SingleDataType_DataType = Generalization(general=DataType, specific=titan_SingleDataType)
gen_titan_MultiDataType_DataType = Generalization(general=DataType, specific=titan_MultiDataType)

# Domain Model
domain_model = DomainModel(
    name="titan",
    types={titan_Module, titan_Package, titan_Feature, titan_Reference, Feature, titan_MultiReference, titan_SingleReference, Reference, titan_DataType, titan_MultiDataType, titan_SingleDataType, DataType, titan_Entity, InternalDSLType, DataTypes},
    associations={packages0, features6, reference8, opposite10, opposite12, entities1, superEntity4},
    generalizations={gen_titan_Reference_Feature, gen_titan_SingleReference_Reference, gen_titan_MultiReference_Reference, gen_titan_DataType_Feature, gen_titan_SingleDataType_DataType, gen_titan_MultiDataType_DataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)