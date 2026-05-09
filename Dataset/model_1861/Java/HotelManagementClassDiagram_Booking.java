




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Booking  {

    private boolean checkedIn;
    private LocalDate endDate;
    private int bookingId;
    private String externalComments;
    private String internalComments;
    private boolean checkedOut;
    private LocalDate startDate;
    private LocalDate created;





    private HotelManagementClassDiagram_Customer hotelmanagementclassdiagram_customer;




    private HotelManagementClassDiagram_Customer hotelmanagementclassdiagram_customer;


    public HotelManagementClassDiagram_Booking(
        boolean checkedIn,        LocalDate endDate,        int bookingId,        String externalComments,        String internalComments,        boolean checkedOut,        LocalDate startDate,        LocalDate created    ) {
        this.checkedIn = checkedIn;
        this.endDate = endDate;
        this.bookingId = bookingId;
        this.externalComments = externalComments;
        this.internalComments = internalComments;
        this.checkedOut = checkedOut;
        this.startDate = startDate;
        this.created = created;
    }


    public boolean getCheckedin() {
        return checkedIn;
    }

    public void setCheckedin(boolean checkedIn) {
        this.checkedIn = checkedIn;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public int getBookingid() {
        return bookingId;
    }

    public void setBookingid(int bookingId) {
        this.bookingId = bookingId;
    }
    public String getExternalcomments() {
        return externalComments;
    }

    public void setExternalcomments(String externalComments) {
        this.externalComments = externalComments;
    }
    public String getInternalcomments() {
        return internalComments;
    }

    public void setInternalcomments(String internalComments) {
        this.internalComments = internalComments;
    }
    public boolean getCheckedout() {
        return checkedOut;
    }

    public void setCheckedout(boolean checkedOut) {
        this.checkedOut = checkedOut;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }

    public HotelManagementClassDiagram_Customer getHotelmanagementclassdiagram_customer() {
        return hotelmanagementclassdiagram_customer;
    }

    public void setHotelmanagementclassdiagram_customer(HotelManagementClassDiagram_Customer hotelmanagementclassdiagram_customer) {
        this.hotelmanagementclassdiagram_customer = hotelmanagementclassdiagram_customer;
    }
    public HotelManagementClassDiagram_Customer getHotelmanagementclassdiagram_customer() {
        return hotelmanagementclassdiagram_customer;
    }

    public void setHotelmanagementclassdiagram_customer(HotelManagementClassDiagram_Customer hotelmanagementclassdiagram_customer) {
        this.hotelmanagementclassdiagram_customer = hotelmanagementclassdiagram_customer;
    }

}