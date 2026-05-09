





import java.util.List;
import java.util.ArrayList;

public class Implementation_OccupancyComponent_Occupancy  {

    private String checkOutDateTime;
    private String bookingReference;
    private String roomNumber;
    private String checkInDateTime;



    public Implementation_OccupancyComponent_Occupancy(
        String checkOutDateTime,        String bookingReference,        String roomNumber,        String checkInDateTime    ) {
        this.checkOutDateTime = checkOutDateTime;
        this.bookingReference = bookingReference;
        this.roomNumber = roomNumber;
        this.checkInDateTime = checkInDateTime;
    }


    public String getCheckoutdatetime() {
        return checkOutDateTime;
    }

    public void setCheckoutdatetime(String checkOutDateTime) {
        this.checkOutDateTime = checkOutDateTime;
    }
    public String getBookingreference() {
        return bookingReference;
    }

    public void setBookingreference(String bookingReference) {
        this.bookingReference = bookingReference;
    }
    public String getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(String roomNumber) {
        this.roomNumber = roomNumber;
    }
    public String getCheckindatetime() {
        return checkInDateTime;
    }

    public void setCheckindatetime(String checkInDateTime) {
        this.checkInDateTime = checkInDateTime;
    }


}