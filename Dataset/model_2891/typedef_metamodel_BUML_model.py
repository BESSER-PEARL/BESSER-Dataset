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
CSIDatatypeCodes: Enumeration = Enumeration(
    name="CSIDatatypeCodes",
    literals={
            EnumerationLiteral(name="CSIInteger"),
			EnumerationLiteral(name="CSIString"),
			EnumerationLiteral(name="CSIFloat"),
			EnumerationLiteral(name="CSIDouble"),
			EnumerationLiteral(name="CSIBoolean"),
			EnumerationLiteral(name="CSIDate"),
			EnumerationLiteral(name="CSIByte"),
			EnumerationLiteral(name="CSILong")
    }
)

CSIExceptionTypes: Enumeration = Enumeration(
    name="CSIExceptionTypes",
    literals={
            EnumerationLiteral(name="USER"),
			EnumerationLiteral(name="SYSTEM"),
			EnumerationLiteral(name="UNRECOVERABLE")
    }
)

# Classes
typedef_TDDocumentation = Class(name="typedef::TDDocumentation")
typedef_CSIDatatype = Class(name="typedef::CSIDatatype")
Type = Class(name="Type")
typedef_DocumentRoot = Class(name="typedef::DocumentRoot")
typedef_Type = Class(name="typedef::Type", is_abstract=True)
typedef_TypeAnnotation = Class(name="typedef::TypeAnnotation")
typedef_Entity = Class(name="typedef::Entity")
typedef_Feature = Class(name="typedef::Feature")
typedef_Exception = Class(name="typedef::Exception")
typedef_TypedArray = Class(name="typedef::TypedArray")
typedef_PrimitiveType = Class(name="typedef::PrimitiveType")
typedef_TypeLanguageBinding = Class(name="typedef::TypeLanguageBinding")
typedef_TDAnnotationDetail = Class(name="typedef::TDAnnotationDetail")
typedef_EnumLiteral = Class(name="typedef::EnumLiteral")
typedef_EnumVal = Class(name="typedef::EnumVal")

# typedef_TDDocumentation class attributes and methods
typedef_TDDocumentation_doc: Property = Property(name="doc", type=StringType)
typedef_TDDocumentation.attributes={typedef_TDDocumentation_doc}

# typedef_CSIDatatype class attributes and methods
typedef_CSIDatatype_code: Property = Property(name="code", type=StringType)
typedef_CSIDatatype_nillable: Property = Property(name="nillable", type=BooleanType)
typedef_CSIDatatype.attributes={typedef_CSIDatatype_nillable, typedef_CSIDatatype_code}

# Type class attributes and methods

# typedef_DocumentRoot class attributes and methods

# typedef_Type class attributes and methods
typedef_Type_name: Property = Property(name="name", type=StringType)
typedef_Type.attributes={typedef_Type_name}

# typedef_TypeAnnotation class attributes and methods
typedef_TypeAnnotation_source: Property = Property(name="source", type=StringType)
typedef_TypeAnnotation.attributes={typedef_TypeAnnotation_source}

# typedef_Entity class attributes and methods
typedef_Entity_versionuid: Property = Property(name="versionuid", type=IntegerType)
typedef_Entity.attributes={typedef_Entity_versionuid}

# typedef_Feature class attributes and methods
typedef_Feature_name: Property = Property(name="name", type=StringType)
typedef_Feature.attributes={typedef_Feature_name}

# typedef_Exception class attributes and methods
typedef_Exception_exceptionType: Property = Property(name="exceptionType", type=StringType)
typedef_Exception.attributes={typedef_Exception_exceptionType}

# typedef_TypedArray class attributes and methods

# typedef_PrimitiveType class attributes and methods
typedef_PrimitiveType_typesetName: Property = Property(name="typesetName", type=StringType)
typedef_PrimitiveType_nillable: Property = Property(name="nillable", type=BooleanType)
typedef_PrimitiveType.attributes={typedef_PrimitiveType_typesetName, typedef_PrimitiveType_nillable}

# typedef_TypeLanguageBinding class attributes and methods
typedef_TypeLanguageBinding_lang: Property = Property(name="lang", type=StringType)
typedef_TypeLanguageBinding_langSpecificType: Property = Property(name="langSpecificType", type=StringType)
typedef_TypeLanguageBinding_langSpecificNS: Property = Property(name="langSpecificNS", type=StringType)
typedef_TypeLanguageBinding_defaultInitValue: Property = Property(name="defaultInitValue", type=StringType)
typedef_TypeLanguageBinding_nullValueLiteral: Property = Property(name="nullValueLiteral", type=StringType)
typedef_TypeLanguageBinding.attributes={typedef_TypeLanguageBinding_lang, typedef_TypeLanguageBinding_defaultInitValue, typedef_TypeLanguageBinding_nullValueLiteral, typedef_TypeLanguageBinding_langSpecificType, typedef_TypeLanguageBinding_langSpecificNS}

# typedef_TDAnnotationDetail class attributes and methods
typedef_TDAnnotationDetail_key: Property = Property(name="key", type=StringType)
typedef_TDAnnotationDetail_value: Property = Property(name="value", type=StringType)
typedef_TDAnnotationDetail.attributes={typedef_TDAnnotationDetail_key, typedef_TDAnnotationDetail_value}

# typedef_EnumLiteral class attributes and methods
typedef_EnumLiteral_name: Property = Property(name="name", type=StringType)
typedef_EnumLiteral_value: Property = Property(name="value", type=StringType)
typedef_EnumLiteral.attributes={typedef_EnumLiteral_name, typedef_EnumLiteral_value}

# typedef_EnumVal class attributes and methods

# Relationships
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="typedef_Type2", type=typedef_TypeAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="typedef_TypeAnnotation", type=typedef_Type, multiplicity=Multiplicity(1, 1))
    }
)
documentation3: BinaryAssociation = BinaryAssociation(
    name="documentation3",
    ends={
        Property(name="typedef_TDDocumentation", type=typedef_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_Type4", type=typedef_TDDocumentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="typedef_Type", type=typedef_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_DocumentRoot", type=typedef_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="typedef_Feature7", type=typedef_Type, multiplicity=Multiplicity(0, 1)),
        Property(name="typedef_Type8", type=typedef_Feature, multiplicity=Multiplicity(1, 1))
    }
)
documentation9: BinaryAssociation = BinaryAssociation(
    name="documentation9",
    ends={
        Property(name="typedef_TDDocumentation11", type=typedef_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_Feature10", type=typedef_TDDocumentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="typedef_Feature", type=typedef_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_Entity", type=typedef_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentType12: BinaryAssociation = BinaryAssociation(
    name="componentType12",
    ends={
        Property(name="typedef_Type13", type=typedef_TypedArray, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_TypedArray", type=typedef_Type, multiplicity=Multiplicity(0, 1))
    }
)
languageBindings16: BinaryAssociation = BinaryAssociation(
    name="languageBindings16",
    ends={
        Property(name="typedef_TypeLanguageBinding", type=typedef_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_PrimitiveType", type=typedef_TypeLanguageBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
details14: BinaryAssociation = BinaryAssociation(
    name="details14",
    ends={
        Property(name="typedef_TDAnnotationDetail", type=typedef_TypeAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_TypeAnnotation15", type=typedef_TDAnnotationDetail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals19: BinaryAssociation = BinaryAssociation(
    name="literals19",
    ends={
        Property(name="typedef_EnumLiteral", type=typedef_EnumVal, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_EnumVal20", type=typedef_EnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation21: BinaryAssociation = BinaryAssociation(
    name="documentation21",
    ends={
        Property(name="typedef_TDDocumentation23", type=typedef_EnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_EnumLiteral22", type=typedef_TDDocumentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType17: BinaryAssociation = BinaryAssociation(
    name="valueType17",
    ends={
        Property(name="typedef_Type18", type=typedef_EnumVal, multiplicity=Multiplicity(1, 1)),
        Property(name="typedef_EnumVal", type=typedef_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_typedef_CSIDatatype_Type = Generalization(general=Type, specific=typedef_CSIDatatype)
gen_typedef_Entity_Type = Generalization(general=Type, specific=typedef_Entity)
gen_typedef_Exception_Type = Generalization(general=Type, specific=typedef_Exception)
gen_typedef_TypedArray_Type = Generalization(general=Type, specific=typedef_TypedArray)
gen_typedef_PrimitiveType_Type = Generalization(general=Type, specific=typedef_PrimitiveType)
gen_typedef_EnumVal_Type = Generalization(general=Type, specific=typedef_EnumVal)

# Domain Model
domain_model = DomainModel(
    name="typedef",
    types={typedef_TDDocumentation, typedef_CSIDatatype, Type, typedef_DocumentRoot, typedef_Type, typedef_TypeAnnotation, typedef_Entity, typedef_Feature, typedef_Exception, typedef_TypedArray, typedef_PrimitiveType, typedef_TypeLanguageBinding, typedef_TDAnnotationDetail, typedef_EnumLiteral, typedef_EnumVal, CSIDatatypeCodes, CSIExceptionTypes},
    associations={annotations1, documentation3, types0, type6, documentation9, features5, componentType12, languageBindings16, details14, literals19, documentation21, valueType17},
    generalizations={gen_typedef_CSIDatatype_Type, gen_typedef_Entity_Type, gen_typedef_Exception_Type, gen_typedef_TypedArray_Type, gen_typedef_PrimitiveType_Type, gen_typedef_EnumVal_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)