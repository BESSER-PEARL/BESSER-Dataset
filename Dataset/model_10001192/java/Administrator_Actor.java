





import java.util.List;
import java.util.ArrayList;

public class Administrator_Actor  {






    private Reschedule_Ticket_UseCase reschedule_ticket_usecase;




    private Cancel_Ticket_UseCase cancel_ticket_usecase;


    public Administrator_Actor(
    ) {
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