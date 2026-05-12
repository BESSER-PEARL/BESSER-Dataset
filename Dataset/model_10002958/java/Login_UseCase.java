





import java.util.List;
import java.util.ArrayList;

public class Login_UseCase  {






    private User_Actor user_actor;




    private Admin_Actor admin_actor;


    public Login_UseCase(
    ) {
    }



    public User_Actor getUser_actor() {
        return user_actor;
    }

    public void setUser_actor(User_Actor user_actor) {
        this.user_actor = user_actor;
    }
    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }

}