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
wh_Import = Class(name="wh::Import")
wh_Type = Class(name="wh::Type")
wh_DataType = Class(name="wh::DataType")
Type = Class(name="Type")
wh_Entity = Class(name="wh::Entity")
wh_Wh = Class(name="wh::Wh")
wh_AbstractElement = Class(name="wh::AbstractElement")
wh_PackageDeclaration = Class(name="wh::PackageDeclaration")
AbstractElement = Class(name="AbstractElement")
wh_Feature = Class(name="wh::Feature")

# wh_Import class attributes and methods
wh_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
wh_Import.attributes={wh_Import_importedNamespace}

# wh_Type class attributes and methods
wh_Type_name: Property = Property(name="name", type=StringType)
wh_Type.attributes={wh_Type_name}

# wh_DataType class attributes and methods

# Type class attributes and methods

# wh_Entity class attributes and methods

# wh_Wh class attributes and methods

# wh_AbstractElement class attributes and methods

# wh_PackageDeclaration class attributes and methods
wh_PackageDeclaration_name: Property = Property(name="name", type=StringType)
wh_PackageDeclaration.attributes={wh_PackageDeclaration_name}

# AbstractElement class attributes and methods

# wh_Feature class attributes and methods
wh_Feature_many: Property = Property(name="many", type=BooleanType)
wh_Feature_name: Property = Property(name="name", type=StringType)
wh_Feature.attributes={wh_Feature_name, wh_Feature_many}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="wh_AbstractElement", type=wh_Wh, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Wh", type=wh_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="wh_AbstractElement2", type=wh_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_PackageDeclaration", type=wh_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="wh_Entity", type=wh_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Entity3", type=wh_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="wh_Feature", type=wh_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Entity6", type=wh_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="wh_Type", type=wh_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Feature8", type=wh_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_wh_Import_AbstractElement = Generalization(general=AbstractElement, specific=wh_Import)
gen_wh_Type_AbstractElement = Generalization(general=AbstractElement, specific=wh_Type)
gen_wh_DataType_Type = Generalization(general=Type, specific=wh_DataType)
gen_wh_Entity_Type = Generalization(general=Type, specific=wh_Entity)
gen_wh_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=wh_PackageDeclaration)

# Domain Model
domain_model = DomainModel(
    name="wh",
    types={wh_Import, wh_Type, wh_DataType, Type, wh_Entity, wh_Wh, wh_AbstractElement, wh_PackageDeclaration, AbstractElement, wh_Feature},
    associations={elements0, elements1, superType4, features5, type7},
    generalizations={gen_wh_Import_AbstractElement, gen_wh_Type_AbstractElement, gen_wh_DataType_Type, gen_wh_Entity_Type, gen_wh_PackageDeclaration_AbstractElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)