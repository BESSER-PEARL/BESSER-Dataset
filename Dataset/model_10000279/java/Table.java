





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String order;
    private boolean occupied;
    private int numSeats;
    private String specialRequest;
    private String table_Id;





    private Booking booking;


    public Table(
        String order,        boolean occupied,        int numSeats,        String specialRequest,        String table_Id    ) {
        this.order = order;
        this.occupied = occupied;
        this.numSeats = numSeats;
        this.specialRequest = specialRequest;
        this.table_Id = table_Id;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
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
    public String getSpecialrequest() {
        return specialRequest;
    }

    public void setSpecialrequest(String specialRequest) {
        this.specialRequest = specialRequest;
    }
    public String getTable_id() {
        return table_Id;
    }

    public void setTable_id(String table_Id) {
        this.table_Id = table_Id;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}