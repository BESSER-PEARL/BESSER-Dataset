





import java.util.List;
import java.util.ArrayList;

public class Payment_Authentecation_System_Actor  {






    private Credit_Card_UseCase1 credit_card_usecase1;




    private PayPal_UseCase1 paypal_usecase1;


    public Payment_Authentecation_System_Actor(
    ) {
    }



    public Credit_Card_UseCase1 getCredit_card_usecase1() {
        return credit_card_usecase1;
    }

    public void setCredit_card_usecase1(Credit_Card_UseCase1 credit_card_usecase1) {
        this.credit_card_usecase1 = credit_card_usecase1;
    }
    public PayPal_UseCase1 getPaypal_usecase1() {
        return paypal_usecase1;
    }

    public void setPaypal_usecase1(PayPal_UseCase1 paypal_usecase1) {
        this.paypal_usecase1 = paypal_usecase1;
    }

}