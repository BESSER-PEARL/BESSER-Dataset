





import java.util.List;
import java.util.ArrayList;

public class Password_UseCase  {






    private customer_Actor customer_actor;




    private Admin_Actor admin_actor;


    public Password_UseCase(
    ) {
    }



    public customer_Actor getCustomer_actor() {
        return customer_actor;
    }

    public void setCustomer_actor(customer_Actor customer_actor) {
        this.customer_actor = customer_actor;
    }
    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }

}