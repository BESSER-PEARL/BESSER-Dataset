





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_BookingHandler  {






    private List<bookingmodel_BookingRefToBookingEntry> bookingmodel_bookingreftobookingentrys;


    public bookingmodel_BookingHandler(
    ) {
        this.bookingmodel_bookingreftobookingentrys = new ArrayList<>();
    }

    public bookingmodel_BookingHandler(
        ArrayList<bookingmodel_BookingRefToBookingEntry> bookingmodel_bookingreftobookingentrys    ) {
        this.bookingmodel_bookingreftobookingentrys = bookingmodel_bookingreftobookingentrys;
    }


    public List<bookingmodel_BookingRefToBookingEntry> getBookingmodel_bookingreftobookingentrys() {
        return bookingmodel_bookingreftobookingentrys;
    }

    public void addBookingmodel_bookingreftobookingentry(Bookingmodel_bookingreftobookingentry bookingmodel_bookingreftobookingentry) {
        this.bookingmodel_bookingreftobookingentrys.add(bookingmodel_bookingreftobookingentry);
    }

}