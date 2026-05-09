





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_Customer extends Person {






    private bookingmodel_Booking bookingmodel_booking;


    public bookingmodel_Customer(
    ) {
        super(
        );
    }



    public bookingmodel_Booking getBookingmodel_booking() {
        return bookingmodel_booking;
    }

    public void setBookingmodel_booking(bookingmodel_Booking bookingmodel_booking) {
        this.bookingmodel_booking = bookingmodel_booking;
    }

}