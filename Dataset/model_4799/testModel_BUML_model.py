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
ElementType: Enumeration = Enumeration(
    name="ElementType",
    literals={
            EnumerationLiteral(name="Type1"),
			EnumerationLiteral(name="Type2")
    }
)

# Classes
testModel_referenziertesElement = Class(name="testModel::referenziertesElement")
testModel_upperBound = Class(name="testModel::upperBound")
testModel_Kategorie = Class(name="testModel::Kategorie")
testModel_ContainedElement = Class(name="testModel::ContainedElement")
Element = Class(name="Element")
testModel_multiRefElement = Class(name="testModel::multiRefElement")
testModel_Element = Class(name="testModel::Element", is_abstract=True)

# testModel_referenziertesElement class attributes and methods
testModel_referenziertesElement_Float: Property = Property(name="Float", type=StringType)
testModel_referenziertesElement_int: Property = Property(name="int", type=IntegerType)
testModel_referenziertesElement_Integer: Property = Property(name="Integer", type=StringType)
testModel_referenziertesElement_long: Property = Property(name="long", type=StringType)
testModel_referenziertesElement_LongObj: Property = Property(name="LongObj", type=StringType)
testModel_referenziertesElement_short: Property = Property(name="short", type=StringType)
testModel_referenziertesElement_ShortObj: Property = Property(name="ShortObj", type=StringType)
testModel_referenziertesElement_name: Property = Property(name="name", type=StringType)
testModel_referenziertesElement_notChangeable: Property = Property(name="notChangeable", type=StringType)
testModel_referenziertesElement.attributes={testModel_referenziertesElement_short, testModel_referenziertesElement_notChangeable, testModel_referenziertesElement_int, testModel_referenziertesElement_LongObj, testModel_referenziertesElement_Integer, testModel_referenziertesElement_ShortObj, testModel_referenziertesElement_Float, testModel_referenziertesElement_long, testModel_referenziertesElement_name}

# testModel_upperBound class attributes and methods
testModel_upperBound_name: Property = Property(name="name", type=StringType)
testModel_upperBound.attributes={testModel_upperBound_name}

# testModel_Kategorie class attributes and methods
testModel_Kategorie_name: Property = Property(name="name", type=StringType)
testModel_Kategorie_bigdeci: Property = Property(name="bigdeci", type=StringType)
testModel_Kategorie_bigint: Property = Property(name="bigint", type=StringType)
testModel_Kategorie_bool: Property = Property(name="bool", type=BooleanType)
testModel_Kategorie_Boolean: Property = Property(name="Boolean", type=StringType)
testModel_Kategorie_byte: Property = Property(name="byte", type=StringType)
testModel_Kategorie.attributes={testModel_Kategorie_Boolean, testModel_Kategorie_bool, testModel_Kategorie_bigint, testModel_Kategorie_byte, testModel_Kategorie_name, testModel_Kategorie_bigdeci}

# testModel_ContainedElement class attributes and methods
testModel_ContainedElement_char: Property = Property(name="char", type=StringType)
testModel_ContainedElement_Character: Property = Property(name="Character", type=StringType)
testModel_ContainedElement_date: Property = Property(name="date", type=DateType)
testModel_ContainedElement_DiagnosticChain: Property = Property(name="DiagnosticChain", type=StringType)
testModel_ContainedElement_double: Property = Property(name="double", type=FloatType)
testModel_ContainedElement_DoubleObj: Property = Property(name="DoubleObj", type=StringType)
testModel_ContainedElement_float: Property = Property(name="float", type=FloatType)
testModel_ContainedElement_elementType: Property = Property(name="elementType", type=StringType)
testModel_ContainedElement_name: Property = Property(name="name", type=StringType)
testModel_ContainedElement_byteArray: Property = Property(name="byteArray", type=StringType)
testModel_ContainedElement_byteObject: Property = Property(name="byteObject", type=StringType)
testModel_ContainedElement.attributes={testModel_ContainedElement_DiagnosticChain, testModel_ContainedElement_char, testModel_ContainedElement_name, testModel_ContainedElement_byteArray, testModel_ContainedElement_elementType, testModel_ContainedElement_Character, testModel_ContainedElement_DoubleObj, testModel_ContainedElement_float, testModel_ContainedElement_byteObject, testModel_ContainedElement_double, testModel_ContainedElement_date}

# Element class attributes and methods

# testModel_multiRefElement class attributes and methods
testModel_multiRefElement_name: Property = Property(name="name", type=StringType)
testModel_multiRefElement.attributes={testModel_multiRefElement_name}

# testModel_Element class attributes and methods

# Relationships
ref4: BinaryAssociation = BinaryAssociation(
    name="ref4",
    ends={
        Property(name="testModel_referenziertesElement", type=testModel_ContainedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_ContainedElement5", type=testModel_referenziertesElement, multiplicity=Multiplicity(0, 9999))
    }
)
upperBound6: BinaryAssociation = BinaryAssociation(
    name="upperBound6",
    ends={
        Property(name="testModel_upperBound", type=testModel_ContainedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_ContainedElement7", type=testModel_upperBound, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
subKategorie1: BinaryAssociation = BinaryAssociation(
    name="subKategorie1",
    ends={
        Property(name="testModel_Kategorie", type=testModel_Kategorie, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_Kategorie0", type=testModel_Kategorie, multiplicity=Multiplicity(0, 9999))
    }
)
contains2: BinaryAssociation = BinaryAssociation(
    name="contains2",
    ends={
        Property(name="testModel_ContainedElement", type=testModel_Kategorie, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_Kategorie3", type=testModel_ContainedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiRef8: BinaryAssociation = BinaryAssociation(
    name="multiRef8",
    ends={
        Property(name="testModel_multiRefElement", type=testModel_referenziertesElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_referenziertesElement9", type=testModel_multiRefElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_testModel_referenziertesElement_Element = Generalization(general=Element, specific=testModel_referenziertesElement)
gen_testModel_multiRefElement_Element = Generalization(general=Element, specific=testModel_multiRefElement)
gen_testModel_upperBound_Element = Generalization(general=Element, specific=testModel_upperBound)

# Domain Model
domain_model = DomainModel(
    name="testModel",
    types={testModel_referenziertesElement, testModel_upperBound, testModel_Kategorie, testModel_ContainedElement, Element, testModel_multiRefElement, testModel_Element, ElementType},
    associations={ref4, upperBound6, subKategorie1, contains2, multiRef8},
    generalizations={gen_testModel_referenziertesElement_Element, gen_testModel_multiRefElement_Element, gen_testModel_upperBound_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)