





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String table_id;
    private boolean avaliable;
    private int numSeats;





    private Booking booking;




    private Order order;


    public Table(
        String table_id,        boolean avaliable,        int numSeats    ) {
        this.table_id = table_id;
        this.avaliable = avaliable;
        this.numSeats = numSeats;
    }


    public String getTable_id() {
        return table_id;
    }

    public void setTable_id(String table_id) {
        this.table_id = table_id;
    }
    public boolean getAvaliable() {
        return avaliable;
    }

    public void setAvaliable(boolean avaliable) {
        this.avaliable = avaliable;
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
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}