





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String checkOutDate;
    private int _numberOfNights;
    private String bookingDate;
    private String checkInDate;



    public Booking(
        String checkOutDate,        int _numberOfNights,        String bookingDate,        String checkInDate    ) {
        this.checkOutDate = checkOutDate;
        this._numberOfNights = _numberOfNights;
        this.bookingDate = bookingDate;
        this.checkInDate = checkInDate;
    }


    public String getCheckoutdate() {
        return checkOutDate;
    }

    public void setCheckoutdate(String checkOutDate) {
        this.checkOutDate = checkOutDate;
    }
    public int get_numberofnights() {
        return _numberOfNights;
    }

    public void set_numberofnights(int _numberOfNights) {
        this._numberOfNights = _numberOfNights;
    }
    public String getBookingdate() {
        return bookingDate;
    }

    public void setBookingdate(String bookingDate) {
        this.bookingDate = bookingDate;
    }
    public String getCheckindate() {
        return checkInDate;
    }

    public void setCheckindate(String checkInDate) {
        this.checkInDate = checkInDate;
    }


}