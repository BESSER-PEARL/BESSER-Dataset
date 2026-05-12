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
ATM_transactions = Class(name="ATM_transactions")
Withdraw_Cash_Interface_Interface = Class(name="Withdraw_Cash_Interface_Interface")
Withdraw_Cash_Customer_Actor = Class(name="Withdraw_Cash_Customer_Actor")
Withdraw_Cash_Bank_Server_Actor = Class(name="Withdraw_Cash_Bank_Server_Actor")
Withdraw_Cash_Go_to_ATM_UseCase = Class(name="Withdraw_Cash_Go_to_ATM_UseCase")
Withdraw_Cash_Insert_the_Card____UseCase = Class(name="Withdraw_Cash_Insert_the_Card____UseCase")
Withdraw_Cash__Enter_the_PIN_UseCase = Class(name="Withdraw_Cash__Enter_the_PIN_UseCase")
Withdraw_Cash__Display_MENU_ATM___UseCase = Class(name="Withdraw_Cash__Display_MENU_ATM___UseCase")
Withdraw_Cash_Withdraw_Cash_UseCase = Class(name="Withdraw_Cash_Withdraw_Cash_UseCase")
Withdraw_Cash_Select_Account_UseCase = Class(name="Withdraw_Cash_Select_Account_UseCase")
Withdraw_Cash_Enter_Amount_UseCase = Class(name="Withdraw_Cash_Enter_Amount_UseCase")
Withdraw_Cash_Collect_Cash_UseCase = Class(name="Withdraw_Cash_Collect_Cash_UseCase")
Withdraw_Cash__15____Take_print_out_UseCase = Class(name="Withdraw_Cash__15____Take_print_out_UseCase")
Withdraw_Cash__Block_the_card_UseCase = Class(name="Withdraw_Cash__Block_the_card_UseCase")
Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase = Class(name="Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase")
Withdraw_Cash_Display_the_PIN_screen_UseCase = Class(name="Withdraw_Cash_Display_the_PIN_screen_UseCase")
Withdraw_Cash__Verify_the_card___UseCase = Class(name="Withdraw_Cash__Verify_the_card___UseCase")
Withdraw_Cash_Verify_the_PIN_UseCase = Class(name="Withdraw_Cash_Verify_the_PIN_UseCase")
Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase = Class(name="Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase")
Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase = Class(name="Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase")
Withdraw_Cash_Display_MENU_ATM__UseCase = Class(name="Withdraw_Cash_Display_MENU_ATM__UseCase")
Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase = Class(name="Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase")
Withdraw_Cash_Display_amount_UseCase = Class(name="Withdraw_Cash_Display_amount_UseCase")
Withdraw_Cash__Verify_check_the_available_balance_UseCase = Class(name="Withdraw_Cash__Verify_check_the_available_balance_UseCase")
Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase = Class(name="Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase")
Withdraw_Cash_Display_error_else_UseCase = Class(name="Withdraw_Cash_Display_error_else_UseCase")
Withdraw_Cash_Dispense_the_cash_UseCase = Class(name="Withdraw_Cash_Dispense_the_cash_UseCase")

# ATM_transactions class attributes and methods

# Withdraw_Cash_Interface_Interface class attributes and methods

# Withdraw_Cash_Customer_Actor class attributes and methods

# Withdraw_Cash_Bank_Server_Actor class attributes and methods

# Withdraw_Cash_Go_to_ATM_UseCase class attributes and methods

# Withdraw_Cash_Insert_the_Card____UseCase class attributes and methods

# Withdraw_Cash__Enter_the_PIN_UseCase class attributes and methods

# Withdraw_Cash__Display_MENU_ATM___UseCase class attributes and methods

# Withdraw_Cash_Withdraw_Cash_UseCase class attributes and methods

# Withdraw_Cash_Select_Account_UseCase class attributes and methods

# Withdraw_Cash_Enter_Amount_UseCase class attributes and methods

# Withdraw_Cash_Collect_Cash_UseCase class attributes and methods

# Withdraw_Cash__15____Take_print_out_UseCase class attributes and methods

# Withdraw_Cash__Block_the_card_UseCase class attributes and methods

# Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase class attributes and methods

# Withdraw_Cash_Display_the_PIN_screen_UseCase class attributes and methods

# Withdraw_Cash__Verify_the_card___UseCase class attributes and methods

# Withdraw_Cash_Verify_the_PIN_UseCase class attributes and methods

# Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase class attributes and methods

# Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase class attributes and methods

# Withdraw_Cash_Display_MENU_ATM__UseCase class attributes and methods

# Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase class attributes and methods

# Withdraw_Cash_Display_amount_UseCase class attributes and methods

# Withdraw_Cash__Verify_check_the_available_balance_UseCase class attributes and methods

# Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase class attributes and methods

# Withdraw_Cash_Display_error_else_UseCase class attributes and methods

# Withdraw_Cash_Dispense_the_cash_UseCase class attributes and methods

# Relationships
Customer_Go_to_ATM: BinaryAssociation = BinaryAssociation(
    name="Customer_Go_to_ATM",
    ends={
        Property(name="go_to_ATM0", type=Withdraw_Cash_Go_to_ATM_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Withdraw_Cash_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Insert_the_Card: BinaryAssociation = BinaryAssociation(
    name="Customer_Insert_the_Card",
    ends={
        Property(name="insert_the_Card2", type=Withdraw_Cash_Insert_the_Card____UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Withdraw_Cash_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Enter_the_PIN_Customer: BinaryAssociation = BinaryAssociation(
    name="Enter_the_PIN_Customer",
    ends={
        Property(name="customer4", type=Withdraw_Cash_Customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="Enter_the_PIN5", type=Withdraw_Cash__Enter_the_PIN_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer__Display_MENU_ATM_: BinaryAssociation = BinaryAssociation(
    name="Customer__Display_MENU_ATM_",
    ends={
        Property(name="Display_MENU_ATM_6", type=Withdraw_Cash__Display_MENU_ATM___UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Withdraw_Cash_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Collect_Cash: BinaryAssociation = BinaryAssociation(
    name="Customer_Collect_Cash",
    ends={
        Property(name="collect_Cash14", type=Withdraw_Cash_Collect_Cash_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer15", type=Withdraw_Cash_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Server_Display_the_PIN_screen: BinaryAssociation = BinaryAssociation(
    name="Bank_Server_Display_the_PIN_screen",
    ends={
        Property(name="display_the_PIN_screen16", type=Withdraw_Cash_Display_the_PIN_screen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="bank_Server17", type=Withdraw_Cash_Bank_Server_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Display_MENU_ATM__Bank_Server: BinaryAssociation = BinaryAssociation(
    name="Display_MENU_ATM__Bank_Server",
    ends={
        Property(name="bank_Server18", type=Withdraw_Cash_Bank_Server_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="display_MENU_ATM_19", type=Withdraw_Cash_Display_MENU_ATM__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Server_Display_the_account_Type__Saving_checking_: BinaryAssociation = BinaryAssociation(
    name="Bank_Server_Display_the_account_Type__Saving_checking_",
    ends={
        Property(name="display_the_account_Type__Saving_checking_20", type=Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="bank_Server21", type=Withdraw_Cash_Bank_Server_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Server_Display_amount: BinaryAssociation = BinaryAssociation(
    name="Bank_Server_Display_amount",
    ends={
        Property(name="display_amount22", type=Withdraw_Cash_Display_amount_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="bank_Server23", type=Withdraw_Cash_Bank_Server_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Verify_the_card___Display_the_PIN_screen: BinaryAssociation = BinaryAssociation(
    name="Verify_the_card___Display_the_PIN_screen",
    ends={
        Property(name="display_the_PIN_screen24", type=Withdraw_Cash_Display_the_PIN_screen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="Verify_the_card25", type=Withdraw_Cash__Verify_the_card___UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Display_the_PIN_screen__Enter_the_PIN: BinaryAssociation = BinaryAssociation(
    name="Display_the_PIN_screen__Enter_the_PIN",
    ends={
        Property(name="Enter_the_PIN26", type=Withdraw_Cash__Enter_the_PIN_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="display_the_PIN_screen27", type=Withdraw_Cash_Display_the_PIN_screen_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
ATM_transactions_ATM_transactions: BinaryAssociation = BinaryAssociation(
    name="ATM_transactions_ATM_transactions",
    ends={
        Property(name="aTM_transactions28", type=ATM_transactions, multiplicity=Multiplicity(0, 1)),
        Property(name="aTM_transactions29", type=ATM_transactions, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Withdraw_Cash: BinaryAssociation = BinaryAssociation(
    name="Customer_Withdraw_Cash",
    ends={
        Property(name="withdraw_Cash8", type=Withdraw_Cash_Withdraw_Cash_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=Withdraw_Cash_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Select_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Select_Account",
    ends={
        Property(name="select_Account10", type=Withdraw_Cash_Select_Account_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Withdraw_Cash_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Enter_Amount: BinaryAssociation = BinaryAssociation(
    name="Customer_Enter_Amount",
    ends={
        Property(name="enter_Amount12", type=Withdraw_Cash_Enter_Amount_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Withdraw_Cash_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_p3Ay4LMEEemcsc4aPpxbEQ",
    types={ATM_transactions, Withdraw_Cash_Interface_Interface, Withdraw_Cash_Customer_Actor, Withdraw_Cash_Bank_Server_Actor, Withdraw_Cash_Go_to_ATM_UseCase, Withdraw_Cash_Insert_the_Card____UseCase, Withdraw_Cash__Enter_the_PIN_UseCase, Withdraw_Cash__Display_MENU_ATM___UseCase, Withdraw_Cash_Withdraw_Cash_UseCase, Withdraw_Cash_Select_Account_UseCase, Withdraw_Cash_Enter_Amount_UseCase, Withdraw_Cash_Collect_Cash_UseCase, Withdraw_Cash__15____Take_print_out_UseCase, Withdraw_Cash__Block_the_card_UseCase, Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase, Withdraw_Cash_Display_the_PIN_screen_UseCase, Withdraw_Cash__Verify_the_card___UseCase, Withdraw_Cash_Verify_the_PIN_UseCase, Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase, Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase, Withdraw_Cash_Display_MENU_ATM__UseCase, Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase, Withdraw_Cash_Display_amount_UseCase, Withdraw_Cash__Verify_check_the_available_balance_UseCase, Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase, Withdraw_Cash_Display_error_else_UseCase, Withdraw_Cash_Dispense_the_cash_UseCase},
    associations={Customer_Go_to_ATM, Customer_Insert_the_Card, Enter_the_PIN_Customer, Customer__Display_MENU_ATM_, Customer_Collect_Cash, Bank_Server_Display_the_PIN_screen, Display_MENU_ATM__Bank_Server, Bank_Server_Display_the_account_Type__Saving_checking_, Bank_Server_Display_amount, Verify_the_card___Display_the_PIN_screen, Display_the_PIN_screen__Enter_the_PIN, ATM_transactions_ATM_transactions, Customer_Withdraw_Cash, Customer_Select_Account, Customer_Enter_Amount},
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