




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Booking  {

    private String roomTypes;
    private String externalComments;
    private LocalDate endDate;
    private boolean checkedIn;
    private int bookingId;
    private LocalDate created;
    private String internalComments;
    private LocalDate startDate;
    private boolean checkedOut;



    public HotelManagementClassDiagram_Booking(
        String roomTypes,        String externalComments,        LocalDate endDate,        boolean checkedIn,        int bookingId,        LocalDate created,        String internalComments,        LocalDate startDate,        boolean checkedOut    ) {
        this.roomTypes = roomTypes;
        this.externalComments = externalComments;
        this.endDate = endDate;
        this.checkedIn = checkedIn;
        this.bookingId = bookingId;
        this.created = created;
        this.internalComments = internalComments;
        this.startDate = startDate;
        this.checkedOut = checkedOut;
    }


    public String getRoomtypes() {
        return roomTypes;
    }

    public void setRoomtypes(String roomTypes) {
        this.roomTypes = roomTypes;
    }
    public String getExternalcomments() {
        return externalComments;
    }

    public void setExternalcomments(String externalComments) {
        this.externalComments = externalComments;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public boolean getCheckedin() {
        return checkedIn;
    }

    public void setCheckedin(boolean checkedIn) {
        this.checkedIn = checkedIn;
    }
    public int getBookingid() {
        return bookingId;
    }

    public void setBookingid(int bookingId) {
        this.bookingId = bookingId;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getInternalcomments() {
        return internalComments;
    }

    public void setInternalcomments(String internalComments) {
        this.internalComments = internalComments;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public boolean getCheckedout() {
        return checkedOut;
    }

    public void setCheckedout(boolean checkedOut) {
        this.checkedOut = checkedOut;
    }


}