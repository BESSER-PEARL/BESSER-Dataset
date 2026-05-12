





import java.util.List;
import java.util.ArrayList;

public class BookedTables  {

    private int TableNo;
    private int BookingID;





    private Bookings bookings;




    private Table table;


    public BookedTables(
        int TableNo,        int BookingID    ) {
        this.TableNo = TableNo;
        this.BookingID = BookingID;
    }


    public int getTableno() {
        return TableNo;
    }

    public void setTableno(int TableNo) {
        this.TableNo = TableNo;
    }
    public int getBookingid() {
        return BookingID;
    }

    public void setBookingid(int BookingID) {
        this.BookingID = BookingID;
    }

    public Bookings getBookings() {
        return bookings;
    }

    public void setBookings(Bookings bookings) {
        this.bookings = bookings;
    }
    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}