





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private boolean occupied;
    private int numSeats;
    private String table_Id;
    private String order;
    private String specialRequest;





    private Booking booking;


    public Table(
        boolean occupied,        int numSeats,        String table_Id,        String order,        String specialRequest    ) {
        this.occupied = occupied;
        this.numSeats = numSeats;
        this.table_Id = table_Id;
        this.order = order;
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
    public String getTable_id() {
        return table_Id;
    }

    public void setTable_id(String table_Id) {
        this.table_Id = table_Id;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getSpecialrequest() {
        return specialRequest;
    }

    public void setSpecialrequest(String specialRequest) {
        this.specialRequest = specialRequest;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}