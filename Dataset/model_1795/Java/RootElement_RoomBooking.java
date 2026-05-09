




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class RootElement_RoomBooking  {

    private LocalDate startDate;
    private LocalDate endDate;
    private String bookingStatus;





    private RootElement_Booking rootelement_booking;


    public RootElement_RoomBooking(
        LocalDate startDate,        LocalDate endDate,        String bookingStatus    ) {
        this.startDate = startDate;
        this.endDate = endDate;
        this.bookingStatus = bookingStatus;
    }


    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public String getBookingstatus() {
        return bookingStatus;
    }

    public void setBookingstatus(String bookingStatus) {
        this.bookingStatus = bookingStatus;
    }

    public RootElement_Booking getRootelement_booking() {
        return rootelement_booking;
    }

    public void setRootelement_booking(RootElement_Booking rootelement_booking) {
        this.rootelement_booking = rootelement_booking;
    }

}