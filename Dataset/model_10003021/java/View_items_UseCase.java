





import java.util.List;
import java.util.ArrayList;

public class View_items_UseCase  {






    private Registered_customer_Actor registered_customer_actor;




    private New_customer_Actor new_customer_actor;


    public View_items_UseCase(
    ) {
    }



    public Registered_customer_Actor getRegistered_customer_actor() {
        return registered_customer_actor;
    }

    public void setRegistered_customer_actor(Registered_customer_Actor registered_customer_actor) {
        this.registered_customer_actor = registered_customer_actor;
    }
    public New_customer_Actor getNew_customer_actor() {
        return new_customer_actor;
    }

    public void setNew_customer_actor(New_customer_Actor new_customer_actor) {
        this.new_customer_actor = new_customer_actor;
    }

}