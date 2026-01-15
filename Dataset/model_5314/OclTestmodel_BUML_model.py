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
ocltestmodel_MyClass = Class(name="ocltestmodel::MyClass")

# ocltestmodel_MyClass class attributes and methods
ocltestmodel_MyClass_static_sequence: Property = Property(name="static_sequence", type=StringType)
ocltestmodel_MyClass_collection_literals: Property = Property(name="collection_literals", type=StringType)
ocltestmodel_MyClass_boolean_unequal: Property = Property(name="boolean_unequal", type=BooleanType)
ocltestmodel_MyClass_boolean_equal: Property = Property(name="boolean_equal", type=BooleanType)
ocltestmodel_MyClass_boolean_and: Property = Property(name="boolean_and", type=BooleanType)
ocltestmodel_MyClass_integer_addition: Property = Property(name="integer_addition", type=IntegerType)
ocltestmodel_MyClass_integer_subtraction: Property = Property(name="integer_subtraction", type=IntegerType)
ocltestmodel_MyClass_integer_lessthan: Property = Property(name="integer_lessthan", type=BooleanType)
ocltestmodel_MyClass_integer_greaterthan: Property = Property(name="integer_greaterthan", type=BooleanType)
ocltestmodel_MyClass_integer_greaterequals: Property = Property(name="integer_greaterequals", type=BooleanType)
ocltestmodel_MyClass_integer_lessequals: Property = Property(name="integer_lessequals", type=BooleanType)
ocltestmodel_MyClass_integer_division: Property = Property(name="integer_division", type=FloatType)
ocltestmodel_MyClass_integer_absolute: Property = Property(name="integer_absolute", type=IntegerType)
ocltestmodel_MyClass_integer_maximum: Property = Property(name="integer_maximum", type=IntegerType)
ocltestmodel_MyClass_integer_minimum: Property = Property(name="integer_minimum", type=IntegerType)
ocltestmodel_MyClass_integer_modulo: Property = Property(name="integer_modulo", type=IntegerType)
ocltestmodel_MyClass_integer_toString: Property = Property(name="integer_toString", type=StringType)
ocltestmodel_MyClass_boolean_implies: Property = Property(name="boolean_implies", type=BooleanType)
ocltestmodel_MyClass_boolean_not: Property = Property(name="boolean_not", type=BooleanType)
ocltestmodel_MyClass_boolean_or: Property = Property(name="boolean_or", type=BooleanType)
ocltestmodel_MyClass_boolean_xor: Property = Property(name="boolean_xor", type=BooleanType)
ocltestmodel_MyClass_boolean_toString: Property = Property(name="boolean_toString", type=StringType)
ocltestmodel_MyClass_integer_multiplication: Property = Property(name="integer_multiplication", type=IntegerType)
ocltestmodel_MyClass_real_lessequals: Property = Property(name="real_lessequals", type=BooleanType)
ocltestmodel_MyClass_real_division: Property = Property(name="real_division", type=StringType)
ocltestmodel_MyClass_real_absolute: Property = Property(name="real_absolute", type=StringType)
ocltestmodel_MyClass_real_maximum: Property = Property(name="real_maximum", type=StringType)
ocltestmodel_MyClass_real_minimum: Property = Property(name="real_minimum", type=StringType)
ocltestmodel_MyClass_real_floor: Property = Property(name="real_floor", type=StringType)
ocltestmodel_MyClass_real_toString: Property = Property(name="real_toString", type=StringType)
ocltestmodel_MyClass_string_addition: Property = Property(name="string_addition", type=StringType)
ocltestmodel_MyClass_string_lessthan: Property = Property(name="string_lessthan", type=BooleanType)
ocltestmodel_MyClass_string_lessequals: Property = Property(name="string_lessequals", type=BooleanType)
ocltestmodel_MyClass_string_unequal: Property = Property(name="string_unequal", type=BooleanType)
ocltestmodel_MyClass_string_equal: Property = Property(name="string_equal", type=BooleanType)
ocltestmodel_MyClass_string_greaterthan: Property = Property(name="string_greaterthan", type=BooleanType)
ocltestmodel_MyClass_real_multiplication: Property = Property(name="real_multiplication", type=StringType)
ocltestmodel_MyClass_real_addition: Property = Property(name="real_addition", type=StringType)
ocltestmodel_MyClass_real_subtraction: Property = Property(name="real_subtraction", type=StringType)
ocltestmodel_MyClass_real_lessthan: Property = Property(name="real_lessthan", type=BooleanType)
ocltestmodel_MyClass_real_greaterthan: Property = Property(name="real_greaterthan", type=BooleanType)
ocltestmodel_MyClass_real_greaterequals: Property = Property(name="real_greaterequals", type=BooleanType)
ocltestmodel_MyClass_string_replaceAll: Property = Property(name="string_replaceAll", type=StringType)
ocltestmodel_MyClass_string_size: Property = Property(name="string_size", type=StringType)
ocltestmodel_MyClass_let2: Property = Property(name="let2", type=BooleanType)
ocltestmodel_MyClass_let3: Property = Property(name="let3", type=IntegerType)
ocltestmodel_MyClass_unEmployed: Property = Property(name="unEmployed", type=BooleanType)
ocltestmodel_MyClass_let: Property = Property(name="let", type=BooleanType)
ocltestmodel_MyClass_integer_sequence: Property = Property(name="integer_sequence", type=IntegerType)
ocltestmodel_MyClass_sequence_selectByKind: Property = Property(name="sequence_selectByKind", type=StringType)
ocltestmodel_MyClass_string_greaterequals: Property = Property(name="string_greaterequals", type=BooleanType)
ocltestmodel_MyClass_string_at: Property = Property(name="string_at", type=StringType)
ocltestmodel_MyClass_string_compareTo: Property = Property(name="string_compareTo", type=StringType)
ocltestmodel_MyClass_string_concat: Property = Property(name="string_concat", type=StringType)
ocltestmodel_MyClass_string_equalsIgnoreCase: Property = Property(name="string_equalsIgnoreCase", type=BooleanType)
ocltestmodel_MyClass_string_indexOf: Property = Property(name="string_indexOf", type=StringType)
ocltestmodel_MyClass_string_lastIndexOf: Property = Property(name="string_lastIndexOf", type=StringType)
ocltestmodel_MyClass__IntegerLiteralExp: Property = Property(name="_IntegerLiteralExp", type=StringType)
ocltestmodel_MyClass__InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER: Property = Property(name="_InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER", type=StringType)
ocltestmodel_MyClass__StringLiteralExp: Property = Property(name="_StringLiteralExp", type=StringType)
ocltestmodel_MyClass__BooleanLiteralExp: Property = Property(name="_BooleanLiteralExp", type=BooleanType)
ocltestmodel_MyClass__RealLiteralExp: Property = Property(name="_RealLiteralExp", type=StringType)
ocltestmodel_MyClass__NumberLiteralExp: Property = Property(name="_NumberLiteralExp", type=StringType)
ocltestmodel_MyClass__IfExp: Property = Property(name="_IfExp", type=StringType)
ocltestmodel_MyClass__IfExp2: Property = Property(name="_IfExp2", type=StringType)
ocltestmodel_MyClass_sequence_selectByType: Property = Property(name="sequence_selectByType", type=StringType)
ocltestmodel_MyClass_tuple_literal: Property = Property(name="tuple_literal", type=BooleanType)
ocltestmodel_MyClass_orderedset_size: Property = Property(name="orderedset_size", type=StringType)
ocltestmodel_MyClass_sequence_count: Property = Property(name="sequence_count", type=StringType)
ocltestmodel_MyClass.attributes={ocltestmodel_MyClass__BooleanLiteralExp, ocltestmodel_MyClass_string_greaterequals, ocltestmodel_MyClass_integer_sequence, ocltestmodel_MyClass_real_lessequals, ocltestmodel_MyClass__IfExp2, ocltestmodel_MyClass_collection_literals, ocltestmodel_MyClass_integer_lessthan, ocltestmodel_MyClass_string_replaceAll, ocltestmodel_MyClass_integer_lessequals, ocltestmodel_MyClass_integer_greaterequals, ocltestmodel_MyClass_integer_multiplication, ocltestmodel_MyClass_boolean_unequal, ocltestmodel_MyClass_real_lessthan, ocltestmodel_MyClass_boolean_and, ocltestmodel_MyClass_string_addition, ocltestmodel_MyClass_string_concat, ocltestmodel_MyClass_string_indexOf, ocltestmodel_MyClass_real_greaterequals, ocltestmodel_MyClass_real_absolute, ocltestmodel_MyClass_boolean_toString, ocltestmodel_MyClass_let3, ocltestmodel_MyClass_string_lessequals, ocltestmodel_MyClass__RealLiteralExp, ocltestmodel_MyClass_integer_division, ocltestmodel_MyClass_real_greaterthan, ocltestmodel_MyClass_string_equalsIgnoreCase, ocltestmodel_MyClass__IfExp, ocltestmodel_MyClass_real_toString, ocltestmodel_MyClass_string_lessthan, ocltestmodel_MyClass__IntegerLiteralExp, ocltestmodel_MyClass_boolean_xor, ocltestmodel_MyClass_boolean_not, ocltestmodel_MyClass_string_compareTo, ocltestmodel_MyClass_boolean_or, ocltestmodel_MyClass_sequence_selectByType, ocltestmodel_MyClass_tuple_literal, ocltestmodel_MyClass_sequence_count, ocltestmodel_MyClass__InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER, ocltestmodel_MyClass_real_floor, ocltestmodel_MyClass_let, ocltestmodel_MyClass_string_at, ocltestmodel_MyClass_string_equal, ocltestmodel_MyClass_boolean_implies, ocltestmodel_MyClass_static_sequence, ocltestmodel_MyClass_string_size, ocltestmodel_MyClass_boolean_equal, ocltestmodel_MyClass_string_lastIndexOf, ocltestmodel_MyClass_integer_toString, ocltestmodel_MyClass_unEmployed, ocltestmodel_MyClass__NumberLiteralExp, ocltestmodel_MyClass__StringLiteralExp, ocltestmodel_MyClass_integer_maximum, ocltestmodel_MyClass_integer_subtraction, ocltestmodel_MyClass_real_multiplication, ocltestmodel_MyClass_integer_greaterthan, ocltestmodel_MyClass_string_unequal, ocltestmodel_MyClass_orderedset_size, ocltestmodel_MyClass_integer_addition, ocltestmodel_MyClass_integer_modulo, ocltestmodel_MyClass_real_subtraction, ocltestmodel_MyClass_real_minimum, ocltestmodel_MyClass_sequence_selectByKind, ocltestmodel_MyClass_integer_absolute, ocltestmodel_MyClass_real_maximum, ocltestmodel_MyClass_let2, ocltestmodel_MyClass_real_division, ocltestmodel_MyClass_string_greaterthan, ocltestmodel_MyClass_integer_minimum, ocltestmodel_MyClass_real_addition}

# Relationships
orderedset1: BinaryAssociation = BinaryAssociation(
    name="orderedset1",
    ends={
        Property(name="ocltestmodel_MyClass", type=ocltestmodel_MyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltestmodel_MyClass0", type=ocltestmodel_MyClass, multiplicity=Multiplicity(0, 9999))
    }
)
set3: BinaryAssociation = BinaryAssociation(
    name="set3",
    ends={
        Property(name="ocltestmodel_MyClass4", type=ocltestmodel_MyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltestmodel_MyClass2", type=ocltestmodel_MyClass, multiplicity=Multiplicity(0, 9999))
    }
)
sequence6: BinaryAssociation = BinaryAssociation(
    name="sequence6",
    ends={
        Property(name="ocltestmodel_MyClass7", type=ocltestmodel_MyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltestmodel_MyClass5", type=ocltestmodel_MyClass, multiplicity=Multiplicity(0, 9999))
    }
)
bag9: BinaryAssociation = BinaryAssociation(
    name="bag9",
    ends={
        Property(name="ocltestmodel_MyClass10", type=ocltestmodel_MyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltestmodel_MyClass8", type=ocltestmodel_MyClass, multiplicity=Multiplicity(0, 9999))
    }
)
orderedset_at15: BinaryAssociation = BinaryAssociation(
    name="orderedset_at15",
    ends={
        Property(name="ocltestmodel_MyClass16", type=ocltestmodel_MyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltestmodel_MyClass14", type=ocltestmodel_MyClass, multiplicity=Multiplicity(0, 1))
    }
)
_SelfExp18: BinaryAssociation = BinaryAssociation(
    name="_SelfExp18",
    ends={
        Property(name="ocltestmodel_MyClass19", type=ocltestmodel_MyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltestmodel_MyClass17", type=ocltestmodel_MyClass, multiplicity=Multiplicity(0, 1))
    }
)
_NullExp21: BinaryAssociation = BinaryAssociation(
    name="_NullExp21",
    ends={
        Property(name="ocltestmodel_MyClass22", type=ocltestmodel_MyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltestmodel_MyClass20", type=ocltestmodel_MyClass, multiplicity=Multiplicity(0, 1))
    }
)
orderedset_select12: BinaryAssociation = BinaryAssociation(
    name="orderedset_select12",
    ends={
        Property(name="ocltestmodel_MyClass13", type=ocltestmodel_MyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltestmodel_MyClass11", type=ocltestmodel_MyClass, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ocltestmodel",
    types={ocltestmodel_MyClass},
    associations={orderedset1, set3, sequence6, bag9, orderedset_at15, _SelfExp18, _NullExp21, orderedset_select12},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)