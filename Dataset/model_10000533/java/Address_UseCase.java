





import java.util.List;
import java.util.ArrayList;

public class Address_UseCase  {






    private Deliver_Actor deliver_actor;




    private Booking_UseCase booking_usecase;


    public Address_UseCase(
    ) {
    }



    public Deliver_Actor getDeliver_actor() {
        return deliver_actor;
    }

    public void setDeliver_actor(Deliver_Actor deliver_actor) {
        this.deliver_actor = deliver_actor;
    }
    public Booking_UseCase getBooking_usecase() {
        return booking_usecase;
    }

    public void setBooking_usecase(Booking_UseCase booking_usecase) {
        this.booking_usecase = booking_usecase;
    }

}