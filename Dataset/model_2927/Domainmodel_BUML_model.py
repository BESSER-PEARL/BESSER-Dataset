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
domainmodel_Domainmodel = Class(name="domainmodel::Domainmodel")
domainmodel_AbstractElement = Class(name="domainmodel::AbstractElement")
domainmodel_PackageDec = Class(name="domainmodel::PackageDec")
AbstractElement = Class(name="AbstractElement")
domainmodel_Type = Class(name="domainmodel::Type")
domainmodel_DataType = Class(name="domainmodel::DataType")
Type = Class(name="Type")
domainmodel_Entity = Class(name="domainmodel::Entity")
domainmodel_Feature = Class(name="domainmodel::Feature")
domainmodel_Import = Class(name="domainmodel::Import")

# domainmodel_Domainmodel class attributes and methods

# domainmodel_AbstractElement class attributes and methods

# domainmodel_PackageDec class attributes and methods
domainmodel_PackageDec_name: Property = Property(name="name", type=StringType)
domainmodel_PackageDec.attributes={domainmodel_PackageDec_name}

# AbstractElement class attributes and methods

# domainmodel_Type class attributes and methods
domainmodel_Type_name: Property = Property(name="name", type=StringType)
domainmodel_Type.attributes={domainmodel_Type_name}

# domainmodel_DataType class attributes and methods

# Type class attributes and methods

# domainmodel_Entity class attributes and methods

# domainmodel_Feature class attributes and methods
domainmodel_Feature_many: Property = Property(name="many", type=BooleanType)
domainmodel_Feature_name: Property = Property(name="name", type=StringType)
domainmodel_Feature.attributes={domainmodel_Feature_name, domainmodel_Feature_many}

# domainmodel_Import class attributes and methods
domainmodel_Import_importedNameSpace: Property = Property(name="importedNameSpace", type=StringType)
domainmodel_Import.attributes={domainmodel_Import_importedNameSpace}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="domainmodel_AbstractElement", type=domainmodel_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Domainmodel", type=domainmodel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element1: BinaryAssociation = BinaryAssociation(
    name="element1",
    ends={
        Property(name="domainmodel_AbstractElement2", type=domainmodel_PackageDec, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_PackageDec", type=domainmodel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="domainmodel_Entity", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity3", type=domainmodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="domainmodel_Feature", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity6", type=domainmodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="domainmodel_Type", type=domainmodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Feature8", type=domainmodel_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_domainmodel_PackageDec_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_PackageDec)
gen_domainmodel_Type_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_Type)
gen_domainmodel_DataType_Type = Generalization(general=Type, specific=domainmodel_DataType)
gen_domainmodel_Entity_Type = Generalization(general=Type, specific=domainmodel_Entity)
gen_domainmodel_Import_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_Import)

# Domain Model
domain_model = DomainModel(
    name="domainmodel",
    types={domainmodel_Domainmodel, domainmodel_AbstractElement, domainmodel_PackageDec, AbstractElement, domainmodel_Type, domainmodel_DataType, Type, domainmodel_Entity, domainmodel_Feature, domainmodel_Import},
    associations={elements0, element1, superType4, features5, type7},
    generalizations={gen_domainmodel_PackageDec_AbstractElement, gen_domainmodel_Type_AbstractElement, gen_domainmodel_DataType_Type, gen_domainmodel_Entity_Type, gen_domainmodel_Import_AbstractElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)