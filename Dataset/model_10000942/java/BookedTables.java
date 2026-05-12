





import java.util.List;
import java.util.ArrayList;

public class BookedTables  {

    private int BookingID;
    private int TableNo;





    private Table table;




    private Bookings bookings;


    public BookedTables(
        int BookingID,        int TableNo    ) {
        this.BookingID = BookingID;
        this.TableNo = TableNo;
    }


    public int getBookingid() {
        return BookingID;
    }

    public void setBookingid(int BookingID) {
        this.BookingID = BookingID;
    }
    public int getTableno() {
        return TableNo;
    }

    public void setTableno(int TableNo) {
        this.TableNo = TableNo;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }
    public Bookings getBookings() {
        return bookings;
    }

    public void setBookings(Bookings bookings) {
        this.bookings = bookings;
    }

}