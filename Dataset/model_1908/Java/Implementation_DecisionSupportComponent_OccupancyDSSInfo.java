





import java.util.List;
import java.util.ArrayList;

public class Implementation_DecisionSupportComponent_OccupancyDSSInfo  {

    private String numberOfGuests;
    private String checkOutDateTime;
    private String checkInDateTime;
    private String roomNumber;





    private Implementation_DecisionSupportComponent_DSSController implementation_decisionsupportcomponent_dsscontroller;


    public Implementation_DecisionSupportComponent_OccupancyDSSInfo(
        String numberOfGuests,        String checkOutDateTime,        String checkInDateTime,        String roomNumber    ) {
        this.numberOfGuests = numberOfGuests;
        this.checkOutDateTime = checkOutDateTime;
        this.checkInDateTime = checkInDateTime;
        this.roomNumber = roomNumber;
    }


    public String getNumberofguests() {
        return numberOfGuests;
    }

    public void setNumberofguests(String numberOfGuests) {
        this.numberOfGuests = numberOfGuests;
    }
    public String getCheckoutdatetime() {
        return checkOutDateTime;
    }

    public void setCheckoutdatetime(String checkOutDateTime) {
        this.checkOutDateTime = checkOutDateTime;
    }
    public String getCheckindatetime() {
        return checkInDateTime;
    }

    public void setCheckindatetime(String checkInDateTime) {
        this.checkInDateTime = checkInDateTime;
    }
    public String getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(String roomNumber) {
        this.roomNumber = roomNumber;
    }

    public Implementation_DecisionSupportComponent_DSSController getImplementation_decisionsupportcomponent_dsscontroller() {
        return implementation_decisionsupportcomponent_dsscontroller;
    }

    public void setImplementation_decisionsupportcomponent_dsscontroller(Implementation_DecisionSupportComponent_DSSController implementation_decisionsupportcomponent_dsscontroller) {
        this.implementation_decisionsupportcomponent_dsscontroller = implementation_decisionsupportcomponent_dsscontroller;
    }

}