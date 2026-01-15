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
ling_Domainmodel = Class(name="ling::Domainmodel")
ling_Import = Class(name="ling::Import")
ling_Type = Class(name="ling::Type")
ling_DataType = Class(name="ling::DataType")
Type = Class(name="Type")
ling_Entity = Class(name="ling::Entity")
ling_AbstractElement = Class(name="ling::AbstractElement")
ling_PackageDeclaration = Class(name="ling::PackageDeclaration")
AbstractElement = Class(name="AbstractElement")
ling_Feature = Class(name="ling::Feature")

# ling_Domainmodel class attributes and methods

# ling_Import class attributes and methods
ling_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
ling_Import.attributes={ling_Import_importedNamespace}

# ling_Type class attributes and methods
ling_Type_name: Property = Property(name="name", type=StringType)
ling_Type.attributes={ling_Type_name}

# ling_DataType class attributes and methods

# Type class attributes and methods

# ling_Entity class attributes and methods

# ling_AbstractElement class attributes and methods

# ling_PackageDeclaration class attributes and methods
ling_PackageDeclaration_name: Property = Property(name="name", type=StringType)
ling_PackageDeclaration.attributes={ling_PackageDeclaration_name}

# AbstractElement class attributes and methods

# ling_Feature class attributes and methods
ling_Feature_many: Property = Property(name="many", type=BooleanType)
ling_Feature_name: Property = Property(name="name", type=StringType)
ling_Feature.attributes={ling_Feature_many, ling_Feature_name}

# Relationships
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="ling_AbstractElement2", type=ling_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ling_PackageDeclaration", type=ling_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="ling_Entity", type=ling_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="ling_Entity3", type=ling_Entity, multiplicity=Multiplicity(0, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="ling_AbstractElement", type=ling_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="ling_Domainmodel", type=ling_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="ling_Type", type=ling_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ling_Feature8", type=ling_Type, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="ling_Feature", type=ling_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="ling_Entity6", type=ling_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ling_Import_AbstractElement = Generalization(general=AbstractElement, specific=ling_Import)
gen_ling_Type_AbstractElement = Generalization(general=AbstractElement, specific=ling_Type)
gen_ling_DataType_Type = Generalization(general=Type, specific=ling_DataType)
gen_ling_Entity_Type = Generalization(general=Type, specific=ling_Entity)
gen_ling_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=ling_PackageDeclaration)

# Domain Model
domain_model = DomainModel(
    name="ling",
    types={ling_Domainmodel, ling_Import, ling_Type, ling_DataType, Type, ling_Entity, ling_AbstractElement, ling_PackageDeclaration, AbstractElement, ling_Feature},
    associations={elements1, superType4, elements0, type7, features5},
    generalizations={gen_ling_Import_AbstractElement, gen_ling_Type_AbstractElement, gen_ling_DataType_Type, gen_ling_Entity_Type, gen_ling_PackageDeclaration_AbstractElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)