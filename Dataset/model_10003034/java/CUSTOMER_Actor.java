





import java.util.List;
import java.util.ArrayList;

public class CUSTOMER_Actor  {






    private ADDS_ITEMS_SERVICE_TO_CART_UseCase adds_items_service_to_cart_usecase;




    private PAYS_THE_BILL_UseCase pays_the_bill_usecase;




    private VISITS_THE_WEBSITE_UseCase visits_the_website_usecase;




    private SELECTS_THE_ITEMS_SERVICE_UseCase selects_the_items_service_usecase;




    private SELECTS_THE_MODE_OF_PAYMENT_UseCase selects_the_mode_of_payment_usecase;




    private SUPPORT_AND_FEEDBACK_UseCase support_and_feedback_usecase;


    public CUSTOMER_Actor(
    ) {
    }



    public ADDS_ITEMS_SERVICE_TO_CART_UseCase getAdds_items_service_to_cart_usecase() {
        return adds_items_service_to_cart_usecase;
    }

    public void setAdds_items_service_to_cart_usecase(ADDS_ITEMS_SERVICE_TO_CART_UseCase adds_items_service_to_cart_usecase) {
        this.adds_items_service_to_cart_usecase = adds_items_service_to_cart_usecase;
    }
    public PAYS_THE_BILL_UseCase getPays_the_bill_usecase() {
        return pays_the_bill_usecase;
    }

    public void setPays_the_bill_usecase(PAYS_THE_BILL_UseCase pays_the_bill_usecase) {
        this.pays_the_bill_usecase = pays_the_bill_usecase;
    }
    public VISITS_THE_WEBSITE_UseCase getVisits_the_website_usecase() {
        return visits_the_website_usecase;
    }

    public void setVisits_the_website_usecase(VISITS_THE_WEBSITE_UseCase visits_the_website_usecase) {
        this.visits_the_website_usecase = visits_the_website_usecase;
    }
    public SELECTS_THE_ITEMS_SERVICE_UseCase getSelects_the_items_service_usecase() {
        return selects_the_items_service_usecase;
    }

    public void setSelects_the_items_service_usecase(SELECTS_THE_ITEMS_SERVICE_UseCase selects_the_items_service_usecase) {
        this.selects_the_items_service_usecase = selects_the_items_service_usecase;
    }
    public SELECTS_THE_MODE_OF_PAYMENT_UseCase getSelects_the_mode_of_payment_usecase() {
        return selects_the_mode_of_payment_usecase;
    }

    public void setSelects_the_mode_of_payment_usecase(SELECTS_THE_MODE_OF_PAYMENT_UseCase selects_the_mode_of_payment_usecase) {
        this.selects_the_mode_of_payment_usecase = selects_the_mode_of_payment_usecase;
    }
    public SUPPORT_AND_FEEDBACK_UseCase getSupport_and_feedback_usecase() {
        return support_and_feedback_usecase;
    }

    public void setSupport_and_feedback_usecase(SUPPORT_AND_FEEDBACK_UseCase support_and_feedback_usecase) {
        this.support_and_feedback_usecase = support_and_feedback_usecase;
    }

}