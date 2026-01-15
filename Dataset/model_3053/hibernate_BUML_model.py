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
            EnumerationLiteral(name="Object"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Long"),
			EnumerationLiteral(name="Double")
    }
)

# Classes
hibernate_Entity = Class(name="hibernate::Entity")
hibernate_NamedElement = Class(name="hibernate::NamedElement", is_abstract=True)
hibernate_Module = Class(name="hibernate::Module")
NamedElement = Class(name="NamedElement")
hibernate_Package = Class(name="hibernate::Package")
hibernate_Reference = Class(name="hibernate::Reference")
Feature = Class(name="Feature")
hibernate_Feature = Class(name="hibernate::Feature", is_abstract=True)
hibernate_DataType = Class(name="hibernate::DataType")

# hibernate_Entity class attributes and methods
hibernate_Entity_annotations: Property = Property(name="annotations", type=StringType)
hibernate_Entity.attributes={hibernate_Entity_annotations}

# hibernate_NamedElement class attributes and methods
hibernate_NamedElement_name: Property = Property(name="name", type=StringType)
hibernate_NamedElement.attributes={hibernate_NamedElement_name}

# hibernate_Module class attributes and methods

# NamedElement class attributes and methods

# hibernate_Package class attributes and methods

# hibernate_Reference class attributes and methods

# Feature class attributes and methods

# hibernate_Feature class attributes and methods
hibernate_Feature_many: Property = Property(name="many", type=BooleanType)
hibernate_Feature_annotations: Property = Property(name="annotations", type=StringType)
hibernate_Feature.attributes={hibernate_Feature_annotations, hibernate_Feature_many}

# hibernate_DataType class attributes and methods
hibernate_DataType_type: Property = Property(name="type", type=StringType)
hibernate_DataType.attributes={hibernate_DataType_type}

# Relationships
entities1: BinaryAssociation = BinaryAssociation(
    name="entities1",
    ends={
        Property(name="hibernate_Entity", type=hibernate_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="hibernate_Package2", type=hibernate_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="hibernate_Package", type=hibernate_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="hibernate_Module", type=hibernate_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference8: BinaryAssociation = BinaryAssociation(
    name="reference8",
    ends={
        Property(name="hibernate_Entity9", type=hibernate_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="hibernate_Reference", type=hibernate_Entity, multiplicity=Multiplicity(1, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="hibernate_Feature", type=hibernate_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="hibernate_Entity4", type=hibernate_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superEntity6: BinaryAssociation = BinaryAssociation(
    name="superEntity6",
    ends={
        Property(name="hibernate_Entity7", type=hibernate_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="hibernate_Entity5", type=hibernate_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_hibernate_Package_NamedElement = Generalization(general=NamedElement, specific=hibernate_Package)
gen_hibernate_Entity_NamedElement = Generalization(general=NamedElement, specific=hibernate_Entity)
gen_hibernate_Module_NamedElement = Generalization(general=NamedElement, specific=hibernate_Module)
gen_hibernate_Feature_NamedElement = Generalization(general=NamedElement, specific=hibernate_Feature)
gen_hibernate_Reference_Feature = Generalization(general=Feature, specific=hibernate_Reference)
gen_hibernate_DataType_Feature = Generalization(general=Feature, specific=hibernate_DataType)

# Domain Model
domain_model = DomainModel(
    name="hibernate",
    types={hibernate_Entity, hibernate_NamedElement, hibernate_Module, NamedElement, hibernate_Package, hibernate_Reference, Feature, hibernate_Feature, hibernate_DataType, EntityAnnotation, FetureAnnotation, DataTypes},
    associations={entities1, packages0, reference8, features3, superEntity6},
    generalizations={gen_hibernate_Package_NamedElement, gen_hibernate_Entity_NamedElement, gen_hibernate_Module_NamedElement, gen_hibernate_Feature_NamedElement, gen_hibernate_Reference_Feature, gen_hibernate_DataType_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)