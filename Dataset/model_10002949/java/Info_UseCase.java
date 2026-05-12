





import java.util.List;
import java.util.ArrayList;

public class Info_UseCase  {






    private Client_Actor client_actor;




    private Cleaning_Management_UseCase cleaning_management_usecase;




    private Payment_UseCase payment_usecase;


    public Info_UseCase(
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
    public Payment_UseCase getPayment_usecase() {
        return payment_usecase;
    }

    public void setPayment_usecase(Payment_UseCase payment_usecase) {
        this.payment_usecase = payment_usecase;
    }

}