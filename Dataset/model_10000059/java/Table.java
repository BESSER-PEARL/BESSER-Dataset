





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private boolean Occupied;
    private String TableNo;





    private BookingController bookingcontroller;


    public Table(
        boolean Occupied,        String TableNo    ) {
        this.Occupied = Occupied;
        this.TableNo = TableNo;
    }


    public boolean getOccupied() {
        return Occupied;
    }

    public void setOccupied(boolean Occupied) {
        this.Occupied = Occupied;
    }
    public String getTableno() {
        return TableNo;
    }

    public void setTableno(String TableNo) {
        this.TableNo = TableNo;
    }

    public BookingController getBookingcontroller() {
        return bookingcontroller;
    }

    public void setBookingcontroller(BookingController bookingcontroller) {
        this.bookingcontroller = bookingcontroller;
    }

}