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
AbstractElement = Class(name="AbstractElement")
aGES_Import = Class(name="aGES::Import")
aGES_Type = Class(name="aGES::Type")
aGES_Domainmodel = Class(name="aGES::Domainmodel")
aGES_AbstractElement = Class(name="aGES::AbstractElement")
aGES_PackageDeclaration = Class(name="aGES::PackageDeclaration")
aGES_DataType = Class(name="aGES::DataType")
Type = Class(name="Type")
aGES_Entity = Class(name="aGES::Entity")
aGES_Feature = Class(name="aGES::Feature")

# AbstractElement class attributes and methods

# aGES_Import class attributes and methods
aGES_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
aGES_Import.attributes={aGES_Import_importedNamespace}

# aGES_Type class attributes and methods
aGES_Type_name: Property = Property(name="name", type=StringType)
aGES_Type.attributes={aGES_Type_name}

# aGES_Domainmodel class attributes and methods

# aGES_AbstractElement class attributes and methods

# aGES_PackageDeclaration class attributes and methods
aGES_PackageDeclaration_name: Property = Property(name="name", type=StringType)
aGES_PackageDeclaration.attributes={aGES_PackageDeclaration_name}

# aGES_DataType class attributes and methods

# Type class attributes and methods

# aGES_Entity class attributes and methods

# aGES_Feature class attributes and methods
aGES_Feature_many: Property = Property(name="many", type=BooleanType)
aGES_Feature_name: Property = Property(name="name", type=StringType)
aGES_Feature.attributes={aGES_Feature_many, aGES_Feature_name}

# Relationships
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="aGES_AbstractElement2", type=aGES_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aGES_PackageDeclaration", type=aGES_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="aGES_AbstractElement", type=aGES_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="aGES_Domainmodel", type=aGES_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="aGES_Entity", type=aGES_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="aGES_Entity3", type=aGES_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="aGES_Feature", type=aGES_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="aGES_Entity6", type=aGES_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="aGES_Type", type=aGES_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aGES_Feature8", type=aGES_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_aGES_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=aGES_PackageDeclaration)
gen_aGES_Import_AbstractElement = Generalization(general=AbstractElement, specific=aGES_Import)
gen_aGES_Type_AbstractElement = Generalization(general=AbstractElement, specific=aGES_Type)
gen_aGES_DataType_Type = Generalization(general=Type, specific=aGES_DataType)
gen_aGES_Entity_Type = Generalization(general=Type, specific=aGES_Entity)

# Domain Model
domain_model = DomainModel(
    name="aGES",
    types={AbstractElement, aGES_Import, aGES_Type, aGES_Domainmodel, aGES_AbstractElement, aGES_PackageDeclaration, aGES_DataType, Type, aGES_Entity, aGES_Feature},
    associations={elements1, elements0, superType4, features5, type7},
    generalizations={gen_aGES_PackageDeclaration_AbstractElement, gen_aGES_Import_AbstractElement, gen_aGES_Type_AbstractElement, gen_aGES_DataType_Type, gen_aGES_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)