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

# Enumerations
NativeTypeKind: Enumeration = Enumeration(
    name="NativeTypeKind",
    literals={
            EnumerationLiteral(name="Simple"),
			EnumerationLiteral(name="Length"),
			EnumerationLiteral(name="LengthAndPrecision"),
			EnumerationLiteral(name="Enum")
    }
)

TypesLibraryKind: Enumeration = Enumeration(
    name="TypesLibraryKind",
    literals={
            EnumerationLiteral(name="logicalTypes"),
			EnumerationLiteral(name="physicalTypes")
    }
)

# Classes
typeslibrary_NativeTypesLibrary = Class(name="typeslibrary::NativeTypesLibrary")
TypesLibrary = Class(name="TypesLibrary")
typeslibrary_NativeType = Class(name="typeslibrary::NativeType")
typeslibrary_ComplexNamedType = Class(name="typeslibrary::ComplexNamedType")
UserDefinedType = Class(name="UserDefinedType")
typeslibrary_UserDefinedType = Class(name="typeslibrary::UserDefinedType", is_abstract=True)
typeslibrary_SimpleNamedType = Class(name="typeslibrary::SimpleNamedType")
typeslibrary_Type = Class(name="typeslibrary::Type", is_abstract=True)
typeslibrary_TypeInstance = Class(name="typeslibrary::TypeInstance")
Type = Class(name="Type")
typeslibrary_TypesLibraryUser = Class(name="typeslibrary::TypesLibraryUser", is_abstract=True)
typeslibrary_TypesLibrary = Class(name="typeslibrary::TypesLibrary", is_abstract=True)
typeslibrary_UserDefinedTypeRef = Class(name="typeslibrary::UserDefinedTypeRef")
typeslibrary_UserDefinedTypesLibrary = Class(name="typeslibrary::UserDefinedTypesLibrary")

# typeslibrary_NativeTypesLibrary class attributes and methods
typeslibrary_NativeTypesLibrary_name: Property = Property(name="name", type=StringType)
typeslibrary_NativeTypesLibrary_m_findTypeByName: Method = Method(name="findTypeByName", parameters={Parameter(name='name')}, type=StringType)
typeslibrary_NativeTypesLibrary.attributes={typeslibrary_NativeTypesLibrary_name}
typeslibrary_NativeTypesLibrary.methods={typeslibrary_NativeTypesLibrary_m_findTypeByName}

# TypesLibrary class attributes and methods

# typeslibrary_NativeType class attributes and methods
typeslibrary_NativeType_name: Property = Property(name="name", type=StringType)
typeslibrary_NativeType_spec: Property = Property(name="spec", type=StringType)
typeslibrary_NativeType.attributes={typeslibrary_NativeType_spec, typeslibrary_NativeType_name}

# typeslibrary_ComplexNamedType class attributes and methods

# UserDefinedType class attributes and methods

# typeslibrary_UserDefinedType class attributes and methods
typeslibrary_UserDefinedType_name: Property = Property(name="name", type=StringType)
typeslibrary_UserDefinedType.attributes={typeslibrary_UserDefinedType_name}

# typeslibrary_SimpleNamedType class attributes and methods

# typeslibrary_Type class attributes and methods

# typeslibrary_TypeInstance class attributes and methods
typeslibrary_TypeInstance_literals: Property = Property(name="literals", type=StringType)
typeslibrary_TypeInstance_length: Property = Property(name="length", type=IntegerType)
typeslibrary_TypeInstance_precision: Property = Property(name="precision", type=IntegerType)
typeslibrary_TypeInstance.attributes={typeslibrary_TypeInstance_literals, typeslibrary_TypeInstance_precision, typeslibrary_TypeInstance_length}

# Type class attributes and methods

# typeslibrary_TypesLibraryUser class attributes and methods

# typeslibrary_TypesLibrary class attributes and methods
typeslibrary_TypesLibrary_kind: Property = Property(name="kind", type=StringType)
typeslibrary_TypesLibrary.attributes={typeslibrary_TypesLibrary_kind}

# typeslibrary_UserDefinedTypeRef class attributes and methods

# typeslibrary_UserDefinedTypesLibrary class attributes and methods
typeslibrary_UserDefinedTypesLibrary_name: Property = Property(name="name", type=StringType)
typeslibrary_UserDefinedTypesLibrary.attributes={typeslibrary_UserDefinedTypesLibrary_name}

# Relationships
nativeTypes0: BinaryAssociation = BinaryAssociation(
    name="nativeTypes0",
    ends={
        Property(name="typeslibrary_NativeType", type=typeslibrary_NativeTypesLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="typeslibrary_NativeTypesLibrary", type=typeslibrary_NativeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapsTo4: BinaryAssociation = BinaryAssociation(
    name="mapsTo4",
    ends={
        Property(name="typeslibrary_NativeType5", type=typeslibrary_NativeType, multiplicity=Multiplicity(1, 1)),
        Property(name="typeslibrary_NativeType3", type=typeslibrary_NativeType, multiplicity=Multiplicity(0, 1))
    }
)
types6: BinaryAssociation = BinaryAssociation(
    name="types6",
    ends={
        Property(name="typeslibrary_UserDefinedType", type=typeslibrary_ComplexNamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="typeslibrary_ComplexNamedType", type=typeslibrary_UserDefinedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="typeslibrary_TypeInstance8", type=typeslibrary_SimpleNamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="typeslibrary_SimpleNamedType", type=typeslibrary_TypeInstance, multiplicity=Multiplicity(1, 1))
    }
)
nativeType1: BinaryAssociation = BinaryAssociation(
    name="nativeType1",
    ends={
        Property(name="typeslibrary_NativeType2", type=typeslibrary_TypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="typeslibrary_TypeInstance", type=typeslibrary_NativeType, multiplicity=Multiplicity(1, 1))
    }
)
userDefinedTypes11: BinaryAssociation = BinaryAssociation(
    name="userDefinedTypes11",
    ends={
        Property(name="typeslibrary_UserDefinedType12", type=typeslibrary_UserDefinedTypesLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="typeslibrary_UserDefinedTypesLibrary", type=typeslibrary_UserDefinedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedLibraries13: BinaryAssociation = BinaryAssociation(
    name="usedLibraries13",
    ends={
        Property(name="typeslibrary_TypesLibrary", type=typeslibrary_TypesLibraryUser, multiplicity=Multiplicity(1, 1)),
        Property(name="typeslibrary_TypesLibraryUser", type=typeslibrary_TypesLibrary, multiplicity=Multiplicity(0, 9999))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="typeslibrary_UserDefinedType10", type=typeslibrary_UserDefinedTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="typeslibrary_UserDefinedTypeRef", type=typeslibrary_UserDefinedType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_typeslibrary_NativeTypesLibrary_TypesLibrary = Generalization(general=TypesLibrary, specific=typeslibrary_NativeTypesLibrary)
gen_typeslibrary_ComplexNamedType_UserDefinedType = Generalization(general=UserDefinedType, specific=typeslibrary_ComplexNamedType)
gen_typeslibrary_SimpleNamedType_UserDefinedType = Generalization(general=UserDefinedType, specific=typeslibrary_SimpleNamedType)
gen_typeslibrary_TypeInstance_Type = Generalization(general=Type, specific=typeslibrary_TypeInstance)
gen_typeslibrary_UserDefinedTypesLibrary_TypesLibrary = Generalization(general=TypesLibrary, specific=typeslibrary_UserDefinedTypesLibrary)
gen_typeslibrary_UserDefinedTypeRef_Type = Generalization(general=Type, specific=typeslibrary_UserDefinedTypeRef)

# Domain Model
domain_model = DomainModel(
    name="typeslibrary",
    types={typeslibrary_NativeTypesLibrary, TypesLibrary, typeslibrary_NativeType, typeslibrary_ComplexNamedType, UserDefinedType, typeslibrary_UserDefinedType, typeslibrary_SimpleNamedType, typeslibrary_Type, typeslibrary_TypeInstance, Type, typeslibrary_TypesLibraryUser, typeslibrary_TypesLibrary, typeslibrary_UserDefinedTypeRef, typeslibrary_UserDefinedTypesLibrary, NativeTypeKind, TypesLibraryKind},
    associations={nativeTypes0, mapsTo4, types6, type7, nativeType1, userDefinedTypes11, usedLibraries13, type9},
    generalizations={gen_typeslibrary_NativeTypesLibrary_TypesLibrary, gen_typeslibrary_ComplexNamedType_UserDefinedType, gen_typeslibrary_SimpleNamedType_UserDefinedType, gen_typeslibrary_TypeInstance_Type, gen_typeslibrary_UserDefinedTypesLibrary_TypesLibrary, gen_typeslibrary_UserDefinedTypeRef_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)