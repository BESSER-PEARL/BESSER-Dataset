





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_BookingProvides extends IBookingProvidesForCustomer, IBookingProvidesForHost, IBookingProvidesForGuest {






    private bookingmodel_BookingHandler bookingmodel_bookinghandler;


    public bookingmodel_BookingProvides(
    ) {
        super(
        );
    }



    public bookingmodel_BookingHandler getBookingmodel_bookinghandler() {
        return bookingmodel_bookinghandler;
    }

    public void setBookingmodel_bookinghandler(bookingmodel_BookingHandler bookingmodel_bookinghandler) {
        this.bookingmodel_bookinghandler = bookingmodel_bookinghandler;
    }

}