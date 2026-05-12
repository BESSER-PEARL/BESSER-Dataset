





import java.util.List;
import java.util.ArrayList;

public class login_UseCase  {






    private admin_Actor admin_actor;




    private user_Actor user_actor;




    private driver_Actor driver_actor;


    public login_UseCase(
    ) {
    }



    public admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }
    public user_Actor getUser_actor() {
        return user_actor;
    }

    public void setUser_actor(user_Actor user_actor) {
        this.user_actor = user_actor;
    }
    public driver_Actor getDriver_actor() {
        return driver_actor;
    }

    public void setDriver_actor(driver_Actor driver_actor) {
        this.driver_actor = driver_actor;
    }

}