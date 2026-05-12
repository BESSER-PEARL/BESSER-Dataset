





import java.util.List;
import java.util.ArrayList;

public class Purchase_UseCase  {






    private Registered_customer_Actor registered_customer_actor;


    public Purchase_UseCase(
    ) {
    }



    public Registered_customer_Actor getRegistered_customer_actor() {
        return registered_customer_actor;
    }

    public void setRegistered_customer_actor(Registered_customer_Actor registered_customer_actor) {
        this.registered_customer_actor = registered_customer_actor;
    }

}