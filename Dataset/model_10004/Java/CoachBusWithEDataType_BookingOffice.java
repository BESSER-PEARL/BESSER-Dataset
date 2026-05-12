





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_BookingOffice  {

    private String name;
    private int officeID;
    private String location;



    public CoachBusWithEDataType_BookingOffice(
        String name,        int officeID,        String location    ) {
        this.name = name;
        this.officeID = officeID;
        this.location = location;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getOfficeid() {
        return officeID;
    }

    public void setOfficeid(int officeID) {
        this.officeID = officeID;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}