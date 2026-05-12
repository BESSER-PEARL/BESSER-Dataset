





import java.util.List;
import java.util.ArrayList;

public class Credit_payment_service_Actor  {






    private Payment_UseCase payment_usecase;


    public Credit_payment_service_Actor(
    ) {
    }



    public Payment_UseCase getPayment_usecase() {
        return payment_usecase;
    }

    public void setPayment_usecase(Payment_UseCase payment_usecase) {
        this.payment_usecase = payment_usecase;
    }

}