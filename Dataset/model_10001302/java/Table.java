





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String table_id;
    private int quantity;
    private int numSeats;





    private Booking booking;


    public Table(
        String table_id,        int quantity,        int numSeats    ) {
        this.table_id = table_id;
        this.quantity = quantity;
        this.numSeats = numSeats;
    }


    public String getTable_id() {
        return table_id;
    }

    public void setTable_id(String table_id) {
        this.table_id = table_id;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getNumseats() {
        return numSeats;
    }

    public void setNumseats(int numSeats) {
        this.numSeats = numSeats;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}