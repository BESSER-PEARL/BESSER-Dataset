





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String checkOutDate;
    private String bookingDate;
    private String checkInDate;
    private int _numberOfNights;





    private List<Guest> guests;


    public Booking(
        String checkOutDate,        String bookingDate,        String checkInDate,        int _numberOfNights    ) {
        this.checkOutDate = checkOutDate;
        this.bookingDate = bookingDate;
        this.checkInDate = checkInDate;
        this._numberOfNights = _numberOfNights;
        this.guests = new ArrayList<>();
    }

    public Booking(
        String checkOutDate,        String bookingDate,        String checkInDate,        int _numberOfNights        ArrayList<Guest> guests    ) {
        this.checkOutDate = checkOutDate;
        this.bookingDate = bookingDate;
        this.checkInDate = checkInDate;
        this._numberOfNights = _numberOfNights;
        this.guests = guests;
    }

    public String getCheckoutdate() {
        return checkOutDate;
    }

    public void setCheckoutdate(String checkOutDate) {
        this.checkOutDate = checkOutDate;
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
    public int get_numberofnights() {
        return _numberOfNights;
    }

    public void set_numberofnights(int _numberOfNights) {
        this._numberOfNights = _numberOfNights;
    }

    public List<Guest> getGuests() {
        return guests;
    }

    public void addGuest(Guest guest) {
        this.guests.add(guest);
    }

}