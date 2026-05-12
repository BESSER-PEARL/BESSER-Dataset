





import java.util.List;
import java.util.ArrayList;

public class Info_UseCase  {






    private Payment_UseCase payment_usecase;




    private Client_Actor client_actor;


    public Info_UseCase(
    ) {
    }



    public Payment_UseCase getPayment_usecase() {
        return payment_usecase;
    }

    public void setPayment_usecase(Payment_UseCase payment_usecase) {
        this.payment_usecase = payment_usecase;
    }
    public Client_Actor getClient_actor() {
        return client_actor;
    }

    public void setClient_actor(Client_Actor client_actor) {
        this.client_actor = client_actor;
    }

}