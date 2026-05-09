





import java.util.List;
import java.util.ArrayList;

public class Implementation_DecisionSupportComponent_BookingDSSInfo  {

    private String departureDate;
    private String roomType;
    private String customerFirstName;
    private String arrivalDate;
    private String address;
    private String numberOfGuests;
    private String customerLastName;





    private Implementation_DecisionSupportComponent_DSSController implementation_decisionsupportcomponent_dsscontroller;


    public Implementation_DecisionSupportComponent_BookingDSSInfo(
        String departureDate,        String roomType,        String customerFirstName,        String arrivalDate,        String address,        String numberOfGuests,        String customerLastName    ) {
        this.departureDate = departureDate;
        this.roomType = roomType;
        this.customerFirstName = customerFirstName;
        this.arrivalDate = arrivalDate;
        this.address = address;
        this.numberOfGuests = numberOfGuests;
        this.customerLastName = customerLastName;
    }


    public String getDeparturedate() {
        return departureDate;
    }

    public void setDeparturedate(String departureDate) {
        this.departureDate = departureDate;
    }
    public String getRoomtype() {
        return roomType;
    }

    public void setRoomtype(String roomType) {
        this.roomType = roomType;
    }
    public String getCustomerfirstname() {
        return customerFirstName;
    }

    public void setCustomerfirstname(String customerFirstName) {
        this.customerFirstName = customerFirstName;
    }
    public String getArrivaldate() {
        return arrivalDate;
    }

    public void setArrivaldate(String arrivalDate) {
        this.arrivalDate = arrivalDate;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getNumberofguests() {
        return numberOfGuests;
    }

    public void setNumberofguests(String numberOfGuests) {
        this.numberOfGuests = numberOfGuests;
    }
    public String getCustomerlastname() {
        return customerLastName;
    }

    public void setCustomerlastname(String customerLastName) {
        this.customerLastName = customerLastName;
    }

    public Implementation_DecisionSupportComponent_DSSController getImplementation_decisionsupportcomponent_dsscontroller() {
        return implementation_decisionsupportcomponent_dsscontroller;
    }

    public void setImplementation_decisionsupportcomponent_dsscontroller(Implementation_DecisionSupportComponent_DSSController implementation_decisionsupportcomponent_dsscontroller) {
        this.implementation_decisionsupportcomponent_dsscontroller = implementation_decisionsupportcomponent_dsscontroller;
    }

}