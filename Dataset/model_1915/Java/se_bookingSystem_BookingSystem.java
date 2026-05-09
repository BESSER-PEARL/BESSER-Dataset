





import java.util.List;
import java.util.ArrayList;

public class se_bookingSystem_BookingSystem extends bookingSystem_IHotelCustomerProvides, bookingSystem_IHotelBookingManager {

    private int bookingId;



    public se_bookingSystem_BookingSystem(
        int bookingId    ) {
        super(
        );
        this.bookingId = bookingId;
    }


    public int getBookingid() {
        return bookingId;
    }

    public void setBookingid(int bookingId) {
        this.bookingId = bookingId;
    }


}