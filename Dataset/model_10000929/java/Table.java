





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private boolean occupied;
    private String specialRequest;
    private String order;
    private String table_Id;
    private int numSeats;





    private Booking booking;


    public Table(
        boolean occupied,        String specialRequest,        String order,        String table_Id,        int numSeats    ) {
        this.occupied = occupied;
        this.specialRequest = specialRequest;
        this.order = order;
        this.table_Id = table_Id;
        this.numSeats = numSeats;
    }


    public boolean getOccupied() {
        return occupied;
    }

    public void setOccupied(boolean occupied) {
        this.occupied = occupied;
    }
    public String getSpecialrequest() {
        return specialRequest;
    }

    public void setSpecialrequest(String specialRequest) {
        this.specialRequest = specialRequest;
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