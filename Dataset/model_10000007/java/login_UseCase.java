





import java.util.List;
import java.util.ArrayList;

public class login_UseCase  {






    private client_Actor client_actor;




    private administrator_Actor administrator_actor;


    public login_UseCase(
    ) {
    }



    public client_Actor getClient_actor() {
        return client_actor;
    }

    public void setClient_actor(client_Actor client_actor) {
        this.client_actor = client_actor;
    }
    public administrator_Actor getAdministrator_actor() {
        return administrator_actor;
    }

    public void setAdministrator_actor(administrator_Actor administrator_actor) {
        this.administrator_actor = administrator_actor;
    }

}