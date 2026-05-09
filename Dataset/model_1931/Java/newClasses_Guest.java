





import java.util.List;
import java.util.ArrayList;

public class newClasses_Guest extends GuestInterface, Customer, GuestBiller {

    private String checkOutDate;
    private String addedServices;
    private String checkedIn;
    private String checkedOut;
    private String extraDays;
    private String cost;
    private String bookingPaid;
    private String roomNum;
    private String checkInDate;



    public newClasses_Guest(
        String checkOutDate,        String addedServices,        String checkedIn,        String checkedOut,        String extraDays,        String cost,        String bookingPaid,        String roomNum,        String checkInDate    ) {
        super(
        );
        this.checkOutDate = checkOutDate;
        this.addedServices = addedServices;
        this.checkedIn = checkedIn;
        this.checkedOut = checkedOut;
        this.extraDays = extraDays;
        this.cost = cost;
        this.bookingPaid = bookingPaid;
        this.roomNum = roomNum;
        this.checkInDate = checkInDate;
    }


    public String getCheckoutdate() {
        return checkOutDate;
    }

    public void setCheckoutdate(String checkOutDate) {
        this.checkOutDate = checkOutDate;
    }
    public String getAddedservices() {
        return addedServices;
    }

    public void setAddedservices(String addedServices) {
        this.addedServices = addedServices;
    }
    public String getCheckedin() {
        return checkedIn;
    }

    public void setCheckedin(String checkedIn) {
        this.checkedIn = checkedIn;
    }
    public String getCheckedout() {
        return checkedOut;
    }

    public void setCheckedout(String checkedOut) {
        this.checkedOut = checkedOut;
    }
    public String getExtradays() {
        return extraDays;
    }

    public void setExtradays(String extraDays) {
        this.extraDays = extraDays;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getBookingpaid() {
        return bookingPaid;
    }

    public void setBookingpaid(String bookingPaid) {
        this.bookingPaid = bookingPaid;
    }
    public String getRoomnum() {
        return roomNum;
    }

    public void setRoomnum(String roomNum) {
        this.roomNum = roomNum;
    }
    public String getCheckindate() {
        return checkInDate;
    }

    public void setCheckindate(String checkInDate) {
        this.checkInDate = checkInDate;
    }


}