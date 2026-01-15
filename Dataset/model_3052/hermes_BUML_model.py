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
EntityAnnotation: Enumeration = Enumeration(
    name="EntityAnnotation",
    literals={
            EnumerationLiteral(name="Cache")
    }
)

FetureAnnotation: Enumeration = Enumeration(
    name="FetureAnnotation",
    literals={
            EnumerationLiteral(name="Index"),
			EnumerationLiteral(name="Id"),
			EnumerationLiteral(name="Load"),
			EnumerationLiteral(name="Ignore")
    }
)

DataTypes: Enumeration = Enumeration(
    name="DataTypes",
    literals={
            EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Long"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Object"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer")
    }
)

# Classes
hermes_Package = Class(name="hermes::Package")
hermes_Entity = Class(name="hermes::Entity")
hermes_NamedElement = Class(name="hermes::NamedElement", is_abstract=True)
hermes_Module = Class(name="hermes::Module")
NamedElement = Class(name="NamedElement")
hermes_Reference = Class(name="hermes::Reference")
Feature = Class(name="Feature")
hermes_DataType = Class(name="hermes::DataType")
hermes_Feature = Class(name="hermes::Feature", is_abstract=True)

# hermes_Package class attributes and methods

# hermes_Entity class attributes and methods
hermes_Entity_annotations: Property = Property(name="annotations", type=StringType)
hermes_Entity.attributes={hermes_Entity_annotations}

# hermes_NamedElement class attributes and methods
hermes_NamedElement_name: Property = Property(name="name", type=StringType)
hermes_NamedElement.attributes={hermes_NamedElement_name}

# hermes_Module class attributes and methods

# NamedElement class attributes and methods

# hermes_Reference class attributes and methods

# Feature class attributes and methods

# hermes_DataType class attributes and methods
hermes_DataType_type: Property = Property(name="type", type=StringType)
hermes_DataType.attributes={hermes_DataType_type}

# hermes_Feature class attributes and methods
hermes_Feature_many: Property = Property(name="many", type=BooleanType)
hermes_Feature_annotations: Property = Property(name="annotations", type=StringType)
hermes_Feature.attributes={hermes_Feature_many, hermes_Feature_annotations}

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="hermes_Package", type=hermes_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="hermes_Module", type=hermes_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities1: BinaryAssociation = BinaryAssociation(
    name="entities1",
    ends={
        Property(name="hermes_Entity", type=hermes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="hermes_Package2", type=hermes_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference8: BinaryAssociation = BinaryAssociation(
    name="reference8",
    ends={
        Property(name="hermes_Entity9", type=hermes_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="hermes_Reference", type=hermes_Entity, multiplicity=Multiplicity(1, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="hermes_Feature", type=hermes_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="hermes_Entity4", type=hermes_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superEntity6: BinaryAssociation = BinaryAssociation(
    name="superEntity6",
    ends={
        Property(name="hermes_Entity7", type=hermes_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="hermes_Entity5", type=hermes_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_hermes_Package_NamedElement = Generalization(general=NamedElement, specific=hermes_Package)
gen_hermes_Entity_NamedElement = Generalization(general=NamedElement, specific=hermes_Entity)
gen_hermes_Module_NamedElement = Generalization(general=NamedElement, specific=hermes_Module)
gen_hermes_Feature_NamedElement = Generalization(general=NamedElement, specific=hermes_Feature)
gen_hermes_Reference_Feature = Generalization(general=Feature, specific=hermes_Reference)
gen_hermes_DataType_Feature = Generalization(general=Feature, specific=hermes_DataType)

# Domain Model
domain_model = DomainModel(
    name="hermes",
    types={hermes_Package, hermes_Entity, hermes_NamedElement, hermes_Module, NamedElement, hermes_Reference, Feature, hermes_DataType, hermes_Feature, EntityAnnotation, FetureAnnotation, DataTypes},
    associations={packages0, entities1, reference8, features3, superEntity6},
    generalizations={gen_hermes_Package_NamedElement, gen_hermes_Entity_NamedElement, gen_hermes_Module_NamedElement, gen_hermes_Feature_NamedElement, gen_hermes_Reference_Feature, gen_hermes_DataType_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)