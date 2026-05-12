





import java.util.List;
import java.util.ArrayList;

public class Digitalk_Actor  {






    private Purchase_Credit_UseCase purchase_credit_usecase;




    private Top_UP_via_card_voucher_UseCase top_up_via_card_voucher_usecase;




    private Register_UseCase register_usecase;




    private View_Dashboard_UseCase view_dashboard_usecase;


    public Digitalk_Actor(
    ) {
    }



    public Purchase_Credit_UseCase getPurchase_credit_usecase() {
        return purchase_credit_usecase;
    }

    public void setPurchase_credit_usecase(Purchase_Credit_UseCase purchase_credit_usecase) {
        this.purchase_credit_usecase = purchase_credit_usecase;
    }
    public Top_UP_via_card_voucher_UseCase getTop_up_via_card_voucher_usecase() {
        return top_up_via_card_voucher_usecase;
    }

    public void setTop_up_via_card_voucher_usecase(Top_UP_via_card_voucher_UseCase top_up_via_card_voucher_usecase) {
        this.top_up_via_card_voucher_usecase = top_up_via_card_voucher_usecase;
    }
    public Register_UseCase getRegister_usecase() {
        return register_usecase;
    }

    public void setRegister_usecase(Register_UseCase register_usecase) {
        this.register_usecase = register_usecase;
    }
    public View_Dashboard_UseCase getView_dashboard_usecase() {
        return view_dashboard_usecase;
    }

    public void setView_dashboard_usecase(View_Dashboard_UseCase view_dashboard_usecase) {
        this.view_dashboard_usecase = view_dashboard_usecase;
    }

}