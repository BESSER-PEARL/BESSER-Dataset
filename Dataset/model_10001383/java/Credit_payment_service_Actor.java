





import java.util.List;
import java.util.ArrayList;

public class Credit_payment_service_Actor  {






    private payment_UseCase payment_usecase;


    public Credit_payment_service_Actor(
    ) {
    }



    public payment_UseCase getPayment_usecase() {
        return payment_usecase;
    }

    public void setPayment_usecase(payment_UseCase payment_usecase) {
        this.payment_usecase = payment_usecase;
    }

}