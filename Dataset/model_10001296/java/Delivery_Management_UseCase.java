





import java.util.List;
import java.util.ArrayList;

public class Delivery_Management_UseCase  {






    private Cleaning_Management_UseCase cleaning_management_usecase;




    private Deliver_Actor deliver_actor;




    private Client_Actor client_actor;


    public Delivery_Management_UseCase(
    ) {
    }



    public Cleaning_Management_UseCase getCleaning_management_usecase() {
        return cleaning_management_usecase;
    }

    public void setCleaning_management_usecase(Cleaning_Management_UseCase cleaning_management_usecase) {
        this.cleaning_management_usecase = cleaning_management_usecase;
    }
    public Deliver_Actor getDeliver_actor() {
        return deliver_actor;
    }

    public void setDeliver_actor(Deliver_Actor deliver_actor) {
        this.deliver_actor = deliver_actor;
    }
    public Client_Actor getClient_actor() {
        return client_actor;
    }

    public void setClient_actor(Client_Actor client_actor) {
        this.client_actor = client_actor;
    }

}