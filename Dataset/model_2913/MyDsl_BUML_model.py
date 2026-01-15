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
myDsl_Model = Class(name="myDsl::Model")
myDsl_AbstractElement = Class(name="myDsl::AbstractElement")
myDsl_PackageDeclaration = Class(name="myDsl::PackageDeclaration")
AbstractElement = Class(name="AbstractElement")
myDsl_Type = Class(name="myDsl::Type")
myDsl_DataType = Class(name="myDsl::DataType")
Type = Class(name="Type")
myDsl_Import = Class(name="myDsl::Import")
myDsl_Entity = Class(name="myDsl::Entity")
myDsl_Feature = Class(name="myDsl::Feature")

# myDsl_Model class attributes and methods

# myDsl_AbstractElement class attributes and methods

# myDsl_PackageDeclaration class attributes and methods
myDsl_PackageDeclaration_name: Property = Property(name="name", type=StringType)
myDsl_PackageDeclaration.attributes={myDsl_PackageDeclaration_name}

# AbstractElement class attributes and methods

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# myDsl_DataType class attributes and methods

# Type class attributes and methods

# myDsl_Import class attributes and methods
myDsl_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
myDsl_Import.attributes={myDsl_Import_importedNamespace}

# myDsl_Entity class attributes and methods

# myDsl_Feature class attributes and methods
myDsl_Feature_many: Property = Property(name="many", type=BooleanType)
myDsl_Feature_name: Property = Property(name="name", type=StringType)
myDsl_Feature.attributes={myDsl_Feature_many, myDsl_Feature_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myDsl_AbstractElement", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="myDsl_AbstractElement2", type=myDsl_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PackageDeclaration", type=myDsl_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="myDsl_Entity", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity3", type=myDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="myDsl_Feature", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity6", type=myDsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="myDsl_Type", type=myDsl_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Feature8", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=myDsl_PackageDeclaration)
gen_myDsl_Type_AbstractElement = Generalization(general=AbstractElement, specific=myDsl_Type)
gen_myDsl_DataType_Type = Generalization(general=Type, specific=myDsl_DataType)
gen_myDsl_Import_AbstractElement = Generalization(general=AbstractElement, specific=myDsl_Import)
gen_myDsl_Entity_Type = Generalization(general=Type, specific=myDsl_Entity)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_AbstractElement, myDsl_PackageDeclaration, AbstractElement, myDsl_Type, myDsl_DataType, Type, myDsl_Import, myDsl_Entity, myDsl_Feature},
    associations={elements0, elements1, superType4, features5, type7},
    generalizations={gen_myDsl_PackageDeclaration_AbstractElement, gen_myDsl_Type_AbstractElement, gen_myDsl_DataType_Type, gen_myDsl_Import_AbstractElement, gen_myDsl_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)