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
AEnum: Enumeration = Enumeration(
    name="AEnum",
    literals={
            EnumerationLiteral(name="ENUM0"),
			EnumerationLiteral(name="ENUM1")
    }
)

StateWithoutDefault: Enumeration = Enumeration(
    name="StateWithoutDefault",
    literals={
            EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="MOVE"),
			EnumerationLiteral(name="CLOSE"),
			EnumerationLiteral(name="MOVING"),
			EnumerationLiteral(name="DELETE")
    }
)

Heavy: Enumeration = Enumeration(
    name="Heavy",
    literals={
            EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="MOVE"),
			EnumerationLiteral(name="CLOSE"),
			EnumerationLiteral(name="MOVING"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="OPEN1"),
			EnumerationLiteral(name="MOVE1"),
			EnumerationLiteral(name="CLOS1E"),
			EnumerationLiteral(name="DELETE2"),
			EnumerationLiteral(name="OPEN3"),
			EnumerationLiteral(name="MOVE3"),
			EnumerationLiteral(name="CLOSE3"),
			EnumerationLiteral(name="MOVING3"),
			EnumerationLiteral(name="DELETE3"),
			EnumerationLiteral(name="OPEN4"),
			EnumerationLiteral(name="MOVE4"),
			EnumerationLiteral(name="CLOSE4"),
			EnumerationLiteral(name="MOVING4"),
			EnumerationLiteral(name="DELETE4"),
			EnumerationLiteral(name="MOVING1"),
			EnumerationLiteral(name="DELETE1"),
			EnumerationLiteral(name="OPEN2"),
			EnumerationLiteral(name="MOVE2"),
			EnumerationLiteral(name="CLOSE2"),
			EnumerationLiteral(name="MOVING2")
    }
)

# Classes
alldatatypes_Element = Class(name="alldatatypes::Element", is_abstract=True)
alldatatypes_Root = Class(name="alldatatypes::Root")
Element = Class(name="Element")
alldatatypes_Type = Class(name="alldatatypes::Type", is_abstract=True)
alldatatypes_Strings = Class(name="alldatatypes::Strings")
Type = Class(name="Type")
alldatatypes_Dates = Class(name="alldatatypes::Dates")
alldatatypes_Enums = Class(name="alldatatypes::Enums")
alldatatypes_Booleans = Class(name="alldatatypes::Booleans")
alldatatypes_Integers = Class(name="alldatatypes::Integers")
alldatatypes_Longs = Class(name="alldatatypes::Longs")
alldatatypes_Shorts = Class(name="alldatatypes::Shorts")
alldatatypes_Doubles = Class(name="alldatatypes::Doubles")
alldatatypes_Floats = Class(name="alldatatypes::Floats")
alldatatypes_BigIntegers = Class(name="alldatatypes::BigIntegers")
alldatatypes_BigDecimals = Class(name="alldatatypes::BigDecimals")

# alldatatypes_Element class attributes and methods
alldatatypes_Element_id: Property = Property(name="id", type=StringType)
alldatatypes_Element_name: Property = Property(name="name", type=StringType)
alldatatypes_Element.attributes={alldatatypes_Element_id, alldatatypes_Element_name}

# alldatatypes_Root class attributes and methods
alldatatypes_Root_m_getAllTypes: Method = Method(name="getAllTypes", parameters={}, type=StringType)
alldatatypes_Root.methods={alldatatypes_Root_m_getAllTypes}

# Element class attributes and methods

# alldatatypes_Type class attributes and methods

# alldatatypes_Strings class attributes and methods
alldatatypes_Strings_text_01_EmptyDefault: Property = Property(name="text_01_EmptyDefault", type=StringType)
alldatatypes_Strings_link_01: Property = Property(name="link_01", type=StringType)
alldatatypes_Strings_html_01: Property = Property(name="html_01", type=StringType)
alldatatypes_Strings_notEditableText_01: Property = Property(name="notEditableText_01", type=StringType)
alldatatypes_Strings_text_01: Property = Property(name="text_01", type=StringType)
alldatatypes_Strings_text_1: Property = Property(name="text_1", type=StringType)
alldatatypes_Strings_textarea: Property = Property(name="textarea", type=StringType)
alldatatypes_Strings.attributes={alldatatypes_Strings_text_01_EmptyDefault, alldatatypes_Strings_link_01, alldatatypes_Strings_html_01, alldatatypes_Strings_notEditableText_01, alldatatypes_Strings_textarea, alldatatypes_Strings_text_1, alldatatypes_Strings_text_01}

# Type class attributes and methods

# alldatatypes_Dates class attributes and methods
alldatatypes_Dates_dateEmptyDefault_01: Property = Property(name="dateEmptyDefault_01", type=DateType)
alldatatypes_Dates_date_01: Property = Property(name="date_01", type=DateType)
alldatatypes_Dates_date_1: Property = Property(name="date_1", type=DateType)
alldatatypes_Dates_date_01_HM: Property = Property(name="date_01_HM", type=DateType)
alldatatypes_Dates_date_01_HMS: Property = Property(name="date_01_HMS", type=DateType)
alldatatypes_Dates_date_01_HMSms: Property = Property(name="date_01_HMSms", type=DateType)
alldatatypes_Dates_notEditableDate_01: Property = Property(name="notEditableDate_01", type=DateType)
alldatatypes_Dates_dates: Property = Property(name="dates", type=DateType)
alldatatypes_Dates.attributes={alldatatypes_Dates_dates, alldatatypes_Dates_date_01, alldatatypes_Dates_date_01_HM, alldatatypes_Dates_date_1, alldatatypes_Dates_date_01_HMS, alldatatypes_Dates_notEditableDate_01, alldatatypes_Dates_dateEmptyDefault_01, alldatatypes_Dates_date_01_HMSms}

# alldatatypes_Enums class attributes and methods
alldatatypes_Enums_enum_01: Property = Property(name="enum_01", type=StringType)
alldatatypes_Enums_enum_01_EmptyDefault: Property = Property(name="enum_01_EmptyDefault", type=StringType)
alldatatypes_Enums_enum_1: Property = Property(name="enum_1", type=StringType)
alldatatypes_Enums_enums: Property = Property(name="enums", type=StringType)
alldatatypes_Enums_notEditableEnum_01: Property = Property(name="notEditableEnum_01", type=StringType)
alldatatypes_Enums_states: Property = Property(name="states", type=StringType)
alldatatypes_Enums_statesMax2: Property = Property(name="statesMax2", type=StringType)
alldatatypes_Enums_statesMin1Max2: Property = Property(name="statesMin1Max2", type=StringType)
alldatatypes_Enums_heavy: Property = Property(name="heavy", type=StringType)
alldatatypes_Enums.attributes={alldatatypes_Enums_states, alldatatypes_Enums_enum_01, alldatatypes_Enums_enums, alldatatypes_Enums_enum_01_EmptyDefault, alldatatypes_Enums_statesMin1Max2, alldatatypes_Enums_statesMax2, alldatatypes_Enums_heavy, alldatatypes_Enums_notEditableEnum_01, alldatatypes_Enums_enum_1}

# alldatatypes_Booleans class attributes and methods
alldatatypes_Booleans_boolean_01: Property = Property(name="boolean_01", type=BooleanType)
alldatatypes_Booleans_boolean_01_EmptyDefault: Property = Property(name="boolean_01_EmptyDefault", type=BooleanType)
alldatatypes_Booleans_boolean_1: Property = Property(name="boolean_1", type=BooleanType)
alldatatypes_Booleans_notEditableBoolean_01: Property = Property(name="notEditableBoolean_01", type=BooleanType)
alldatatypes_Booleans.attributes={alldatatypes_Booleans_boolean_01, alldatatypes_Booleans_notEditableBoolean_01, alldatatypes_Booleans_boolean_1, alldatatypes_Booleans_boolean_01_EmptyDefault}

# alldatatypes_Integers class attributes and methods
alldatatypes_Integers_ints: Property = Property(name="ints", type=IntegerType)
alldatatypes_Integers_hiddenInt_01: Property = Property(name="hiddenInt_01", type=IntegerType)
alldatatypes_Integers_int_01: Property = Property(name="int_01", type=IntegerType)
alldatatypes_Integers_int_1: Property = Property(name="int_1", type=IntegerType)
alldatatypes_Integers_int_01_EmptyDefault: Property = Property(name="int_01_EmptyDefault", type=IntegerType)
alldatatypes_Integers_notEditableInt_01: Property = Property(name="notEditableInt_01", type=IntegerType)
alldatatypes_Integers.attributes={alldatatypes_Integers_hiddenInt_01, alldatatypes_Integers_int_01_EmptyDefault, alldatatypes_Integers_notEditableInt_01, alldatatypes_Integers_int_01, alldatatypes_Integers_ints, alldatatypes_Integers_int_1}

# alldatatypes_Longs class attributes and methods
alldatatypes_Longs_long_01: Property = Property(name="long_01", type=StringType)
alldatatypes_Longs_long_1: Property = Property(name="long_1", type=StringType)
alldatatypes_Longs_long_01_EmptyDefault: Property = Property(name="long_01_EmptyDefault", type=StringType)
alldatatypes_Longs_notEditableLong_01: Property = Property(name="notEditableLong_01", type=StringType)
alldatatypes_Longs.attributes={alldatatypes_Longs_notEditableLong_01, alldatatypes_Longs_long_01_EmptyDefault, alldatatypes_Longs_long_1, alldatatypes_Longs_long_01}

# alldatatypes_Shorts class attributes and methods
alldatatypes_Shorts_short_01: Property = Property(name="short_01", type=StringType)
alldatatypes_Shorts_short_1: Property = Property(name="short_1", type=StringType)
alldatatypes_Shorts_short_01_EmptyDefault: Property = Property(name="short_01_EmptyDefault", type=StringType)
alldatatypes_Shorts_notEditableShort_01: Property = Property(name="notEditableShort_01", type=StringType)
alldatatypes_Shorts.attributes={alldatatypes_Shorts_short_1, alldatatypes_Shorts_short_01_EmptyDefault, alldatatypes_Shorts_notEditableShort_01, alldatatypes_Shorts_short_01}

# alldatatypes_Doubles class attributes and methods
alldatatypes_Doubles_double_01: Property = Property(name="double_01", type=FloatType)
alldatatypes_Doubles_double_1: Property = Property(name="double_1", type=FloatType)
alldatatypes_Doubles_double_01_EmptyDefault: Property = Property(name="double_01_EmptyDefault", type=FloatType)
alldatatypes_Doubles_notEditableDouble_01: Property = Property(name="notEditableDouble_01", type=FloatType)
alldatatypes_Doubles.attributes={alldatatypes_Doubles_double_1, alldatatypes_Doubles_double_01, alldatatypes_Doubles_double_01_EmptyDefault, alldatatypes_Doubles_notEditableDouble_01}

# alldatatypes_Floats class attributes and methods
alldatatypes_Floats_float_01: Property = Property(name="float_01", type=FloatType)
alldatatypes_Floats_float_1: Property = Property(name="float_1", type=FloatType)
alldatatypes_Floats_float_01_EmptyDefault: Property = Property(name="float_01_EmptyDefault", type=FloatType)
alldatatypes_Floats_notEditableFloat_01: Property = Property(name="notEditableFloat_01", type=FloatType)
alldatatypes_Floats.attributes={alldatatypes_Floats_notEditableFloat_01, alldatatypes_Floats_float_1, alldatatypes_Floats_float_01_EmptyDefault, alldatatypes_Floats_float_01}

# alldatatypes_BigIntegers class attributes and methods
alldatatypes_BigIntegers_bigInt_01: Property = Property(name="bigInt_01", type=StringType)
alldatatypes_BigIntegers_bigInt_1: Property = Property(name="bigInt_1", type=StringType)
alldatatypes_BigIntegers_bigInt_01_EmptyDefault: Property = Property(name="bigInt_01_EmptyDefault", type=StringType)
alldatatypes_BigIntegers_notEditableBigInt_01: Property = Property(name="notEditableBigInt_01", type=StringType)
alldatatypes_BigIntegers_bigInts: Property = Property(name="bigInts", type=StringType)
alldatatypes_BigIntegers.attributes={alldatatypes_BigIntegers_notEditableBigInt_01, alldatatypes_BigIntegers_bigInt_01, alldatatypes_BigIntegers_bigInt_01_EmptyDefault, alldatatypes_BigIntegers_bigInt_1, alldatatypes_BigIntegers_bigInts}

# alldatatypes_BigDecimals class attributes and methods
alldatatypes_BigDecimals_bigDecimal_01: Property = Property(name="bigDecimal_01", type=StringType)
alldatatypes_BigDecimals_bigDecimal_1: Property = Property(name="bigDecimal_1", type=StringType)
alldatatypes_BigDecimals_bigDecimal_01_EmptyDefault: Property = Property(name="bigDecimal_01_EmptyDefault", type=StringType)
alldatatypes_BigDecimals_notEditableBigDecimal_01: Property = Property(name="notEditableBigDecimal_01", type=StringType)
alldatatypes_BigDecimals_bigDecimals: Property = Property(name="bigDecimals", type=StringType)
alldatatypes_BigDecimals.attributes={alldatatypes_BigDecimals_bigDecimals, alldatatypes_BigDecimals_notEditableBigDecimal_01, alldatatypes_BigDecimals_bigDecimal_01, alldatatypes_BigDecimals_bigDecimal_1, alldatatypes_BigDecimals_bigDecimal_01_EmptyDefault}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="alldatatypes_Type", type=alldatatypes_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="alldatatypes_Root", type=alldatatypes_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_alldatatypes_Root_Element = Generalization(general=Element, specific=alldatatypes_Root)
gen_alldatatypes_Type_Element = Generalization(general=Element, specific=alldatatypes_Type)
gen_alldatatypes_Strings_Type = Generalization(general=Type, specific=alldatatypes_Strings)
gen_alldatatypes_Dates_Type = Generalization(general=Type, specific=alldatatypes_Dates)
gen_alldatatypes_Enums_Type = Generalization(general=Type, specific=alldatatypes_Enums)
gen_alldatatypes_Booleans_Type = Generalization(general=Type, specific=alldatatypes_Booleans)
gen_alldatatypes_Integers_Type = Generalization(general=Type, specific=alldatatypes_Integers)
gen_alldatatypes_Longs_Type = Generalization(general=Type, specific=alldatatypes_Longs)
gen_alldatatypes_Shorts_Type = Generalization(general=Type, specific=alldatatypes_Shorts)
gen_alldatatypes_Doubles_Type = Generalization(general=Type, specific=alldatatypes_Doubles)
gen_alldatatypes_Floats_Type = Generalization(general=Type, specific=alldatatypes_Floats)
gen_alldatatypes_BigIntegers_Type = Generalization(general=Type, specific=alldatatypes_BigIntegers)
gen_alldatatypes_BigDecimals_Type = Generalization(general=Type, specific=alldatatypes_BigDecimals)

# Domain Model
domain_model = DomainModel(
    name="alldatatypes",
    types={alldatatypes_Element, alldatatypes_Root, Element, alldatatypes_Type, alldatatypes_Strings, Type, alldatatypes_Dates, alldatatypes_Enums, alldatatypes_Booleans, alldatatypes_Integers, alldatatypes_Longs, alldatatypes_Shorts, alldatatypes_Doubles, alldatatypes_Floats, alldatatypes_BigIntegers, alldatatypes_BigDecimals, AEnum, StateWithoutDefault, Heavy},
    associations={types0},
    generalizations={gen_alldatatypes_Root_Element, gen_alldatatypes_Type_Element, gen_alldatatypes_Strings_Type, gen_alldatatypes_Dates_Type, gen_alldatatypes_Enums_Type, gen_alldatatypes_Booleans_Type, gen_alldatatypes_Integers_Type, gen_alldatatypes_Longs_Type, gen_alldatatypes_Shorts_Type, gen_alldatatypes_Doubles_Type, gen_alldatatypes_Floats_Type, gen_alldatatypes_BigIntegers_Type, gen_alldatatypes_BigDecimals_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)