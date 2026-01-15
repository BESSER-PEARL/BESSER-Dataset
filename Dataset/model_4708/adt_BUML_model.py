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
adt_ADT = Class(name="adt::ADT")
adt_Signature = Class(name="adt::Signature")
adt_VariableDeclaration = Class(name="adt::VariableDeclaration")
adt_Equation = Class(name="adt::Equation")
adt_ASort = Class(name="adt::ASort", is_abstract=True)
adt_SubSort = Class(name="adt::SubSort")
ASort = Class(name="ASort")
adt_Sort = Class(name="adt::Sort")
adt_ATerm = Class(name="adt::ATerm", is_abstract=True)
adt_Term = Class(name="adt::Term")
ATerm = Class(name="ATerm")
adt_Variable = Class(name="adt::Variable")
adt_Operation = Class(name="adt::Operation")

# adt_ADT class attributes and methods
adt_ADT_name: Property = Property(name="name", type=StringType)
adt_ADT.attributes={adt_ADT_name}

# adt_Signature class attributes and methods
adt_Signature_ops: Property = Property(name="ops", type=StringType)
adt_Signature.attributes={adt_Signature_ops}

# adt_VariableDeclaration class attributes and methods
adt_VariableDeclaration_name: Property = Property(name="name", type=StringType)
adt_VariableDeclaration.attributes={adt_VariableDeclaration_name}

# adt_Equation class attributes and methods

# adt_ASort class attributes and methods
adt_ASort_name: Property = Property(name="name", type=StringType)
adt_ASort_m_isSubSortOf: Method = Method(name="isSubSortOf", parameters={Parameter(name='sort')}, type=BooleanType)
adt_ASort.attributes={adt_ASort_name}
adt_ASort.methods={adt_ASort_m_isSubSortOf}

# adt_SubSort class attributes and methods

# ASort class attributes and methods

# adt_Sort class attributes and methods

# adt_ATerm class attributes and methods
adt_ATerm_symbol: Property = Property(name="symbol", type=StringType)
adt_ATerm.attributes={adt_ATerm_symbol}

# adt_Term class attributes and methods

# ATerm class attributes and methods

# adt_Variable class attributes and methods

# adt_Operation class attributes and methods
adt_Operation_name: Property = Property(name="name", type=StringType)
adt_Operation.attributes={adt_Operation_name}

# Relationships
signature0: BinaryAssociation = BinaryAssociation(
    name="signature0",
    ends={
        Property(name="adt_Signature", type=adt_ADT, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_ADT", type=adt_Signature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variables1: BinaryAssociation = BinaryAssociation(
    name="variables1",
    ends={
        Property(name="adt_VariableDeclaration", type=adt_ADT, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_ADT2", type=adt_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equations3: BinaryAssociation = BinaryAssociation(
    name="equations3",
    ends={
        Property(name="adt_Equation", type=adt_ADT, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_ADT4", type=adt_Equation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superSort5: BinaryAssociation = BinaryAssociation(
    name="superSort5",
    ends={
        Property(name="adt_ASort", type=adt_SubSort, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_SubSort", type=adt_ASort, multiplicity=Multiplicity(1, 1))
    }
)
sort17: BinaryAssociation = BinaryAssociation(
    name="sort17",
    ends={
        Property(name="adt_ASort19", type=adt_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_VariableDeclaration18", type=adt_ASort, multiplicity=Multiplicity(1, 1))
    }
)
returnType20: BinaryAssociation = BinaryAssociation(
    name="returnType20",
    ends={
        Property(name="adt_ASort22", type=adt_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Operation21", type=adt_ASort, multiplicity=Multiplicity(1, 1))
    }
)
formalParameters23: BinaryAssociation = BinaryAssociation(
    name="formalParameters23",
    ends={
        Property(name="adt_ASort25", type=adt_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Operation24", type=adt_ASort, multiplicity=Multiplicity(0, 9999))
    }
)
adt26: BinaryAssociation = BinaryAssociation(
    name="adt26",
    ends={
        Property(name="adt_ADT27", type=adt_ATerm, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_ATerm", type=adt_ADT, multiplicity=Multiplicity(1, 1))
    }
)
sort28: BinaryAssociation = BinaryAssociation(
    name="sort28",
    ends={
        Property(name="adt_ASort30", type=adt_ATerm, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_ATerm29", type=adt_ASort, multiplicity=Multiplicity(1, 1))
    }
)
operationSymbol31: BinaryAssociation = BinaryAssociation(
    name="operationSymbol31",
    ends={
        Property(name="adt_Operation32", type=adt_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Term", type=adt_Operation, multiplicity=Multiplicity(1, 1))
    }
)
subterms33: BinaryAssociation = BinaryAssociation(
    name="subterms33",
    ends={
        Property(name="adt_ATerm35", type=adt_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Term34", type=adt_ATerm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allOperations6: BinaryAssociation = BinaryAssociation(
    name="allOperations6",
    ends={
        Property(name="adt_Operation", type=adt_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Signature7", type=adt_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
sorts8: BinaryAssociation = BinaryAssociation(
    name="sorts8",
    ends={
        Property(name="adt_ASort10", type=adt_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Signature9", type=adt_ASort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
operations11: BinaryAssociation = BinaryAssociation(
    name="operations11",
    ends={
        Property(name="adt_Operation13", type=adt_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Signature12", type=adt_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generators14: BinaryAssociation = BinaryAssociation(
    name="generators14",
    ends={
        Property(name="adt_Operation16", type=adt_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Signature15", type=adt_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
declaration36: BinaryAssociation = BinaryAssociation(
    name="declaration36",
    ends={
        Property(name="adt_VariableDeclaration37", type=adt_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Variable", type=adt_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
leftHandTerm38: BinaryAssociation = BinaryAssociation(
    name="leftHandTerm38",
    ends={
        Property(name="adt_ATerm40", type=adt_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Equation39", type=adt_ATerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandTerm41: BinaryAssociation = BinaryAssociation(
    name="rightHandTerm41",
    ends={
        Property(name="adt_ATerm43", type=adt_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="adt_Equation42", type=adt_ATerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_adt_SubSort_ASort = Generalization(general=ASort, specific=adt_SubSort)
gen_adt_Sort_ASort = Generalization(general=ASort, specific=adt_Sort)
gen_adt_Term_ATerm = Generalization(general=ATerm, specific=adt_Term)
gen_adt_Variable_ATerm = Generalization(general=ATerm, specific=adt_Variable)

# Domain Model
domain_model = DomainModel(
    name="adt",
    types={adt_ADT, adt_Signature, adt_VariableDeclaration, adt_Equation, adt_ASort, adt_SubSort, ASort, adt_Sort, adt_ATerm, adt_Term, ATerm, adt_Variable, adt_Operation},
    associations={signature0, variables1, equations3, superSort5, sort17, returnType20, formalParameters23, adt26, sort28, operationSymbol31, subterms33, allOperations6, sorts8, operations11, generators14, declaration36, leftHandTerm38, rightHandTerm41},
    generalizations={gen_adt_SubSort_ASort, gen_adt_Sort_ASort, gen_adt_Term_ATerm, gen_adt_Variable_ATerm},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)