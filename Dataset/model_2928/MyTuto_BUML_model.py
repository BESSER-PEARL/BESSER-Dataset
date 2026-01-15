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
myTuto_Import = Class(name="myTuto::Import")
myTuto_MyTuto = Class(name="myTuto::MyTuto")
myTuto_AbstractElement = Class(name="myTuto::AbstractElement")
myTuto_PackageDeclaration = Class(name="myTuto::PackageDeclaration")
AbstractElement = Class(name="AbstractElement")
myTuto_Type = Class(name="myTuto::Type")
myTuto_DataType = Class(name="myTuto::DataType")
Type = Class(name="Type")
myTuto_Entity = Class(name="myTuto::Entity")
myTuto_Feature = Class(name="myTuto::Feature")

# myTuto_Import class attributes and methods
myTuto_Import_importedNameSpace: Property = Property(name="importedNameSpace", type=StringType)
myTuto_Import.attributes={myTuto_Import_importedNameSpace}

# myTuto_MyTuto class attributes and methods

# myTuto_AbstractElement class attributes and methods

# myTuto_PackageDeclaration class attributes and methods
myTuto_PackageDeclaration_name: Property = Property(name="name", type=StringType)
myTuto_PackageDeclaration.attributes={myTuto_PackageDeclaration_name}

# AbstractElement class attributes and methods

# myTuto_Type class attributes and methods
myTuto_Type_name: Property = Property(name="name", type=StringType)
myTuto_Type.attributes={myTuto_Type_name}

# myTuto_DataType class attributes and methods

# Type class attributes and methods

# myTuto_Entity class attributes and methods

# myTuto_Feature class attributes and methods
myTuto_Feature_many: Property = Property(name="many", type=BooleanType)
myTuto_Feature_name: Property = Property(name="name", type=StringType)
myTuto_Feature.attributes={myTuto_Feature_name, myTuto_Feature_many}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myTuto_AbstractElement", type=myTuto_MyTuto, multiplicity=Multiplicity(1, 1)),
        Property(name="myTuto_MyTuto", type=myTuto_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="myTuto_AbstractElement2", type=myTuto_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myTuto_PackageDeclaration", type=myTuto_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="myTuto_Type", type=myTuto_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="myTuto_Feature8", type=myTuto_Type, multiplicity=Multiplicity(0, 1))
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="myTuto_Entity", type=myTuto_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myTuto_Entity3", type=myTuto_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="myTuto_Feature", type=myTuto_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myTuto_Entity6", type=myTuto_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myTuto_Import_AbstractElement = Generalization(general=AbstractElement, specific=myTuto_Import)
gen_myTuto_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=myTuto_PackageDeclaration)
gen_myTuto_Type_AbstractElement = Generalization(general=AbstractElement, specific=myTuto_Type)
gen_myTuto_DataType_Type = Generalization(general=Type, specific=myTuto_DataType)
gen_myTuto_Entity_Type = Generalization(general=Type, specific=myTuto_Entity)

# Domain Model
domain_model = DomainModel(
    name="myTuto",
    types={myTuto_Import, myTuto_MyTuto, myTuto_AbstractElement, myTuto_PackageDeclaration, AbstractElement, myTuto_Type, myTuto_DataType, Type, myTuto_Entity, myTuto_Feature},
    associations={elements0, elements1, type7, superType4, features5},
    generalizations={gen_myTuto_Import_AbstractElement, gen_myTuto_PackageDeclaration_AbstractElement, gen_myTuto_Type_AbstractElement, gen_myTuto_DataType_Type, gen_myTuto_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)