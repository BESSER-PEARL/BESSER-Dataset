





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String table_id;
    private int numSeats;
    private boolean avaliable;





    private Booking booking;


    public Table(
        String table_id,        int numSeats,        boolean avaliable    ) {
        this.table_id = table_id;
        this.numSeats = numSeats;
        this.avaliable = avaliable;
    }


    public String getTable_id() {
        return table_id;
    }

    public void setTable_id(String table_id) {
        this.table_id = table_id;
    }
    public int getNumseats() {
        return numSeats;
    }

    public void setNumseats(int numSeats) {
        this.numSeats = numSeats;
    }
    public boolean getAvaliable() {
        return avaliable;
    }

    public void setAvaliable(boolean avaliable) {
        this.avaliable = avaliable;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}