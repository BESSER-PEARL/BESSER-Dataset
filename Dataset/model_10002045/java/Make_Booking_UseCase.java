





import java.util.List;
import java.util.ArrayList;

public class Make_Booking_UseCase  {






    private Guest_Actor guest_actor;




    private Receptionist_Actor receptionist_actor;


    public Make_Booking_UseCase(
    ) {
    }



    public Guest_Actor getGuest_actor() {
        return guest_actor;
    }

    public void setGuest_actor(Guest_Actor guest_actor) {
        this.guest_actor = guest_actor;
    }
    public Receptionist_Actor getReceptionist_actor() {
        return receptionist_actor;
    }

    public void setReceptionist_actor(Receptionist_Actor receptionist_actor) {
        this.receptionist_actor = receptionist_actor;
    }

}