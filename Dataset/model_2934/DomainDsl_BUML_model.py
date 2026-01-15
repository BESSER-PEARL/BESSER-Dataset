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
domainDsl_Domainmodel = Class(name="domainDsl::Domainmodel")
domainDsl_AbstractElement = Class(name="domainDsl::AbstractElement")
domainDsl_PackageDeclaration = Class(name="domainDsl::PackageDeclaration")
AbstractElement = Class(name="AbstractElement")
domainDsl_Import = Class(name="domainDsl::Import")
domainDsl_EType = Class(name="domainDsl::EType")
domainDsl_Type = Class(name="domainDsl::Type")
domainDsl_DataType = Class(name="domainDsl::DataType")
Type = Class(name="Type")
domainDsl_Entity = Class(name="domainDsl::Entity")
domainDsl_Feature = Class(name="domainDsl::Feature")
domainDsl_Validator = Class(name="domainDsl::Validator")

# domainDsl_Domainmodel class attributes and methods

# domainDsl_AbstractElement class attributes and methods

# domainDsl_PackageDeclaration class attributes and methods
domainDsl_PackageDeclaration_name: Property = Property(name="name", type=StringType)
domainDsl_PackageDeclaration.attributes={domainDsl_PackageDeclaration_name}

# AbstractElement class attributes and methods

# domainDsl_Import class attributes and methods
domainDsl_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
domainDsl_Import.attributes={domainDsl_Import_importedNamespace}

# domainDsl_EType class attributes and methods
domainDsl_EType_name: Property = Property(name="name", type=StringType)
domainDsl_EType.attributes={domainDsl_EType_name}

# domainDsl_Type class attributes and methods
domainDsl_Type_name: Property = Property(name="name", type=StringType)
domainDsl_Type.attributes={domainDsl_Type_name}

# domainDsl_DataType class attributes and methods

# Type class attributes and methods

# domainDsl_Entity class attributes and methods

# domainDsl_Feature class attributes and methods
domainDsl_Feature_many: Property = Property(name="many", type=BooleanType)
domainDsl_Feature_name: Property = Property(name="name", type=StringType)
domainDsl_Feature_defaultVal: Property = Property(name="defaultVal", type=StringType)
domainDsl_Feature.attributes={domainDsl_Feature_defaultVal, domainDsl_Feature_many, domainDsl_Feature_name}

# domainDsl_Validator class attributes and methods
domainDsl_Validator_name: Property = Property(name="name", type=StringType)
domainDsl_Validator_value: Property = Property(name="value", type=IntegerType)
domainDsl_Validator_svalue: Property = Property(name="svalue", type=StringType)
domainDsl_Validator.attributes={domainDsl_Validator_svalue, domainDsl_Validator_name, domainDsl_Validator_value}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="domainDsl_AbstractElement", type=domainDsl_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="domainDsl_Domainmodel", type=domainDsl_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="domainDsl_AbstractElement2", type=domainDsl_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="domainDsl_PackageDeclaration", type=domainDsl_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="domainDsl_Entity", type=domainDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainDsl_Entity3", type=domainDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="domainDsl_Feature", type=domainDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainDsl_Entity6", type=domainDsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="domainDsl_Type", type=domainDsl_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainDsl_Feature8", type=domainDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
valdiators9: BinaryAssociation = BinaryAssociation(
    name="valdiators9",
    ends={
        Property(name="domainDsl_Validator", type=domainDsl_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainDsl_Feature10", type=domainDsl_Validator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_domainDsl_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=domainDsl_PackageDeclaration)
gen_domainDsl_Import_AbstractElement = Generalization(general=AbstractElement, specific=domainDsl_Import)
gen_domainDsl_Type_AbstractElement = Generalization(general=AbstractElement, specific=domainDsl_Type)
gen_domainDsl_DataType_Type = Generalization(general=Type, specific=domainDsl_DataType)
gen_domainDsl_Entity_Type = Generalization(general=Type, specific=domainDsl_Entity)

# Domain Model
domain_model = DomainModel(
    name="domainDsl",
    types={domainDsl_Domainmodel, domainDsl_AbstractElement, domainDsl_PackageDeclaration, AbstractElement, domainDsl_Import, domainDsl_EType, domainDsl_Type, domainDsl_DataType, Type, domainDsl_Entity, domainDsl_Feature, domainDsl_Validator},
    associations={elements0, elements1, superType4, features5, type7, valdiators9},
    generalizations={gen_domainDsl_PackageDeclaration_AbstractElement, gen_domainDsl_Import_AbstractElement, gen_domainDsl_Type_AbstractElement, gen_domainDsl_DataType_Type, gen_domainDsl_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)