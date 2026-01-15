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
Vis: Enumeration = Enumeration(
    name="Vis",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected")
    }
)

PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="JByte"),
			EnumerationLiteral(name="JShort"),
			EnumerationLiteral(name="JInt"),
			EnumerationLiteral(name="JLong"),
			EnumerationLiteral(name="JChar"),
			EnumerationLiteral(name="JFloat"),
			EnumerationLiteral(name="JDouble"),
			EnumerationLiteral(name="JBoolean")
    }
)

ReferenceType: Enumeration = Enumeration(
    name="ReferenceType",
    literals={
            EnumerationLiteral(name="JClassType"),
			EnumerationLiteral(name="JInterfaceType"),
			EnumerationLiteral(name="JArrayType")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="return")
    }
)

# Classes
javaMetaModel_JParameter = Class(name="javaMetaModel::JParameter", is_abstract=True)
javaMetaModel_JElement = Class(name="javaMetaModel::JElement")
javaMetaModel_JMethod = Class(name="javaMetaModel::JMethod")
JFeature = Class(name="JFeature")
javaMetaModel_JPackage = Class(name="javaMetaModel::JPackage")
javaMetaModel_JClass = Class(name="javaMetaModel::JClass")
JElement = Class(name="JElement")
javaMetaModel_JFeature = Class(name="javaMetaModel::JFeature", is_abstract=True)
javaMetaModel_JReferenceTypePar = Class(name="javaMetaModel::JReferenceTypePar")
javaMetaModel_JField = Class(name="javaMetaModel::JField", is_abstract=True)
javaMetaModel_JAttribute = Class(name="javaMetaModel::JAttribute")
JField = Class(name="JField")
javaMetaModel_JReference = Class(name="javaMetaModel::JReference")
javaMetaModel_JPrimitiveTypePar = Class(name="javaMetaModel::JPrimitiveTypePar")
JParameter = Class(name="JParameter")

# javaMetaModel_JParameter class attributes and methods
javaMetaModel_JParameter_direction: Property = Property(name="direction", type=StringType)
javaMetaModel_JParameter.attributes={javaMetaModel_JParameter_direction}

# javaMetaModel_JElement class attributes and methods
javaMetaModel_JElement_name: Property = Property(name="name", type=StringType)
javaMetaModel_JElement.attributes={javaMetaModel_JElement_name}

# javaMetaModel_JMethod class attributes and methods

# JFeature class attributes and methods

# javaMetaModel_JPackage class attributes and methods

# javaMetaModel_JClass class attributes and methods
javaMetaModel_JClass_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
javaMetaModel_JClass_isFinal: Property = Property(name="isFinal", type=BooleanType)
javaMetaModel_JClass.attributes={javaMetaModel_JClass_isAbstract, javaMetaModel_JClass_isFinal}

# JElement class attributes and methods

# javaMetaModel_JFeature class attributes and methods
javaMetaModel_JFeature_visibility: Property = Property(name="visibility", type=StringType)
javaMetaModel_JFeature_isStatic: Property = Property(name="isStatic", type=BooleanType)
javaMetaModel_JFeature.attributes={javaMetaModel_JFeature_visibility, javaMetaModel_JFeature_isStatic}

# javaMetaModel_JReferenceTypePar class attributes and methods
javaMetaModel_JReferenceTypePar_refType: Property = Property(name="refType", type=StringType)
javaMetaModel_JReferenceTypePar.attributes={javaMetaModel_JReferenceTypePar_refType}

# javaMetaModel_JField class attributes and methods

# javaMetaModel_JAttribute class attributes and methods
javaMetaModel_JAttribute_primitiveType: Property = Property(name="primitiveType", type=StringType)
javaMetaModel_JAttribute.attributes={javaMetaModel_JAttribute_primitiveType}

# JField class attributes and methods

# javaMetaModel_JReference class attributes and methods
javaMetaModel_JReference_refType: Property = Property(name="refType", type=StringType)
javaMetaModel_JReference.attributes={javaMetaModel_JReference_refType}

# javaMetaModel_JPrimitiveTypePar class attributes and methods
javaMetaModel_JPrimitiveTypePar_primitiveType: Property = Property(name="primitiveType", type=StringType)
javaMetaModel_JPrimitiveTypePar.attributes={javaMetaModel_JPrimitiveTypePar_primitiveType}

# JParameter class attributes and methods

# Relationships
jparameter0: BinaryAssociation = BinaryAssociation(
    name="jparameter0",
    ends={
        Property(name="JParameter", type=javaMetaModel_JMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=javaMetaModel_JParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="JPackage", type=javaMetaModel_JClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jclass", type=javaMetaModel_JPackage, multiplicity=Multiplicity(0, 1))
    }
)
jsubClass5: BinaryAssociation = BinaryAssociation(
    name="jsubClass5",
    ends={
        Property(name="JClass", type=javaMetaModel_JClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jsuperClass", type=javaMetaModel_JClass, multiplicity=Multiplicity(0, 9999))
    }
)
jfeature1: BinaryAssociation = BinaryAssociation(
    name="jfeature1",
    ends={
        Property(name="JFeature", type=javaMetaModel_JClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner2", type=javaMetaModel_JFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
jsuperClass7: BinaryAssociation = BinaryAssociation(
    name="jsuperClass7",
    ends={
        Property(name="JClass8", type=javaMetaModel_JClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jsubClass", type=javaMetaModel_JClass, multiplicity=Multiplicity(0, 1))
    }
)
jclass9: BinaryAssociation = BinaryAssociation(
    name="jclass9",
    ends={
        Property(name="JClass11", type=javaMetaModel_JPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="owner10", type=javaMetaModel_JClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="JMethod", type=javaMetaModel_JParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="jparameter", type=javaMetaModel_JMethod, multiplicity=Multiplicity(0, 1))
    }
)
owner13: BinaryAssociation = BinaryAssociation(
    name="owner13",
    ends={
        Property(name="JClass14", type=javaMetaModel_JFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="jfeature", type=javaMetaModel_JClass, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_javaMetaModel_JMethod_JFeature = Generalization(general=JFeature, specific=javaMetaModel_JMethod)
gen_javaMetaModel_JClass_JElement = Generalization(general=JElement, specific=javaMetaModel_JClass)
gen_javaMetaModel_JReferenceTypePar_JParameter = Generalization(general=JParameter, specific=javaMetaModel_JReferenceTypePar)
gen_javaMetaModel_JFeature_JElement = Generalization(general=JElement, specific=javaMetaModel_JFeature)
gen_javaMetaModel_JPackage_JElement = Generalization(general=JElement, specific=javaMetaModel_JPackage)
gen_javaMetaModel_JField_JFeature = Generalization(general=JFeature, specific=javaMetaModel_JField)
gen_javaMetaModel_JAttribute_JField = Generalization(general=JField, specific=javaMetaModel_JAttribute)
gen_javaMetaModel_JReference_JField = Generalization(general=JField, specific=javaMetaModel_JReference)
gen_javaMetaModel_JParameter_JElement = Generalization(general=JElement, specific=javaMetaModel_JParameter)
gen_javaMetaModel_JPrimitiveTypePar_JParameter = Generalization(general=JParameter, specific=javaMetaModel_JPrimitiveTypePar)

# Domain Model
domain_model = DomainModel(
    name="javaMetaModel",
    types={javaMetaModel_JParameter, javaMetaModel_JElement, javaMetaModel_JMethod, JFeature, javaMetaModel_JPackage, javaMetaModel_JClass, JElement, javaMetaModel_JFeature, javaMetaModel_JReferenceTypePar, javaMetaModel_JField, javaMetaModel_JAttribute, JField, javaMetaModel_JReference, javaMetaModel_JPrimitiveTypePar, JParameter, Vis, PrimitiveType, ReferenceType, Direction},
    associations={jparameter0, owner3, jsubClass5, jfeature1, jsuperClass7, jclass9, owner12, owner13},
    generalizations={gen_javaMetaModel_JMethod_JFeature, gen_javaMetaModel_JClass_JElement, gen_javaMetaModel_JReferenceTypePar_JParameter, gen_javaMetaModel_JFeature_JElement, gen_javaMetaModel_JPackage_JElement, gen_javaMetaModel_JField_JFeature, gen_javaMetaModel_JAttribute_JField, gen_javaMetaModel_JReference_JField, gen_javaMetaModel_JParameter_JElement, gen_javaMetaModel_JPrimitiveTypePar_JParameter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)