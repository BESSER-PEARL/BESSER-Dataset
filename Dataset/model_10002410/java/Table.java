





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String table_Id;
    private boolean occupied;
    private String specialRequest;
    private int numSeats;
    private String order;





    private Order order;




    private Booking booking;


    public Table(
        String table_Id,        boolean occupied,        String specialRequest,        int numSeats,        String order    ) {
        this.table_Id = table_Id;
        this.occupied = occupied;
        this.specialRequest = specialRequest;
        this.numSeats = numSeats;
        this.order = order;
    }


    public String getTable_id() {
        return table_Id;
    }

    public void setTable_id(String table_Id) {
        this.table_Id = table_Id;
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
    public int getNumseats() {
        return numSeats;
    }

    public void setNumseats(int numSeats) {
        this.numSeats = numSeats;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}