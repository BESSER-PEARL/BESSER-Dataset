





import java.util.List;
import java.util.ArrayList;

public class Update_Order_UseCase  {






    private Manager_Actor manager_actor;




    private Customer_Actor customer_actor;


    public Update_Order_UseCase(
    ) {
    }



    public Manager_Actor getManager_actor() {
        return manager_actor;
    }

    public void setManager_actor(Manager_Actor manager_actor) {
        this.manager_actor = manager_actor;
    }
    public Customer_Actor getCustomer_actor() {
        return customer_actor;
    }

    public void setCustomer_actor(Customer_Actor customer_actor) {
        this.customer_actor = customer_actor;
    }

}