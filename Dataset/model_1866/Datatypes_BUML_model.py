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
datatypes_TypeModel = Class(name="datatypes::TypeModel")
datatypes_AbstractElement = Class(name="datatypes::AbstractElement")
datatypes_DataTypeLibrary = Class(name="datatypes::DataTypeLibrary")
AbstractElement = Class(name="AbstractElement")
datatypes_Import = Class(name="datatypes::Import")
datatypes_DataType = Class(name="datatypes::DataType")
datatypes_SimpleType = Class(name="datatypes::SimpleType")
DataType = Class(name="DataType")
datatypes_ComplexType = Class(name="datatypes::ComplexType")
datatypes_Field = Class(name="datatypes::Field")

# datatypes_TypeModel class attributes and methods

# datatypes_AbstractElement class attributes and methods

# datatypes_DataTypeLibrary class attributes and methods
datatypes_DataTypeLibrary_name: Property = Property(name="name", type=StringType)
datatypes_DataTypeLibrary.attributes={datatypes_DataTypeLibrary_name}

# AbstractElement class attributes and methods

# datatypes_Import class attributes and methods
datatypes_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
datatypes_Import.attributes={datatypes_Import_importedNamespace}

# datatypes_DataType class attributes and methods
datatypes_DataType_name: Property = Property(name="name", type=StringType)
datatypes_DataType.attributes={datatypes_DataType_name}

# datatypes_SimpleType class attributes and methods

# DataType class attributes and methods

# datatypes_ComplexType class attributes and methods

# datatypes_Field class attributes and methods
datatypes_Field_many: Property = Property(name="many", type=BooleanType)
datatypes_Field_name: Property = Property(name="name", type=StringType)
datatypes_Field.attributes={datatypes_Field_many, datatypes_Field_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="datatypes_AbstractElement", type=datatypes_TypeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_TypeModel", type=datatypes_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="datatypes_AbstractElement2", type=datatypes_DataTypeLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_DataTypeLibrary", type=datatypes_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="datatypes_ComplexType", type=datatypes_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_ComplexType3", type=datatypes_ComplexType, multiplicity=Multiplicity(0, 1))
    }
)
fields5: BinaryAssociation = BinaryAssociation(
    name="fields5",
    ends={
        Property(name="datatypes_Field", type=datatypes_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_ComplexType6", type=datatypes_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="datatypes_DataType", type=datatypes_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_Field8", type=datatypes_DataType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_datatypes_DataTypeLibrary_AbstractElement = Generalization(general=AbstractElement, specific=datatypes_DataTypeLibrary)
gen_datatypes_Import_AbstractElement = Generalization(general=AbstractElement, specific=datatypes_Import)
gen_datatypes_DataType_AbstractElement = Generalization(general=AbstractElement, specific=datatypes_DataType)
gen_datatypes_SimpleType_DataType = Generalization(general=DataType, specific=datatypes_SimpleType)
gen_datatypes_ComplexType_DataType = Generalization(general=DataType, specific=datatypes_ComplexType)

# Domain Model
domain_model = DomainModel(
    name="datatypes",
    types={datatypes_TypeModel, datatypes_AbstractElement, datatypes_DataTypeLibrary, AbstractElement, datatypes_Import, datatypes_DataType, datatypes_SimpleType, DataType, datatypes_ComplexType, datatypes_Field},
    associations={elements0, elements1, superType4, fields5, type7},
    generalizations={gen_datatypes_DataTypeLibrary_AbstractElement, gen_datatypes_Import_AbstractElement, gen_datatypes_DataType_AbstractElement, gen_datatypes_SimpleType_DataType, gen_datatypes_ComplexType_DataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)