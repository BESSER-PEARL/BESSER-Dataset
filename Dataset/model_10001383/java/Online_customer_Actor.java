





import java.util.List;
import java.util.ArrayList;

public class Online_customer_Actor  {






    private Checkout_UseCase1 checkout_usecase1;




    private Customer_authentication__UseCase customer_authentication__usecase;


    public Online_customer_Actor(
    ) {
    }



    public Checkout_UseCase1 getCheckout_usecase1() {
        return checkout_usecase1;
    }

    public void setCheckout_usecase1(Checkout_UseCase1 checkout_usecase1) {
        this.checkout_usecase1 = checkout_usecase1;
    }
    public Customer_authentication__UseCase getCustomer_authentication__usecase() {
        return customer_authentication__usecase;
    }

    public void setCustomer_authentication__usecase(Customer_authentication__UseCase customer_authentication__usecase) {
        this.customer_authentication__usecase = customer_authentication__usecase;
    }

}