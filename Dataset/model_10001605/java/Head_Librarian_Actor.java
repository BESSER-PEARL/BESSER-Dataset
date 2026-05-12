





import java.util.List;
import java.util.ArrayList;

public class Head_Librarian_Actor  {






    private Carry_Out_Stock_Check_UseCase carry_out_stock_check_usecase;




    private Suspend_Membership_UseCase suspend_membership_usecase;




    private Purchase_Books_UseCase purchase_books_usecase;




    private Cancel_Membership_UseCase cancel_membership_usecase;




    private Amend_Membership_details_UseCase amend_membership_details_usecase;




    private Withdraw_Books_UseCase withdraw_books_usecase;


    public Head_Librarian_Actor(
    ) {
    }



    public Carry_Out_Stock_Check_UseCase getCarry_out_stock_check_usecase() {
        return carry_out_stock_check_usecase;
    }

    public void setCarry_out_stock_check_usecase(Carry_Out_Stock_Check_UseCase carry_out_stock_check_usecase) {
        this.carry_out_stock_check_usecase = carry_out_stock_check_usecase;
    }
    public Suspend_Membership_UseCase getSuspend_membership_usecase() {
        return suspend_membership_usecase;
    }

    public void setSuspend_membership_usecase(Suspend_Membership_UseCase suspend_membership_usecase) {
        this.suspend_membership_usecase = suspend_membership_usecase;
    }
    public Purchase_Books_UseCase getPurchase_books_usecase() {
        return purchase_books_usecase;
    }

    public void setPurchase_books_usecase(Purchase_Books_UseCase purchase_books_usecase) {
        this.purchase_books_usecase = purchase_books_usecase;
    }
    public Cancel_Membership_UseCase getCancel_membership_usecase() {
        return cancel_membership_usecase;
    }

    public void setCancel_membership_usecase(Cancel_Membership_UseCase cancel_membership_usecase) {
        this.cancel_membership_usecase = cancel_membership_usecase;
    }
    public Amend_Membership_details_UseCase getAmend_membership_details_usecase() {
        return amend_membership_details_usecase;
    }

    public void setAmend_membership_details_usecase(Amend_Membership_details_UseCase amend_membership_details_usecase) {
        this.amend_membership_details_usecase = amend_membership_details_usecase;
    }
    public Withdraw_Books_UseCase getWithdraw_books_usecase() {
        return withdraw_books_usecase;
    }

    public void setWithdraw_books_usecase(Withdraw_Books_UseCase withdraw_books_usecase) {
        this.withdraw_books_usecase = withdraw_books_usecase;
    }

}