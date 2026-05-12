





import java.util.List;
import java.util.ArrayList;

public class Logout_UseCase  {






    private Logout_UseCase logout_usecase;




    private Customer_Actor customer_actor;


    public Logout_UseCase(
    ) {
    }



    public Logout_UseCase getLogout_usecase() {
        return logout_usecase;
    }

    public void setLogout_usecase(Logout_UseCase logout_usecase) {
        this.logout_usecase = logout_usecase;
    }
    public Customer_Actor getCustomer_actor() {
        return customer_actor;
    }

    public void setCustomer_actor(Customer_Actor customer_actor) {
        this.customer_actor = customer_actor;
    }

}