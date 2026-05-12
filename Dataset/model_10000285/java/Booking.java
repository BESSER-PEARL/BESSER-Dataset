





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String checkInDate;
    private String bookingDate;
    private int _numberOfNights;
    private String checkOutDate;



    public Booking(
        String checkInDate,        String bookingDate,        int _numberOfNights,        String checkOutDate    ) {
        this.checkInDate = checkInDate;
        this.bookingDate = bookingDate;
        this._numberOfNights = _numberOfNights;
        this.checkOutDate = checkOutDate;
    }


    public String getCheckindate() {
        return checkInDate;
    }

    public void setCheckindate(String checkInDate) {
        this.checkInDate = checkInDate;
    }
    public String getBookingdate() {
        return bookingDate;
    }

    public void setBookingdate(String bookingDate) {
        this.bookingDate = bookingDate;
    }
    public int get_numberofnights() {
        return _numberOfNights;
    }

    public void set_numberofnights(int _numberOfNights) {
        this._numberOfNights = _numberOfNights;
    }
    public String getCheckoutdate() {
        return checkOutDate;
    }

    public void setCheckoutdate(String checkOutDate) {
        this.checkOutDate = checkOutDate;
    }


}