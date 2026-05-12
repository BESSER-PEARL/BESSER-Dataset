





import java.util.List;
import java.util.ArrayList;

public class Clerk_Actor  {






    private Cancel_ticket_UseCase cancel_ticket_usecase;


    public Clerk_Actor(
    ) {
    }



    public Cancel_ticket_UseCase getCancel_ticket_usecase() {
        return cancel_ticket_usecase;
    }

    public void setCancel_ticket_usecase(Cancel_ticket_UseCase cancel_ticket_usecase) {
        this.cancel_ticket_usecase = cancel_ticket_usecase;
    }

}