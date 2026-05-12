





import java.util.List;
import java.util.ArrayList;

public class donner_des_informayions_UseCase  {






    private Client_Actor client_actor;




    private Payer_UseCase payer_usecase;


    public donner_des_informayions_UseCase(
    ) {
    }



    public Client_Actor getClient_actor() {
        return client_actor;
    }

    public void setClient_actor(Client_Actor client_actor) {
        this.client_actor = client_actor;
    }
    public Payer_UseCase getPayer_usecase() {
        return payer_usecase;
    }

    public void setPayer_usecase(Payer_UseCase payer_usecase) {
        this.payer_usecase = payer_usecase;
    }

}