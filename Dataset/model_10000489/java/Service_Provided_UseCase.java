





import java.util.List;
import java.util.ArrayList;

public class Service_Provided_UseCase  {






    private Client_Actor client_actor;




    private Cleaning_Management_UseCase cleaning_management_usecase;




    private Service_Provided_By_Actor service_provided_by_actor;


    public Service_Provided_UseCase(
    ) {
    }



    public Client_Actor getClient_actor() {
        return client_actor;
    }

    public void setClient_actor(Client_Actor client_actor) {
        this.client_actor = client_actor;
    }
    public Cleaning_Management_UseCase getCleaning_management_usecase() {
        return cleaning_management_usecase;
    }

    public void setCleaning_management_usecase(Cleaning_Management_UseCase cleaning_management_usecase) {
        this.cleaning_management_usecase = cleaning_management_usecase;
    }
    public Service_Provided_By_Actor getService_provided_by_actor() {
        return service_provided_by_actor;
    }

    public void setService_provided_by_actor(Service_Provided_By_Actor service_provided_by_actor) {
        this.service_provided_by_actor = service_provided_by_actor;
    }

}