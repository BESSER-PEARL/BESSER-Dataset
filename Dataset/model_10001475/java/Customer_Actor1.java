





import java.util.List;
import java.util.ArrayList;

public class Customer_Actor1  {






    private Checkout_UseCase1 checkout_usecase1;




    private Customer_authentication_UseCase customer_authentication_usecase;


    public Customer_Actor1(
    ) {
    }



    public Checkout_UseCase1 getCheckout_usecase1() {
        return checkout_usecase1;
    }

    public void setCheckout_usecase1(Checkout_UseCase1 checkout_usecase1) {
        this.checkout_usecase1 = checkout_usecase1;
    }
    public Customer_authentication_UseCase getCustomer_authentication_usecase() {
        return customer_authentication_usecase;
    }

    public void setCustomer_authentication_usecase(Customer_authentication_UseCase customer_authentication_usecase) {
        this.customer_authentication_usecase = customer_authentication_usecase;
    }

}