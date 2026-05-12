





import java.util.List;
import java.util.ArrayList;

public class Login_UseCase  {






    private Show_Ticket_History_UseCase show_ticket_history_usecase;




    private User_Kaktus_Actor user_kaktus_actor;


    public Login_UseCase(
    ) {
    }



    public Show_Ticket_History_UseCase getShow_ticket_history_usecase() {
        return show_ticket_history_usecase;
    }

    public void setShow_ticket_history_usecase(Show_Ticket_History_UseCase show_ticket_history_usecase) {
        this.show_ticket_history_usecase = show_ticket_history_usecase;
    }
    public User_Kaktus_Actor getUser_kaktus_actor() {
        return user_kaktus_actor;
    }

    public void setUser_kaktus_actor(User_Kaktus_Actor user_kaktus_actor) {
        this.user_kaktus_actor = user_kaktus_actor;
    }

}