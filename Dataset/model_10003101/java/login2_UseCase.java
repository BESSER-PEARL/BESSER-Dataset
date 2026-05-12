





import java.util.List;
import java.util.ArrayList;

public class login2_UseCase  {






    private admin2_Actor admin2_actor;




    private user2_Actor user2_actor;


    public login2_UseCase(
    ) {
    }



    public admin2_Actor getAdmin2_actor() {
        return admin2_actor;
    }

    public void setAdmin2_actor(admin2_Actor admin2_actor) {
        this.admin2_actor = admin2_actor;
    }
    public user2_Actor getUser2_actor() {
        return user2_actor;
    }

    public void setUser2_actor(user2_Actor user2_actor) {
        this.user2_actor = user2_actor;
    }

}