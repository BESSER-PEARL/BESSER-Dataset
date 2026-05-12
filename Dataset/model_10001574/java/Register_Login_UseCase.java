





import java.util.List;
import java.util.ArrayList;

public class Register_Login_UseCase  {






    private non_Registered_Actor non_registered_actor;




    private Registered_User_Actor registered_user_actor;


    public Register_Login_UseCase(
    ) {
    }



    public non_Registered_Actor getNon_registered_actor() {
        return non_registered_actor;
    }

    public void setNon_registered_actor(non_Registered_Actor non_registered_actor) {
        this.non_registered_actor = non_registered_actor;
    }
    public Registered_User_Actor getRegistered_user_actor() {
        return registered_user_actor;
    }

    public void setRegistered_user_actor(Registered_User_Actor registered_user_actor) {
        this.registered_user_actor = registered_user_actor;
    }

}