





import java.util.List;
import java.util.ArrayList;

public class Details_in_Database_UseCase  {






    private Booking_UseCase booking_usecase;


    public Details_in_Database_UseCase(
    ) {
    }



    public Booking_UseCase getBooking_usecase() {
        return booking_usecase;
    }

    public void setBooking_usecase(Booking_UseCase booking_usecase) {
        this.booking_usecase = booking_usecase;
    }

}