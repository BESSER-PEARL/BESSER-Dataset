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
datatypes_SimpleType = Class(name="datatypes::SimpleType")
DataType = Class(name="DataType")
datatypes_ComplexType = Class(name="datatypes::ComplexType", is_abstract=True)
datatypes_RosIDLReference = Class(name="datatypes::RosIDLReference")
IDLReference = Class(name="IDLReference")
datatypes_TypesLibrary = Class(name="datatypes::TypesLibrary")
datatypes_DataType = Class(name="datatypes::DataType", is_abstract=True)
datatypes_IDLReference = Class(name="datatypes::IDLReference", is_abstract=True)
datatypes_VectorType = Class(name="datatypes::VectorType")
ComplexType = Class(name="ComplexType")
datatypes_CustomType = Class(name="datatypes::CustomType")
datatypes_Field = Class(name="datatypes::Field")

# datatypes_SimpleType class attributes and methods

# DataType class attributes and methods

# datatypes_ComplexType class attributes and methods
datatypes_ComplexType_m_getLabel: Method = Method(name="getLabel", parameters={}, type=StringType)
datatypes_ComplexType.methods={datatypes_ComplexType_m_getLabel}

# datatypes_RosIDLReference class attributes and methods
datatypes_RosIDLReference_namespace: Property = Property(name="namespace", type=StringType)
datatypes_RosIDLReference_rosPackage: Property = Property(name="rosPackage", type=StringType)
datatypes_RosIDLReference.attributes={datatypes_RosIDLReference_rosPackage, datatypes_RosIDLReference_namespace}

# IDLReference class attributes and methods

# datatypes_TypesLibrary class attributes and methods
datatypes_TypesLibrary_name: Property = Property(name="name", type=StringType)
datatypes_TypesLibrary.attributes={datatypes_TypesLibrary_name}

# datatypes_DataType class attributes and methods
datatypes_DataType_name: Property = Property(name="name", type=StringType)
datatypes_DataType.attributes={datatypes_DataType_name}

# datatypes_IDLReference class attributes and methods

# datatypes_VectorType class attributes and methods

# ComplexType class attributes and methods

# datatypes_CustomType class attributes and methods

# datatypes_Field class attributes and methods
datatypes_Field_measureUnit: Property = Property(name="measureUnit", type=StringType)
datatypes_Field_name: Property = Property(name="name", type=StringType)
datatypes_Field_description: Property = Property(name="description", type=StringType)
datatypes_Field.attributes={datatypes_Field_measureUnit, datatypes_Field_description, datatypes_Field_name}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="DataType", type=datatypes_TypesLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="typesLibrary", type=datatypes_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includes2: BinaryAssociation = BinaryAssociation(
    name="includes2",
    ends={
        Property(name="datatypes_TypesLibrary", type=datatypes_TypesLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_TypesLibrary1", type=datatypes_TypesLibrary, multiplicity=Multiplicity(0, 9999))
    }
)
typesLibrary3: BinaryAssociation = BinaryAssociation(
    name="typesLibrary3",
    ends={
        Property(name="TypesLibrary", type=datatypes_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="types", type=datatypes_TypesLibrary, multiplicity=Multiplicity(1, 1))
    }
)
template4: BinaryAssociation = BinaryAssociation(
    name="template4",
    ends={
        Property(name="datatypes_DataType", type=datatypes_VectorType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_VectorType", type=datatypes_DataType, multiplicity=Multiplicity(1, 1))
    }
)
fields5: BinaryAssociation = BinaryAssociation(
    name="fields5",
    ends={
        Property(name="datatypes_Field", type=datatypes_CustomType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_CustomType", type=datatypes_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="datatypes_DataType8", type=datatypes_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_Field7", type=datatypes_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_datatypes_SimpleType_DataType = Generalization(general=DataType, specific=datatypes_SimpleType)
gen_datatypes_ComplexType_DataType = Generalization(general=DataType, specific=datatypes_ComplexType)
gen_datatypes_RosIDLReference_IDLReference = Generalization(general=IDLReference, specific=datatypes_RosIDLReference)
gen_datatypes_IDLReference_ComplexType = Generalization(general=ComplexType, specific=datatypes_IDLReference)
gen_datatypes_VectorType_ComplexType = Generalization(general=ComplexType, specific=datatypes_VectorType)
gen_datatypes_CustomType_ComplexType = Generalization(general=ComplexType, specific=datatypes_CustomType)

# Domain Model
domain_model = DomainModel(
    name="datatypes",
    types={datatypes_SimpleType, DataType, datatypes_ComplexType, datatypes_RosIDLReference, IDLReference, datatypes_TypesLibrary, datatypes_DataType, datatypes_IDLReference, datatypes_VectorType, ComplexType, datatypes_CustomType, datatypes_Field},
    associations={types0, includes2, typesLibrary3, template4, fields5, type6},
    generalizations={gen_datatypes_SimpleType_DataType, gen_datatypes_ComplexType_DataType, gen_datatypes_RosIDLReference_IDLReference, gen_datatypes_IDLReference_ComplexType, gen_datatypes_VectorType_ComplexType, gen_datatypes_CustomType_ComplexType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)