





import java.util.List;
import java.util.ArrayList;

public class Show_Ticket_History_UseCase  {






    private User_Actor user_actor;




    private Login_UseCase login_usecase;


    public Show_Ticket_History_UseCase(
    ) {
    }



    public User_Actor getUser_actor() {
        return user_actor;
    }

    public void setUser_actor(User_Actor user_actor) {
        this.user_actor = user_actor;
    }
    public Login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(Login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }

}