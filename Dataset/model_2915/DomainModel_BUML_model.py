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
domainModel_AbstractElement = Class(name="domainModel::AbstractElement")
domainModel_PackageDeclaration = Class(name="domainModel::PackageDeclaration")
AbstractElement = Class(name="AbstractElement")
domainModel_Model = Class(name="domainModel::Model")
domainModel_Feature = Class(name="domainModel::Feature")
domainModel_Import = Class(name="domainModel::Import")
domainModel_Type = Class(name="domainModel::Type")
domainModel_DataType = Class(name="domainModel::DataType")
Type = Class(name="Type")
domainModel_Entity = Class(name="domainModel::Entity")

# domainModel_AbstractElement class attributes and methods

# domainModel_PackageDeclaration class attributes and methods
domainModel_PackageDeclaration_name: Property = Property(name="name", type=StringType)
domainModel_PackageDeclaration.attributes={domainModel_PackageDeclaration_name}

# AbstractElement class attributes and methods

# domainModel_Model class attributes and methods

# domainModel_Feature class attributes and methods
domainModel_Feature_many: Property = Property(name="many", type=BooleanType)
domainModel_Feature_name: Property = Property(name="name", type=StringType)
domainModel_Feature.attributes={domainModel_Feature_many, domainModel_Feature_name}

# domainModel_Import class attributes and methods
domainModel_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
domainModel_Import.attributes={domainModel_Import_importedNamespace}

# domainModel_Type class attributes and methods
domainModel_Type_name: Property = Property(name="name", type=StringType)
domainModel_Type.attributes={domainModel_Type_name}

# domainModel_DataType class attributes and methods

# Type class attributes and methods

# domainModel_Entity class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="domainModel_AbstractElement", type=domainModel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="domainModel_Model", type=domainModel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="domainModel_AbstractElement2", type=domainModel_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="domainModel_PackageDeclaration", type=domainModel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="domainModel_Entity3", type=domainModel_Entity, multiplicity=Multiplicity(0, 1)),
        Property(name="domainModel_Entity", type=domainModel_Entity, multiplicity=Multiplicity(1, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="domainModel_Feature", type=domainModel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainModel_Entity6", type=domainModel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="domainModel_Type", type=domainModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainModel_Feature8", type=domainModel_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_domainModel_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=domainModel_PackageDeclaration)
gen_domainModel_Import_AbstractElement = Generalization(general=AbstractElement, specific=domainModel_Import)
gen_domainModel_Type_AbstractElement = Generalization(general=AbstractElement, specific=domainModel_Type)
gen_domainModel_DataType_Type = Generalization(general=Type, specific=domainModel_DataType)
gen_domainModel_Entity_Type = Generalization(general=Type, specific=domainModel_Entity)

# Domain Model
domain_model = DomainModel(
    name="domainModel",
    types={domainModel_AbstractElement, domainModel_PackageDeclaration, AbstractElement, domainModel_Model, domainModel_Feature, domainModel_Import, domainModel_Type, domainModel_DataType, Type, domainModel_Entity},
    associations={elements0, elements1, superType4, features5, type7},
    generalizations={gen_domainModel_PackageDeclaration_AbstractElement, gen_domainModel_Import_AbstractElement, gen_domainModel_Type_AbstractElement, gen_domainModel_DataType_Type, gen_domainModel_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)