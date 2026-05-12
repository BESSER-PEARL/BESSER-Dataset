





import java.util.List;
import java.util.ArrayList;

public class CoachBus_BookingOffice  {

    private int officeID;
    private String location;
    private String name;



    public CoachBus_BookingOffice(
        int officeID,        String location,        String name    ) {
        this.officeID = officeID;
        this.location = location;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}