





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private int numSeats;
    private String specialRequest;
    private boolean occupied;
    private None customerDetail;
    private String order;
    private String table_Id;





    private Staff staff;




    private Booking booking;


    public Table(
        int numSeats,        String specialRequest,        boolean occupied,        None customerDetail,        String order,        String table_Id    ) {
        this.numSeats = numSeats;
        this.specialRequest = specialRequest;
        this.occupied = occupied;
        this.customerDetail = customerDetail;
        this.order = order;
        this.table_Id = table_Id;
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
    public boolean getOccupied() {
        return occupied;
    }

    public void setOccupied(boolean occupied) {
        this.occupied = occupied;
    }
    public None getCustomerdetail() {
        return customerDetail;
    }

    public void setCustomerdetail(None customerDetail) {
        this.customerDetail = customerDetail;
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

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }
    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}