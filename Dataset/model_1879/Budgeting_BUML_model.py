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
MonthEnum: Enumeration = Enumeration(
    name="MonthEnum",
    literals={
            EnumerationLiteral(name="AUGUST"),
			EnumerationLiteral(name="SEPTEMBER"),
			EnumerationLiteral(name="OCTOBER"),
			EnumerationLiteral(name="JANUARY"),
			EnumerationLiteral(name="FEBRUARY"),
			EnumerationLiteral(name="MARCH"),
			EnumerationLiteral(name="APRIL"),
			EnumerationLiteral(name="MAY"),
			EnumerationLiteral(name="JUNE"),
			EnumerationLiteral(name="JULY"),
			EnumerationLiteral(name="NOVEMBER"),
			EnumerationLiteral(name="DECEMBER")
    }
)

# Classes
budgeting_BudgetingFile = Class(name="budgeting::BudgetingFile")
budgeting_Library = Class(name="budgeting::Library")
BudgetingFile = Class(name="BudgetingFile")
budgeting_Category = Class(name="budgeting::Category")
budgeting_Year = Class(name="budgeting::Year")
budgeting_Month = Class(name="budgeting::Month")
budgeting_BudgetEntry = Class(name="budgeting::BudgetEntry")
budgeting_ActualEntry = Class(name="budgeting::ActualEntry")
budgeting_BudgetFactorEntry = Class(name="budgeting::BudgetFactorEntry")
budgeting_Transaction = Class(name="budgeting::Transaction")
budgeting_IncomeCategory = Class(name="budgeting::IncomeCategory")
Category = Class(name="Category")
budgeting_ExpenseCategory = Class(name="budgeting::ExpenseCategory")
budgeting_BudgetAmountEntry = Class(name="budgeting::BudgetAmountEntry")
BudgetEntry = Class(name="BudgetEntry")
budgeting_ActualAmountEntry = Class(name="budgeting::ActualAmountEntry")
ActualEntry = Class(name="ActualEntry")
budgeting_ActualTransactionEntry = Class(name="budgeting::ActualTransactionEntry")
budgeting_CashTransaction = Class(name="budgeting::CashTransaction")
Transaction = Class(name="Transaction")
budgeting_CardTransaction = Class(name="budgeting::CardTransaction")

# budgeting_BudgetingFile class attributes and methods

# budgeting_Library class attributes and methods
budgeting_Library_name: Property = Property(name="name", type=StringType)
budgeting_Library.attributes={budgeting_Library_name}

# BudgetingFile class attributes and methods

# budgeting_Category class attributes and methods
budgeting_Category_name: Property = Property(name="name", type=StringType)
budgeting_Category.attributes={budgeting_Category_name}

# budgeting_Year class attributes and methods
budgeting_Year_name: Property = Property(name="name", type=IntegerType)
budgeting_Year.attributes={budgeting_Year_name}

# budgeting_Month class attributes and methods
budgeting_Month_name: Property = Property(name="name", type=StringType)
budgeting_Month.attributes={budgeting_Month_name}

# budgeting_BudgetEntry class attributes and methods

# budgeting_ActualEntry class attributes and methods

# budgeting_BudgetFactorEntry class attributes and methods
budgeting_BudgetFactorEntry_factor: Property = Property(name="factor", type=FloatType)
budgeting_BudgetFactorEntry.attributes={budgeting_BudgetFactorEntry_factor}

# budgeting_Transaction class attributes and methods
budgeting_Transaction_amount: Property = Property(name="amount", type=StringType)
budgeting_Transaction.attributes={budgeting_Transaction_amount}

# budgeting_IncomeCategory class attributes and methods

# Category class attributes and methods

# budgeting_ExpenseCategory class attributes and methods
budgeting_ExpenseCategory_patterns: Property = Property(name="patterns", type=StringType)
budgeting_ExpenseCategory.attributes={budgeting_ExpenseCategory_patterns}

# budgeting_BudgetAmountEntry class attributes and methods
budgeting_BudgetAmountEntry_amount: Property = Property(name="amount", type=StringType)
budgeting_BudgetAmountEntry.attributes={budgeting_BudgetAmountEntry_amount}

# BudgetEntry class attributes and methods

# budgeting_ActualAmountEntry class attributes and methods
budgeting_ActualAmountEntry_amount: Property = Property(name="amount", type=StringType)
budgeting_ActualAmountEntry.attributes={budgeting_ActualAmountEntry_amount}

# ActualEntry class attributes and methods

# budgeting_ActualTransactionEntry class attributes and methods

# budgeting_CashTransaction class attributes and methods
budgeting_CashTransaction_day: Property = Property(name="day", type=StringType)
budgeting_CashTransaction.attributes={budgeting_CashTransaction_day}

# Transaction class attributes and methods

# budgeting_CardTransaction class attributes and methods
budgeting_CardTransaction_day: Property = Property(name="day", type=IntegerType)
budgeting_CardTransaction_from: Property = Property(name="from", type=StringType)
budgeting_CardTransaction.attributes={budgeting_CardTransaction_from, budgeting_CardTransaction_day}

# Relationships
library1: BinaryAssociation = BinaryAssociation(
    name="library1",
    ends={
        Property(name="budgeting_Library2", type=budgeting_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_Year", type=budgeting_Library, multiplicity=Multiplicity(0, 1))
    }
)
categories0: BinaryAssociation = BinaryAssociation(
    name="categories0",
    ends={
        Property(name="budgeting_Category", type=budgeting_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_Library", type=budgeting_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
months3: BinaryAssociation = BinaryAssociation(
    name="months3",
    ends={
        Property(name="budgeting_Month", type=budgeting_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_Year4", type=budgeting_Month, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
budgetEntries5: BinaryAssociation = BinaryAssociation(
    name="budgetEntries5",
    ends={
        Property(name="budgeting_BudgetEntry", type=budgeting_Month, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_Month6", type=budgeting_BudgetEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actualEntries7: BinaryAssociation = BinaryAssociation(
    name="actualEntries7",
    ends={
        Property(name="budgeting_ActualEntry", type=budgeting_Month, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_Month8", type=budgeting_ActualEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category9: BinaryAssociation = BinaryAssociation(
    name="category9",
    ends={
        Property(name="budgeting_Category11", type=budgeting_BudgetEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_BudgetEntry10", type=budgeting_Category, multiplicity=Multiplicity(0, 1))
    }
)
category12: BinaryAssociation = BinaryAssociation(
    name="category12",
    ends={
        Property(name="budgeting_Category14", type=budgeting_ActualEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_ActualEntry13", type=budgeting_Category, multiplicity=Multiplicity(0, 1))
    }
)
baseEntry15: BinaryAssociation = BinaryAssociation(
    name="baseEntry15",
    ends={
        Property(name="budgeting_BudgetEntry16", type=budgeting_BudgetFactorEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_BudgetFactorEntry", type=budgeting_BudgetEntry, multiplicity=Multiplicity(0, 1))
    }
)
transactions17: BinaryAssociation = BinaryAssociation(
    name="transactions17",
    ends={
        Property(name="budgeting_Transaction", type=budgeting_ActualTransactionEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="budgeting_ActualTransactionEntry", type=budgeting_Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_budgeting_Library_BudgetingFile = Generalization(general=BudgetingFile, specific=budgeting_Library)
gen_budgeting_Year_BudgetingFile = Generalization(general=BudgetingFile, specific=budgeting_Year)
gen_budgeting_BudgetFactorEntry_BudgetEntry = Generalization(general=BudgetEntry, specific=budgeting_BudgetFactorEntry)
gen_budgeting_IncomeCategory_Category = Generalization(general=Category, specific=budgeting_IncomeCategory)
gen_budgeting_ExpenseCategory_Category = Generalization(general=Category, specific=budgeting_ExpenseCategory)
gen_budgeting_BudgetAmountEntry_BudgetEntry = Generalization(general=BudgetEntry, specific=budgeting_BudgetAmountEntry)
gen_budgeting_ActualAmountEntry_ActualEntry = Generalization(general=ActualEntry, specific=budgeting_ActualAmountEntry)
gen_budgeting_ActualTransactionEntry_ActualEntry = Generalization(general=ActualEntry, specific=budgeting_ActualTransactionEntry)
gen_budgeting_CashTransaction_Transaction = Generalization(general=Transaction, specific=budgeting_CashTransaction)
gen_budgeting_CardTransaction_Transaction = Generalization(general=Transaction, specific=budgeting_CardTransaction)

# Domain Model
domain_model = DomainModel(
    name="budgeting",
    types={budgeting_BudgetingFile, budgeting_Library, BudgetingFile, budgeting_Category, budgeting_Year, budgeting_Month, budgeting_BudgetEntry, budgeting_ActualEntry, budgeting_BudgetFactorEntry, budgeting_Transaction, budgeting_IncomeCategory, Category, budgeting_ExpenseCategory, budgeting_BudgetAmountEntry, BudgetEntry, budgeting_ActualAmountEntry, ActualEntry, budgeting_ActualTransactionEntry, budgeting_CashTransaction, Transaction, budgeting_CardTransaction, MonthEnum},
    associations={library1, categories0, months3, budgetEntries5, actualEntries7, category9, category12, baseEntry15, transactions17},
    generalizations={gen_budgeting_Library_BudgetingFile, gen_budgeting_Year_BudgetingFile, gen_budgeting_BudgetFactorEntry_BudgetEntry, gen_budgeting_IncomeCategory_Category, gen_budgeting_ExpenseCategory_Category, gen_budgeting_BudgetAmountEntry_BudgetEntry, gen_budgeting_ActualAmountEntry_ActualEntry, gen_budgeting_ActualTransactionEntry_ActualEntry, gen_budgeting_CashTransaction_Transaction, gen_budgeting_CardTransaction_Transaction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)