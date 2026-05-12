





import java.util.List;
import java.util.ArrayList;

public class Sign_In_UseCase  {






    private Registered_User_Actor registered_user_actor;


    public Sign_In_UseCase(
    ) {
    }



    public Registered_User_Actor getRegistered_user_actor() {
        return registered_user_actor;
    }

    public void setRegistered_user_actor(Registered_User_Actor registered_user_actor) {
        this.registered_user_actor = registered_user_actor;
    }

}