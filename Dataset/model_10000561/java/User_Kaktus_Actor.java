





import java.util.List;
import java.util.ArrayList;

public class User_Kaktus_Actor  {






    private Show_Ticket_History_UseCase show_ticket_history_usecase;




    private Reschedule_Ticket_UseCase reschedule_ticket_usecase;




    private Cancel_Ticket_UseCase cancel_ticket_usecase;


    public User_Kaktus_Actor(
    ) {
    }



    public Show_Ticket_History_UseCase getShow_ticket_history_usecase() {
        return show_ticket_history_usecase;
    }

    public void setShow_ticket_history_usecase(Show_Ticket_History_UseCase show_ticket_history_usecase) {
        this.show_ticket_history_usecase = show_ticket_history_usecase;
    }
    public Reschedule_Ticket_UseCase getReschedule_ticket_usecase() {
        return reschedule_ticket_usecase;
    }

    public void setReschedule_ticket_usecase(Reschedule_Ticket_UseCase reschedule_ticket_usecase) {
        this.reschedule_ticket_usecase = reschedule_ticket_usecase;
    }
    public Cancel_Ticket_UseCase getCancel_ticket_usecase() {
        return cancel_ticket_usecase;
    }

    public void setCancel_ticket_usecase(Cancel_Ticket_UseCase cancel_ticket_usecase) {
        this.cancel_ticket_usecase = cancel_ticket_usecase;
    }

}