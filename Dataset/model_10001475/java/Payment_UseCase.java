





import java.util.List;
import java.util.ArrayList;

public class Payment_UseCase  {






    private Checkout_UseCase checkout_usecase;


    public Payment_UseCase(
    ) {
    }



    public Checkout_UseCase getCheckout_usecase() {
        return checkout_usecase;
    }

    public void setCheckout_usecase(Checkout_UseCase checkout_usecase) {
        this.checkout_usecase = checkout_usecase;
    }

}