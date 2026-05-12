





import java.util.List;
import java.util.ArrayList;

public class ADMINISTRATOR_Actor  {






    private SUPPORT_AND_FEEDBACK_UseCase support_and_feedback_usecase;




    private MAINTAINS_THE_PRODUCTS_SERVICES_UseCase maintains_the_products_services_usecase;




    private PAYS_THE_BILL_UseCase pays_the_bill_usecase;




    private SELECTS_THE_MODE_OF_PAYMENT_UseCase selects_the_mode_of_payment_usecase;




    private DELIVERS_THE_PRODUCT_UseCase delivers_the_product_usecase;


    public ADMINISTRATOR_Actor(
    ) {
    }



    public SUPPORT_AND_FEEDBACK_UseCase getSupport_and_feedback_usecase() {
        return support_and_feedback_usecase;
    }

    public void setSupport_and_feedback_usecase(SUPPORT_AND_FEEDBACK_UseCase support_and_feedback_usecase) {
        this.support_and_feedback_usecase = support_and_feedback_usecase;
    }
    public MAINTAINS_THE_PRODUCTS_SERVICES_UseCase getMaintains_the_products_services_usecase() {
        return maintains_the_products_services_usecase;
    }

    public void setMaintains_the_products_services_usecase(MAINTAINS_THE_PRODUCTS_SERVICES_UseCase maintains_the_products_services_usecase) {
        this.maintains_the_products_services_usecase = maintains_the_products_services_usecase;
    }
    public PAYS_THE_BILL_UseCase getPays_the_bill_usecase() {
        return pays_the_bill_usecase;
    }

    public void setPays_the_bill_usecase(PAYS_THE_BILL_UseCase pays_the_bill_usecase) {
        this.pays_the_bill_usecase = pays_the_bill_usecase;
    }
    public SELECTS_THE_MODE_OF_PAYMENT_UseCase getSelects_the_mode_of_payment_usecase() {
        return selects_the_mode_of_payment_usecase;
    }

    public void setSelects_the_mode_of_payment_usecase(SELECTS_THE_MODE_OF_PAYMENT_UseCase selects_the_mode_of_payment_usecase) {
        this.selects_the_mode_of_payment_usecase = selects_the_mode_of_payment_usecase;
    }
    public DELIVERS_THE_PRODUCT_UseCase getDelivers_the_product_usecase() {
        return delivers_the_product_usecase;
    }

    public void setDelivers_the_product_usecase(DELIVERS_THE_PRODUCT_UseCase delivers_the_product_usecase) {
        this.delivers_the_product_usecase = delivers_the_product_usecase;
    }

}