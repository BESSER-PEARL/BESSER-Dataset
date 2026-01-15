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
TestEnumeration: Enumeration = Enumeration(
    name="TestEnumeration",
    literals={
            EnumerationLiteral(name="TestLiteral1"),
			EnumerationLiteral(name="TestLiteral2")
    }
)

# Classes
package1_TestTypeClass1 = Class(name="package1::TestTypeClass1")
package1_TestTypeClass2 = Class(name="package1::TestTypeClass2")
TestTypeClass1 = Class(name="TestTypeClass1")
package1_TestOperationAndParameterClass = Class(name="package1::TestOperationAndParameterClass")
package1_TestPrimitiveTypeClass = Class(name="package1::TestPrimitiveTypeClass")
package1_TestPropertyClass = Class(name="package1::TestPropertyClass")

# package1_TestTypeClass1 class attributes and methods
package1_TestTypeClass1_property1: Property = Property(name="property1", type=BooleanType)
package1_TestTypeClass1_m_operation1: Method = Method(name="operation1", parameters={})
package1_TestTypeClass1.attributes={package1_TestTypeClass1_property1}
package1_TestTypeClass1.methods={package1_TestTypeClass1_m_operation1}

# package1_TestTypeClass2 class attributes and methods
package1_TestTypeClass2_property2: Property = Property(name="property2", type=BooleanType)
package1_TestTypeClass2_m_operation2: Method = Method(name="operation2", parameters={})
package1_TestTypeClass2.attributes={package1_TestTypeClass2_property2}
package1_TestTypeClass2.methods={package1_TestTypeClass2_m_operation2}

# TestTypeClass1 class attributes and methods

# package1_TestOperationAndParameterClass class attributes and methods
package1_TestOperationAndParameterClass_m_operationWithoutParameters: Method = Method(name="operationWithoutParameters", parameters={}, type=TestTypeClass1)
package1_TestOperationAndParameterClass_m_voidOperationWithParameter: Method = Method(name="voidOperationWithParameter", parameters={Parameter(name='in1')})
package1_TestOperationAndParameterClass_m_orderedMultipleOperation: Method = Method(name="orderedMultipleOperation", parameters={}, type=TestTypeClass1)
package1_TestOperationAndParameterClass_m_unorderedMultipleOperation: Method = Method(name="unorderedMultipleOperation", parameters={}, type=TestTypeClass1)
package1_TestOperationAndParameterClass_m_uniqueMultipleOperation: Method = Method(name="uniqueMultipleOperation", parameters={}, type=TestTypeClass1)
package1_TestOperationAndParameterClass_m_nonuniqueMultipleOperation: Method = Method(name="nonuniqueMultipleOperation", parameters={}, type=TestTypeClass1)
package1_TestOperationAndParameterClass.methods={package1_TestOperationAndParameterClass_m_unorderedMultipleOperation, package1_TestOperationAndParameterClass_m_nonuniqueMultipleOperation, package1_TestOperationAndParameterClass_m_orderedMultipleOperation, package1_TestOperationAndParameterClass_m_operationWithoutParameters, package1_TestOperationAndParameterClass_m_uniqueMultipleOperation, package1_TestOperationAndParameterClass_m_voidOperationWithParameter}

# package1_TestPrimitiveTypeClass class attributes and methods
package1_TestPrimitiveTypeClass_anIntegerBigDecimal: Property = Property(name="anIntegerBigDecimal", type=StringType)
package1_TestPrimitiveTypeClass_aRealFloat: Property = Property(name="aRealFloat", type=StringType)
package1_TestPrimitiveTypeClass_aRealFloatObject: Property = Property(name="aRealFloatObject", type=StringType)
package1_TestPrimitiveTypeClass_aRealDouble: Property = Property(name="aRealDouble", type=StringType)
package1_TestPrimitiveTypeClass_aRealDoubleObject: Property = Property(name="aRealDoubleObject", type=StringType)
package1_TestPrimitiveTypeClass_aBooleanBoolean: Property = Property(name="aBooleanBoolean", type=StringType)
package1_TestPrimitiveTypeClass_aBooleanBooleanObject: Property = Property(name="aBooleanBooleanObject", type=StringType)
package1_TestPrimitiveTypeClass_aStringChar: Property = Property(name="aStringChar", type=StringType)
package1_TestPrimitiveTypeClass_aStringCharacterObject: Property = Property(name="aStringCharacterObject", type=StringType)
package1_TestPrimitiveTypeClass_aStringString: Property = Property(name="aStringString", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerEByte: Property = Property(name="anIntegerEByte", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerEByteObject: Property = Property(name="anIntegerEByteObject", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerEShort: Property = Property(name="anIntegerEShort", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerEShortObject: Property = Property(name="anIntegerEShortObject", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerEInt: Property = Property(name="anIntegerEInt", type=IntegerType)
package1_TestPrimitiveTypeClass_anIntegerEIntegerObject: Property = Property(name="anIntegerEIntegerObject", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerELong: Property = Property(name="anIntegerELong", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerELongObject: Property = Property(name="anIntegerELongObject", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerEBigInteger: Property = Property(name="anIntegerEBigInteger", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerEBigDecimal: Property = Property(name="anIntegerEBigDecimal", type=StringType)
package1_TestPrimitiveTypeClass_aRealEFloat: Property = Property(name="aRealEFloat", type=FloatType)
package1_TestPrimitiveTypeClass_aRealEFloatObject: Property = Property(name="aRealEFloatObject", type=StringType)
package1_TestPrimitiveTypeClass_aRealEDouble: Property = Property(name="aRealEDouble", type=FloatType)
package1_TestPrimitiveTypeClass_aRealEDoubleObject: Property = Property(name="aRealEDoubleObject", type=StringType)
package1_TestPrimitiveTypeClass_aBooleanEBoolean: Property = Property(name="aBooleanEBoolean", type=BooleanType)
package1_TestPrimitiveTypeClass_aBooleanEBooleanObject: Property = Property(name="aBooleanEBooleanObject", type=StringType)
package1_TestPrimitiveTypeClass_aStringEChar: Property = Property(name="aStringEChar", type=StringType)
package1_TestPrimitiveTypeClass_aStringECharacterObject: Property = Property(name="aStringECharacterObject", type=StringType)
package1_TestPrimitiveTypeClass_aStringEString: Property = Property(name="aStringEString", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerByte: Property = Property(name="anIntegerByte", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerByteObject: Property = Property(name="anIntegerByteObject", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerShort: Property = Property(name="anIntegerShort", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerShortObject: Property = Property(name="anIntegerShortObject", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerInt: Property = Property(name="anIntegerInt", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerIntegerObject: Property = Property(name="anIntegerIntegerObject", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerLong: Property = Property(name="anIntegerLong", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerLongObject: Property = Property(name="anIntegerLongObject", type=StringType)
package1_TestPrimitiveTypeClass_anIntegerBigInteger: Property = Property(name="anIntegerBigInteger", type=StringType)
package1_TestPrimitiveTypeClass.attributes={package1_TestPrimitiveTypeClass_anIntegerEByteObject, package1_TestPrimitiveTypeClass_aStringCharacterObject, package1_TestPrimitiveTypeClass_aStringChar, package1_TestPrimitiveTypeClass_anIntegerIntegerObject, package1_TestPrimitiveTypeClass_anIntegerBigInteger, package1_TestPrimitiveTypeClass_aRealFloat, package1_TestPrimitiveTypeClass_aStringString, package1_TestPrimitiveTypeClass_aRealFloatObject, package1_TestPrimitiveTypeClass_aBooleanBooleanObject, package1_TestPrimitiveTypeClass_aRealEFloatObject, package1_TestPrimitiveTypeClass_anIntegerEBigDecimal, package1_TestPrimitiveTypeClass_anIntegerEShort, package1_TestPrimitiveTypeClass_anIntegerShort, package1_TestPrimitiveTypeClass_anIntegerEByte, package1_TestPrimitiveTypeClass_anIntegerLongObject, package1_TestPrimitiveTypeClass_aStringEString, package1_TestPrimitiveTypeClass_anIntegerInt, package1_TestPrimitiveTypeClass_aRealDouble, package1_TestPrimitiveTypeClass_aStringEChar, package1_TestPrimitiveTypeClass_anIntegerLong, package1_TestPrimitiveTypeClass_aRealDoubleObject, package1_TestPrimitiveTypeClass_anIntegerBigDecimal, package1_TestPrimitiveTypeClass_aRealEDouble, package1_TestPrimitiveTypeClass_anIntegerEInt, package1_TestPrimitiveTypeClass_aBooleanEBoolean, package1_TestPrimitiveTypeClass_anIntegerEShortObject, package1_TestPrimitiveTypeClass_aBooleanBoolean, package1_TestPrimitiveTypeClass_anIntegerByte, package1_TestPrimitiveTypeClass_aRealEFloat, package1_TestPrimitiveTypeClass_anIntegerShortObject, package1_TestPrimitiveTypeClass_aBooleanEBooleanObject, package1_TestPrimitiveTypeClass_anIntegerEIntegerObject, package1_TestPrimitiveTypeClass_aStringECharacterObject, package1_TestPrimitiveTypeClass_aRealEDoubleObject, package1_TestPrimitiveTypeClass_anIntegerEBigInteger, package1_TestPrimitiveTypeClass_anIntegerELong, package1_TestPrimitiveTypeClass_anIntegerELongObject, package1_TestPrimitiveTypeClass_anIntegerByteObject}

# package1_TestPropertyClass class attributes and methods
package1_TestPropertyClass_identifierProperty: Property = Property(name="identifierProperty", type=StringType)
package1_TestPropertyClass_nonidentifierProperty: Property = Property(name="nonidentifierProperty", type=StringType)
package1_TestPropertyClass.attributes={package1_TestPropertyClass_identifierProperty, package1_TestPropertyClass_nonidentifierProperty}

# Relationships
nonmultipleProperty0: BinaryAssociation = BinaryAssociation(
    name="nonmultipleProperty0",
    ends={
        Property(name="package1_TestTypeClass1", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 1))
    }
)
orderedMultipleProperty1: BinaryAssociation = BinaryAssociation(
    name="orderedMultipleProperty1",
    ends={
        Property(name="package1_TestTypeClass13", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass2", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 9999))
    }
)
unorderedMultipleProperty4: BinaryAssociation = BinaryAssociation(
    name="unorderedMultipleProperty4",
    ends={
        Property(name="package1_TestTypeClass16", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass5", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 9999))
    }
)
uniqueMultipleProperty7: BinaryAssociation = BinaryAssociation(
    name="uniqueMultipleProperty7",
    ends={
        Property(name="package1_TestTypeClass19", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass8", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 9999))
    }
)
nonuniqueMultipleProperty10: BinaryAssociation = BinaryAssociation(
    name="nonuniqueMultipleProperty10",
    ends={
        Property(name="package1_TestTypeClass112", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass11", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 9999))
    }
)
associationEnd113: BinaryAssociation = BinaryAssociation(
    name="associationEnd113",
    ends={
        Property(name="package1_TestTypeClass115", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass14", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 1))
    }
)
orderedMultiplePropertyAssociationEnd16: BinaryAssociation = BinaryAssociation(
    name="orderedMultiplePropertyAssociationEnd16",
    ends={
        Property(name="package1_TestTypeClass118", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass17", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 9999))
    }
)
unorderedMultiplePropertyAssociationEnd19: BinaryAssociation = BinaryAssociation(
    name="unorderedMultiplePropertyAssociationEnd19",
    ends={
        Property(name="package1_TestTypeClass121", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass20", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 9999))
    }
)
uniqueMultiplePropertyAssociationEnd22: BinaryAssociation = BinaryAssociation(
    name="uniqueMultiplePropertyAssociationEnd22",
    ends={
        Property(name="package1_TestTypeClass124", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass23", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 9999))
    }
)
nonuniqueMultiplePropertyAssociationEnd25: BinaryAssociation = BinaryAssociation(
    name="nonuniqueMultiplePropertyAssociationEnd25",
    ends={
        Property(name="package1_TestTypeClass127", type=package1_TestPropertyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="package1_TestPropertyClass26", type=package1_TestTypeClass1, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_package1_TestTypeClass2_TestTypeClass1 = Generalization(general=TestTypeClass1, specific=package1_TestTypeClass2)

# Domain Model
domain_model = DomainModel(
    name="package1",
    types={package1_TestTypeClass1, package1_TestTypeClass2, TestTypeClass1, package1_TestOperationAndParameterClass, package1_TestPrimitiveTypeClass, package1_TestPropertyClass, TestEnumeration},
    associations={nonmultipleProperty0, orderedMultipleProperty1, unorderedMultipleProperty4, uniqueMultipleProperty7, nonuniqueMultipleProperty10, associationEnd113, orderedMultiplePropertyAssociationEnd16, unorderedMultiplePropertyAssociationEnd19, uniqueMultiplePropertyAssociationEnd22, nonuniqueMultiplePropertyAssociationEnd25},
    generalizations={gen_package1_TestTypeClass2_TestTypeClass1},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)