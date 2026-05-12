





import java.util.List;
import java.util.ArrayList;

public class Renew_UseCase  {






    private User_Status_UseCase user_status_usecase;




    private Patron_Actor patron_actor;


    public Renew_UseCase(
    ) {
    }



    public User_Status_UseCase getUser_status_usecase() {
        return user_status_usecase;
    }

    public void setUser_status_usecase(User_Status_UseCase user_status_usecase) {
        this.user_status_usecase = user_status_usecase;
    }
    public Patron_Actor getPatron_actor() {
        return patron_actor;
    }

    public void setPatron_actor(Patron_Actor patron_actor) {
        this.patron_actor = patron_actor;
    }

}