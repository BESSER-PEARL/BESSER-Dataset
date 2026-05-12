





import java.util.List;
import java.util.ArrayList;

public class Cancel_Booking_UseCase  {






    private Receptionist_Actor receptionist_actor;




    private Guest_Actor guest_actor;


    public Cancel_Booking_UseCase(
    ) {
    }



    public Receptionist_Actor getReceptionist_actor() {
        return receptionist_actor;
    }

    public void setReceptionist_actor(Receptionist_Actor receptionist_actor) {
        this.receptionist_actor = receptionist_actor;
    }
    public Guest_Actor getGuest_actor() {
        return guest_actor;
    }

    public void setGuest_actor(Guest_Actor guest_actor) {
        this.guest_actor = guest_actor;
    }

}