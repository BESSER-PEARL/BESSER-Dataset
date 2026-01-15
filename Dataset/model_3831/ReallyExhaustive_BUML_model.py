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
UnserializableEnumTest: Enumeration = Enumeration(
    name="UnserializableEnumTest",
    literals={
            EnumerationLiteral(name="name1"),
			EnumerationLiteral(name="name2")
    }
)

SerializableEnumTest: Enumeration = Enumeration(
    name="SerializableEnumTest",
    literals={
            EnumerationLiteral(name="name3"),
			EnumerationLiteral(name="name4")
    }
)

# Classes
exhaustive_AbstractTest = Class(name="exhaustive::AbstractTest", is_abstract=True)
OperationsTest = Class(name="OperationsTest")
exhaustive_InterfaceTest = Class(name="exhaustive::InterfaceTest", is_abstract=True)
exhaustive_MultipleSuperTest = Class(name="exhaustive::MultipleSuperTest")
AbstractTest = Class(name="AbstractTest")
InterfaceTest = Class(name="InterfaceTest")
exhaustive_ReferencesTest = Class(name="exhaustive::ReferencesTest")
exhaustive_AttributesTest = Class(name="exhaustive::AttributesTest")
MultipleSuperTest = Class(name="MultipleSuperTest")
exhaustive_OperationsTest = Class(name="exhaustive::OperationsTest")
exhaustive_GenericTest = Class(name="exhaustive::GenericTest")
exhaustive_BindedChildTest = Class(name="exhaustive::BindedChildTest")
exhaustive_UnbindedChildTest = Class(name="exhaustive::UnbindedChildTest")
exhaustive_PartiallyBindedChildTest = Class(name="exhaustive::PartiallyBindedChildTest")
exhaustive_MultipleBoundsGeneric = Class(name="exhaustive::MultipleBoundsGeneric")

# exhaustive_AbstractTest class attributes and methods

# OperationsTest class attributes and methods

# exhaustive_InterfaceTest class attributes and methods

# exhaustive_MultipleSuperTest class attributes and methods

# AbstractTest class attributes and methods

# InterfaceTest class attributes and methods

# exhaustive_ReferencesTest class attributes and methods

# exhaustive_AttributesTest class attributes and methods
exhaustive_AttributesTest_changeableYes: Property = Property(name="changeableYes", type=FloatType)
exhaustive_AttributesTest_changeableNo: Property = Property(name="changeableNo", type=StringType)
exhaustive_AttributesTest_defaultValue: Property = Property(name="defaultValue", type=StringType)
exhaustive_AttributesTest_derivedYes: Property = Property(name="derivedYes", type=StringType)
exhaustive_AttributesTest_derivedNo: Property = Property(name="derivedNo", type=StringType)
exhaustive_AttributesTest_idYes: Property = Property(name="idYes", type=StringType)
exhaustive_AttributesTest_idNo: Property = Property(name="idNo", type=StringType)
exhaustive_AttributesTest_lowerBound0: Property = Property(name="lowerBound0", type=IntegerType)
exhaustive_AttributesTest_lowerBound1: Property = Property(name="lowerBound1", type=StringType)
exhaustive_AttributesTest_lowerBound2: Property = Property(name="lowerBound2", type=StringType)
exhaustive_AttributesTest_lowerBoundN: Property = Property(name="lowerBoundN", type=StringType)
exhaustive_AttributesTest_upperBound0: Property = Property(name="upperBound0", type=StringType)
exhaustive_AttributesTest_upperBound1: Property = Property(name="upperBound1", type=DateType)
exhaustive_AttributesTest_upperBound2: Property = Property(name="upperBound2", type=StringType)
exhaustive_AttributesTest_upperBoundN: Property = Property(name="upperBoundN", type=StringType)
exhaustive_AttributesTest_orderedYes: Property = Property(name="orderedYes", type=StringType)
exhaustive_AttributesTest_orderenedNo: Property = Property(name="orderenedNo", type=StringType)
exhaustive_AttributesTest_transientYes: Property = Property(name="transientYes", type=FloatType)
exhaustive_AttributesTest_transientNo: Property = Property(name="transientNo", type=StringType)
exhaustive_AttributesTest_unsettableYes: Property = Property(name="unsettableYes", type=StringType)
exhaustive_AttributesTest_unsettableNo: Property = Property(name="unsettableNo", type=StringType)
exhaustive_AttributesTest_volatileYes: Property = Property(name="volatileYes", type=StringType)
exhaustive_AttributesTest_volatileNo: Property = Property(name="volatileNo", type=StringType)
exhaustive_AttributesTest_uniqueYes: Property = Property(name="uniqueYes", type=StringType)
exhaustive_AttributesTest_uniqueNo: Property = Property(name="uniqueNo", type=StringType)
exhaustive_AttributesTest.attributes={exhaustive_AttributesTest_volatileYes, exhaustive_AttributesTest_lowerBound1, exhaustive_AttributesTest_orderenedNo, exhaustive_AttributesTest_changeableYes, exhaustive_AttributesTest_changeableNo, exhaustive_AttributesTest_unsettableYes, exhaustive_AttributesTest_defaultValue, exhaustive_AttributesTest_upperBound0, exhaustive_AttributesTest_upperBound2, exhaustive_AttributesTest_transientNo, exhaustive_AttributesTest_idNo, exhaustive_AttributesTest_uniqueNo, exhaustive_AttributesTest_volatileNo, exhaustive_AttributesTest_lowerBound0, exhaustive_AttributesTest_uniqueYes, exhaustive_AttributesTest_orderedYes, exhaustive_AttributesTest_upperBound1, exhaustive_AttributesTest_idYes, exhaustive_AttributesTest_upperBoundN, exhaustive_AttributesTest_derivedYes, exhaustive_AttributesTest_derivedNo, exhaustive_AttributesTest_lowerBound2, exhaustive_AttributesTest_lowerBoundN, exhaustive_AttributesTest_unsettableNo, exhaustive_AttributesTest_transientYes}

# MultipleSuperTest class attributes and methods

# exhaustive_OperationsTest class attributes and methods
exhaustive_OperationsTest_m_empty: Method = Method(name="empty", parameters={})
exhaustive_OperationsTest_m_lowerBound1: Method = Method(name="lowerBound1", parameters={}, type=StringType)
exhaustive_OperationsTest_m_lowerBound2: Method = Method(name="lowerBound2", parameters={}, type=InterfaceTest)
exhaustive_OperationsTest_m_orderedNo: Method = Method(name="orderedNo", parameters={})
exhaustive_OperationsTest_m_uniqueNo: Method = Method(name="uniqueNo", parameters={})
exhaustive_OperationsTest_m_upperBound2: Method = Method(name="upperBound2", parameters={}, type=StringType)
exhaustive_OperationsTest_m_upperBoundN: Method = Method(name="upperBoundN", parameters={}, type=StringType)
exhaustive_OperationsTest_m_manyParameters: Method = Method(name="manyParameters", parameters={Parameter(name='p1'), Parameter(name='p2')})
exhaustive_OperationsTest.methods={exhaustive_OperationsTest_m_upperBound2, exhaustive_OperationsTest_m_manyParameters, exhaustive_OperationsTest_m_orderedNo, exhaustive_OperationsTest_m_lowerBound1, exhaustive_OperationsTest_m_uniqueNo, exhaustive_OperationsTest_m_lowerBound2, exhaustive_OperationsTest_m_empty, exhaustive_OperationsTest_m_upperBoundN}

# exhaustive_GenericTest class attributes and methods
exhaustive_GenericTest_genericAttr: Property = Property(name="genericAttr", type=StringType)
exhaustive_GenericTest_m_genericOperationReturn: Method = Method(name="genericOperationReturn", parameters={})
exhaustive_GenericTest_m_genericOperationParameters: Method = Method(name="genericOperationParameters", parameters={Parameter(name='bar'), Parameter(name='foo')})
exhaustive_GenericTest_m_genericOperationThrow: Method = Method(name="genericOperationThrow", parameters={})
exhaustive_GenericTest_m_complexGenericOperation: Method = Method(name="complexGenericOperation", parameters={})
exhaustive_GenericTest_m_multipleBoundsGenericOperation: Method = Method(name="multipleBoundsGenericOperation", parameters={})
exhaustive_GenericTest.attributes={exhaustive_GenericTest_genericAttr}
exhaustive_GenericTest.methods={exhaustive_GenericTest_m_genericOperationThrow, exhaustive_GenericTest_m_complexGenericOperation, exhaustive_GenericTest_m_genericOperationParameters, exhaustive_GenericTest_m_genericOperationReturn, exhaustive_GenericTest_m_multipleBoundsGenericOperation}

# exhaustive_BindedChildTest class attributes and methods

# exhaustive_UnbindedChildTest class attributes and methods

# exhaustive_PartiallyBindedChildTest class attributes and methods

# exhaustive_MultipleBoundsGeneric class attributes and methods

# Relationships
changeableYes0: BinaryAssociation = BinaryAssociation(
    name="changeableYes0",
    ends={
        Property(name="exhaustive_AbstractTest", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest", type=exhaustive_AbstractTest, multiplicity=Multiplicity(0, 1))
    }
)
changeableNo1: BinaryAssociation = BinaryAssociation(
    name="changeableNo1",
    ends={
        Property(name="exhaustive_AbstractTest3", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest2", type=exhaustive_AbstractTest, multiplicity=Multiplicity(0, 1))
    }
)
containmentYes4: BinaryAssociation = BinaryAssociation(
    name="containmentYes4",
    ends={
        Property(name="exhaustive_MultipleSuperTest", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest5", type=exhaustive_MultipleSuperTest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite16: BinaryAssociation = BinaryAssociation(
    name="opposite16",
    ends={
        Property(name="AttributesTest", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="opposite2", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 1))
    }
)
resolveProxiesFalse9: BinaryAssociation = BinaryAssociation(
    name="resolveProxiesFalse9",
    ends={
        Property(name="exhaustive_AttributesTest11", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest10", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 1))
    }
)
transientTrue12: BinaryAssociation = BinaryAssociation(
    name="transientTrue12",
    ends={
        Property(name="exhaustive_AttributesTest14", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest13", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 1))
    }
)
uniqueFalse15: BinaryAssociation = BinaryAssociation(
    name="uniqueFalse15",
    ends={
        Property(name="exhaustive_AttributesTest17", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest16", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 1))
    }
)
unsettableTrue18: BinaryAssociation = BinaryAssociation(
    name="unsettableTrue18",
    ends={
        Property(name="exhaustive_AttributesTest20", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest19", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 1))
    }
)
volatileTrue21: BinaryAssociation = BinaryAssociation(
    name="volatileTrue21",
    ends={
        Property(name="exhaustive_AttributesTest23", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest22", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 1))
    }
)
derivedYes24: BinaryAssociation = BinaryAssociation(
    name="derivedYes24",
    ends={
        Property(name="exhaustive_AttributesTest26", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest25", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 1))
    }
)
upperBoundN27: BinaryAssociation = BinaryAssociation(
    name="upperBoundN27",
    ends={
        Property(name="exhaustive_AttributesTest29", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest28", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 9999))
    }
)
upperBound230: BinaryAssociation = BinaryAssociation(
    name="upperBound230",
    ends={
        Property(name="exhaustive_AttributesTest32", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest31", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 2))
    }
)
lowerBound133: BinaryAssociation = BinaryAssociation(
    name="lowerBound133",
    ends={
        Property(name="exhaustive_AttributesTest35", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest34", type=exhaustive_AttributesTest, multiplicity=Multiplicity(1, 1))
    }
)
orderedFalse7: BinaryAssociation = BinaryAssociation(
    name="orderedFalse7",
    ends={
        Property(name="exhaustive_AttributesTest", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest8", type=exhaustive_AttributesTest, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound236: BinaryAssociation = BinaryAssociation(
    name="lowerBound236",
    ends={
        Property(name="exhaustive_AttributesTest38", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="exhaustive_ReferencesTest37", type=exhaustive_AttributesTest, multiplicity=Multiplicity(2, 9999))
    }
)
opposite239: BinaryAssociation = BinaryAssociation(
    name="opposite239",
    ends={
        Property(name="ReferencesTest", type=exhaustive_AttributesTest, multiplicity=Multiplicity(1, 1)),
        Property(name="opposite1", type=exhaustive_ReferencesTest, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_exhaustive_AbstractTest_OperationsTest = Generalization(general=OperationsTest, specific=exhaustive_AbstractTest)
gen_exhaustive_InterfaceTest_OperationsTest = Generalization(general=OperationsTest, specific=exhaustive_InterfaceTest)
gen_exhaustive_MultipleSuperTest_AbstractTest = Generalization(general=AbstractTest, specific=exhaustive_MultipleSuperTest)
gen_exhaustive_MultipleSuperTest_InterfaceTest = Generalization(general=InterfaceTest, specific=exhaustive_MultipleSuperTest)
gen_exhaustive_ReferencesTest_AbstractTest = Generalization(general=AbstractTest, specific=exhaustive_ReferencesTest)
gen_exhaustive_AttributesTest_MultipleSuperTest = Generalization(general=MultipleSuperTest, specific=exhaustive_AttributesTest)
gen_exhaustive_AttributesTest_InterfaceTest = Generalization(general=InterfaceTest, specific=exhaustive_AttributesTest)

# Domain Model
domain_model = DomainModel(
    name="exhaustive",
    types={exhaustive_AbstractTest, OperationsTest, exhaustive_InterfaceTest, exhaustive_MultipleSuperTest, AbstractTest, InterfaceTest, exhaustive_ReferencesTest, exhaustive_AttributesTest, MultipleSuperTest, exhaustive_OperationsTest, exhaustive_GenericTest, exhaustive_BindedChildTest, exhaustive_UnbindedChildTest, exhaustive_PartiallyBindedChildTest, exhaustive_MultipleBoundsGeneric, UnserializableEnumTest, SerializableEnumTest},
    associations={changeableYes0, changeableNo1, containmentYes4, opposite16, resolveProxiesFalse9, transientTrue12, uniqueFalse15, unsettableTrue18, volatileTrue21, derivedYes24, upperBoundN27, upperBound230, lowerBound133, orderedFalse7, lowerBound236, opposite239},
    generalizations={gen_exhaustive_AbstractTest_OperationsTest, gen_exhaustive_InterfaceTest_OperationsTest, gen_exhaustive_MultipleSuperTest_AbstractTest, gen_exhaustive_MultipleSuperTest_InterfaceTest, gen_exhaustive_ReferencesTest_AbstractTest, gen_exhaustive_AttributesTest_MultipleSuperTest, gen_exhaustive_AttributesTest_InterfaceTest},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)