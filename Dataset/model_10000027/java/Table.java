





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String order;
    private String table_Id;
    private String specialRequest;
    private boolean occupied;
    private int numSeats;





    private Booking booking;


    public Table(
        String order,        String table_Id,        String specialRequest,        boolean occupied,        int numSeats    ) {
        this.order = order;
        this.table_Id = table_Id;
        this.specialRequest = specialRequest;
        this.occupied = occupied;
        this.numSeats = numSeats;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getTable_id() {
        return table_Id;
    }

    public void setTable_id(String table_Id) {
        this.table_Id = table_Id;
    }
    public String getSpecialrequest() {
        return specialRequest;
    }

    public void setSpecialrequest(String specialRequest) {
        this.specialRequest = specialRequest;
    }
    public boolean getOccupied() {
        return occupied;
    }

    public void setOccupied(boolean occupied) {
        this.occupied = occupied;
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